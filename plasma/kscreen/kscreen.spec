%global commit0 d04dd6c4f3314b6c35f5bb22b42a9e1065e72618
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

Name:    kscreen
Epoch:   1
Version: 6.2.3
Release: 1%{?dist}
Summary: KDE Display Management software

License: CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later (GPL-2.0-only OR GPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{name}
%plasma_source

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  systemd-rpm-macros

BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires:  qt6-qtsensors-devel

BuildRequires:  cmake(LayerShellQt)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(PlasmaQuick)
BuildRequires:  cmake(KF6Screen)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6XmlGui)

BuildRequires:  pkgconfig(xcb-atom)
BuildRequires:  pkgconfig(xi)

%description
KCM and KDED modules for managing displays in KDE.


%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%find_lang %{name} --with-kde --all-name


%files -f %{name}.lang
%license LICENSES
%{_kf6_bindir}/kscreen-console
%{_kf6_datadir}/applications/kcm_kscreen.desktop
%{_kf6_datadir}/dbus-1/services/org.kde.kscreen.osdService.service
%{_kf6_datadir}/kglobalaccel/org.kde.kscreen.desktop
%{_kf6_datadir}/metainfo/org.kde.kscreen.appdata.xml
%{_kf6_datadir}/plasma/plasmoids/org.kde.kscreen/
%{_kf6_datadir}/qlogging-categories6/kscreen.categories
%{_kf6_plugindir}/kded/kscreen.so
%{_kf6_qtplugindir}/plasma/applets/org.kde.kscreen.so
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_kscreen.so
%{_libexecdir}/kscreen_osd_service
%{_userunitdir}/plasma-kscreen-osd.service


%changelog
* Tue Nov 05 2024 Pavel Solovev <daron439@gmail.com> - 1:6.2.3-1
- Update to 6.2.3

* Thu Oct 31 2024 Pavel Solovev <daron439@gmail.com> - 1:6.2.2-2
- rebuilt

* Tue Oct 22 2024 Pavel Solovev <daron439@gmail.com> - 1:6.2.2-1
- Update to 6.2.2

* Tue Oct 15 2024 Pavel Solovev <daron439@gmail.com> - 1:6.2.1-1
- Update to 6.2.1

* Thu Oct 03 2024 Pavel Solovev <daron439@gmail.com> - 1:6.2.0-1
- Update to 6.2.0

* Tue Sep 10 2024 Pavel Solovev <daron439@gmail.com> - 1:6.1.5-1
- Update to 6.1.5

* Tue Aug 06 2024 Pavel Solovev <daron439@gmail.com> - 1:6.1.4-1
- Update to 6.1.4

* Tue Jul 16 2024 Pavel Solovev <daron439@gmail.com> - 1:6.1.3-1
- Update to 6.1.3

* Tue Jul 02 2024 Pavel Solovev <daron439@gmail.com> - 1:6.1.2-1
- Update to 6.1.2

* Tue Jun 25 2024 Pavel Solovev <daron439@gmail.com> - 1:6.1.1-1
- Update to 6.1.1

* Tue Jun 18 2024 Pavel Solovev <daron439@gmail.com> - 1:6.1.0-1
- Update to 6.1.0

* Fri May 24 2024 Pavel Solovev <daron439@gmail.com> - 1:6.0.90-1
- Update to 6.0.90

* Tue May 21 2024 Pavel Solovev <daron439@gmail.com> - 1:6.0.5-1
- Update to 6.0.5

* Tue Apr 16 2024 Pavel Solovev <daron439@gmail.com> - 1:6.0.4-1
- Update to 6.0.4

* Tue Mar 26 2024 Pavel Solovev <daron439@gmail.com> - 1:6.0.3-1
- Update to 6.0.3

* Wed Mar 20 2024 Pavel Solovev <daron439@gmail.com> - 1:6.0.2-2
- qmlcache rebuild

* Mon Nov 13 2023 Alessandro Astone <ales.astone@gmail.com> - 1:5.27.80-1
- 5.27.80

* Tue Oct 24 2023 Steve Cossette <farchord@gmail.com> - 1:5.27.9-1
- 5.27.9

* Tue Sep 12 2023 justin.zobel@gmail.com - 1:5.27.8-1
- 5.27.8

* Tue Aug 01 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:5.27.7-1
- 5.27.7

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.27.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jun 25 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:5.27.6-1
- 5.27.6

* Wed May 10 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:5.27.5-1
- 5.27.5

