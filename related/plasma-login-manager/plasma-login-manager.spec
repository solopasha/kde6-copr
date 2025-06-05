%global commit0 09132f0622822e87c6628895a8de2eed850eccea
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 11

%global selinuxtype targeted

Name:           plasma-login-manager
Summary:        Plasma Login Manager
Version:        0.21.0%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}

License:        GPL-2.0-or-later
URL:            https://invent.kde.org/plasma/plasma-login-manager
Source0:        %{url}/-/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

Source10:       sddm.pam
Source11:       sddm-autologin.pam
Source12:       sddm-greeter.pam

Source20:       plasmalogin.fc
Source21:       plasmalogin.te

Patch:          revert-bc6341a.patch

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
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickTest)
BuildRequires:  cmake(Qt6Test)

BuildRequires:  cmake(LayerShellQt)
BuildRequires:  cmake(LibKWorkspace)
BuildRequires:  cmake(PlasmaQuick)

BuildRequires:  pam-devel
BuildRequires:  shadow-utils
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-xkb)

Obsoletes:      plasma-login < 6.3.0~1.git41bcb26-2

Requires:       systemd
Requires:       (%{name}-selinux = %{version}-%{release} if selinux-policy-%{selinuxtype})

%description
%{summary}.

%package          selinux
BuildArch:        noarch
Summary:          SELinux support for %{name}
BuildRequires:    selinux-policy-devel
Requires(post):   %{name}
Requires(preun):  %{name}
Requires(preun):  policycoreutils
%{?selinux_requires}

%description selinux
SELinux support for %{name}.

%files selinux
%{_datadir}/selinux/packages/%{selinuxtype}/plasmalogin.pp.*
%ghost %verify(not md5 size mtime) %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/plasmalogin

%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/plasmalogin.pp.bz2
%selinux_relabel_post -s %{selinuxtype}

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{name}
    %selinux_relabel_post -s %{selinuxtype}
fi

%install -a
mkdir selinux
cp -p %{SOURCE20} %{SOURCE21} selinux/
pushd selinux
make -f %{_datadir}/selinux/devel/Makefile plasmalogin.pp
bzip2 -9 plasmalogin.pp
install -D -m 0644 plasmalogin.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/plasmalogin.pp.bz2
popd

install -Dpm 644 %{SOURCE10} %{buildroot}%{_sysconfdir}/pam.d/plasmalogin
install -Dpm 644 %{SOURCE11} %{buildroot}%{_sysconfdir}/pam.d/plasmalogin-autologin
install -Dpm 644 %{SOURCE12} %{buildroot}%{_sysconfdir}/pam.d/plasmalogin-greeter

mv %{buildroot}%{_datadir}/dbus-1/system.d/org.freedesktop.DisplayManager.conf \
   %{buildroot}%{_datadir}/dbus-1/system.d/org.freedesktop.DisplayManager-plasmalogin.conf

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/*.desktop

%post
%systemd_post plasmalogin.service

%preun
%systemd_preun plasmalogin.service

%postun
%systemd_postun plasmalogin.service

%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/pam.d/plasmalogin*
%{_kf6_bindir}/plasma-login-wallpaper
%{_kf6_bindir}/plasmalogin
%{_kf6_bindir}/startplasma-login-wayland
%{_kf6_datadir}/applications/kcm_plasmalogin.desktop
%{_kf6_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmplasmalogin.service
%{_kf6_datadir}/dbus-1/system.d/org.freedesktop.DisplayManager-plasmalogin.conf
%{_kf6_datadir}/dbus-1/system.d/org.kde.kcontrol.kcmplasmalogin.conf
%{_kf6_datadir}/plasmalogin/
%{_kf6_datadir}/polkit-1/actions/org.kde.kcontrol.kcmplasmalogin.policy
%{_kf6_libexecdir}/kauth/kcmplasmalogin_authhelper
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_plasmalogin.so
%{_libexecdir}/plasma-login-greeter
%{_libexecdir}/plasmalogin-helper
%{_libexecdir}/plasmalogin-helper-start-x11user
%{_sysusersdir}/plasmalogin.conf
%{_tmpfilesdir}/plasmalogin.conf
%{_unitdir}/plasmalogin.service
%{_userunitdir}/plasma-login-kwin_wayland.service
%{_userunitdir}/plasma-login-wayland.target
%{_userunitdir}/plasma-login.service
%{_userunitdir}/plasma-wallpaper.service

%changelog
%{?kde_snapshot_changelog_entry}
* Wed Mar 26 2025 Pavel Solovev <daron439@gmail.com> - 6.3.0~1.git2b66fe0-1
- Initial build
