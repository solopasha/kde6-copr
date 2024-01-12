%global commit0 cddaa836580f59df94795b2daec26be6ee48fd3d
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

%global appname kColorPicker
%global libname lib%{appname}

Name: kcolorpicker
Version: 0.2.0%{?bumpver:^%{bumpver}.git%{shortcommit0}}
Release: 2%{?dist}

License: LGPL-3.0-or-later
Summary: QToolButton control with color popup menu
URL: https://github.com/ksnip/%{appname}
Source0: %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build

%description
QToolButton with color popup menu which lets you select a color.

The popup features a color dialog button which can be used to add
custom colors to the popup menu.

%package        qt5
Summary:        Qt5 support for %{name}
%description    qt5
%{summary}.

%package        qt5-devel
Summary:        Development files for %{name}
Requires:       %{name}-qt5%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description    qt5-devel
%{summary}.

%package        qt6
Summary:        Qt6 support for %{name}
Obsoletes:      kcolorpicker < 0.2.0-5
%description    qt6
%{summary}.

%package        qt6-devel
Summary:        Development files for %{name}
Requires:       %{name}-qt6%{?_isa} = %{version}-%{release}
%description    qt6-devel
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

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 23 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 0.2.0-1
- Updated to version 0.2.0.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May 25 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.1.6-1
- Updated to version 0.1.6.

* Mon Feb 15 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 0.1.5-1
- Updated to version 0.1.5.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.1.4-1
- Initial SPEC release.