* Tue Apr 04 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:5.27.4-1
- 5.27.4

* Tue Mar 14 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:5.27.3-1
- 5.27.3

* Tue Feb 28 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:5.27.2-1
- 5.27.2

* Tue Feb 21 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:5.27.1.1-1
- 5.27.1.1

* Tue Feb 21 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:5.27.1-1
- 5.27.1

* Thu Feb 09 2023 Marc Deop <marcdeop@fedoraproject.org> - 1:5.27.0-1
- 5.27.0

* Thu Jan 19 2023 Marc Deop <marcdeop@fedoraproject.org> - 1:5.26.90-1
- 5.26.90

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.26.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 05 2023 Justin Zobel <justin@1707.io> - 1:5.26.5-1
- Update to 5.26.5

* Tue Nov 29 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:5.26.4-1
- 5.26.4

* Wed Nov 09 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:5.26.3-1
- 5.26.3

* Wed Oct 26 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:5.26.2-1
- 5.26.2

* Tue Oct 18 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:5.26.1-1
- 5.26.1

* Thu Oct 06 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:5.26.0-1
- 5.26.0

* Sat Sep 17 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:5.25.90-1
- 5.25.90

* Wed Sep 07 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:5.25.5-1
- 5.25.5

* Wed Aug 03 2022 Justin Zobel <justin@1707.io> - 5.25.4-1
- Update to 5.25.4

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.25.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 12 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:5.25.3-1
- 5.25.3

* Tue Jun 28 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:5.25.2-1
- 5.25.2

* Tue Jun 21 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:5.25.1-1
- 5.25.1

* Thu Jun 09 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:5.25.0-1
- 5.25.0

* Fri May 20 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:5.24.90-1
- 5.24.90

* Tue May 03 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:5.24.5-1
- 5.24.5

* Thu Mar 31 2022 Justin Zobel <justin@1707.io> - 5.24.4-1
- Update to 5.24.4

* Tue Mar 08 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:5.24.3-1
- 5.24.3

* Tue Feb 22 2022 Rex Dieter <rdieter@fedoraproject.org> - 1:5.24.2-1
- 5.24.2

* Tue Feb 15 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:5.24.1-1
- 5.24.1

* Thu Feb 03 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:5.24.0-1
- 5.24.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.23.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 13 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:5.23.90-1
- 5.23.90

* Tue Jan 04 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:5.23.5-1
- 5.23.5

* Tue Dec 14 2021 Marc Deop <marcdeop@fedoraproject.org> - 1:5.23.4-1
- 5.23.4

* Wed Nov 10 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:5.23.3-1
- 5.23.3

* Tue Oct 26 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:5.23.2-1
- 5.23.2

* Sat Oct 23 2021 Marc Deop <marcdeop@fedoraproject.org> - 1:5.23.1-1
- 5.23.1

* Fri Oct 08 2021 Marc Deop <marcdeop@fedoraproject.org> - 1:5.23.0-1
- 5.23.0

* Sun Sep 19 2021 Marc Deop <marcdeop@fedoraproject.org> - 1:5.22.90-2
- Adjust Licenses

* Fri Sep 17 2021 Marc Deop <marcdeop@fedoraproject.org> - 1:5.22.90-1
- 5.22.90

* Tue Aug 31 2021 Jan Grulich <jgrulich@redhat.com> - 1:5.22.5-1
- 5.22.5

* Tue Jul 27 2021 Jan Grulich <jgrulich@redhat.com> - 1:5.22.4-1
- 5.22.4

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.22.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 12 2021 Jan Grulich <jgrulich@redhat.com> - 1:5.22.3-1
- 5.22.3

* Tue Jun 22 2021 Jan Grulich <jgrulich@redhat.com> - 1:5.22.2.1-1
- 5.22.2.1

* Tue Jun 22 2021 Jan Grulich <jgrulich@redhat.com> - 1:5.22.2-1
- 5.22.2

* Tue Jun 15 2021 Jan Grulich <jgrulich@redhat.com> - 1:5.22.1-1
- 5.22.1

* Sun Jun 06 2021 Jan Grulich <jgrulich@redhat.com> - 1:5.22.0-1
- 5.22.0

* Fri May 14 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:5.21.90-1
- 5.21.90

* Tue May 04 2021 Jan Grulich <jgrulich@redhat.com> - 1:5.21.5-1
- 5.21.5

* Tue Apr 06 2021 Jan Grulich <jgrulich@redhat.com> - 1:5.21.4-1
- 5.21.4

