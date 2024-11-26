%global commit0 cb65c46b3d24845c00dcb28f37bbcabd059f10ea
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

Name:    plasma-systemmonitor
Version: 6.2.4
Release: 1%{?dist}
Summary: An application for monitoring system resources

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND LGPL-3.0-or-later AND LicenseRef-KDE-Accepted-GPL AND LicenseRef-KDE-Accepted-LGPL
URL:     https://invent.kde.org/plasma/%{name}
%plasma_source

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6ItemModels)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KF6KirigamiAddons)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6Package)
BuildRequires: cmake(KF6Service)

BuildRequires: libksysguard-devel

BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtdeclarative-devel

Requires: kf6-kirigami2%{?_isa}
Requires: ksystemstats%{?_isa}

Obsoletes:     ksysguard < 5.22.0-11
Obsoletes:     ksysguardd < 5.22.0-11

%description
An interface for monitoring system sensors, process information and other system
resources.


%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%license LICENSES/*.txt
%{_kf6_bindir}/plasma-systemmonitor
%{_kf6_datadir}/kglobalaccel/org.kde.plasma-systemmonitor.desktop
%{_kf6_datadir}/applications/org.kde.plasma-systemmonitor.desktop
%{_kf6_datadir}/config.kcfg/systemmonitor.kcfg
%{_kf6_datadir}/knsrcfiles/
%{_kf6_datadir}/ksysguard/sensorfaces/
%{_kf6_datadir}/metainfo/org.kde.plasma-systemmonitor.metainfo.xml
%{_kf6_datadir}/plasma-systemmonitor/
%{_kf6_datadir}/plasma/kinfocenter/externalmodules/kcm_external_plasma-systemmonitor.desktop
%{_kf6_libdir}/libPlasmaSystemMonitorPage.so
%{_kf6_libdir}/libPlasmaSystemMonitorTable.so
%{_kf6_qmldir}/org/kde/ksysguard/

%changelog
* Tue Nov 26 2024 Pavel Solovev <daron439@gmail.com> - 6.2.4-1
- Update to 6.2.4

* Tue Nov 05 2024 Pavel Solovev <daron439@gmail.com> - 6.2.3-1
- Update to 6.2.3

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

* Sun Mar 31 2024 Pavel Solovev <daron439@gmail.com> - 6.0.3-2
- relax obsoletes

* Tue Mar 26 2024 Pavel Solovev <daron439@gmail.com> - 6.0.3-1
- Update to 6.0.3

* Wed Mar 20 2024 Pavel Solovev <daron439@gmail.com> - 6.0.2-2
- qmlcache rebuild

* Sat Nov 18 2023 Alessandro Astone <ales.astone@gmail.com> - 5.27.80-2
- Fix Plasma 6 runtime requirements

* Mon Nov 13 2023 Steve Cossette <farchord@gmail.com> - 5.27.80-1
- 5.27.80

* Tue Oct 24 2023 Steve Cossette <farchord@gmail.com> - 5.27.9-1
- 5.27.9

* Tue Sep 12 2023 justin.zobel@gmail.com - 5.27.8-1
- 5.27.8

* Tue Aug 01 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.7-1
- 5.27.7

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.27.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jun 25 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.6-1
- 5.27.6

* Wed May 10 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.5-1
- 5.27.5

* Tue Apr 04 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.4-1
- 5.27.4

* Tue Mar 14 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.3-1
- 5.27.3

* Tue Feb 28 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.2-1
- 5.27.2

* Tue Feb 21 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.1-1
- 5.27.1

* Thu Feb 09 2023 Marc Deop <marcdeop@fedoraproject.org> - 5.27.0-1
- 5.27.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.26.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 19 2023 Marc Deop <marcdeop@fedoraproject.org> - 5.26.90-1
- 5.26.90

* Thu Jan 05 2023 Justin Zobel <justin@1707.io> - 5.26.5-1
- Update to 5.26.5

* Tue Nov 29 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.26.4-1
- 5.26.4

* Wed Nov 09 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.26.3-1
- 5.26.3

* Wed Oct 26 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.26.2-1
- 5.26.2

* Tue Oct 18 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.26.1-1
- 5.26.1

* Thu Oct 06 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.26.0-1
- 5.26.0

* Sat Sep 17 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.25.90-1
- 5.25.90

* Wed Sep 07 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.25.5-1
- 5.25.5

* Wed Aug 03 2022 Justin Zobel <justin@1707.io> - 5.25.4-1
- Update to 5.25.4

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.25.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 12 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.25.3-1
- 5.25.3

* Tue Jun 28 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.25.2-1
- 5.25.2

* Tue Jun 21 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.25.1-1
- 5.25.1

* Thu Jun 09 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.25.0-1
- 5.25.0

* Fri May 20 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.24.90-1
- 5.24.90

* Tue May 03 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.24.5-1
- 5.24.5

* Thu Mar 31 2022 Justin Zobel <justin@1707.io> - 5.24.4-1
- Update to 5.24.4

* Tue Mar 08 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.24.3-1
- 5.24.3

* Tue Feb 22 2022 Rex Dieter <rdieter@fedoraproject.org> - 5.24.2-1
- 5.24.2

* Tue Feb 15 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.24.1-1
- 5.24.1

* Thu Feb 03 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.24.0-1
- 5.24.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.23.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 13 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.23.90-1
- 5.23.90

* Tue Jan 04 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.23.5-1
- 5.23.5

* Tue Dec 14 2021 Marc Deop <marcdeop@fedoraproject.org> - 5.23.4-1
- 5.23.4

* Wed Nov 10 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.23.3-1
- 5.23.3

* Tue Oct 26 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.23.2-1
- 5.23.2

* Sat Oct 23 2021 Marc Deop <marcdeop@fedoraproject.org> - 5.23.1-1
- 5.23.1

* Fri Oct 08 2021 Marc Deop <marcdeop@fedoraproject.org> - 5.23.0-1
- 5.23.0

* Fri Sep 17 2021 Marc Deop <marcdeop@fedoraproject.org> - 5.22.90-1
- 5.22.90

* Tue Aug 31 2021 Jan Grulich <jgrulich@redhat.com> - 5.22.5-1
- 5.22.5

* Tue Jul 27 2021 Jan Grulich <jgrulich@redhat.com> - 5.22.4-1
- 5.22.4

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.22.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 12 2021 Jan Grulich <jgrulich@redhat.com> - 5.22.3-1
- 5.22.3

* Tue Jun 22 2021 Jan Grulich <jgrulich@redhat.com> - 5.22.2.1-1
- 5.22.2.1

* Tue Jun 22 2021 Jan Grulich <jgrulich@redhat.com> - 5.22.2-1
- 5.22.2

* Tue Jun 15 2021 Jan Grulich <jgrulich@redhat.com> - 5.22.1-1
- 5.22.1

* Sun Jun 06 2021 Jan Grulich <jgrulich@redhat.com> - 5.22.0-1
- 5.22.0

* Tue May 18 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.21.90-3
- Requires: ksystemstats

* Sun May 16 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.21.90-2
- rebuild

* Sun May 16 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.21.90-1
- 5.21.90

* Tue May 04 2021 Jan Grulich <jgrulich@redhat.com> - 5.21.5-1
- 5.21.5

* Tue Apr 06 2021 Jan Grulich <jgrulich@redhat.com> - 5.21.4-1
- 5.21.4

* Tue Mar 16 2021 Jan Grulich <jgrulich@redhat.com> - 5.21.3-1
- 5.21.3

* Tue Mar 02 2021 Jan Grulich <jgrulich@redhat.com> - 5.21.2-1
- 5.21.2

* Sun Feb 28 2021 Neal Gompa <ngompa13@gmail.com> - 5.21.1-2
- Require ksystemstats from ksysguard (rhbz#1930514)

* Tue Feb 23 2021 Jan Grulich <jgrulich@redhat.com> - 5.21.1-1
- 5.21.1

* Thu Feb 11 2021 Jan Grulich <jgrulich@redhat.com> - 5.21.0-1
- 5.21.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.20.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jan Grulich <jgrulich@redhat.com> - 5.20.90-1
- 5.20.90 (beta)
