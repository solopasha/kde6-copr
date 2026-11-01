%global commit0 dd219c01bc74def5f21b2596b6d4a29ffda02347
%global shortcommit0 %{sub %{commit0} 1 7}
%global bumpver 14

Name:           plasma-keyboard
Epoch:          1
Version:        6.8.80%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
Summary:        Virtual Keyboard for Qt based desktops

License:        LGPL-2.1-only AND GPL-2.0-only AND CC0-1.0 AND LGPL-3.0-only AND GPL-3.0-or-later AND GPL-2.0-or-later AND GPL-3.0-only
URL:            https://invent.kde.org/plasma/plasma-keyboard
%plasma_source

BuildRequires:  desktop-file-utils

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(Qt6Quick)

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6Package)

BuildRequires:  cmake(PlasmaQuick)

BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  qt6-qtbase-private-devel

Requires:       (kcm-%{name}%{?_isa} if plasma-systemsettings%{?_isa})

%description
The plasma-keyboard is a virtual keyboard
based on Qt Virtual Keyboard designed to
integrate in Plasma.

%package -n     kcm-%{name}
Summary:        KDE KCM for %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}
%description -n kcm-%{name}
%{summary}.

%install -a
rm -r %{buildroot}%{_kf6_libdir}/libplasma-keyboard-virtualkeyboardplugin.a
%find_lang plasma-keyboard
%find_lang kcm_plasmakeyboard
%find_lang plasma-keyboard-virtualkeyboard

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.plasma.keyboard.desktop

%files -f plasma-keyboard.lang -f plasma-keyboard-virtualkeyboard.lang
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/plasma-keyboard
%{_kf6_datadir}/applications/org.kde.plasma.keyboard.desktop
%{_kf6_datadir}/config.kcfg/plasmakeyboardsettings.kcfg
%{_kf6_datadir}/plasma/keyboard/
%{_kf6_metainfodir}/org.kde.plasma.keyboard.metainfo.xml
%{_kf6_qmldir}/org/kde/plasma/keyboard/

%files -n kcm-%{name} -f kcm_plasmakeyboard.lang
%{_kf6_datadir}/applications/kcm_plasmakeyboard.desktop
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_plasmakeyboard.so

%changelog
%{?kde_snapshot_changelog_entry}
* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Tue Jul 14 2026 Steve Cossette <farchord@gmail.com> - 1:6.7.3-1
- 6.7.3

* Wed Jul 01 2026 Steve Cossette <farchord@gmail.com> - 1:6.7.2-1
- 6.7.2

* Tue Jun 23 2026 Steve Cossette <farchord@gmail.com> - 1:6.7.1-1
- 6.7.1

* Thu Jun 11 2026 Steve Cossette <farchord@gmail.com> - 1:6.7.0-1
- 6.7.0

* Fri May 29 2026 Steve Cossette <farchord@gmail.com> - 1:6.6.91-1
- 6.6.91

* Sat May 16 2026 Steve Cossette <farchord@gmail.com> - 1:6.6.90-1
- 6.6.90

* Thu May 14 2026 Steve Cossette <farchord@gmail.com> - 1:6.6.5-1
- 6.6.5

* Thu May 14 2026 Jan Grulich <jgrulich@redhat.com> - 1:6.6.4-3
- Rebuild (qt6)

* Thu Apr 16 2026 Jan Grulich <jgrulich@redhat.com> - 1:6.6.4-2
- Rebuild (qt6)

* Fri Apr 10 2026 Steve Cossette <farchord@gmail.com> - 1:6.6.4-1
- 6.6.4

* Wed Apr 01 2026 Jan Grulich <jgrulich@redhat.com> - 1:6.6.3-2
- Fix corrupted text on selection
  Resolves: bz#2449945

* Tue Mar 17 2026 Steve Cossette <farchord@gmail.com> - 1:6.6.3-1
- 6.6.3

* Tue Mar 03 2026 Steve Cossette <farchord@gmail.com> - 1:6.6.2-1
- 6.6.2

* Tue Feb 24 2026 Steve Cossette <farchord@gmail.com> - 1:6.6.1-1
- 6.6.1

* Thu Feb 12 2026 Steve Cossette <farchord@gmail.com> - 1:6.6.0-1
- 6.6.0

* Tue Jan 27 2026 Steve Cossette <farchord@gmail.com> - 1:6.5.91-1
- 6.5.91

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.5.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Tue Jan 13 2026 farchord@gmail.com - 1:6.5.90-1
- 6.5.90

* Sun Dec 21 2025 Alessandro Astone <ales.astone@gmail.com> - 1:0.1.0-2
- Requires kcm if systemsettings is installed

* Tue Nov 11 2025 Alessandro Astone <ales.astone@gmail.com> - 1:0.1.0-1
- First official release 0.1.0
- Bump epoch

* Thu Oct 02 2025 Jan Grulich <jgrulich@redhat.com> - 1.0~20250824.094649.6bf37e5-2
- Rebuild (qt6)

* Sat Feb 15 2025 Steve Cossette <farchord@gmail.com> - 1.0~20250824.094649.6bf37e5-1
- Initial
