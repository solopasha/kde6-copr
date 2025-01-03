%global commit0 75b702b547c2053807ddb36010f4aff2f32343a0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

%global framework kwindowsystem

Name:           kf6-%{framework}
Version:        6.10.0
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 1 integration module with classes for windows management
License:        CC0-1.0 AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND MIT
URL:            https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  qt6-qtbase-private-devel

BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  egl-wayland-devel
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xrender)

Requires:       kf6-filesystem

%description
KDE Frameworks Tier 1 integration module that provides classes for managing and
working with windows.

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
%find_lang_kf6 kwindowsystem6_qt

%files -f kwindowsystem6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6WindowSystem.so.%{version_no_git}
%{_kf6_libdir}/libKF6WindowSystem.so.6
%dir %{_kf6_plugindir}/kwindowsystem
%{_kf6_plugindir}/kwindowsystem/KF6WindowSystemKWaylandPlugin.so
%{_kf6_plugindir}/kwindowsystem/KF6WindowSystemX11Plugin.so
%{_kf6_qmldir}/org/kde/kwindowsystem/

%files devel
%{_kf6_includedir}/KWindowSystem/
%{_kf6_libdir}/cmake/KF6WindowSystem/
%{_kf6_libdir}/libKF6WindowSystem.so
%{_kf6_libdir}/pkgconfig/KF6WindowSystem.pc
%{_qt6_docdir}/*.tags

%changelog
* Fri Jan 03 2025 Pavel Solovev <daron439@gmail.com> - 6.10.0-1
- Update to 6.10.0

* Fri Dec 06 2024 Pavel Solovev <daron439@gmail.com> - 6.9.0-1
- Update to 6.9.0

* Mon Dec 02 2024 Pavel Solovev <daron439@gmail.com> - 6.8.0-2
- Remove Qt6 version constraints

* Sat Nov 02 2024 Pavel Solovev <daron439@gmail.com> - 6.8.0-1
- Update to 6.8.0

* Thu Oct 31 2024 Pavel Solovev <daron439@gmail.com> - 6.7.0-2
- rebuilt

* Fri Oct 04 2024 Pavel Solovev <daron439@gmail.com> - 6.7.0-1
- Update to 6.7.0

* Fri Sep 06 2024 Pavel Solovev <daron439@gmail.com> - 6.6.0-1
- Update to 6.6.0

* Fri Aug 09 2024 Pavel Solovev <daron439@gmail.com> - 6.5.0-1
- Update to 6.5.0

* Fri Jul 12 2024 Pavel Solovev <daron439@gmail.com> - 6.4.0-1
- Update to 6.4.0

* Fri Jun 07 2024 Pavel Solovev <daron439@gmail.com> - 6.3.0-1
- Update to 6.3.0

* Sun Jun 02 2024 Pavel Solovev <daron439@gmail.com> - 6.2.0-1.1
- rebuild for f40

* Sun May 12 2024 Pavel Solovev <daron439@gmail.com> - 6.2.0-1
- Update to 6.2.0

* Fri Apr 12 2024 Pavel Solovev <daron439@gmail.com> - 6.1.0-1
- Update to 6.1.0

* Wed Mar 20 2024 Pavel Solovev <daron439@gmail.com> - 6.0.0-2
- qmlcache rebuild

* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Tue Oct 17 2023 Jan Grulich <jgrulich@redhat.com> - 5.240.0^20231003.213655.0aa4d07-3
- Rebuild (qt6)

* Thu Oct 05 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20231003.213655.0aa4d07-2
- Rebuild for Qt Private API

* Tue Oct 03 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231003.213655.0aa4d07-1
- Fix for build on s390x arch

* Tue Sep 26 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230905.004205.b59a819-1
- Initial Release