* Tue Mar 16 2021 Jan Grulich <jgrulich@redhat.com> - 1:5.21.3-1
- 5.21.3

* Tue Mar 02 2021 Jan Grulich <jgrulich@redhat.com> - 1:5.21.2-1
- 5.21.2

* Tue Feb 23 2021 Jan Grulich <jgrulich@redhat.com> - 1:5.21.1-1
- 5.21.1

* Thu Feb 11 2021 Jan Grulich <jgrulich@redhat.com> - 1:5.21.0-1
- 5.21.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.20.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Jan Grulich <jgrulich@redhat.com> - 1:5.20.90-1
- 5.20.90 (beta)

* Tue Jan  5 16:03:31 CET 2021 Jan Grulich <jgrulich@redhat.com> - 1:5.20.5-1
- 5.20.5

* Tue Dec  1 09:42:58 CET 2020 Jan Grulich <jgrulich@redhat.com> - 1:5.20.4-1
- 5.20.4

* Wed Nov 11 08:22:39 CET 2020 Jan Grulich <jgrulich@redhat.com> - 1:5.20.3-1
- 5.20.3

* Tue Oct 27 14:22:39 CET 2020 Jan Grulich <jgrulich@redhat.com> - 1:5.20.2-1
- 5.20.2

* Tue Oct 20 15:28:34 CEST 2020 Jan Grulich <jgrulich@redhat.com> - 1:5.20.1-1
- 5.20.1

* Sun Oct 11 19:50:03 CEST 2020 Jan Grulich <jgrulich@redhat.com> - 1:5.20.0-1
- 5.20.0

* Fri Sep 18 2020 Jan Grulich <jgrulich@redhat.com> - 1:5.19.90-1
- 5.19.90

* Tue Sep 01 2020 Jan Grulich <jgrulich@redhat.com> - 1:5.19.5-1
- 5.19.5

* Tue Jul 28 2020 Jan Grulich <jgrulich@redhat.com> - 1:5.19.4-1
- 5.19.4

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.19.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Jan Grulich <jgrulich@redhat.com> - 1:5.19.3-1
- 5.19.3

* Tue Jun 23 2020 Jan Grulich <jgrulich@redhat.com> - 1:5.19.2-1
- 5.19.2

* Wed Jun 17 2020 Martin Kyral <martin.kyral@gmail.com> - 5.19.1-1
- 5.19.1

* Tue Jun 9 2020 Martin Kyral <martin.kyral@gmail.com> - 5.19.0-1
- 5.19.0

* Fri May 15 2020 Martin Kyral <martin.kyral@gmail.com> - 5.18.90-1
- 5.18.90

* Tue May 05 2020 Jan Grulich <jgrulich@redhat.com> - 1:5.18.5-1
- 5.18.5

* Sat Apr 04 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:5.18.4.1-1
- 5.18.4.1

* Tue Mar 31 2020 Jan Grulich <jgrulich@redhat.com> - 1:5.18.4-1
- 5.18.4

* Tue Mar 10 2020 Jan Grulich <jgrulich@redhat.com> - 1:5.18.3-1
- 5.18.3

* Tue Feb 25 2020 Jan Grulich <jgrulich@redhat.com> - 1:5.18.2-1
- 5.18.2

* Tue Feb 18 2020 Jan Grulich <jgrulich@redhat.com> - 1:5.18.1-1
- 5.18.1

* Tue Feb 11 2020 Jan Grulich <jgrulich@redhat.com> - 1:5.18.0-1
- 5.18.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.17.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Jan Grulich <jgrulich@redhat.com> - 1:5.17.90-1
- 5.17.90

* Wed Jan 08 2020 Jan Grulich <jgrulich@redhat.com> - 1:5.17.5-1
- 5.17.5

* Thu Dec 05 2019 Jan Grulich <jgrulich@redhat.com> - 1:5.17.4-1
- 5.17.4

* Wed Nov 13 2019 Martin Kyral <martin.kyral@gmail.com> - 5.17.3-1
- 5.17.3

* Wed Oct 30 2019 Jan Grulich <jgrulich@redhat.com> - 1:5.17.2-1
- 5.17.2

* Wed Oct 23 2019 Jan Grulich <jgrulich@redhat.com> - 1:5.17.1-1
- 5.17.1

* Thu Oct 10 2019 Jan Grulich <jgrulich@redhat.com> - 1:5.17.0-1
- 5.17.0

* Fri Sep 20 2019 Martin Kyral <martin.kyral@gmail.com> - 5.16.90-1
- 5.16.90

