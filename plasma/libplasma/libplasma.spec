%global commit0 87f07a85fdf1865e7f216b85d6cc9ebb5a59088f
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

Name:    libplasma
Version: 6.2.3
Release: 1%{?dist}
Summary: Plasma is the foundation of the KDE user interface (v6)

# LicenseRef-QtCommercial is also in the licenses, but is being omitted as it is optional.
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only) AND Qt-LGPL-exception-1.1
URL:     https://invent.kde.org/plasma/plasma-framework
%plasma_source

BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6KirigamiPlatform)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6WindowSystem)

BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}

BuildRequires:  cmake(PlasmaActivities)

BuildRequires:  cmake(PlasmaWaylandProtocols)

BuildRequires:  wayland-devel

Requires:       kf6-filesystem

# Renamed from kf6-plasma
Obsoletes:      kf6-plasma < 1:%{version}-%{release}
Provides:       kf6-plasma = 1:%{version}-%{release}
Provides:       kf6-plasma%{_isa} = 1:%{version}-%{release}

Obsoletes:      plasma-framework < %{version}-%{release}
Provides:       plasma-framework = %{version}-%{release}
Provides:       plasma-framework%{_isa} = %{version}-%{release}

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6Package)
Requires:       qt6-qtbase-devel
Requires:       cmake(KF6Service)
Requires:       cmake(KF6WindowSystem)
Obsoletes:      kf6-plasma-devel < 1:%{version}-%{release}
Provides:       kf6-plasma-devel = 1:%{version}-%{release}
Provides:       kf6-plasma-devel%{_isa} = 1:%{version}-%{release}
Obsoletes:      plasma-framework-devel < %{version}-%{release}
Provides:       plasma-framework-devel = %{version}-%{release}
Provides:       plasma-framework-devel%{_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name}6 --all-name --with-man --all-name

# create/own dirs
mkdir -p %{buildroot}%{_kf6_datadir}/plasma/plasmoids
mkdir -p %{buildroot}%{_kf6_qmldir}/org/kde/private

%files -f %{name}6.lang
%dir %{_kf6_qmldir}/org
%dir %{_kf6_qmldir}/org/kde
%dir %{_kf6_qmldir}/org/kde/private
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/plasma/
%{_kf6_datadir}/qlogging-categories6/*plasma*
%{_kf6_libdir}/libPlasma.so.%{version_no_git}
%{_kf6_libdir}/libPlasma.so.6
%{_kf6_libdir}/libPlasmaQuick.so.%{version_no_git}
%{_kf6_libdir}/libPlasmaQuick.so.6
%{_kf6_plugindir}/kirigami/
%{_kf6_plugindir}/packagestructure/
%{_kf6_qmldir}/org/kde/kirigami/styles/Plasma/
%{_kf6_qmldir}/org/kde/plasma/

%files devel
%{_includedir}/Plasma/
%{_includedir}/PlasmaQuick/
%dir %{_kf6_datadir}/kdevappwizard
%{_kf6_datadir}/kdevappwizard/templates/
%{_kf6_libdir}/cmake/Plasma/
%{_kf6_libdir}/cmake/PlasmaQuick/
%{_kf6_libdir}/libPlasma.so
%{_kf6_libdir}/libPlasmaQuick.so

%changelog
* Tue Nov 05 2024 Pavel Solovev <daron439@gmail.com> - 6.2.3-1
- Update to 6.2.3

* Thu Oct 31 2024 Pavel Solovev <daron439@gmail.com> - 6.2.2-2
- rebuilt

* Tue Oct 22 2024 Pavel Solovev <daron439@gmail.com> - 6.2.2-1
- Update to 6.2.2

* Tue Oct 15 2024 Pavel Solovev <daron439@gmail.com> - 6.2.1-1
- Update to 6.2.1

* Thu Oct 03 2024 Pavel Solovev <daron439@gmail.com> - 6.2.0-1
- Update to 6.2.0

* Tue Sep 10 2024 Pavel Solovev <daron439@gmail.com> - 6.1.5-1
- Update to 6.1.5

* Tue Aug 06 2024 Pavel Solovev <daron439@gmail.com> - 6.1.4-1
- Update to 6.1.4

* Tue Jul 16 2024 Pavel Solovev <daron439@gmail.com> - 6.1.3-1
- Update to 6.1.3

* Tue Jul 02 2024 Pavel Solovev <daron439@gmail.com> - 6.1.2-1
- Update to 6.1.2

* Tue Jun 25 2024 Pavel Solovev <daron439@gmail.com> - 6.1.1-1
- Update to 6.1.1

* Tue Jun 18 2024 Pavel Solovev <daron439@gmail.com> - 6.1.0-1
- Update to 6.1.0

* Fri May 24 2024 Pavel Solovev <daron439@gmail.com> - 6.0.90-1
- Update to 6.0.90

* Tue May 21 2024 Pavel Solovev <daron439@gmail.com> - 6.0.5-1
- Update to 6.0.5

* Tue Apr 16 2024 Pavel Solovev <daron439@gmail.com> - 6.0.4-1
- Update to 6.0.4

* Tue Mar 26 2024 Pavel Solovev <daron439@gmail.com> - 6.0.3-1
- Update to 6.0.3

* Wed Mar 20 2024 Pavel Solovev <daron439@gmail.com> - 6.0.2-2
- qmlcache rebuild

* Mon Nov 13 2023 Alessandro Astone <ales.astone@gmail.com> - 5.27.80-3
- Provide kf6-plasma%%{_isa}

* Sun Nov 12 2023 Alessandro Astone <ales.astone@gmail.com> - 5.27.80-2
- Add Obsoletes/Provides to the devel subpackage

* Fri Nov 10 2023 Alessandro Astone <ales.astone@gmail.com> - 5.27.80-1
- Renamed from kf6-plasma
- 5.27.80

* Fri Nov 10 2023 Alessandro Astone <ales.astone@gmail.com> - 5.240.0^20231012.020924.59e67fc-1
- Rebuild for kf6-kirigami2
- Update git snapshot to be buildable against new kf6-knotifications
- This package is about to be obsoleted, but for now it has to be installable

* Tue Oct 17 2023 Jan Grulich <jgrulich@redhat.com> - 5.240.0^20231012.020924.b3da7d9-2
- Rebuild (qt6)

* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231012.020924.b3da7d9-1
- Initial release
