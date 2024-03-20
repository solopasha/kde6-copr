%global		framework kidletime

Name:		kf6-%{framework}
Version:	6.0.0
Release:	2%{?dist}
Summary:	KDE Frameworks 6 Tier 1 integration module for idle time detection
License:	CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
URL:		https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	extra-cmake-modules >= %{version}
BuildRequires:	kf6-rpm-macros
BuildRequires:	qt6-qtbase-devel
BuildRequires:	cmake(Qt6WaylandClient)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(x11-xcb)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xcb-sync)
BuildRequires:	pkgconfig(Qt6WaylandClient)
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	wayland-devel
BuildRequires:	cmake(PlasmaWaylandProtocols)
BuildRequires:	wayland-protocols-devel
BuildRequires:  qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
Requires:	kf6-filesystem

%description
KDE Frameworks 6 Tier 1 integration module for idle time detection.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	qt6-qtbase-devel
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%qch_package

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6IdleTime.so.6
%{_kf6_libdir}/libKF6IdleTime.so.%{version}
%dir %{_kf6_plugindir}/org.kde.kidletime.platforms/
%{_kf6_plugindir}/org.kde.kidletime.platforms/KF6IdleTimeWaylandPlugin.so
%{_kf6_plugindir}/org.kde.kidletime.platforms/KF6IdleTimeXcbPlugin0.so
%{_kf6_plugindir}/org.kde.kidletime.platforms/KF6IdleTimeXcbPlugin1.so

%files devel
%{_qt6_docdir}/*.tags
%{_kf6_includedir}/KIdleTime/
%{_kf6_libdir}/cmake/KF6IdleTime/
%{_kf6_libdir}/libKF6IdleTime.so

%changelog
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
