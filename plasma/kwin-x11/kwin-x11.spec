%global commit0 afde0aab9e9d36dad25433b92867c8e063a51bbb
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 2

Name:           kwin-x11
Version:        6.4.80%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
Summary:        An X11 window manager and a compositing manager

License:        BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-GPL AND LicenseRef-KDE-Accepted-LGPL AND MIT
URL:            https://invent.kde.org/plasma/kwin-x11
%plasma_source

BuildRequires:  systemd-rpm-macros

BuildRequires:  cmake(KF6Auth)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IdleTime)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)

BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Sensors)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6UiTools)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  qt6-qtbase-private-devel

BuildRequires:  cmake(Breeze)
BuildRequires:  cmake(KDecoration3)
BuildRequires:  cmake(KGlobalAccelD)
BuildRequires:  cmake(KScreenLocker)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(PlasmaActivities)

BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(QAccessibilityClient6)
BuildRequires:  hwdata-devel
BuildRequires:  libcap-devel
BuildRequires:  libX11-devel
BuildRequires:  libxcb-devel
BuildRequires:  libXi-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xwayland)
BuildRequires:  wayland-devel
BuildRequires:  xcb-util-cursor-devel
BuildRequires:  xcb-util-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  xcb-util-wm-devel

## Runtime deps
Requires:       aurorae%{?_isa} >= %{majmin_ver_kf6}
Requires:       kf6-kcmutils%{?_isa}
Requires:       kf6-kconfig%{?_isa}
Requires:       kf6-kdeclarative%{?_isa}
Requires:       kf6-kirigami%{?_isa}
Requires:       kf6-kitemmodels%{?_isa}
Requires:       kf6-knewstuff%{?_isa}
Requires:       kf6-kquickcharts%{?_isa}
Requires:       kf6-ksvg%{?_isa}
Requires:       kscreenlocker%{?_isa} >= %{majmin_ver_kf6}
Requires:       libplasma%{?_isa} >= %{majmin_ver_kf6}
Requires:       plasma-milou%{?_isa} >= %{majmin_ver_kf6}
Requires:       qt6-qt5compat%{?_isa}
Requires:       qt6-qtdeclarative%{?_isa}
Requires:       qt6-qtmultimedia%{?_isa}
Requires:       xorg-x11-server-Xorg%{?_isa}
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}

# http://bugzilla.redhat.com/605675
Provides:       firstboot(windowmanager) = kwin_x11

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       cmake(Qt6Core)
Requires:       cmake(Qt6Gui)
Requires:       cmake(Qt6Quick)
Requires:       cmake(KF6Config)
Requires:       cmake(KF6CoreAddons)
Requires:       cmake(KF6WindowSystem)
Requires:       pkgconfig(wayland-server)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%install -a

%files -f %{name}.lang
%license LICENSES/*.txt
%{_kf6_bindir}/kwin_x11
%{_kf6_datadir}/%{name}/
%{_kf6_datadir}/applications/*.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}.*
%{_kf6_datadir}/kconf_update/%{name}.upd
%{_kf6_datadir}/knotifications6/%{name}.notifyrc
%{_kf6_datadir}/knsrcfiles/*-x11.knsrc
%{_kf6_datadir}/krunner/dbusplugins/kwin-runner-windows-x11.desktop
%{_kf6_datadir}/qlogging-categories6/org_kde_kwin_x11.categories
%{_kf6_libdir}/kconf_update_bin/kwin-6.0-delete-desktop-switching-shortcuts-x11
%{_kf6_libdir}/kconf_update_bin/kwin-6.0-remove-breeze-tabbox-default-x11
%{_kf6_libdir}/kconf_update_bin/kwin-6.0-reset-active-mouse-screen-x11
%{_kf6_libdir}/kconf_update_bin/kwin-6.1-remove-gridview-expose-shortcuts-x11
%{_kf6_libdir}/kconf_update_bin/kwin-6.5-showpaint-changes-x11
%{_kf6_libdir}/kconf_update_bin/kwin5_update_default_rules_x11
%{_kf6_libdir}/lib%{name}.so.6{,.*}
%{_kf6_libdir}/libkcmkwincommon-x11.so.6{,.*}
%{_kf6_qtplugindir}/%{name}/
%{_kf6_qtplugindir}/kf6/packagestructure/kwin_*_x11.so
%{_kf6_qtplugindir}/plasma/kcms/systemsettings_qwidgets/*.so
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/*.so
%{_libexecdir}/kwin_killer_helper_x11
%{_libexecdir}/kwin-applywindowdecoration-x11
%{_qt6_qmldir}/org/kde/kwin_x11/
%{_userunitdir}/plasma-kwin_x11.service

%files devel
%{_includedir}/%{name}/
%{_kf6_datadir}/dbus-1/interfaces/*.xml
%{_kf6_libdir}/cmake/KWinX11/
%{_kf6_libdir}/cmake/KWinX11DBusInterface/
%{_kf6_libdir}/lib%{name}.so

%changelog
%{?kde_snapshot_changelog_entry}
* Mon Mar 10 2025 Pavel Solovev <daron439@gmail.com> - 6.3.80~1-1
- Initial package
