%global commit0 ef6a85475963c34643f65144a7d72cc9072a1921
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

Name:		knights
Version:	24.08.1
Release:	1%{?dist}
Summary:	A chess board for KDE

# KDE e.V. may determine that future GPL versions are accepted
License: GPL-2.0-only OR GPL-3.0-only
URL:     https://invent.kde.org/games/knights
%apps_source

BuildRequires:  libkdegames-devel >= 22.03.80
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules >= 5.240.0
BuildRequires:  kf6-kdbusaddons-devel
BuildRequires:  kf6-kconfigwidgets-devel
BuildRequires:  kf6-kcrash-devel
BuildRequires:  kf6-kxmlgui-devel
BuildRequires:  kf6-kio-devel
BuildRequires:  kf6-kplotting-devel
BuildRequires:  kf6-kdoctools-devel
BuildRequires:  kf6-ktextwidgets-devel
BuildRequires:  kf6-kwallet-devel
BuildRequires:  kf6-plasma-devel
BuildRequires:  kf6-ksvg-devel
BuildRequires:  kf6-kcolorscheme-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qt5compat-devel

Requires:	gnuchess

%description
Knights is a chess board for KDE that supports playing against
computer engines that support the XBoard protocol like GNUChess and also
multiplayer games over the internet on FICS. It features automatic rule
checking, themes, and nice animations


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
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.knights.desktop

%files -f %{name}.lang
%doc README* ChangeLog DESIGN doc/
%{_bindir}/%{name}
%{_datadir}/dbus-1/interfaces/org.kde.Knights.xml
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_kf6_datadir}/applications/org.kde.knights.desktop
%{_datadir}/config.kcfg/%{name}.kcfg
%{_datadir}/metainfo/org.kde.knights.appdata.xml
%exclude %{_datadir}/doc/HTML/
%{_datadir}/qlogging-categories6/knights*categories
%{_datadir}/knsrcfiles/knights.knsrc

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

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.95-1
- 24.01.95

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Gwyn Ciesla <gwync@protonmail.com> - 24.01.90-1
- 24.01.90

* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Mon Dec 04 2023 Justin Zobel <justin.zobel@gmail.com> - 24.01.80-1
- Update to 24.01.80

* Wed Nov 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 24.01.75-1
- 24.01.75

* Thu Oct 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.2-1
- 23.08.2

* Sat Sep 16 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.1-1
- 23.08.1

* Thu Aug 24 2023 Gwyn Ciesla <gwync@protonmail.com> - 23.08.0-1
- 23.08.0

* Mon Aug 14 2023 Gwyn Ciesla <gwync@protonmail.com> - 23.07.90-1
- 23.07.90

* Mon Jul 31 2023 Gwyn Ciesla <gwync@protonmail.com> - 23.07.80-1
- 23.07.80

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 07 2023 Gwyn Ciesla <gwync@protonmail.com> - 23.04.3-1
- 23.04.3

* Tue Jun 06 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.2-1
- 23.04.2

* Fri May 12 2023 Gwyn Ciesla <gwync@protonmail.com> - 23.04.1-1
- 23.04.1

* Fri Apr 14 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.0-1
- 23.04.0

* Fri Mar 31 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.90-1
- 23.03.90

* Mon Mar 20 2023 Gwyn Ciesla <gwync@protonmail.com> - 23.03.80-1
- 23.03.80

* Sat Mar 04 2023 Gwyn Ciesla <gwync@protonmail.com> - 22.12.3-2
- migrated to SPDX license

* Thu Mar 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 22.12.3-1
- 22.12.3

* Tue Jan 31 2023 Marc Deop <marcdeop@fedoraproject.org> - 22.12.2-1
- 22.12.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jan 07 2023 Marc Deop <marcdeop@fedoraproject.org> - 22.12.1-1
- 22.12.1

* Fri Dec 09 2022 Gwyn Ciesla <gwync@protonmail.com> - 22.12.0-1
- 22.12.0

* Mon Nov 28 2022 Gwyn Ciesla <gwync@protonmail.com> - 22.11.90-1
- 22.11.90

* Fri Nov 11 2022 Gwyn Ciesla <gwync@protonmail.com> - 22.11.80-1
- 22.11.80

* Mon Nov 07 2022 Gwyn Ciesla <gwync@protonmail.com> - 22.08.3-1
- 22.08.3

* Thu Oct 13 2022 Gwyn Ciesla <gwync@protonmail.com> - 22.08.2-1
- 22.08.2

