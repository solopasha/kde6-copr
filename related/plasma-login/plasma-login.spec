%global commit0 41bcb26e4235478f87a64872167f51a1d7492eb6
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

Name:           plasma-login
Summary:        Plasma Login
Version:        6.3.0%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}

License:        GPL-2.0-or-later AND LGPL-2.0-or-later AND (GPL-2.0-only OR GPL-3.0-only) AND CC0-1.0
URL:            https://invent.kde.org/davidedmundson/plasma-login
Source:         %{url}/-/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
BuildSystem:    cmake_kf6

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  systemd-rpm-macros

BuildRequires:  cmake(KF6Auth)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6WindowSystem)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Quick)

BuildRequires:  cmake(LayerShellQt)
BuildRequires:  cmake(LibKWorkspace)
BuildRequires:  cmake(PlasmaQuick)

%description
%{summary}.

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/*.desktop

%files
%doc README.md
%{_kf6_bindir}/plasma-login-wallpaper
%{_kf6_bindir}/startplasma-login-wayland
%{_kf6_datadir}/applications/kcm_plasmalogin.desktop
%{_kf6_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmplasmalogin.service
%{_kf6_datadir}/dbus-1/system.d/org.kde.kcontrol.kcmplasmalogin.conf
%{_kf6_datadir}/polkit-1/actions/org.kde.kcontrol.kcmplasmalogin.policy
%{_kf6_libexecdir}/kauth/kcmplasmalogin_authhelper
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_plasmalogin.so
%{_libexecdir}/plasma-login-greeter
%{_userunitdir}/plasma-login-kwin_wayland.service
%{_userunitdir}/plasma-login-wayland.target
%{_userunitdir}/plasma-login.service
%{_userunitdir}/plasma-wallpaper.service

%changelog
%{?kde_snapshot_changelog_entry}
* Wed Mar 26 2025 Pavel Solovev <daron439@gmail.com> - 6.3.0~1.gitb067aeb-1
- Initial build