* Fri Sep 06 2019 Martin Kyral <martin.kyral@gmail.com> - 5.16.5-1
- 5.16.5

* Tue Jul 30 2019 Martin Kyral <martin.kyral@gmail.com> - 5.16.4-1
- 5.16.4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.16.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 10 2019 Martin Kyral <martin.kyral@gmail.com> - 5.16.3-1
- 5.16.3

* Wed Jun 26 2019 Martin Kyral <martin.kyral@gmail.com> - 5.16.2-1
- 5.16.2

* Tue Jun 18 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:5.16.1-1
- 5.16.1

* Tue Jun 11 2019 Martin Kyral <martin.kyral@gmail.com> - 5.16.0-1
- 5.16.0

* Thu May 16 2019 Martin Kyral <martin.kyral@gmail.com> - 5.15.90-1
- 5.15.90

* Thu May 09 2019 Martin Kyral <martin.kyral@gmail.com> - 5.15.5-1
- 5.15.5

* Wed Apr 03 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:5.15.4-1
- 5.15.4

* Tue Mar 12 2019 Martin Kyral <martin.kyral@gmail.com> - 5.15.3-1
- 5.15.3

* Tue Feb 26 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:5.15.2-1
- 5.15.2

* Tue Feb 19 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:5.15.1-1
- 5.15.1

* Wed Feb 13 2019 Martin Kyral <martin.kyral@gmail.com> - 5.15.0-1
- 5.15.0

* Mon Feb 04 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:5.14.90-3
- Add versioned runtime dep for libkscreen-qt5
- use %%make_build

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.14.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 20 2019 Martin Kyral <martin.kyral@gmail.com> - 5.14.90-1
- 5.14.90

* Tue Nov 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:5.14.4-1
- 5.14.4

* Thu Nov 08 2018 Martin Kyral <martin.kyral@gmail.com> - 5.14.3-1
- 5.14.3

* Wed Oct 24 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:5.14.2-1
- 5.14.2

* Tue Oct 16 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:5.14.1-1
- 5.14.1

* Fri Oct 05 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:5.14.0-1
- 5.14.0

* Fri Sep 14 2018 Martin Kyral <martin.kyral@gmail.com> - 5.13.90-1
- 5.13.90

* Tue Sep 04 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:5.13.5-1
- 5.13.5

* Thu Aug 02 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:5.13.4-1
- 5.13.4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.13.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Martin Kyral <martin.kyral@gmail.com> - 5.13.3-1
- 5.13.3

* Mon Jul 09 2018 Martin Kyral <martin.kyral@gmail.com> - 5.13.2-1
- 5.13.2

* Tue Jun 19 2018 Martin Kyral <martin.kyral@gmail.com> - 5.13.1-1
- 5.13.1

* Sat Jun 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:5.13.0-1
- 5.13.0

* Fri May 18 2018 Martin Kyral <martin.kyral@gmail.com> - 5.12.90-1
- 5.12.90

* Tue May 01 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:5.12.5-1
- 5.12.5

* Tue Mar 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:5.12.4-1
- 5.12.4

* Tue Mar 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:5.12.3-1
- 5.12.3

* Wed Feb 21 2018 Jan Grulich <jgrulich@redhat.com> - 5.12.2-1
- 5.12.2

* Tue Feb 13 2018 Jan Grulich <jgrulich@redhat.com> - 5.12.1-1
- 5.12.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Jan Grulich <jgrulich@redhat.com> - 5.12.0-1
- 5.12.0

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:5.11.95-2
- Remove obsolete scriptlets

* Mon Jan 15 2018 Jan Grulich <jgrulich@redhat.com> - 5.11.95-1
- 5.11.95

* Tue Jan 02 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:5.11.5-1
- 5.11.5

* Thu Nov 30 2017 Martin Kyral <martin.kyral@gmail.com> - 5.11.4-1
- 5.11.4

* Wed Nov 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:5.11.3-1
- 5.11.3

* Wed Oct 25 2017 Martin Kyral <martin.kyral@gmail.com> - 5.11.2-1
- 5.11.2

* Tue Oct 17 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:5.11.1-1
- 5.11.1

* Wed Oct 11 2017 Martin Kyral <martin.kyral@gmail.com> - 5.11.0-1
- 5.11.0

* Thu Aug 24 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:5.10.5-1
- 5.10.5

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.10.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:5.10.4-1
- 5.10.4