* Thu Sep 08 2022 Gwyn Ciesla <gwync@protonmail.com> - 22.08.1-1
- 22.08.1

* Fri Aug 19 2022 Gwyn Ciesla <gwync@protonmail.com> - 22.08.0-1
- 22.08.0

* Tue Aug 09 2022 Gwyn Ciesla <gwync@protonmail.com> - 22.07.90-1
- 22.07.90

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.07.80-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Gwyn Ciesla <gwync@protonmail.com> - 22.07.80-1
- 22.07.80

* Fri Jul 08 2022 Gwyn Ciesla <gwync@protonmail.com> - 22.04.3-1
- 22.04.3

* Thu Jun 16 2022 Gwyn Ciesla <gwync@protonmail.com> - 22.04.2-1
- 22.04.2

* Fri May 13 2022 Gwyn Ciesla <gwync@protonmail.com> - 22.04.1-1
- 22.04.1

* Fri Apr 22 2022 Gwyn Ciesla <gwync@protonmail.com> - 22.04.0-1
- 22.04.0

* Fri Mar 18 2022 Gwyn Ciesla <gwync@protonmail.com> - 22.03.80-1
- 22.03.80

* Mon Mar 07 2022 Gwyn Ciesla <gwync@protonmail.com> - 21.12.3-1
- 21.12.3

* Thu Feb 03 2022 Gwyn Ciesla <gwync@protonmail.com> - 21.12.2-1
- 21.12.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 07 2022 Gwyn Ciesla <gwync@protonmail.com> - 21.12.1-1
- 21.12.1

* Mon Dec 13 2021 Gwyn Ciesla <gwync@protonmail.com> - 21.12.0-1
- 21.12.0

* Wed Dec 01 2021 Gwyn Ciesla <gwync@protonmail.com> - 21.11.90-1
- 21.11.90

* Sun Nov 14 2021 Gwyn Ciesla <gwync@protonmail.com> - 21.11.80-1
- 21.11.80

* Fri Nov 05 2021 Gwyn Ciesla <gwync@protonmail.com> - 21.08.3-1
- 21.08.3

* Thu Oct 07 2021 Gwyn Ciesla <gwync@protonmail.com> - 21.08.2-1
- 21.08.2

* Thu Sep 02 2021 Gwyn Ciesla <gwync@protonmail.com> - 21.08.1-1
- 21.08.1

* Fri Aug 13 2021 Gwyn Ciesla <gwync@protonmail.com> - 21.08.0-1
- 21.08.0

* Fri Jul 30 2021 Gwyn Ciesla <gwync@protonmail.com> - 21.07.90-1
- 21.07.90

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.07.80-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 16 2021 Gwyn Ciesla <gwync@protonmail.com> - 21.07.80-1
- 21.07.80

* Thu Jul 08 2021 Gwyn Ciesla <gwync@protonmail.com> - 21.04.3-1
- 21.04.3

* Thu Jun 10 2021 Gwyn Ciesla <gwync@protonmail.com> - 21.04.2-1
- 21.04.2

* Fri May 14 2021 Gwyn Ciesla <gwync@protonmail.com> - 21.04.1-1
- 21.04.1

* Fri Apr 23 2021 Gwyn Ciesla <gwync@protonmail.com> - 21.04.0-1
- 21.04.0

* Mon Apr 12 2021 Gwyn Ciesla <gwync@protonmail.com> - 21.03.90-1
- 21.03.90

* Mon Mar 22 2021 Gwyn Ciesla <gwync@protonmail.com> - 21.03.80-1
- 21.03.80

* Thu Mar 04 2021 Gwyn Ciesla <gwync@protonmail.com> - 20.12.3-1
- 20.12.3

* Thu Feb 04 2021 Gwyn Ciesla <gwync@protonmail.com> - 20.12.2-1
- 20.12.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 08 2021 Gwyn Ciesla <gwync@protonmail.com> - 20.12.1-1
- 20.12.1

* Thu Dec 10 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.12.0-1
- 20.12.0

* Mon Nov 30 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.11.90-1
- 20.11.90

* Mon Nov 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.11.80-1
- 20.11.80

* Fri Nov 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.08.3-1
- 20.08.3

* Sat Oct 10 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.08.2-1
- 20.08.2

* Thu Sep 03 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.08.1-1
- 20.08.1

* Fri Aug 14 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.08.0-1
- 20.08.0

