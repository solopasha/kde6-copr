%global commit0 4e94d04e67b3a27214a47413bf3b743e21133696
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

%global appname kImageAnnotator
%global libname lib%{appname}

Name: kimageannotator
Version: 0.6.1%{?bumpver:^%{bumpver}.git%{shortcommit0}}
Release: 2%{?dist}

License: LGPL-3.0-or-later
Summary: Library and a tool for annotating images
URL: https://github.com/ksnip/%{appname}
Source0: %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

BuildRequires: cmake(kColorPicker-Qt5)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5X11Extras)

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(kColorPicker-Qt6)

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build

%description
Library and a tool for annotating images. Part of KSnip project.

%package        qt5
Summary:        Qt5 support for %{name}
Requires:       %{name}-common = %{version}-%{release}
%description    qt5
%{summary}.

%package        qt5-devel
Summary:        Development files for %{name}
Requires:       %{name}-qt5%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description    qt5-devel
%{summary}.

%package        qt6
Summary:        Qt6 support for %{name}
Obsoletes:      %{name} < 0.6.1-3
Requires:       %{name}-common = %{version}-%{release}
%description    qt6
%{summary}.

%package        qt6-devel
Summary:        Development files for %{name}
Requires:       %{name}-qt6%{?_isa} = %{version}-%{release}
%description    qt6-devel
%{summary}.

%package        common
Summary:        Common files for %{name}
%description    common
%{summary}.

%prep
%autosetup -n %{appname}-%{commit0} -p1

%build
%global _vpath_builddir %{_target_platform}-qt6
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_TESTS:BOOL=OFF \
    -DBUILD_EXAMPLE:BOOL=OFF \
    -DBUILD_WITH_QT6:BOOL=ON
%cmake_build

%global _vpath_builddir %{_target_platform}-qt5
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_TESTS:BOOL=OFF \
    -DBUILD_EXAMPLE:BOOL=OFF
%cmake_build

%install
%global _vpath_builddir %{_target_platform}-qt5
%cmake_install

%global _vpath_builddir %{_target_platform}-qt6
%cmake_install
%find_lang %{appname} --with-qt

%files qt6
%doc README.md
%license LICENSE
%{_libdir}/%{libname}-Qt6.so.0*

%files qt5
%doc README.md
%license LICENSE
%{_libdir}/%{libname}-Qt5.so.0*

%files qt6-devel
%{_includedir}/%{appname}-Qt6/
%{_libdir}/cmake/%{appname}-Qt6/
%{_libdir}/%{libname}-Qt6.so

%files qt5-devel
%{_includedir}/%{appname}-Qt5/
%{_libdir}/cmake/%{appname}-Qt5/
%{_libdir}/%{libname}-Qt5.so

%files common -f %{appname}.lang

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 15 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.1-1
- Updated to version 0.6.1.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 23 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.6.0-1
- Updated to version 0.6.0.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 23 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.3-1
- Updated to version 0.5.3.

* Tue Sep 14 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.2-1
- Updated to version 0.5.2.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 31 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.1-1
- Updated to version 0.5.1.

* Tue May 25 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.5.0-1
- Updated to version 0.5.0.

* Tue Mar 23 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.4.2-1
- Updated to version 0.4.2.

* Mon Feb 15 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.4.1-1
- Updated to version 0.4.1.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 14 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.4.0-1
- Updated to version 0.4.0.

* Fri Jul 31 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3.2-1
- Initial SPEC release.
