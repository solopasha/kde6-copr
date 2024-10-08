%global commit0 485ca02be22f9703d4203c80742dbed291bf61b1
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

Name:    kosmindoormap
Version: 24.08.2
Release: 1%{?dist}
Summary: OSM multi-floor indoor map renderer

License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-3.0-or-later AND MIT AND ODbL-1.0
URL:     https://invent.kde.org/libraries/%{name}
%apps_source

BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Svg)

BuildRequires:  zlib-devel
BuildRequires:  cmake(KOpeningHours)
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  osmctools
BuildRequires:  rsync
BuildRequires:  protobuf-devel
BuildRequires:  openssl-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  protobuf-lite-devel

BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KPublicTransport)
BuildRequires:  cmake(KOpeningHours)

Requires:       kf6-filesystem

%description
A library and QML component for rendering multi-level OSM indoor
maps of for example a (large) train station.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1


%build
%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build


%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%license LICENSES/*.txt
%doc README.md
%{_kf6_datadir}/qlogging-categories6/org_kde_kosmindoormap.categories
%{_kf6_libdir}/libKOSM.so.%{version_no_git}
%{_kf6_libdir}/libKOSM.so.1
%{_kf6_libdir}/libKOSMIndoorMap.so.%{version_no_git}
%{_kf6_libdir}/libKOSMIndoorMap.so.1
%{_kf6_libdir}/libKOSMIndoorRouting.so.%{version_no_git}
%{_kf6_libdir}/libKOSMIndoorRouting.so.1
%{_qt6_qmldir}/org/kde/kosmindoormap/
%{_qt6_qmldir}/org/kde/kosmindoorrouting/
%{_qt6_qmldir}/org/kde/osm/

%files devel
%{_includedir}/kosm/
%{_includedir}/KOSM/
%{_includedir}/kosmindoormap_version.h
%{_includedir}/kosmindoormap/
%{_includedir}/KOSMIndoorMap/
%{_includedir}/kosmindoorrouting/
%{_includedir}/KOSMIndoorRouting/
%{_kf6_libdir}/cmake/KOSMIndoorMap/
%{_kf6_libdir}/libKOSM.so
%{_kf6_libdir}/libKOSMIndoorMap.so
%{_kf6_libdir}/libKOSMIndoorRouting.so

%changelog
* Mon Oct 07 2024 Pavel Solovev <daron439@gmail.com> - 24.08.2-1
- Update to 24.08.2

* Tue Sep 10 2024 Pavel Solovev <daron439@gmail.com> - 24.08.1-1
- Update to 24.08.1

* Fri Aug 16 2024 Pavel Solovev <daron439@gmail.com> - 24.08.0-1
- Update to 24.08.0

* Fri Aug 09 2024 Pavel Solovev <daron439@gmail.com> - 24.07.90-1
- Update to 24.07.90

* Thu Jul 25 2024 Pavel Solovev <daron439@gmail.com> - 24.07.80-1
- Update to 24.07.80

* Thu Jul 04 2024 Pavel Solovev <daron439@gmail.com> - 24.05.2-1
- Update to 24.05.2

* Thu Jun 13 2024 Pavel Solovev <daron439@gmail.com> - 24.05.1-1
- Update to 24.05.1

* Thu May 23 2024 Pavel Solovev <daron439@gmail.com> - 24.05.0-1
- Update to 24.05.0

* Fri Apr 26 2024 Pavel Solovev <daron439@gmail.com> - 24.04.80-1
- Update to 24.04.80

* Thu Apr 11 2024 Pavel Solovev <daron439@gmail.com> - 24.02.2-1
- Update to 24.02.2

* Thu Mar 21 2024 Pavel Solovev <daron439@gmail.com> - 24.02.1-1
- Update to 24.02.1

* Wed Mar 20 2024 Pavel Solovev <daron439@gmail.com> - 24.02.0-2
- qmlcache rebuild

* Mon Dec 18 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80

* Mon Oct 09 2023 Steve Cossette <farchord@gmail.com> - 23.08.2-1
- Initial Release