* Mon Aug 03 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.07.90-1
- 20.07.90

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.07.80-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.07.80-1
- 20.07.80

* Fri Jul 10 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.04.3-1
- 20.04.3

* Thu Jun 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.04.2-1
- 20.04.2

* Mon May 18 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.04.1-1
- 20.04.1

* Thu Apr 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.04.0-1
- 20.04.0

* Fri Apr 03 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.03.90-1
- 20.03.90

* Fri Mar 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 20.03.80-1
- 20.03.80

* Thu Mar 05 2020 Gwyn Ciesla <gwync@protonmail.com> - 19.12.3-1
- 19.12.3

* Fri Feb 07 2020 Gwyn Ciesla <gwync@protonmail.com> - 19.12.2-1
- 19.12.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Gwyn Ciesla <gwync@protonmail.com> - 19.12.1-1
- 19.12.1

* Thu Dec 12 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.12.0-1
- 19.12.0

* Mon Dec 02 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.11.90-1
- 19.11.90

* Mon Nov 18 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.11.80-1
- 19.11.80

* Thu Nov 07 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.08.3-1
- 19.08.3

* Fri Oct 11 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.08.2-1
- 19.08.2

* Thu Sep 05 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.08.1-1
- 19.08.1

* Fri Aug 16 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.08.0-1
- 19.08.0

* Fri Aug 02 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.07.90-1
- 19.07.90

* Wed Jul 24 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.07.80-1
- 19.07.80

* Thu Jul 11 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.04.3-1
- 19.04.3

* Thu Jun 06 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.04.2-1
- 19.04.2

* Thu May 09 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.04.1-1
- 19.04.1

* Thu Apr 18 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.04.0-1
- 19.04.0

* Fri Apr 05 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.03.90-1
- 19.03.90

* Fri Mar 22 2019 Gwyn Ciesla <gwync@protonmail.com> - 19.03.80-1
- 19.03.80

* Thu Mar 07 2019 Gwyn Ciesla <gwync@protonmail.com> - 18.12.3-1
- 18.12.3

* Fri Feb 08 2019 Gwyn Ciesla <limburgher@gmail.com> - 18.12.2-1
- 18.12.2

* Thu Jan 31 2019 Gwyn Ciesla <limburgher@gmail.com> - 18.12.1-1
- 18.12.1

* Mon Nov 26 2018 Gwyn Ciesla <limburgher@gmail.com> - 18.11.80-1
- 18.11.80

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.5.0-13
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 15 2015 Jon Ciesla <limburgher@gmail.com> - 2.5.0-7
- libkdegames rebuild.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 03 2012 Rex Dieter <rdieter@fedoraproject.org> 2.5.0-2
- do safer out-of-src-tree build
- add minimal/versioned kdelibs4 dep
- drop .desktop permissions hack (rpmlint be darned, it's legit)
- use %%find_lang --with-kde
- use %%_kde4_iconsdir consistently

* Thu Aug 30 2012 Julian Aloofi <julian@fedoraproject.org> 2.5.0-1
- update to latest upstream release
- remove the patch for building against the new KDEgames API

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Julian Aloofi <julian@fedoraproject.org> 2.4.2-2
- apply patch to build against the new KDEgames API
- removed the buildroot tag

* Mon Apr 30 2012 Julian Aloofi <julian@fedoraproject.org> 2.4.2-1
- update to latest upstream release

* Sat Nov 12 2011 Julian Aloofi <julian@fedoraproject.org> 2.4.0-1
- update to latest upstream release

* Mon Jun 13 2011 Julian Aloofi <julian@fedoraproject.org> 2.3.2-1
- update to latest upstream release

* Mon Mar 21 2011 Julian Aloofi <julian@fedoraproject.org> 2.3.1-1
- update to latest upstream release

* Fri Mar 11 2011 Julian Aloofi <julian@fedoraproject.org> 2.3.0-1
- update to latest upstream release

* Sun Feb 13 2011 Julian Aloofi <julian@fedoraproject.org> 2.2.0-4
- fix permissions of the desktop file

* Mon Feb 07 2011 Julian Aloofi <julian@fedoraproject.org> 2.2.0-3
- clarification on the license tag

* Mon Feb 07 2011 Julian Aloofi <julian@fedoraproject.org> 2.2.0-2
- using macros in Source0
- build with the proper make flags

* Mon Jan 31 2011 Julian Aloofi <julian@fedoraproject.org> 2.2.0-1
- initial package