* Tue Jun 27 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:5.10.3-1
- 5.10.3

* Thu Jun 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:5.10.2-1
- 5.10.2

* Tue Jun 06 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:5.10.1-1
- 5.10.1

* Wed May 31 2017 Jan Grulich <jgrulich@redhat.com> - 5.10.0-1
- 5.10.0

* Wed Apr 26 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:5.9.5-1
- 5.9.5

* Thu Mar 23 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:5.9.4-1
- 5.9.4

* Sat Mar 04 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:5.9.3-2
- rebuild

* Wed Mar 01 2017 Jan Grulich <jgrulich@redhat.com> - 5.9.3-1
- 5.9.3

* Tue Feb 21 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:5.8.6-1
- 5.8.6

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 02 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:5.8.5-2
- filter plugin provides

* Wed Dec 28 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:5.8.5-1
- 5.8.5

* Tue Nov 22 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:5.8.4-1
- 5.8.4

* Tue Nov 01 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:5.8.3-1
- 5.8.3

* Tue Oct 18 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:5.8.2-1
- 5.8.2

* Tue Oct 11 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:5.8.1-1
- 5.8.1

* Thu Sep 29 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:5.8.0-1
- 5.8.0

* Thu Sep 22 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:5.7.95-1
- 5.7.95

* Tue Sep 13 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:5.7.5-1
- 5.7.5

* Tue Aug 23 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:5.7.4-1
- 5.7.4

* Tue Aug 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:5.7.3-1
- 5.7.3

* Tue Jul 19 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:5.7.2-1
- 5.7.2

* Tue Jul 19 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.7.1-2
- rebuild (qt5)

* Tue Jul 12 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:5.7.1-1
- 5.7.1

* Thu Jun 30 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:5.7.0-1
- 5.7.0

* Sat Jun 25 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:5.6.95-1
- 5.6.95

* Tue Jun 14 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:5.6.5-1
- 5.6.5

* Sat May 14 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:5.6.4-1
- 5.6.4

* Tue Apr 19 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:5.6.3-1
- 5.6.3

* Sun Apr 10 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:5.6.2-1.1
- rebuild

* Sat Apr 09 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:5.6.2-1
- 5.6.2

* Fri Apr 08 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:5.6.1-1
- 5.6.1

* Tue Mar 01 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.5.5-1
- Plasma 5.5.5

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.5.4-1
- Plasma 5.5.4

* Thu Jan 07 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.5.3-1
- Plasma 5.5.3

* Thu Dec 31 2015 Rex Dieter <rdieter@fedoraproject.org> - 1:5.5.2-1
- 5.5.2

* Fri Dec 18 2015 Daniel Vrátil <dvratil@fedoraproject.org> - 5.5.1-1
- Plasma 5.5.1

* Thu Dec 03 2015 Daniel Vrátil <dvratil@fedoraproject.org> - 5.5.0-1
- Plasma 5.5.0

* Wed Nov 25 2015 Daniel Vrátil <dvratil@fedoraproject.org> - 5.4.95-1
- Plasma 5.4.95

* Thu Nov 05 2015 Daniel Vrátil <dvratil@fedoraproject.org> - 5.4.3-1
- Plasma 5.4.3

* Thu Oct 01 2015 Rex Dieter <rdieter@fedoraproject.org> - 1:5.4.2-1
- 5.4.2

* Wed Sep 09 2015 Rex Dieter <rdieter@fedoraproject.org> - 1:5.4.1-1
- 5.4.1

* Fri Aug 21 2015 Daniel Vrátil <dvratil@redhat.com> - 5.4.0-1
- Plasma 5.4.0

* Thu Aug 13 2015 Daniel Vrátil <dvratil@redhat.com> - 5.3.95-1
- Plasma 5.3.95

* Thu Jun 25 2015 Daniel Vrátil <dvratil@redhat.com> - 5.3.2-1
- Plasma 5.3.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 26 2015 Daniel Vrátil <dvratil@redhat.com> - 5.3.1-1
- Plasma 5.3.1

* Mon Apr 27 2015 Daniel Vrátil <dvratil@redhat.com> - 5.3.0-1
- Plasma 5.3.0

* Wed Apr 22 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.95-1
- Plasma 5.2.95

* Wed Apr 15 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.2-2
- add upstream fix for RHBZ#1211881

* Fri Mar 20 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.2-1
- Plasma 5.2.2

