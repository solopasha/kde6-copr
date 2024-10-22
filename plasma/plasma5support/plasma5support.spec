%global commit0 98360974eb771fe5afdae9f85eb4213fb9e165eb
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

Name:    plasma5support
Summary: Support components for porting from KF5/Qt5 to KF6/Qt6
Version: 6.2.2
Release: 1%{?dist}

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/plasma/%{name}
%plasma_source

BuildRequires:  extra-cmake-modules
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6Solid)

BuildRequires:  cmake(KSysGuard)
BuildRequires:  cmake(Plasma)

Requires:  kf6-filesystem

# Renamed from kf6-plasma5support
Obsoletes:      kf6-plasma5support < 1:%{version}-%{release}
Provides:       kf6-plasma5support = 1:%{version}-%{release}

%description
%{summary}.

%package devel
Summary:        Developer files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
Obsoletes:      kf6-plasma5support-devel < 1:%{version}-%{release}
Provides:       kf6-plasma5support-devel = 1:%{version}-%{release}
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
%find_lang libplasma5support --all-name

%files -f libplasma5support.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/plasma5support/
%{_kf6_datadir}/qlogging-categories6/plasma5support.categories
%{_kf6_datadir}/qlogging-categories6/plasma5support.renamecategories
%{_kf6_libdir}/libPlasma5Support.so.%{version_no_git}
%{_kf6_libdir}/libPlasma5Support.so.6
%{_kf6_qtplugindir}/plasma5support/
%{_qt6_qmldir}/org/kde/plasma/plasma5support/

%files devel
%{_includedir}/Plasma5Support/
%{_kf6_libdir}/cmake/Plasma5Support/
%{_kf6_libdir}/libPlasma5Support.so

%changelog
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

* Sun Nov 12 2023 Alessandro Astone <ales.astone@gmail.com> - 5.27.80-2
- Add Obsoletes/Provides to the devel subpackage

* Fri Nov 10 2023 Alessandro Astone <ales.astone@gmail.com> - 5.27.80-1
- Renamed from kf6-plasma5support
- 5.27.80

* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231011.222045.245b3dd-1
- Initial release
