%global commit0 118930c2be8f009e590dfa8f3a5a5eb5d85827e3
%global shortcommit0 %{sub %{commit0} 1 7}
%global bumpver 11

# Disable X11 for RHEL
%bcond x11 %[%{undefined rhel}]

Name:           plasma-login-manager
Version:        6.8.80%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
License:        BSD-3-Clause and CC0-1.0 and (GPL-2.0-only or GPL-3.0-only) and GPL-2.0-or-later and LGPL-2.0-or-later and LGPL-2.1-or-later
Summary:        QML based login manager from KDE

URL:            https://invent.kde.org/plasma/plasma-login-manager
%plasma_source

# README.scripts
Source10:       README.scripts
# sysconfig snippet
Source11:       plasmalogin.sysconfig
# sysusers config file. note these are shipped in the upstream tarball
# but we cannot use the files from the tarball for %pre scriptlet
# generation, so we duplicate them as source files for that purpose;
# this is an ugly hack that should be removed if it becomes possible.
# see https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/TFDMAU7KLMSQTKPJELHSM6PFVXIZ56GK/
Source12:       plasmalogin.sysusers
# sample plasmalogin.conf generated with plasmalogin --example-config, and entries commented-out
Source13:       plasmalogin.conf

# downstream patches
## plasmalogin.service: +EnvironmentFile=-/etc/sysconfig/plasmalogin
Patch1001:      plasmalogin-environment_file.patch
## Workaround for https://pagure.io/fedora-kde/SIG/issue/87
Patch1002:      plasmalogin-rpmostree-tmpfiles-hack.patch

Provides:       service(graphical-login) = plasmalogin

BuildRequires:  desktop-file-utils
BuildRequires:  cmake >= 3.22
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6ShaderTools)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6QuickTest)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6Auth)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6KirigamiPlatform)
BuildRequires:  cmake(PlasmaQuick)
BuildRequires:  cmake(LayerShellQt)
BuildRequires:  cmake(LibKWorkspace)
BuildRequires:  cmake(LibKLookAndFeel)
BuildRequires:  cmake(KF6Screen)
# verify presence to pull defaults from /etc/login.defs
BuildRequires:  shadow-utils
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
BuildRequires:  kf6-rpm-macros

# for jxl support
Requires:       kf6-kimageformats%{?_isa}

%if %{with x11}
Requires:       xorg-x11-xinit
%endif
%{?systemd_requires}

Requires:      kf6-filesystem
Requires:      kf6-kauth
Requires(pre): shadow-utils

Requires:      kde-settings-plasma

# Requires kwin-wayland
Requires:      kwin-wayland%{?_isa}
Requires:      (kcm-plasmalogin%{?_isa} if plasma-systemsettings%{?_isa})

%description
Plasma Login provides a display manager for KDE Plasma
and with an new frontend providing a greeter,
wallpaper plugin integration and a System Settings module (KCM).

%package -n kcm-plasmalogin
Summary: KDE KCM for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: dbus-common
Requires: plasma-systemsettings%{?_isa}
Requires: polkit
Requires: qt6-filesystem

%description -n kcm-plasmalogin
%{summary}.

%conf
%cmake_kf6 \
  -DCMAKE_BUILD_TYPE:STRING="Release" \
  -DPAM_OS_CONFIGURATION:STRING="fedora" \
  -DSESSION_COMMAND:PATH=/etc/X11/xinit/Xsession \
  -DWAYLAND_SESSION_COMMAND:PATH=/etc/plasmalogin/wayland-session

%install
%cmake_install

%find_lang plasma_login
%find_lang kcm_plasmalogin


mkdir -p %{buildroot}%{_sysconfdir}/plasmalogin.conf.d
mkdir -p %{buildroot}%{_prefix}/lib/plasmalogin/plasmalogin.conf.d

