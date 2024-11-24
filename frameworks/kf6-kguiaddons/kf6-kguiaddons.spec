%global commit0 0971293dbe8115cbfde021a83d780c7fcbe48058
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 2

%global framework kguiaddons

Name:           kf6-%{framework}
Version:        6.9.0%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 1 addon with various classes on top of QtGui

License:        BSD-2-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only
URL:            https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}

BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xkbcommon)

Requires:       kf6-filesystem

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
%doc README.md
%license LICENSES/*.txt
%{_kf6_bindir}/kde-geo-uri-handler
%{_kf6_datadir}/applications/*-handler.desktop
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6GuiAddons.so.%{version_no_git}
%{_kf6_libdir}/libKF6GuiAddons.so.6
%{_kf6_qmldir}/org/kde/guiaddons/

%files devel
%{_kf6_includedir}/KGuiAddons/
%{_kf6_libdir}/cmake/KF6GuiAddons/
%{_kf6_libdir}/libKF6GuiAddons.so
%{_kf6_libdir}/pkgconfig/KF6GuiAddons.pc
%{_qt6_docdir}/*.tags

%changelog
%{?kde_snapshot_changelog_entry}
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

* Tue Oct 17 2023 Jan Grulich <jgrulich@redhat.com> - 5.240.0^20230916.160754.7ff692a-3
- Rebuild (qt6)

* Thu Oct 05 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230916.160754.7ff692a-2
- Rebuild for Qt Private API

* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230916.160754.7ff692a-1
- Initial release
