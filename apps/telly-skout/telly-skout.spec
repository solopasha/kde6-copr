%global commit0 47b6fd3bdebe5f7f30fcb0a47f79d1c0b12052c1
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 2

Name:           telly-skout
Version:        24.02.1%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
Summary:        Convergent TV guide based on Kirigami
License:        LGPL-2.1-or-later
URL:            https://invent.kde.org/utilities/telly-skout
%apps_source

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Crash)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake(KF6KirigamiAddons)

Requires:       kf6-kirigami%{?_isa}
Requires:       kf6-kirigami-addons%{?_isa}

%description
%{summary}.


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
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/*.desktop


%files -f %{name}.lang
%doc README.md
%license LICENSES/*
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.telly-skout.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.telly-skout.svg
%{_kf6_metainfodir}/org.kde.telly-skout.appdata.xml


%changelog
%{?kde_snapshot_changelog_entry}
%autochangelog
