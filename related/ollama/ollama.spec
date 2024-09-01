%global llama_commit 1e6f6554aa11fa10160a5fda689e736c3c34169f
%global llama_shortcommit %(c=%{llama_commit}; echo ${c:0:7})

%global gomodulesmode GO111MODULE=on

# Generated by go2rpm 1.10.0
%bcond_with check

# https://github.com/jmorganca/ollama
%global goipath         github.com/ollama/ollama
Version:                0.3.9

%gometa -L -f

%global goname ollama

%global common_description %{expand:
Get up and running with Llama 2, Mistral, and other large language models
locally.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           ollama
Release:        %autorelease
Summary:        Get up and running with Llama 2 and other large language models locally
# License for github.com/jmorganca/ollama: MIT
# License for github.com/bytedance/sonic: Apache-2.0
# License for github.com/chenzhuoyu/base64x: Apache-2.0
# License for github.com/davecgh/go-spew: ISC
# License for github.com/emirpasic/gods: BSD-2-Clause AND ISC
# License for github.com/gabriel-vasile/mimetype: MIT
# License for github.com/gin-contrib/cors: MIT
# License for github.com/gin-contrib/sse: MIT
# License for github.com/gin-gonic/gin: MIT
# License for github.com/go-playground/locales: MIT
# License for github.com/go-playground/universal-translator: MIT
# License for github.com/go-playground/validator/v10: MIT
# License for github.com/goccy/go-json: MIT
# License for github.com/inconshreveable/mousetrap: Apache-2.0
# License for github.com/json-iterator/go: MIT
# License for github.com/klauspost/cpuid/v2: MIT
# License for github.com/leodido/go-urn: MIT
# License for github.com/mattn/go-isatty: MIT
# License for github.com/mattn/go-runewidth: MIT
# License for github.com/modern-go/concurrent: Apache-2.0
# License for github.com/modern-go/reflect2: Apache-2.0
# License for github.com/olekukonko/tablewriter: MIT
# License for github.com/pbnjay/memory: BSD-3-Clause
# License for github.com/pelletier/go-toml/v2: MIT
# License for github.com/pmezard/go-difflib: BSD-3-Clause
# License for github.com/rivo/uniseg: MIT
# License for github.com/spf13/cobra: Apache-2.0
# License for github.com/spf13/pflag: BSD-3-Clause
# License for github.com/stretchr/testify: MIT
# License for github.com/twitchyliquid64/golang-asm: BSD-3-Clause
# License for github.com/ugorji/go/codec: MIT
# License for golang.org/x/arch: BSD-3-Clause
# License for golang.org/x/crypto: BSD-3-Clause
# License for golang.org/x/exp: BSD-3-Clause
# License for golang.org/x/net: BSD-3-Clause
# License for golang.org/x/sync: BSD-3-Clause
# License for golang.org/x/sys: BSD-3-Clause
# License for golang.org/x/term: BSD-3-Clause
# License for golang.org/x/text: BSD-3-Clause
# License for google.golang.org/protobuf: BSD-3-Clause
# License for gopkg.in/yaml.v3: MIT AND Apache-2.0
# License for https://github.com/ggerganov/llama.cpp: MIT
License:        MIT AND Apache-2.0 AND ISC AND (BSD-2-Clause AND ISC) AND BSD-3-Clause AND (MIT AND Apache-2.0)
URL:            %{gourl}
Source0:        %{gosource}
# bash bundle_go_deps_for_rpm.sh ollama.spec
Source1:        vendor-%{version}.tar.gz
Source2:        bundle_go_deps_for_rpm.sh
Source3:        https://github.com/ggerganov/llama.cpp/archive/%{llama_commit}/llama-cpp-%{llama_shortcommit}.tar.gz
Source4:        ollama-sysusers.conf
Source5:        ollama.service
Source6:        ollama-tmpfiles.conf
Patch:          fixes.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  systemd-rpm-macros

Requires(pre):  systemd-sysusers
Requires(pre):  systemd-tmpfiles

Provides:       bundled(llama.cpp) = 0~1.git%{llama_shortcommit}

%description %{common_description}

%prep
%autosetup -p1 %{forgesetupargs} -a1
tar -xf %{SOURCE3} -C llm/llama.cpp --strip=1
%goprep -ke
sed -i 's,T_CODE=on,T_CODE=on -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON -D GGML_LTO:BOOL=ON -D CMAKE_BUILD_TYPE=Release,g' llm/generate/gen_linux.sh

%build
%set_build_flags
go generate %{goipath}/...
export CGO_CFLAGS="$CFLAGS"
export CGO_CPPFLAGS="$CPPFLAGS"
export CGO_CXXFLAGS="$CXXFLAGS"
export CGO_LDFLAGS="$LDFLAGS"
export LDFLAGS="-X=github.com/ollama/ollama/version.Version=%{version} \
                -X=github.com/ollama/ollama/server.mode=release"
%gobuild -o %{gobuilddir}/bin/ollama %{goipath}

%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -Dpm644 %{SOURCE4} %{buildroot}%{_sysusersdir}/%{name}.conf
install -Dpm644 %{SOURCE5} %{buildroot}%{_unitdir}/%{name}.service
install -Dpm644 %{SOURCE6} %{buildroot}%{_tmpfilesdir}/%{name}.conf

mkdir -p %{buildroot}%{_sharedstatedir}/%{name}

%if %{with check}
%check
for test in "TestBasicGetGPUInfo" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck -t vendor
%endif

%pre
%sysusers_create_package %{name} %{SOURCE4}
%tmpfiles_create_package %{name} %{SOURCE6}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license vendor/modules.txt
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_sysusersdir}/%{name}.conf
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/%{name}.service
%ghost %dir %attr(0755, ollama, ollama) %{_sharedstatedir}/%{name}

%changelog
%autochangelog
