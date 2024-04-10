%global commit0 b62c6f8a6932f70282d90a88150d068648182dd1
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

Name:           kalm
Version:        24.05.0%{?bumpver:^%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
License:        LGPL-2.1-or-later AND CC0-1.0
Summary:        Kalm can teach you different breathing techniques
URL:            https://invent.kde.org/utilities/francis
%apps_source

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6I18n)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6QQC2DesktopStyle)

Requires:       kf6-kirigami-addons%{?_isa}
Requires:       kf6-kirigami%{?_isa}
Requires:       kf6-qqc2-desktop-style%{?_isa}

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

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/*.xml || :
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/*.desktop

%find_lang %{name}

%files -f %{name}.lang
%license LICENSES/*.txt
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.%{name}.svg
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml

%changelog
* Fri Apr 26 2024 Pavel Solovev <daron439@gmail.com> - 24.04.80-1
- Initial build
