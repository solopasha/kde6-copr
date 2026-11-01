%global commit0 76206394f226c7d5af52037b0feeee15d78db0f6
%global shortcommit0 %{sub %{commit0} 1 7}
%global bumpver 11

Name:           keepsecret
Version:        26.11.70%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
Summary:        Client for a Secret Service compatible provider

License:        BSD-2-Clause AND BSD-3-Clause AND CC-BY-4.0 AND CC0-1.0 AND FSFAP AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://invent.kde.org/utilities/keepsecret
%apps_source

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Crash)

BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  cmake(KF6KirigamiAppComponents)

Requires:       qt6qml(org.kde.kirigamiaddons.components)
Requires:       qt6qml(org.kde.kirigamiaddons.formcard)
Requires:       qt6qml(org.kde.config)
Requires:       qt6qml(org.kde.coreaddons)
Requires:       qt6qml(org.kde.kirigami)
Requires:       qt6qml(org.kde.kitemmodels)
Requires:       hicolor-icon-theme

%description
KeepSecret is a Password manager GUI intended to be a
client for a Secret Service compatible provider.

%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1

%build
%cmake
%cmake_build

%install
%cmake_install
%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.keepsecret.*.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.keepsecret.desktop

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/keepsecret
%{_kf6_datadir}/applications/org.kde.keepsecret.desktop
%{_kf6_metainfodir}/org.kde.keepsecret.metainfo.xml
%{_kf6_datadir}/qlogging-categories6/keepsecret.categories
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.keepsecret.svg

%changelog
%{?kde_snapshot_changelog_entry}
