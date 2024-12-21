%global commit0 87f9d4a40f373f50dd30309b3b4514d710d038c1
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 5

Name:           plasma-activities
Summary:        Core components for the KDE's Activities System
Version:        6.2.80%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}

License:        CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-LGPL AND MIT
URL:            https://invent.kde.org/plasma/%{name}
%plasma_source

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  boost-devel

Requires:       kf6-filesystem

# Renamed from kf6-kactivities
Obsoletes:      kf6-kactivities < 1:%{version}-%{release}
Provides:       kf6-kactivities = 1:%{version}-%{release}
Obsoletes:      kactivities < 5.27.80-2
Provides:       kactivities = %{version}-%{release}

%description
A KDE Frameworks 6 Tier 3 API for using and interacting with Activities as a
consumer, application adding information to them or as an activity manager.

%package        devel
Summary:        Developer files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core)
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
%{?kde_snapshot_changelog_entry}
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
