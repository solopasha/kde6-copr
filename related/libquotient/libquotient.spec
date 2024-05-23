%global appname Quotient
%global libname lib%{appname}
%global _description %{expand:
The Quotient project aims to produce a Qt-based SDK to develop applications
for Matrix. libQuotient is a library that enables client applications. It is
the backbone of Quaternion, Spectral and other projects. Versions 0.5.x and
older use the previous name - libQMatrixClient.}

Name: libquotient
Version: 0.8.2
Release: 1%{?dist}

License: BSD-3-Clause AND LGPL-2.1-or-later
URL: https://github.com/quotient-im/%{libname}
Summary: Qt library to write cross-platform clients for Matrix
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake(Olm)
BuildRequires: cmake(Qt5Concurrent)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Keychain)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5Multimedia)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Sql)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Keychain)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: pkgconfig(openssl)

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: ninja-build

%description %_description

%package qt5
Summary: Files for qt5
Provides: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name} < %{?epoch:%{epoch}:}%{version}-%{release}
%description qt5 %_description

%package qt5-devel
Summary: Development files for %{name} for qt5
Provides: %{name}-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-qt5%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: cmake(Olm)
Requires: cmake(Qt5Keychain)
Requires: cmake(Qt5Sql)
Requires: pkgconfig(openssl)
%description qt5-devel %_description

%package qt6
Summary: Files for qt6
%description qt6 %_description

%package qt6-devel
Summary: Development files for %{name} for qt6
Requires: %{name}-qt6%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: cmake(Olm)
Requires: cmake(Qt6Keychain)
Requires: cmake(Qt6Sql)
Requires: pkgconfig(openssl)
%description qt6-devel %_description

%prep
%autosetup -n %{libname}-%{version}
rm -rf 3rdparty

%build
mkdir %{name}_qt5
pushd %{name}_qt5
%cmake -G Ninja \
    -S'..' \
    -DCMAKE_BUILD_TYPE=Release \
    -DQuotient_ENABLE_E2EE:BOOL=ON \
    -DQuotient_INSTALL_TESTS:BOOL=OFF \
    -DQuotient_INSTALL_EXAMPLE:BOOL=OFF
%cmake_build
popd
mkdir %{name}_qt6
pushd %{name}_qt6
%cmake -G Ninja \
    -S'..' \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir}/%{appname}Qt6 \
    -DQuotient_ENABLE_E2EE:BOOL=ON \
    -DQuotient_INSTALL_TESTS:BOOL=OFF \
    -DQuotient_INSTALL_EXAMPLE:BOOL=OFF \
    -DBUILD_WITH_QT6=ON
%cmake_build
popd


%check
pushd %{name}_qt5
%ctest --exclude-regex 'testolmaccount|testkeyverification'
popd
pushd %{name}_qt6
%ctest --exclude-regex 'testolmaccount|testkeyverification'
popd

%install
pushd %{name}_qt5
%cmake_install
popd
pushd %{name}_qt6
%cmake_install
popd
rm -rf %{buildroot}%{_datadir}/ndk-modules

%files qt5
%license COPYING
%doc README.md CONTRIBUTING.md SECURITY.md
%{_libdir}/%{libname}.so.0*

%files qt5-devel
%{_includedir}/%{appname}/
%{_libdir}/cmake/%{appname}/
%{_libdir}/pkgconfig/%{appname}.pc
%{_libdir}/%{libname}.so

%files qt6
%license COPYING
%doc README.md CONTRIBUTING.md SECURITY.md
%{_libdir}/%{libname}Qt6.so.0*

%files qt6-devel
%{_includedir}/%{appname}Qt6/
%{_libdir}/cmake/%{appname}Qt6/
%{_libdir}/%{libname}Qt6.so
%{_libdir}/pkgconfig/%{appname}Qt6.pc

%changelog
* Thu May 23 2024 Pavel Solovev <daron439@gmail.com> - 0.8.2-1
- new version

* Wed Dec 06 2023 Yaakov Selkowitz <yselkowitz@fedoraproject.org> - 0.8.1.2-5
- Make headers parallel-installable

* Wed Dec 06 2023 Yaakov Selkowitz <yselkowitz@fedoraproject.org> - 0.8.1.2-4
- Add devel dependencies on QtKeychain

* Wed Dec 06 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.8.1.2-3
- Drop unused dependency on QtOlm

* Thu Nov 30 2023 Alessandro Astone <ales.astone@gmail.com> - 0.8.1.2-2
- Rebuild (qt6)

* Wed Nov 22 2023 Steve Cossette <farchord@gmail.com> - 0.8.1.2-1
- 0.8.1.2 (And branching into qt6)

* Sat Sep 02 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.8.1.1-1
- Update to 0.8.1.1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat May 06 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 0.7.2-1
- Update to 0.7.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 10 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 0.7.1-1
- Updated to version 0.7.1.

* Tue Dec 20 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.7.0-1
- Updated to version 0.7.0.
- Enabled E2EE support.
- Switched to SPDX license tag.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Apr 30 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.11-3
- Rebuilt to mitigate GCC 12 regressions.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 07 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.11-1
- Updated to version 0.6.11.

* Mon Oct 04 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.10-1
- Updated to version 0.6.10.

* Mon Sep 13 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.9-1
- Updated to version 0.6.9.

* Wed Aug 25 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.8-1
- Updated to version 0.6.8.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 08 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.7-1
- Updated to version 0.6.7.

* Thu Mar 18 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.6-1
- Updated to version 0.6.6.

* Mon Feb 22 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.5-1
- Updated to version 0.6.5.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 16 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.4-1
- Updated to version 0.6.4.

* Sun Dec 27 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.3-2
- Disabled E2EE support due to lots of crashes.

* Fri Dec 25 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.3-1
- Updated to version 0.6.3.

* Sat Oct 31 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.2-1
- Updated to version 0.6.2.

* Sat Sep 05 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.1-1
- Updated to version 0.6.1.

* Wed Jul 29 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.0-1
- Updated to version 0.6.0.

* Sat Mar 07 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.0-0.4.20200207git9bcf0cb
- Updated to latest Git snapshot.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-0.3.20200121gite3a5b3a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.0-0.2.20200121gite3a5b3a
- Updated to version 0.6.0-git.
