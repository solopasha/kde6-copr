%global commit0 794be63661668ea5247bc0833b39e17e7d8db86e
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

Name:    plasma-activities
Summary: Core components for the KDE's Activities System
Version: 6.2.5
Release: 1%{?dist}

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-LGPL AND MIT
URL:     https://invent.kde.org/plasma/%{name}
%plasma_source

BuildRequires:  boost-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel

Requires:       kf6-filesystem

# Renamed from kf6-kactivities
Obsoletes:      kf6-kactivities < 1:%{version}-%{release}
Provides:       kf6-kactivities = 1:%{version}-%{release}
Obsoletes:      kactivities < 5.27.80-2
Provides:       kactivities = %{version}-%{release}

%description
A KDE Frameworks 6 Tier 3 API for using and interacting with Activities as a
consumer, application adding information to them or as an activity manager.

%package devel
Summary:        Developer files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
Obsoletes:      kf6-kactivities-devel < 1:%{version}-%{release}
Provides:       kf6-kactivities-devel = 1:%{version}-%{release}
Obsoletes:      kactivities-devel < 5.27.80-2
Provides:       kactivities-devel = %{version}-%{release}
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
%doc README.md
%license LICENSES/*.txt
%{_kf6_bindir}/plasma-activities-cli6
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libPlasmaActivities.so.%{version_no_git}
%{_kf6_libdir}/libPlasmaActivities.so.6
%{_kf6_qmldir}/org/kde/activities/

%files devel
%{_includedir}/PlasmaActivities/
%{_kf6_libdir}/cmake/PlasmaActivities/
%{_kf6_libdir}/libPlasmaActivities.so
%{_kf6_libdir}/pkgconfig/PlasmaActivities.pc

%changelog
* Thu Jan 02 2025 Pavel Solovev <daron439@gmail.com> - 6.2.5-1
- Update to 6.2.5

* Tue Nov 26 2024 Pavel Solovev <daron439@gmail.com> - 6.2.4-1
- Update to 6.2.4

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
- Renamed from kf6-kactivities
- 5.27.80

* Tue Oct 17 2023 Jan Grulich <jgrulich@redhat.com> - 5.240.0^20231009.214418.330a3e2-2
- Rebuild (qt6)

* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231009.214418.330a3e2-1
- Initial release
