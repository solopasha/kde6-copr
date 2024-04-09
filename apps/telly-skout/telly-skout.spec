Name:           telly-skout
Version:        24.02.2
Release:        1%{?dist}
Summary:        Convergent TV guide based on Kirigami
License:        LGPL-2.1-or-later
URL:            https://invent.kde.org/utilities/telly-skout
%apps_source

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf5-rpm-macros
BuildRequires:  libappstream-glib

BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KirigamiAddons)

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)

Requires:       kf5-kirigami2%{?_isa}
Requires:       kf5-kirigami2-addons%{?_isa}

%description
%{summary}.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1


%build
%cmake_kf5
%cmake_build


%install
%cmake_install

%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%doc README.md
%license LICENSES/*
%{_kf5_bindir}/%{name}
%{_kf5_datadir}/applications/org.kde.telly-skout.desktop
%{_kf5_datadir}/icons/hicolor/scalable/apps/org.kde.telly-skout.svg
%{_kf5_metainfodir}/org.kde.telly-skout.appdata.xml


%changelog
* Thu Apr 11 2024 Pavel Solovev <daron439@gmail.com> - 24.02.2-1
- Update to 24.02.2

* Thu Mar 21 2024 Pavel Solovev <daron439@gmail.com> - 24.02.1-1
- Update to 24.02.1
