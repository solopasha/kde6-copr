Name:           cxx-rust-cssparser
Version:        1.1.0
Release:        1%{?dist}
Summary:        Library for parsing CSS using the Rust cssparser crate

# Rust Crates Licensing:
# Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# MPL-2.0
# Unlicense OR MIT
# Zlib

License:        BSD-2-Clause AND CC0-1.0 AND LGPL-2.1-only AND LGPL-3.0-only AND (Apache-2.0 OR MIT) and MIT AND MPL-2.0 AND (Unlicense OR MIT) AND Zlib

URL:            https://invent.kde.org/libraries/cxx-rust-cssparser
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules

BuildRequires:  cmake(Qt6Core)

BuildRequires:  cmake(Corrosion)
BuildRequires:  rust-packaging
BuildRequires:  cxxbridge

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%conf
%cmake_kf6

%build
export CARGO_HOME=.cargo
%cmake_build

%install
%cmake_install


%files
%license LICENSES/*
%{_kf6_bindir}/cxx-rust-cssparser-parse
%{_kf6_libdir}/lib%{name}.so.1
%{_kf6_libdir}/lib%{name}.so.%{version}

%files devel
%{_includedir}/%{name}/
%{_kf6_libdir}/cmake/%{name}/
%{_kf6_libdir}/lib%{name}.so

%changelog
* Thu Sep 10 2026 Zakir Zamirov <268826384+solopashachas@users.noreply.github.com> - 1.1.0-1
- new version

* Thu Sep 03 2026 Maxwell G <maxwell@gtmx.me> - 1.0.0-3
- Rebuild with latest Rust compiler to enable SHSTK support

* Wed Jul 15 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Tue May 12 2026 Steve Cossette <farchord@gmail.com> - 1.0.0-1
- Initial Release
