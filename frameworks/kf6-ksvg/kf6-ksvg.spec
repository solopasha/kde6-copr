%global commit0 977636aeb3cd095287dcc7cf11bbb817066f081a
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

%global framework ksvg

Name:    kf6-ksvg
Summary: Components for handling SVGs
Version: 6.0.0%{?bumpver:^%{bumpver}.git%{shortcommit0}}
Release: 1%{?dist}

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6ColorScheme)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6KirigamiPlatform)

BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Svg)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Gui)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.



%qch_package

%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%files
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/ksvg.categories
%{_kf6_libdir}/libKF6Svg.so.6
%{_kf6_libdir}/libKF6Svg.so.%{lua: print((macros.version:gsub('[%^~].*', '')))}
%{_kf6_libdir}/qt6/qml/org/kde/ksvg/

%files devel
%{_qt6_docdir}/*.tags
%{_kf6_includedir}/KSvg/
%{_kf6_libdir}/cmake/KF6Svg/
%{_kf6_libdir}/libKF6Svg.so

%changelog
* Wed Mar 20 2024 Pavel Solovev <daron439@gmail.com> - 6.0.0-2
- qmlcache rebuild

* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231011.024143.b56185b-1
- Initial release
