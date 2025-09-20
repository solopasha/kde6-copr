%global commit0 c38811d16e3b22c1d49702ca493824363b643b3b
%global shortcommit0 %{sub %{commit0} 1 7}
%global bumpver 2

Name:           plasma5support
Summary:        Support components for porting from KF5/Qt5 to KF6/Qt6
Version:        6.5.80%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}

License:        CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://invent.kde.org/plasma/%{name}
%plasma_source

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  qt6-qtbase-private-devel

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6Holidays)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IdleTime)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NetworkManagerQt)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6UnitConversion)

BuildRequires:  cmake(KSysGuard)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(PlasmaActivities)

BuildRequires:  pkgconfig(libgps)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xfixes)

Requires:       kf6-filesystem

# Renamed from kf6-plasma5support
Obsoletes:      kf6-plasma5support < 1:%{version}-%{release}
Provides:       kf6-plasma5support = 1:%{version}-%{release}

Obsoletes:      plasma-workspace-geolocation < 6.2.80
Provides:       plasma-workspace-geolocation = %{version}-%{release}
Provides:       plasma-workspace-geolocation%{?_isa} = %{version}-%{release}
Obsoletes:      plasma-workspace-geolocation-libs < 6.2.80
Provides:       plasma-workspace-geolocation-libs = %{version}-%{release}
Provides:       plasma-workspace-geolocation-libs%{?_isa} = %{version}-%{release}

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

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%dir %{_kf6_datadir}/plasma/weather_legacy
%{_kf6_datadir}/plasma/weather_legacy/noaa_station_list.xml
%{_kf6_datadir}/plasma5support/
%{_kf6_datadir}/qlogging-categories6/plasma5support.categories
%{_kf6_datadir}/qlogging-categories6/plasma5support.renamecategories
%{_kf6_libdir}/libplasma-geolocation-interface.so.%{version_no_git}
%{_kf6_libdir}/libplasma-geolocation-interface.so.6
%{_kf6_libdir}/libPlasma5Support.so.%{version_no_git}
%{_kf6_libdir}/libPlasma5Support.so.6
%{_kf6_libdir}/libweather_ion.so.7{,.*}
%{_kf6_qtplugindir}/plasma5support/
%{_qt6_qmldir}/org/kde/plasma/plasma5support/

%files devel
%{_includedir}/plasma/
%{_includedir}/[Pp]lasma5[Ss]upport/
%{_kf6_libdir}/cmake/Plasma5Support/
%{_kf6_libdir}/libplasma-geolocation-interface.so
%{_kf6_libdir}/libPlasma5Support.so
%{_kf6_libdir}/libweather_ion.so

%changelog
%{?kde_snapshot_changelog_entry}
* Fri Jan 10 2025 Pavel Solovev <daron439@gmail.com> - 6.2.90-2
- Add missing provides

* Thu Jan 09 2025 Pavel Solovev <daron439@gmail.com> - 6.2.90-1
- Update to 6.2.90

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