* Thu Mar 05 2015 Rex Dieter <rdieter@fedoraproject.org> 5.2.1-3
- Requires: qt5-qtgraphicaleffects (#1199084)

* Fri Feb 27 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.1-2
- Rebuild (GCC 5)

* Tue Feb 24 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.1-1
- Plasma 5.2.1

* Wed Jan 28 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.0-2
- BR libkscreen-qt5-devel (it Provides kf5-kscreen-devel, but lets use the correct name)

* Mon Jan 26 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.0-1
- Plasma 5.2.0

* Wed Jan 14 2015 Daniel Vrátil <dvratil@redhat.com> - 5.1.95-2.beta.20150112git7a8460a
- BR kf5-kscreen-devel (renamed from libkscreen)

* Mon Jan 12 2015 Daniel Vrátil <dvratil@redhat.com> - 5.1.95-1.beta.20150112git7a8460a
- Update to latest git snapshot

* Thu Jan 08 2015 Daniel Vrátil <dvratil@redhat.com> - 5.1.2-2.20150108git0d70c77
- Update to latest git snapshot

* Wed Dec 17 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.2-2
- Plasma 5.1.2

* Fri Nov 28 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.1-1.20141128gitccf52c4
- Update to latest git snapshot

* Fri Nov 07 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.1-1.20141107git88b2a3f
- Plasma 5.1.1

* Thu Oct 23 2014 Daniel Vrátil <dvratil@redhat.com> 1:5.0.92-20141023git
 - kscreen 5.0.92 (git)

* Fri Nov 22 2013 Dan Vrátil <dvratil@redhat.com> 1:1.0.2.1-1
 - kscreen 1:1.0.2.1-1

* Wed Nov 20 2013 Dan Vrátil <dvratil@redhat.com> 1:1.0.2-1
 - kscreen 1:1.0.2-1

* Thu Aug 01 2013 Dan Vrátil <dvratil@redhat.com> 1:1.0.1-1
 - kscreen 1:1.0.1-1

* Mon Jun 17 2013 Dan Vrátil <dvratil@redhat.com> 1:1.0-1
 - kscreen 1:1.0-1

* Thu May 02 2013 Dan Vrátil <dvratil@redhat.com> 1:0.0.92-1
 - update to 1:0.0.92-1

* Tue Apr 23 2013 Dan Vrátil <dvratil@redhat.com> 1:0.0.82.git20130424-1
 - dev git build

* Mon Apr 08 2013 Dan Vrátil <dvratil@redhat.com> 1:0.0.81-2
 - Explicitely depend on the same version of libkscreen

* Wed Mar 27 2013 Dan Vrátil <dvratil@redhat.com> 1:0.0.81-1
 - Update to 1:0.0.81-1

* Mon Jan 28 2013 Rex Dieter <rdieter@fedoraproject.org> 1:0.0.71-3
- drop Provides: kde-display-management, Conflicts: kded_randrmonitor

* Thu Jan 24 2013 Dan Vrátil <dvratil@redhat.com> 1:0.0.71-2
 - add Provides and Conflicts fields so make sure radrmonitor and
   kscreen never run side by side

* Sun Jan 20 2013 Dan Vrátil <dvratil@redhat.com> 1:0.0.71-1
 - update to 0.0.71 - first official release
 - install kscreen-console, which has been moved from libkscreen
 - the KCM is now called kcm_kscreen

* Wed Jan 09 2013 Dan Vrátil <dvratil@redhat.com> 0.9.0-5.20121228git
 - Update description, we don't ship the Plasma applet yet
 - Provides kde-display-management, a metapackage for KScreen and kded_randrmonitor
 - Conflicts with kded_randrmonitor

* Wed Jan 09 2013 Rex Dieter <rdieter@fedoraproject.org> 0.9.0-4.20121228git
- BR: qjson-devel >= 0.8.1
- License: GPLv2 or GPLv3
- tighten %%files

* Wed Jan 02 2013 Dan Vrátil <dvratil@redhat.com> 0.9.0-3.20121228git
 - Added qjson-devel to BuildRequires

* Fri Dec 28 2012 Dan Vrátil <dvratil@redhat.com> 0.9.0-2.20121228git
 - Fixed URL

* Fri Dec 28 2012 Dan Vrátil <dvratil@redhat.com> 0.9.0-1.20121228git
 - Fixed versioning
 - Added instructions how to obtain sources
 - Removed 'rm -rf $RPM_BUILD_ROOT'

* Wed Dec 26 2012 Dan Vrátil <dvratil@redhat.com> 20121226gitb31ab08-1
 - Initial SPEC
