%global commit0 21b102066456f146a95101c89aacaedaa4eaa9fc
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

Name:           qrca
Version:        25.11.70%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
License:        CC0-1.0 AND BSD-3-Clause AND BSD-2-Clause AND GPL-2.0-or-later AND LGPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.1-or-later
Summary:        QR code scanner for KDE Plasma
URL:            https://invent.kde.org/utilities/qrca
%apps_source

BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6NetworkManagerQt)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Prison)
BuildRequires:  cmake(KF6Service)

Requires:       qt6qml(org.kde.config)
Requires:       qt6qml(org.kde.kirigami)
Requires:       qt6qml(org.kde.kirigamiaddons.formcard)
Requires:       qt6qml(org.kde.prison)
Requires:       qt6qml(org.kde.purpose)
Requires:       qt6qml(QtMultimedia)
Requires:       kf6-qqc2-desktop-style%{?_isa}

%description
Qrca is a simple application for Plasma Desktop and Plasma Mobile that lets
you scan many barcode formats and create your own QR code images.

%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/qrca
%{_kf6_datadir}/applications/org.kde.qrca.*desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.qrca.svg
%{_kf6_metainfodir}/org.kde.qrca.appdata.xml

%changelog
%{?kde_snapshot_changelog_entry}
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1~20241206.203647.da129cc-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 08 2024 Steve Cossette <farchord@gmail.com> - 0.1~20241206.203647.da129cc-1
- Initial Release
