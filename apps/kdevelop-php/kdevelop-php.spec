%global commit0 2446569a5e9babd1bf1a0ffa2f40dbb86fa3ac88
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

%global base_name kdev-php

Name:           kdevelop-php
Summary:        Php language and documentation plugins for KDevelop
Version:        24.08.3
Release:        1%{?dist}

# Most files LGPLv2+/GPLv2+
License:        GPL-2.0-or-later
URL:            https://invent.kde.org/kdevelop/kdev-php
%apps_source

BuildRequires:  extra-cmake-modules

BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6TextEditor)
BuildRequires:  cmake(KF6ThreadWeaver)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake(KDevPlatform)
BuildRequires:  cmake(KDevelop-PG-Qt)

%{?kdevelop_requires}

%description
%{summary}.


%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name


%files -f %{name}.lang
%doc AUTHORS
%license LICENSES/*
%{_includedir}/kdev-php/
%{_kf6_datadir}/kdevappwizard/
%{_kf6_datadir}/kdevphpsupport/
%{_kf6_datadir}/metainfo/org.kde.kdev-php.metainfo.xml
%{_kf6_datadir}/qlogging-categories6/kdevphpsupport.categories
%{_kf6_libdir}/cmake/KDevPHP/
%{_kf6_libdir}/libkdevphp*.so
%{_kf6_qtplugindir}/kdevplatform/


%changelog
* Tue Nov 05 2024 Pavel Solovev <daron439@gmail.com> - 24.08.3-1
- Update to 24.08.3

* Mon Oct 07 2024 Pavel Solovev <daron439@gmail.com> - 24.08.2-1
- Update to 24.08.2

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

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90


* Fri Jan 05 2024 Marie Loise Nolden <loise@kde.org> - 24.01.85-1
- update to 24.01.85 (still using qt5/kf5)

* Wed Dec 20 2023 Than Ngo <than@redhat.com> - 23.08.4-1
- update to 23.08.4

* Thu Oct 12 2023 Than Ngo <than@redhat.com> - 23.08.2-1
- update to 23.08.2

* Sat Sep 16 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.1-1
- 23.08.1

* Sat Aug 26 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.0-1
- 23.08.0

* Fri Aug 11 2023 Than Ngo <than@redhat.com> - 23.07.90-1
- 23.07.90

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.3-1
- 23.04.3

* Tue Jun 06 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.2-1
- 23.04.2

* Thu May 11 2023 Than Ngo <than@redhat.com> - 23.04.1-1
- update to 23.04.1

* Fri Apr 14 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.0-1
- 23.04.0

* Fri Mar 31 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.90-1
- 23.03.90

* Wed Mar 22 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.80-1
- 23.03.80

* Wed Mar 22 2023 Jan Grulich <jgrulich@redhat.com> - 22.12.3-2
- Rebuild (grantlee-qt5)

* Thu Mar 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 22.12.3-1
- 22.12.3

* Mon Feb 20 2023 Than Ngo <than@redhat.com> - 22.12.2-2
- migrated to SPDX license

* Tue Jan 31 2023 Marc Deop <marcdeop@fedoraproject.org> - 22.12.2-1
- 22.12.2

* Tue Jan 31 2023 Marc Deop <marcdeop@fedoraproject.org> - 22.12.1-3
- BuildRequires on kdevelop-devel instead of old kdevplatform-devel

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jan 07 2023 Marc Deop <marcdeop@fedoraproject.org> - 22.12.1-1
- 22.12.1

* Fri Dec 09 2022 Than Ngo <than@redhat.com> - 22.12.0-1
- 22.12.0

* Thu Nov 03 2022 Than Ngo <than@redhat.com> - 22.08.3-1
- 22.08.3

* Fri Oct 14 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.2-1
- 22.08.2

* Thu Sep 08 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.1-1
- 22.08.1

* Fri Aug 19 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.0-1
- 22.08.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 07 2022 Than Ngo <than@redhat.com> - 22.04.3-1
- 22.04.3

* Thu Jun 09 2022 Than Ngo <than@redhat.com> - 22.04.2-1
- 22.04.2

* Thu May 12 2022 Than Ngo <than@redhat.com> - 22.04.1-1
- 22.04.1

* Thu Apr 21 2022 Than Ngo <than@redhat.com> - 22.04.0-1
- 22.04.0

* Thu Mar 03 2022 Marc Deop <marcdeop@fedoraproject.org> - 21.12.3-1
- 21.12.3

* Thu Feb 03 2022 Than Ngo <than@redhat.com> - 21.12.2-1
- update to 21.12.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 19 2022 Than Ngo <than@redhat.com> - 21.12.1-1
- update to 21.12.1

* Tue Dec 14 2021 Than Ngo <than@redhat.com> - 21.12.0-1
- update to 21.12.0
- enable s390x build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 5.6.2-2
- Rebuilt for removed libstdc++ symbol (#1937698)

* Tue Feb 02 2021 Jan Grulich <jgrulich@redhat.com> - 5.6.2-1
- 5.6.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec  9 10:49:22 CET 2020 Jan Grulich <jgrulich@redhat.com> - 5.6.1-1
- 5.6.1

* Tue Sep 08 2020 Jan Grulich <jgrulich@redhat.com> - 5.6.0-1
- 5.6.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 02 2020 Jan Grulich <jgrulich@redhat.com> - 5.5.2-1
- 5.5.2

* Wed May 06 2020 Jan Grulich <jgrulich@redhat.com> - 5.5.1-1
- 5.5.1

* Mon Feb 03 2020 Jan Grulich <jgrulich@redhat.com> - 5.5.0-1
- 5.5.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Jan Grulich <jgrulich@redhat.com> - 5.4.6-1
- 5.4.6

* Tue Dec 03 2019 Jan Grulich <jgrulich@redhat.com> - 5.4.5-1
- 5.4.5

* Tue Nov 05 2019 Jan Grulich <jgrulich@redhat.com> - 5.4.4-1
- 5.4.4

* Tue Oct 22 2019 Jan Grulich <jgrulich@redhat.com> - 5.4.3-1
- 5.4.3

* Tue Sep 03 2019 Jan Grulich <jgrulich@redhat.com> - 5.4.2-1
- 5.4.2

* Tue Aug 13 2019 Jan Grulich <jgrulich@redhat.com> - 5.4.1-1
- 5.4.1

* Wed Aug 07 2019 Jan Grulich <jgrulich@redhat.com> - 5.4.0-1
- 5.4.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Jan Grulich <jgrulich@redhat.com> - 5.3.3-1
- 5.3.3

* Fri Mar 15 2019 Jan Grulich <jgrulich@redhat.com> - 5.3.2-1
- 5.3.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 11 2018 Jan Grulich <jgrulich@redhat.com> - 5.3.1-1
- 5.3.1

* Wed Nov 14 2018 Jan Grulich <jgrulich@redhat.com> - 5.3.0-1
- 5.3.0

* Tue Oct 02 2018 Jan Grulich <jgrulich@redhat.com> - 5.2.80-1
- 5.2.80 (beta)

* Mon Aug 27 2018 Jan Grulich <jgrulich@redhat.com> - 5.2.4-1
- 5.2.4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 21 2018 Jan Grulich <jgrulich@redhat.com> - 5.2.3-1
- Update to 5.2.3

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 24 2017 Jan Grulich <jgrulich@redhat.com> - 5.2.1-1
- Update to 5.2.1

* Tue Nov 14 2017 Jan Grulich <jgrulich@redhat.com> - 5.2.0-1
- Update to 5.2.0

* Fri Oct 06 2017 Jan Grulich <jgrulich@redhat.com> - 5.1.80-1
- Update to 5.1.80 (beta)

* Tue Aug 29 2017 Jan Grulich <jgrulich@redhat.com> - 5.1.2-1
- Update to 5.1.2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 29 2017 Jan Grulich <jgrulich@redhat.com> - 5.1.1-1
- Update to 5.1.1

* Mon Mar 20 2017 Jan Grulich <jgrulich@redhat.com> - 5.1.0-1
- Update to 5.1.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.80-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 17 2017 Jan Grulich <jgrulich@redhat.com> - 5.0.80-1
- Update to 5.0.80 (beta)

* Fri Dec 02 2016 Jan Grulich <jgrulich@redhat.com> - 5.0.3-1
- Update to 5.0.3

* Mon Oct 17 2016 Jan Grulich <jgrulich@redhat.com> - 5.0.2-1
- Update to 5.0.2

* Mon Sep 19 2016 Jan Grulich <jgrulich@redhat.com> - 5.0.1-1
- Update to 5.0.1

* Wed Sep 07 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.0.0-2
- use %%{?kdevelop_requires}, cosmetics

* Wed Aug 31 2016 Helio Chissini de Castro <helio@kde.org> - 5.0.0-1
- New upstream version 5.0.0

* Wed Jun 08 2016 Jan Grulich <jgrulich@redhat.com> - 5.0.0-0.1.20160608git
- Package latest git snapshot to address GCC 6 related crashes
  Resolves: bz#1343439

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.90.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Jan Grulich <jgrulich@redhat.com> - 4.90.91-1
- Update to 4.90.91 (beta 2)

* Fri Oct 30 2015 Jan Grulich <jgrulich@redhat.com> - 4.90.90-1
- Update to 4.90.90 (beta 1)

* Tue Oct 13 2015 Jan Grulich <jgrulich@redhat.com> - 1.7.2-2
- Bump required kdevelop version

* Mon Oct 12 2015 Jan Grulich <jgrulich@redhat.com> - 1.7.2-1
- Update to 1.7.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.7.1-2
- Rebuilt for GCC 5 C++11 ABI change

* Wed Feb 04 2015 Jan Grulich <jgrulich@redhat.com> - 1.7.1-1
- Update to 1.7.1

* Fri Sep 26 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.7.0-2
- Version the Requires: kdevelop correctly

* Wed Aug 27 2014 Jan Grulich <jgrulich@redhat.com> - 1.7.0-1
- Update to 1.7.0

* Fri Jul 11 2014 Jan Grulich <jgrulich@redhat.com> - 1.6.90-1
- Update to 1.6.90

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Dec 08 2013 Jan Grulich <jgrulich@redhat.com> - 1.6.0-1
- Update to 1.6.0

* Wed Nov 27 2013 Jan Grulich <jgrulich@redhat.com> - 1.5.90-1
- Update to 1.5.90

* Mon Nov 18 2013 Jan Grulich <jgrulich@redhat.com> - 1.5.80-1
- Update to 1.5.80

* Thu Oct 31 2013 Jan Grulich <jgrulich@redhat.com> - 1.5.2-1
- Update to 1.5.2

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 30 2013 Jan Grulich <jgrulich@redhat.com> - 1.5.1-1
- Update to 1.5.1

* Fri Apr 26 2013 Jan Grulich <jgrulich@redhat.com> 1.5.0-1
- Update to 1.5.0

* Thu Apr 25 2013 Jan Grulich <jgrulich@redhat.com> 1.4.90-1
- Update to 1.4.90 (RC1)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 05 2012 Jan Grulich <jgrulich@redhat.com> 1.4.1-1
- Update to 1.4.1

* Wed Oct 24 2012 Radek Novacek <rnovacek@redhat.com> 1.4.0-1
- Update to 1.4.0

* Fri Sep 07 2012 Radek Novacek <rnovacek@redhat.com> 1.3.90-1
- Update to 1.3.90 (RC 1)

* Thu Aug 09 2012 Radek Novacek <rnovacek@redhat.com> 1.3.80-1
- Update to 1.3.80 (beta 1)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 16 2012 Radek Novacek <rnovacek@redhat.com> 1.3.1-1
- Update to 1.3.1

* Tue Mar 13 2012 Than Ngo <than@redhat.com> - 1.3.0-2
- add missing kdevelop-php-docs

* Mon Mar 12 2012 Jaroslav Reznik <jreznik@redhat.com> 1.3.0-1
- Update to 1.3.0

* Mon Feb 27 2012 Radek Novacek <rnovacek@redhat.com> 1.2.90-2
- Rebuild for kdevelop-pg-qt 1.0.0

* Sun Feb 26 2012 Radek Novacek <rnovacek@redhat.com> 1.2.90-1
- Update to 1.2.90 (RC 1)

* Tue Feb 14 2012 Jaroslav Reznik <jreznik@redhat.com> 1.2.82-1
- Update to 1.2.82 (beta 2)

* Mon Jan 23 2012 Radek Novacek <rnovacek@redhat.com> 1.2.81-1
- Update to 1.2.81 (1.3 beta)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 28 2011 Radek Novacek <rnovacek@redhat.com> 1.2.3-1
- Update to 1.2.3

* Mon Apr 11 2011 Radek Novacek <rnovacek@redhat.com> 1.2.2-2
- BuildRequires kdevelop-pg-qt >= 0.9.5

* Thu Apr 07 2011 Radek Novacek <rnovacek@redhat.com> 1.2.2-1
- Update to 1.2.2

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 25 2011 Rex Dieter <rdieter@fedoraproject.org> - 1.2.0-1
- 1.2.0

* Fri Jan 21 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.1.90-1
- Update to 1.1.90 (1.2 RC1)

* Wed Jan 05 2011 Rex Dieter <rdieter@fedoraproject.org> - 1.1.81-1
- 1.1.81
- License: GPLv2+

* Fri Dec 10 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.1.1-3
- License: GPLv3+

* Fri Dec 10 2010 Rex Dieter <rdieter@fedoraproject.org> -  1.1.1-2
- License: GPLv2+

* Mon Dec 06 2010 Rex Dieter <rdieter@fedoraproject.org> - 1.1.1-1
- first try

