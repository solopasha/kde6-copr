%global base_name elisa

Name:       elisa-player
Version:    24.02.0
Release:    1%{?dist}
Summary:    Elisa music player

# Main program LGPLv3+
# Background image CC-BY-SA
License:    LGPLv3+ and CC-BY-SA
URL:        https://apps.kde.org/elisa
%apps_source

# Compile Tools
BuildRequires:  gcc-c++
BuildRequires:  cmake

# Tests
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

# KDE Frameworks
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Baloo)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6FileMetaData)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6QQC2DesktopStyle)

# Qt
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickTest)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6DBus)

# Runtime Dependencies
Requires:       hicolor-icon-theme
Requires:       kf6-kirigami2
Requires:       dbus-common

%description
Elisa is a simple music player aiming to provide a nice experience for its
users.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n elisa-%{version} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang elisa --all-name --with-kde --with-html

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.elisa.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.elisa.appdata.xml

%files -f elisa.lang
%license COPYING
%{_kf6_bindir}/elisa
%{_kf6_datadir}/applications/org.kde.elisa.desktop
%{_kf6_datadir}/dbus-1/services/org.kde.elisa.service
%{_kf6_datadir}/icons/hicolor/*/apps/elisa*
%{_kf6_datadir}/qlogging-categories6/elisa.categories
%{_kf6_metainfodir}/org.kde.elisa.appdata.xml
%{_kf6_libdir}/elisa/
%{_kf6_libdir}/qt6/qml/org/kde/elisa/

%changelog
%autochangelog
