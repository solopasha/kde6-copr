%global commit0 91575da028418426c8765b8cc89480f45d16d984
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

Name:    plasma-activities-stats
Summary: A KDE Frameworks 6 Tier 3 library for accessing the usage data collected by the activities system
Version: 6.2.3
Release: 1%{?dist}

License: CC0-1.0, GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-GPL AND LicenseRef-KDE-Accepted-LGPL
URL:     https://invent.kde.org/plasma/%{name}
%plasma_source

BuildRequires:  boost-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(PlasmaActivities)
BuildRequires:  cmake(KF6Config)
BuildRequires:  kf6-rpm-macros

BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtbase-devel

# Renamed from kf6-kactivities-stats
Obsoletes:      kf6-kactivities-stats < 1:%{version}-%{release}
Provides:       kf6-kactivities-stats = 1:%{version}-%{release}

Obsoletes:      kactivities-stats < %{version}-%{release}
Provides:       kactivities-stats = %{version}-%{release}

%description
%{summary}.

%package        devel
Summary:        Developer files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
Obsoletes:      kf6-kactivities-stats-devel < 1:%{version}-%{release}
Provides:       kf6-kactivities-stats-devel = 1:%{version}-%{release}
Obsoletes:      kactivities-stats-devel < %{version}-%{release}
Provides:       kactivities-stats-devel = %{version}-%{release}
%description    devel
%{summary}.


%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%files
%doc MAINTAINER README.developers TODO
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{name}.*
%{_kf6_libdir}/libPlasmaActivitiesStats.so.%{version_no_git}
%{_kf6_libdir}/libPlasmaActivitiesStats.so.1

%files devel
%{_includedir}/PlasmaActivitiesStats/
%{_kf6_libdir}/cmake/PlasmaActivitiesStats/
%{_kf6_libdir}/libPlasmaActivitiesStats.so
%{_kf6_libdir}/pkgconfig/PlasmaActivitiesStats.pc

%changelog
* Tue Nov 05 2024 Pavel Solovev <daron439@gmail.com> - 6.2.3-1
- Update to 6.2.3

* Tue Oct 22 2024 Pavel Solovev <daron439@gmail.com> - 6.2.2-1
- Update to 6.2.2

* Tue Oct 15 2024 Pavel Solovev <daron439@gmail.com> - 6.2.1-1
- Update to 6.2.1

* Thu Oct 03 2024 Pavel Solovev <daron439@gmail.com> - 6.2.0-1
- Update to 6.2.0

* Tue Sep 10 2024 Pavel Solovev <daron439@gmail.com> - 6.1.5-1
- Update to 6.1.5

* Tue Aug 06 2024 Pavel Solovev <daron439@gmail.com> - 6.1.4-1
- Update to 6.1.4

* Tue Jul 16 2024 Pavel Solovev <daron439@gmail.com> - 6.1.3-1
- Update to 6.1.3

* Tue Jul 02 2024 Pavel Solovev <daron439@gmail.com> - 6.1.2-1
- Update to 6.1.2

* Tue Jun 25 2024 Pavel Solovev <daron439@gmail.com> - 6.1.1-1
- Update to 6.1.1

* Tue Jun 18 2024 Pavel Solovev <daron439@gmail.com> - 6.1.0-1
- Update to 6.1.0

* Fri May 24 2024 Pavel Solovev <daron439@gmail.com> - 6.0.90-1
- Update to 6.0.90

* Tue May 21 2024 Pavel Solovev <daron439@gmail.com> - 6.0.5-1
- Update to 6.0.5

* Tue Apr 16 2024 Pavel Solovev <daron439@gmail.com> - 6.0.4-1
- Update to 6.0.4

* Tue Mar 26 2024 Pavel Solovev <daron439@gmail.com> - 6.0.3-1
- Update to 6.0.3

* Wed Mar 20 2024 Pavel Solovev <daron439@gmail.com> - 6.0.2-2
- qmlcache rebuild

* Sun Nov 12 2023 Alessandro Astone <ales.astone@gmail.com> - 5.27.80-1
- Renamed from kf6-kactivities-stats
- 5.27.80

* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231007.105021.eae8543-1
- Initial release
