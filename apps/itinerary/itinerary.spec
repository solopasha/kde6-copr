%global commit0 5e644bd93a568fbc49fc6415742097f052b03017
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

Name:           itinerary
Version:        24.08.1
Release:        1%{?dist}
Summary:        Itinerary and boarding pass management application

License:        Apache-2.0 and BSD-3-Clause and LGPL-2.0-or-later AND CC0-1.0
URL:            https://apps.kde.org/en-gb/itinerary/
%apps_source

# Compile Tools
BuildRequires:  cmake
BuildRequires:  gcc-c++

# Fedora
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib

# Qt
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Positioning)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}

# KDE Frameworks
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6FileMetaData)
BuildRequires:  cmake(KF6Holidays)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NetworkManagerQt)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6QQC2DesktopStyle)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6UnitConversion)
BuildRequires:  cmake(KF6WindowSystem)

BuildRequires:  cmake(KF6KirigamiAddons)

# KDE PIM
BuildRequires:  cmake(KPim6PkPass)
BuildRequires:  cmake(KPim6Itinerary)

# KDE Libraries
BuildRequires:  cmake(KPublicTransport)
BuildRequires:  cmake(KOSMIndoorMap)
BuildRequires:  cmake(KHealthCertificate)
BuildRequires:  cmake(QuotientQt6)

# Misc
BuildRequires:  pkgconfig(zlib)
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

# Runtime requirements
Requires:       qt6-qtlocation
Requires:       qt6-qtmultimedia
Requires:       kf6-kitemmodels
Requires:       kf6-prison
Requires:       kf6-kirigami
Requires:       kf6-kirigami-addons

%description
%summary.

%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1

%build
%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build

%install
%cmake_install
%find_lang kde-itinerary
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.itinerary.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files -f kde-itinerary.lang
%license LICENSES/*
%{_kf6_bindir}/itinerary
%{_kf6_datadir}/applications/org.kde.itinerary.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.itinerary.svg
%{_kf6_datadir}/knotifications6/itinerary.notifyrc
%{_kf6_datadir}/qlogging-categories6/org_kde_itinerary.categories
%{_kf6_libdir}/libSolidExtras.so
%{_kf6_metainfodir}/org.kde.itinerary.appdata.xml
%{_qt6_plugindir}/kf6/kfilemetadata/kfilemetadata_itineraryextractor.so
%{_qt6_plugindir}/kf6/thumbcreator/itinerarythumbnail.so
%{_qt6_qmldir}/org/kde/solidextras/

%changelog
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

* Sat Oct 14 2023 Steve Cossette <farchord@gmail.com> - 23.08.2-1
- Initial Release
