%global		framework kwindowsystem

Name:		kf6-%{framework}
Version:	5.246.0
Release:	1%{?dist}
Summary:	KDE Frameworks 6 Tier 1 integration module with classes for windows management
License:	CC0-1.0 AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND MIT
URL:		https://invent.kde.org/frameworks/%{framework}
%frameworks_source

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	extra-cmake-modules >= %{version}
BuildRequires:	kf6-rpm-macros
BuildRequires:	make
BuildRequires:	qt6-qtbase-devel
BuildRequires:	qt6-qttools-devel
BuildRequires:	cmake(Qt6Qml)
BuildRequires:  pkgconfig(Qt6WaylandClient)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xcb-icccm)
BuildRequires:	pkgconfig(xcb-keysyms)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xrender)
BuildRequires:  wayland-devel
BuildRequires:  egl-wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  plasma-wayland-protocols-devel
BuildRequires:	fdupes
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  qt6-qtbase-private-devel
Requires:	kf6-filesystem

%description
KDE Frameworks Tier 1 integration module that provides classes for managing and
working with windows.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	qt6-qtbase-devel
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang_kf6 kwindowsystem6_qt
%fdupes %{buildroot}%{_kf6_includedir}

%files -f kwindowsystem6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6WindowSystem.so.*
%dir %{_kf6_plugindir}/kwindowsystem/
%{_kf6_plugindir}/kwindowsystem/KF6WindowSystemX11Plugin.so
%{_kf6_qmldir}/org/kde/kwindowsystem
%{_qt6_plugindir}/kf6/kwindowsystem/KF6WindowSystemKWaylandPlugin.so

%files devel
%{_kf6_includedir}/KWindowSystem/
%{_kf6_libdir}/libKF6WindowSystem.so
%{_kf6_libdir}/cmake/KF6WindowSystem/

%changelog
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
