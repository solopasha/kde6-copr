%global commit0 35a95944ca2257e719feee885928ca0cdb59f923
%global shortcommit0 %{sub %{commit0} 1 7}
%global bumpver 6

Name:           plasma-bigscreen
Summary:        Plasma shell for TVs
Version:        6.4.80%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}

License:        CC0-1.0 AND GPL-2.0-or-later AND (GPL-2.0-only OR GPL-3.0-only) AND LGPL-2.0-or-later AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:            https://invent.kde.org/plasma/plasma-bigscreen
%kde_meta

ExclusiveArch:  %{qt6_qtwebengine_arches}

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires:  cmake(KF6BluezQt)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6WindowSystem)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6WebEngineCore)
BuildRequires:  cmake(Qt6WebEngineQuick)

BuildRequires:  cmake(KF6Screen)
BuildRequires:  cmake(LibKWorkspace)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(PlasmaActivities)
BuildRequires:  cmake(PlasmaActivitiesStats)

BuildRequires:  cmake(QCoro6Core)
BuildRequires:  cmake(QCoro6Qml)
BuildRequires:  cmake(QCoro6Quick)

Requires:       kde-connect%{?_isa}
Requires:       kf6-kdeclarative%{?_isa}
Requires:       kf6-kirigami-addons%{?_isa}
Requires:       kf6-kirigami%{?_isa}
Requires:       kf6-kitemmodels%{?_isa}
Requires:       kf6-ksvg%{?_isa}
Requires:       plasma-milou%{?_isa} >= %{majmin_ver_kf6}
Requires:       plasma-nano%{?_isa} >= %{majmin_ver_kf6}
Requires:       plasma-nm%{?_isa} >= %{majmin_ver_kf6}
Requires:       plasma-pa%{?_isa} >= %{majmin_ver_kf6}
Requires:       plasma-workspace%{?_isa} >= %{majmin_ver_kf6}
Requires:       plasma5support%{?_isa} >= %{majmin_ver_kf6}
Requires:       qt6-qt5compat%{?_isa}
Requires:       qt6-qtmultimedia%{?_isa}

Obsoletes:      %{name}-wayland < 6.4.80
Provides:       %{name}-wayland = %{version}-%{release}
Provides:       %{name}-wayland%{?_isa} = %{version}-%{release}

%description
Plasma Bigscreen is a user-friendly, open-source interface designed for
devices like HTPCs and SBCs connected to TVs and projectors.
It provides an intuitive experience that allows for easy navigation
from a distance using remote controls.

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/*.xml

%files -f %{name}.lang
%{_kf6_bindir}/plasma-bigscreen-common-env
%{_kf6_bindir}/plasma-bigscreen-envmanager
%{_kf6_bindir}/plasma-bigscreen-settings
%{_kf6_bindir}/plasma-bigscreen-swap-session
%{_kf6_bindir}/plasma-bigscreen-uvcviewer
%{_kf6_bindir}/plasma-bigscreen-wayland
%{_kf6_bindir}/plasma-bigscreen-webapp
%{_kf6_datadir}/applications/kcm_mediacenter_*.desktop
%{_kf6_datadir}/applications/org.kde.plasma.bigscreen.uvcviewer.desktop
%{_kf6_datadir}/applications/plasma-bigscreen-swap-session.desktop
%{_kf6_datadir}/plasma/look-and-feel/org.kde.plasma.bigscreen/
%{_kf6_datadir}/plasma/plasmoids/org.kde.bigscreen.homescreen/
%{_kf6_datadir}/plasma/shells/org.kde.plasma.bigscreen/
%{_kf6_datadir}/sounds/plasma-bigscreen/
%{_kf6_datadir}/wayland-sessions/plasma-bigscreen-wayland.desktop
%{_kf6_metainfodir}/org.kde.plasma.bigscreen.metainfo.xml
%{_kf6_qmldir}/org/kde/bigscreen/
%{_kf6_qtplugindir}/plasma/applets/org.kde.bigscreen.homescreen.so
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_mediacenter_*.so

%changelog
%{?kde_snapshot_changelog_entry}
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.27.80~20240204.214319.046d404-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.27.80~20240204.214319.046d404-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.27.80~20240204.214319.046d404-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue May 21 2024 Jan Grulich <jgrulich@redhat.com> - 5.27.80~20240204.214319.046d404-4
- Rebuild (qt6)

* Thu Apr 04 2024 Jan Grulich <jgrulich@redhat.com> - 5.27.80~20240204.214319.046d404-3
- Rebuild (qt6)

* Mon Mar 18 2024 Steve Cossette <farchord@gmail.com> - 5.27.80~20240204.214319.046d404-2
- Building to accomodate new depend library sonames

* Mon Feb 05 2024 Steve Cossette <farchord@gmail.com> - 5.27.80~20240204.214319.046d404-1
- Updated to Qt6

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.27.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.27.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Nov 05 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.9-1
- 5.27.9

* Sun Oct 15 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.8-1
- Update to 5.27.8

* Thu Mar 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.2-4
- Fixes on the spec file

* Thu Mar 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.2-3
- Add plasma-workspace requirements.

* Thu Mar 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.2-2
- Create wayland/x11 subpackages

* Wed Mar 01 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.2-1
- Update to 5.27.2

* Sun Jan 22 2023 Marc Deop <marcdeop@fedoraproject.org> - 5.26.90-1
- Initial Package
