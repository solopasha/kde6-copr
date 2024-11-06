%global commit0 e82a5c94421e48a28581680879cc34b5e893b7fc
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

Name:    neochat
Version: 24.08.3
Release: 2%{?dist}

License: GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND BSD-3-Clause
URL: https://invent.kde.org/network/%{name}
Summary: Client for matrix, the decentralized communication protocol
%apps_source

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Svg)
%ifarch %{qt6_qtwebengine_arches}
BuildRequires: cmake(Qt6WebView)
%endif
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6LinguistTools)

BuildRequires: cmake(KF6ColorScheme)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6ItemModels)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KF6KirigamiAddons)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6Purpose)
BuildRequires: cmake(KF6QQC2DesktopStyle)
BuildRequires: cmake(KF6Sonnet)
BuildRequires: cmake(KF6StatusNotifierItem)
BuildRequires: cmake(KF6SyntaxHighlighting)
BuildRequires: cmake(KF6WindowSystem)

BuildRequires: cmake(KQuickImageEditor)
BuildRequires: cmake(KUnifiedPush)
BuildRequires: cmake(QCoro6Core)
BuildRequires: cmake(QCoro6Network)
BuildRequires: cmake(QuotientQt6)

BuildRequires: pkgconfig(icu-uc)
BuildRequires: pkgconfig(libcmark)

BuildRequires: cmake
BuildRequires: cmark
BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: libappstream-glib

Requires: breeze-icon-theme
Requires: hicolor-icon-theme
# QML module dependencies
Requires: kf6-kirigami%{?_isa}
Requires: kf6-kirigami-addons%{?_isa}
Requires: kf6-kitemmodels%{?_isa}
Requires: kf6-knotifications%{?_isa}
Requires: kf6-kquickcharts%{?_isa}
Requires: kf6-prison%{?_isa}
Requires: kf6-purpose%{?_isa}
Requires: kf6-sonnet%{?_isa}
Requires: kf6-syntax-highlighting%{?_isa}
Requires: kf6-qqc2-desktop-style%{?_isa}
Requires: kquickimageeditor-qt6%{?_isa}
Requires: qt6-qtlocation%{?_isa}
Requires: qt6-qtmultimedia%{?_isa}
Requires: qt6-qtpositioning%{?_isa}
%ifarch %{qt6_qtwebengine_arches}
Requires: qt6-qtwebview%{?_isa}
%endif

Recommends: google-noto-emoji-color-fonts
Recommends: google-noto-emoji-fonts

Provides: spectral = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: spectral < 0-19.20201224gitfba0df0

%description
Neochat is a client for Matrix, the decentralized communication protocol for
instant messaging. It is a fork of Spectral, using KDE frameworks, most
notably Kirigami, KConfig and KI18n.

%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-qt --with-man

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/*.desktop

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.neochat.desktop
%{_kf6_datadir}/dbus-1/services/org.kde.neochat.service
%{_kf6_datadir}/icons/hicolor/*/apps/org.kde.neochat.*
%{_kf6_datadir}/knotifications6/%{name}.notifyrc
%{_kf6_datadir}/krunner/dbusplugins/plasma-runner-neochat.desktop
%{_kf6_datadir}/qlogging-categories6/neochat.categories
%{_kf6_mandir}/man1/neochat.1.*
%{_kf6_metainfodir}/org.kde.neochat.appdata.xml
%{_kf6_plugindir}/purpose/neochatshareplugin.so

%changelog
* Wed Nov 06 2024 Pavel Solovev <daron439@gmail.com> - 24.08.3-2
- rebuild against libquotient 0.9.0 and with kunifiedpush

* Tue Nov 05 2024 Pavel Solovev <daron439@gmail.com> - 24.08.3-1
- Update to 24.08.3

* Mon Oct 07 2024 Pavel Solovev <daron439@gmail.com> - 24.08.2-1
- Update to 24.08.2

* Tue Sep 17 2024 Pavel Solovev <daron439@gmail.com> - 24.08.1-2
- pick upstream commits

* Tue Sep 10 2024 Pavel Solovev <daron439@gmail.com> - 24.08.1-1
- Update to 24.08.1

* Fri Aug 16 2024 Pavel Solovev <daron439@gmail.com> - 24.08.0-1
- Update to 24.08.0

* Fri Aug 09 2024 Pavel Solovev <daron439@gmail.com> - 24.07.90-1
- Update to 24.07.90

* Mon Jul 29 2024 Pavel Solovev <daron439@gmail.com> - 24.07.80-3
- pick upstream commits

* Sat Jul 27 2024 Pavel Solovev <daron439@gmail.com> - 24.07.80-2
- pick upstream commits

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

* Wed Mar 20 2024 Pavel Solovev <daron439@gmail.com> - 24.02.0-3
- qmlcache rebuild

* Thu Dec 07 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 24.01.80-2
- Fix QML module dependencies
- Build without webview on unsupported arches

* Sun Dec 03 2023 Yaakov Selkowitz <yselkowitz@fedoraproject.org> - 24.01.80-1
- 24.01.80

* Thu Oct 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.2-1
- 23.08.2

* Thu Oct 05 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.1-2
- Add missing Requires BZ#2242379

* Sat Sep 16 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.1-1
- 23.08.1

* Thu Sep 07 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.0-1
- 23.08.0

* Mon Sep 04 2023 Neal Gompa <ngompa@fedoraproject.org> - 23.04.3-5
- Add patch to enforce E2EE enabled in libQuotient 0.8.x

* Sun Sep 03 2023 Neal Gompa <ngompa@fedoraproject.org> - 23.04.3-4
- Add runtime dependency on kf5-kitemmodels (#2216142)

* Sat Sep 02 2023 Neal Gompa <ngompa@fedoraproject.org> - 23.04.3-3
- Rebuild for libquotient 0.8.1.1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.04.3-2
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

* Tue Feb 07 2023 Marc Deop <marcdeop@fedoraproject.org> - 23.01.0-2
- Require kf5-kirigami2-addons

* Mon Jan 30 2023 Justin Zobel <justin@1707.io> - 23.01.0-1
- Update to 23.01.0

* Fri Jan 27 2023 Jens Petersen <petersen@redhat.com> - 22.11-4
- rebuild f38 against newer cmark

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 21 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 22.11-2
- Rebuilt against libquotient 0.7.0 with E2EE enabled.
- Switched to SPDX license tag.

* Thu Dec 01 2022 Justin Zobel <justin@1707.io> - 22.11-1
- Update to 22.11

* Wed Sep 28 2022 Justin Zobel <justin@1707.io> - 22.09-1
- Update to 22.09

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 24 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 22.06-1
- Updated to version 22.06.

* Sun Apr 24 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 22.04-1
- Updated to version 22.04.

* Wed Feb 09 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 22.02-1
- Updated to version 22.02.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 09 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 21.12-2
- Backported upstream patch with qcoro 0.4.0 build fixes.

* Tue Dec 07 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 21.12-1
- Updated to version 21.12.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 01 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 1.2.0-1
- Updated to version 1.2.0.

* Tue Feb 23 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1.1-1
- Updated to version 1.1.1.

* Tue Feb 23 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 1.1.0-1
- Updated to version 1.1.0.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0.1-1
- Updated to version 1.0.1.

* Wed Dec 23 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0-1
- Updated to version 1.0.

* Tue Dec 15 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.1.0-0.2.20201214git54b0773
- Updated to the latest Git snapshot.

* Mon Nov 23 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 0.1.0-0.1.20201123git5d4e787
- Initial SPEC release.
