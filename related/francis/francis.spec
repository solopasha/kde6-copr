Name:           francis
Version:        1.1.0
Release:        1%{?dist}
License:        GPL-3.0-or-later AND CC0-1.0 AND LGPL-2.1-or-later
Summary:        Track your time
URL:            https://invent.kde.org/utilities/francis
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        signing-key.pgp

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6Notifications)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake(KF6KirigamiAddons)

Requires:       qt6qml(org.kde.coreaddons)
Requires:       qt6qml(org.kde.kirigami)
Requires:       qt6qml(org.kde.kirigamiaddons.formcard)
Requires:       qt6qml(org.kde.notification)

%description
Francis uses the well-known pomodoro technique to help you get more productive.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/*.desktop

%find_lang %{name}

%files -f %{name}.lang
%license LICENSES/*.txt
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.%{name}.svg
%{_kf6_metainfodir}/org.kde.%{name}.metainfo.xml


%changelog
* Wed Feb 28 2024 Pavel Solovev <daron439@gmail.com> - 1.1.0-1
- Initial build
