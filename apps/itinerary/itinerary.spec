Name:           itinerary
Version:        24.01.85
Release:        1%{?dist}
Summary:        Itinerary and boarding pass management application

License:        Apache-2.0 and BSD-3-Clause and LGPL-2.0-or-later AND CC0-1.0
URL:            https://apps.kde.org/en-gb/itinerary/
%apps_source
Patch:          https://invent.kde.org/pim/itinerary/-/merge_requests/236.patch

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
Requires:       kirigami-addons

%description
%summary.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

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
* Mon Dec 18 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80

* Sat Oct 14 2023 Steve Cossette <farchord@gmail.com> - 23.08.2-1
- Initial Release
