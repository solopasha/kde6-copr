%global commit0 9cc24ffa9c2e85a429c06e9ee3a1bdc070a8e97e
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

%global framework kidletime

Name:           kf6-%{framework}
Version:        6.9.0
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 1 integration module for idle time detection
License:        CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
URL:            https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6WaylandClient)

BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb-sync)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel

Requires:       kf6-filesystem
Requires:       %{name}-x11%{?_isa} = %{version}-%{release}

%description
KDE Frameworks 6 Tier 1 integration module for idle time detection.

%package        x11
Summary:        Idle time detection plugins for X11 environments
Conflicts:      %{name} < 6.7.0-2
%description    x11
The %{name}-x11 package contains plugins for applications using
%{name} to detect idle time on X11 environments.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core)
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
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6IdleTime.so.%{version_no_git}
%{_kf6_libdir}/libKF6IdleTime.so.6
%dir %{_kf6_plugindir}/org.kde.kidletime.platforms/
%{_kf6_plugindir}/org.kde.kidletime.platforms/KF6IdleTimeWaylandPlugin.so

%files x11
%{_kf6_plugindir}/org.kde.kidletime.platforms/KF6IdleTimeXcbPlugin0.so
%{_kf6_plugindir}/org.kde.kidletime.platforms/KF6IdleTimeXcbPlugin1.so

%files devel
%{_kf6_includedir}/KIdleTime/
%{_kf6_libdir}/cmake/KF6IdleTime/
%{_kf6_libdir}/libKF6IdleTime.so
%{_qt6_docdir}/*.tags

%changelog
* Fri Dec 06 2024 Pavel Solovev <daron439@gmail.com> - 6.9.0-1
- Update to 6.9.0

* Sat Nov 02 2024 Pavel Solovev <daron439@gmail.com> - 6.8.0-1
- Update to 6.8.0

* Tue Oct 29 2024 Pavel Solovev <daron439@gmail.com> - 6.7.0-2
- Adopt Fedora changes

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

* Tue Oct 17 2023 Jan Grulich <jgrulich@redhat.com> - 5.240.0^20230829.233116.5bf73aa-3
- Rebuild (qt6)

* Thu Oct 05 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.233116.5bf73aa-2
- Rebuild for Qt Private API

* Sun Sep 24 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230829.233116.5bf73aa-1
- Initial release
