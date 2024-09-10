%global commit0 5f22d5e06cce0dd14cc404c6b7a8faa2fb399d48
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

Name:           angelfish
Version:        24.08.1
Release:        1%{?dist}
Summary:        Plasma Mobile minimal web browser

# Cargo license summary:
# MIT
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR Zlib
# MPL-2.0
# Unlicense OR MIT
# Zlib OR Apache-2.0 OR MIT
License:        MIT and GPLv2+ and LGPLv2 and LGPLv2+ AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR Zlib) AND MPL-2.0 AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
# For a breakdown of the licensing, see PACKAGE-LICENSING
URL:            https://invent.kde.org/network/%{name}
%apps_source

%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

BuildRequires:  appstream
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib

BuildRequires:  cmake(FutureSQL6)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Purpose)
BuildRequires:  cmake(KF6QQC2DesktopStyle)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(QCoro6Core)
BuildRequires:  cmake(QCoro6Quick)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6WebEngineCore)
BuildRequires:  cmake(Qt6WebEngineQuick)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  cmake(Corrosion)
BuildRequires:  rust-packaging

Requires:       hicolor-icon-theme
# QML module dependencies
Requires:       kf6-kirigami%{?_isa}
Requires:       kf6-kirigami-addons%{?_isa}
Requires:       kf6-purpose%{?_isa}
Requires:       kf6-qqc2-desktop-style%{?_isa}
Requires:       qt6-qt5compat%{?_isa}
Requires:       qt6-qtwayland%{?_isa}
Requires:       qt6-qtwebengine%{?_isa}

%description
Web browser for mobile devices with Plasma integration

%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.metainfo.xml


%files -f %{name}.lang
%license LICENSES/{MIT,GPL-2.0-or-later,LGPL-2.0-only,LGPL-2.0-or-later}.txt
%doc README.md
%{_kf6_bindir}/%{name}
%{_kf6_bindir}/%{name}-webapp
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/config.kcfg/%{name}settings.kcfg
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.%{name}.svg
%{_kf6_datadir}/knotifications6/%{name}.notifyrc
%{_kf6_metainfodir}/org.kde.%{name}.metainfo.xml

%changelog
* Tue Sep 10 2024 Pavel Solovev <daron439@gmail.com> - 24.08.1-1
- Update to 24.08.1

* Fri Aug 16 2024 Pavel Solovev <daron439@gmail.com> - 24.08.0-1
- Update to 24.08.0

* Fri Aug 09 2024 Pavel Solovev <daron439@gmail.com> - 24.07.90-1
- Update to 24.07.90

* Thu Jul 25 2024 Pavel Solovev <daron439@gmail.com> - 24.07.80-1
- Update to 24.07.80

* Thu Jul 04 2024 Pavel Solovev <daron439@gmail.com> - 24.05.2-1
- Update to 24.05.2

* Thu Jun 13 2024 Pavel Solovev <daron439@gmail.com> - 24.05.1-1
- Update to 24.05.1

* Thu May 23 2024 Pavel Solovev <daron439@gmail.com> - 24.05.0-1
- Update to 24.05.0

* Fri Apr 26 2024 Pavel Solovev <daron439@gmail.com> - 24.04.80-1
- Update to 24.04.80

* Thu Apr 11 2024 Pavel Solovev <daron439@gmail.com> - 24.02.2-1
- Update to 24.02.2

* Thu Mar 21 2024 Pavel Solovev <daron439@gmail.com> - 24.02.1-1
- Update to 24.02.1

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.0-1
- 24.02.0

* Fri Feb 16 2024 Jan Grulich <jgrulich@redhat.com> - 24.01.95-3
- Rebuild (qt6)

* Mon Feb 05 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 24.01.95-2
- Enable adblock

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.95-1
- 24.01.95

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90

* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Sun Dec 03 2023 Yaakov Selkowitz <yselkowitz@fedoraproject.org> - 24.01.80-1
- 24.01.80

* Wed Nov 29 2023 Jan Grulich <jgrulich@redhat.com> - 24.01.75-2
- Rebuild (qt6)

* Thu Nov 23 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 24.01.75-1
- 24.01.75

* Thu Oct 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.2-1
- 23.08.2

* Thu Oct 05 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 23.08.1-1
- 23.08.1

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.3-1
- 23.04.3

* Tue Jun 06 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.2-1
- 23.04.2

* Sat May 13 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.1-1
- 23.04.1

* Thu Apr 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.0-1
- 23.04.0

* Fri Mar 31 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.90-1
- 23.03.90

* Mon Mar 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.80-1
- 23.03.80

* Mon Jan 30 2023 Justin Zobel <justin@1707.io> - 23.01.0-1
- Update to 23.01.0

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 01 2022 Justin Zobel <justin@1707.io> - 22.11-1
- Update to 22.11

* Wed Sep 28 2022 Justin Zobel <justin@1707.io> - 22.09-1
- Update to 22.09

* Thu Aug 25 2022 Justin Zobel <justin@1707.io> - 22.06-1
- Update to 22.06

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Jan Grulich <jgrulich@redhat.com> - 22.04-3
- Rebuild (qt5)

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 22.04-2
- Rebuild (qt5)

* Wed May 04 2022 Justin Zobel <justin@1707.io> - 22.04-1
- Update to 22.04

* Wed Mar 30 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 22.02-3
- Rebuild (qt5)

* Mon Mar 14 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 22.02-2
- Rebuild for Qt5WebEngine

* Thu Feb 10 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 22.02-1
- Plasma mobile version 22.02

* Fri Jan 21 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.12-2
- Ignore ppc64le and s390x

* Tue Jan 11 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.12-1
- Version bump 21.12 and cosmetic fixes

* Fri Nov 05 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.08-1
- initial version angelfish