install -Dpm 644 %{SOURCE10} %{buildroot}%{_datadir}/plasmalogin/scripts/README.scripts
install -Dpm 644 %{SOURCE11} %{buildroot}%{_sysconfdir}/sysconfig/plasmalogin
install -Dpm 644 %{SOURCE13} %{buildroot}%{_sysconfdir}/plasmalogin.conf

mkdir -p %{buildroot}/run/plasmalogin
mkdir -p %{buildroot}%{_localstatedir}/lib/plasmalogin
mkdir -p %{buildroot}%{_sysconfdir}/plasmalogin/
cp -a %{buildroot}%{_datadir}/plasmalogin/scripts/* \
      %{buildroot}%{_sysconfdir}/plasmalogin/
# we're using /etc/X11/xinit/Xsession (by default) instead
rm -fv %{buildroot}%{_sysconfdir}/plasmalogin/Xsession

# De-conflict the dbus file
mv %{buildroot}%{_datadir}/dbus-1/system.d/org.freedesktop.DisplayManager.conf \
   %{buildroot}%{_datadir}/dbus-1/system.d/org.freedesktop.DisplayManager-plasmalogin.conf


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/kcm_plasmalogin.desktop


%pre
%sysusers_create_compat %{SOURCE12}


%post
%systemd_post plasmalogin.service
%systemd_user_post plasma-login.service plasma-login-kwin_wayland.service plasma-login-wayland.target plasma-wallpaper.service


%preun
%systemd_preun plasmalogin.service
%systemd_user_preun plasma-login.service plasma-login-kwin_wayland.service plasma-login-wayland.target plasma-wallpaper.service


%postun
%systemd_postun plasmalogin.service
%systemd_user_postun plasma-login.service plasma-login-kwin_wayland.service plasma-login-wayland.target plasma-wallpaper.service


%files -f plasma_login.lang
%license LICENSE LICENSE.* LICENSES/*
%doc README.md
%dir %{_sysconfdir}/plasmalogin/
%dir %{_sysconfdir}/plasmalogin.conf.d
%dir %{_prefix}/lib/plasmalogin
%dir %{_prefix}/lib/plasmalogin/plasmalogin.conf.d
%config(noreplace) %{_sysconfdir}/plasmalogin/*
%config(noreplace) %{_sysconfdir}/plasmalogin.conf
%config(noreplace) %{_sysconfdir}/sysconfig/plasmalogin
%{_prefix}/lib/pam.d/plasmalogin*
%{_datadir}/dbus-1/system.d/org.freedesktop.DisplayManager-plasmalogin.conf
%{_bindir}/plasmalogin
%{_bindir}/startplasma-login-wayland
%{_bindir}/plasma-login-wallpaper
%{_libexecdir}/plasmalogin-helper
%{_libexecdir}/plasmalogin-helper-start-x11user
%{_libexecdir}/plasma-login-greeter
%{_tmpfilesdir}/plasmalogin.conf
%{_sysusersdir}/plasmalogin.conf
%attr(0711, root, plasmalogin) %dir /run/plasmalogin
%attr(1770, plasmalogin, plasmalogin) %dir %{_localstatedir}/lib/plasmalogin
%{_unitdir}/plasmalogin.service
%{_userunitdir}/plasma-login.service
%{_userunitdir}/plasma-login-kwin_wayland.service
%{_userunitdir}/plasma-login-wayland.target
%{_userunitdir}/plasma-wallpaper.service
%dir %{_datadir}/plasmalogin
%{_datadir}/plasmalogin/scripts/


%files -n kcm-plasmalogin -f kcm_plasmalogin.lang
%{_kf6_libexecdir}/kauth/kcmplasmalogin_authhelper
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_plasmalogin.so
%{_datadir}/applications/kcm_plasmalogin.desktop
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmplasmalogin.service
%{_datadir}/dbus-1/system.d/org.kde.kcontrol.kcmplasmalogin.conf
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmplasmalogin.policy


%changelog
%{?kde_snapshot_changelog_entry}
