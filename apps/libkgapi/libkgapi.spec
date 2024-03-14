# https://bugzilla.redhat.com/show_bug.cgi?id=1895674
%global _lto_cflags %{nil}

Name:    libkgapi
Version: 24.02.1
Release: 1%{?dist}
Summary: Library to access to Google services

License: GPLv2+
URL:     https://invent.kde.org/pim/%{name}
%apps_source

BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules

BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6Wallet)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)

BuildRequires:  pkgconfig(libsasl2)


%description
Library to access to Google services, this package is needed by kdepim-runtime
to build akonadi-google resources.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6CalendarCore)
Requires:       cmake(KF6Contacts)
%description devel
Libraries and header files for developing applications that use akonadi-google
resources.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%find_lang_kf6 libkgapi6_qt


%files -f libkgapi6_qt.lang
%doc README*
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_libdir}/sasl2/libkdexoauth2.so*
%{_kf6_libdir}/libKPim6GAPIBlogger.so.*
%{_kf6_libdir}/libKPim6GAPICalendar.so.*
%{_kf6_libdir}/libKPim6GAPICore.so.*
%{_kf6_libdir}/libKPim6GAPIDrive.so.*
%{_kf6_libdir}/libKPim6GAPILatitude.so.*
%{_kf6_libdir}/libKPim6GAPIMaps.so.*
%{_kf6_libdir}/libKPim6GAPIPeople.so.*
%{_kf6_libdir}/libKPim6GAPITasks.so.*

%files devel
%{_kf6_libdir}/libKPim6GAPIPeople.so
%{_kf6_libdir}/libKPim6GAPIBlogger.so
%{_kf6_libdir}/libKPim6GAPICalendar.so
%{_kf6_libdir}/libKPim6GAPICore.so
%{_kf6_libdir}/libKPim6GAPIDrive.so
%{_kf6_libdir}/libKPim6GAPILatitude.so
%{_kf6_libdir}/libKPim6GAPIMaps.so
%{_kf6_libdir}/libKPim6GAPITasks.so
%{_kf6_libdir}/cmake/KPim6GAPI/
%dir %{_includedir}/KPim6/
%{_includedir}/KPim6/KGAPI/


%changelog
* Thu Mar 21 2024 Pavel Solovev <daron439@gmail.com> - 24.02.1-1
- Update to 24.02.1

* Thu Oct 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.2-1
- 23.08.2

* Sat Sep 16 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.1-1
- 23.08.1

* Sat Aug 26 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.0-1
- 23.08.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.3-1
- 23.04.3

* Tue Jun 06 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.2-1
- 23.04.2

* Sat May 13 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.1-1
- 23.04.1

* Fri Apr 14 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.0-1
- 23.04.0

* Fri Mar 31 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.90-1
- 23.03.90

* Mon Mar 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.80-1
- 23.03.80

* Thu Mar 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 22.12.3-1
- 22.12.3

* Tue Jan 31 2023 Marc Deop <marcdeop@fedoraproject.org> - 22.12.2-1
- 22.12.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 Justin Zobel <justin@1707.io> - 22.12.1-1
- Update to 22.12.1

* Mon Dec 19 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.12.0-1
- 22.12.0

* Fri Nov 04 2022 Marc Deop i Argemí (Private) <marc@marcdeop.com> - 22.08.3-1
- 22.08.3

* Fri Oct 14 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.2-1
- 22.08.2

* Thu Sep 08 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.1-1
- 22.08.1

* Fri Aug 19 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.0-1
- 22.08.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Than Ngo <than@redhat.com> - 22.04.3-1
- 22.04.3

* Fri Jun 24 2022 Than Ngo <than@redhat.com> - 22.04.2-1
- 22.04.2

* Thu May 12 2022 Justin Zobel <justin@1707.io> - 22.04.1-1
- Update to 22.04.1

* Mon May 09 2022 Justin Zobel <justin@1707.io> - 22.04.0-1
- Update to 22.04.0

* Wed Mar 02 2022 Marc Deop <marcdeop@fedoraproject.org> - 21.12.3-1
- 21.12.3

* Fri Feb 04 2022 Rex Dieter <rdieter@fedoraproject.org> - 21.12.2-1
- 21.12.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 06 2022 Marc Deop <marcdeop@fedoraproject.org> - 21.12.1-1
- 21.12.1

* Mon Dec 20 2021 Marc Deop <marcdeop@fedoraproject.org> - 21.12.0-1
- 21.12.0

* Tue Nov 02 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.08.3-1
- 21.08.3

* Thu Oct 21 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.08.2-1
- 21.08.2

* Wed Jul 28 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.3-1
- 21.04.3

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.2-1
- 21.04.2

* Tue May 11 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.1-1
- 21.04.1

* Tue Apr 27 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.0-1
- 21.04.0

* Mon Apr 05 2021 Rex Dieter <rdieter@fedoraproject.org> - 20.12.3-2
- drop qtwebengine dependency (yay, more arch's support)

* Wed Mar 03 2021 Rex Dieter <rdieter@fedoraproject.org> - 20.12.3-1
- 20.12.3

* Thu Feb 04 2021 Rex Dieter <rdieter@fedoraproject.org> - 20.12.2-1
- 20.12.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.08.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 08 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.3-2
- build without lto (#1895674)

* Fri Nov  6 15:35:45 CST 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.3-1
- 20.08.3

* Tue Sep 15 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.1-1
- 20.08.1

* Tue Aug 18 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.0-1
- 20.08.0

* Mon Aug 10 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.3-4
- use new cmake macros, cosmetics

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.3-1
- 20.04.3

* Fri Jun 12 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.2-1
- 20.04.2

* Wed May 27 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.1-1
- 20.04.1

* Fri Apr 24 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.0-1
- 20.04.0

* Sat Mar 07 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.3-1
- 19.12.3

* Tue Feb 04 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.2-1
- 19.12.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.1-1
- 19.12.1

* Mon Nov 11 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.3-1
- 19.08.3

* Fri Oct 18 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.2-1
- 19.08.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.04.3-1
- 19.04.3

* Wed Jun 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.04.2-1
- 19.04.2

* Fri Mar 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.3-1
- 18.12.3

* Tue Feb 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.2-1
- 18.12.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.1-1
- 18.12.1

* Fri Dec 14 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.12.0-1
- 18.12.0

* Tue Nov 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.3-1
- 18.08.3

* Wed Oct 10 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.2-1
- 18.08.2

* Mon Oct 01 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.1-1
- 18.08.1

* Fri Jul 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.3-1
- 18.04.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.2-1
- 18.04.2

* Wed May 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.1-1
- 18.04.1

* Fri Apr 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.0-1
- 18.04.0

* Tue Mar 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.3-1
- 17.12.3

* Tue Feb 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.2-1
- 17.12.2

* Thu Jan 11 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.1-1
- 17.12.1

* Tue Dec 12 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.12.0-1
- 17.12.0

* Wed Dec 06 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.11.90-1
- 17.11.90

* Wed Nov 22 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.11.80-1
- 17.11.80

* Wed Nov 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.3-1
- 17.08.3

* Mon Sep 25 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.1-1
- 17.08.1

* Fri Jul 28 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.3-1
- 17.04.3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.2-1
- 17.04.2

* Sun May 14 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.1 -1
- 17.04.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 16 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.3.1-2
- rebuild (kde-apps-16.12)

* Thu Oct 20 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.3.1-1
- 5.3.1 (#1387323)

* Mon Aug 08 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.3.0-1
- LibKGAPI 5.3.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 23 2016 Robert Scheck <robert@fedoraproject.org> - 5.1.0-2
- Rebuild for libical 2.0.0

* Mon Dec 07 2015 Jan Grulich <jgrulich@redhat.com> - 5.1.0-1
- Update to 5.1.0 (KF5-based)

* Fri Nov 13 2015 Rex Dieter <rdieter@fedoraproject.org> - 2.2.0-6
- fix(drop) hard-coded kdepimlibs dep (it won't be changing any time soon)
- use %%license
- .spec cosmetics
- trim changelog

* Wed Jul 05 2015 Daniel Vrátil <dvratil@redhat.com> - 2.2.0-5
- Pull upstream patch to fix timezone conversion

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.2.0-3
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 05 2014 Rex Dieter <rdieter@fedoraproject.org> 2.2.0-1
- 2.2.0

* Thu Jun 19 2014 Rex Dieter <rdieter@fedoraproject.org> 2.1.0-3
- BR: kdelibs4-webkit-devel

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 19 2014 Dan Vrátil <dvratil@redhat.com> - 2.1.0-1
- 2.1.0

* Thu Dec 05 2013 Dan Vrátil <dvratil@redhat.com> - 2.0.2-1
- 2.0.2

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 01 2013 Dan Vrátil <dvratil@redhat.com> 2.0.1-1
- 2.0.1

* Wed May 22 2013 Dan Vrátil <dvratil@redhat.com> 2.0.0-1
- 2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 16 2012 Dan Vrátil <dvratil@redhat.com> 0.4.4-1
- 0.4.4

* Tue Nov 27 2012 Dan Vrátil <dvratil@redhat.com> 0.4.3-3
- Rebuild against qjson 0.8.1

* Fri Nov 23 2012 Dan Vrátil <dvratil@redhat.com> 0.4.3-2
- Rebuild against qjson 0.8.0

* Sun Nov 11 2012 Mario Santagiuliana <fedora@marionline.it> 0.4.3-1
- Update to new version 0.4.3

* Sun Aug 26 2012 Rex Dieter <rdieter@fedoraproject.org> 0.4.2-1
- 0.4.2

* Sat Aug 11 2012 Mario Santagiuliana <fedora@marionline.it> 0.4.1-1
- Update to new version 0.4.1

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Rex Dieter <rdieter@fedoraproject.org>
- 0.4.0-5
- -devel: tighten subpkg dep via %%_isa, Req: kdepimlibs-devel
- Parsing token page failed (kde#301240)

* Sun Jun 10 2012 Rex Dieter <rdieter@fedoraproject.org> 0.4.0-4
- -devel: track files closer
- pkgconfig-style deps

* Thu Jun 07 2012 Mario Santagiuliana <fedora@marionline.it> 0.4.0-3
- Update spec file following Gregor Tätzner request:
https://bugzilla.redhat.com/show_bug.cgi?id=817622#c8

* Thu May 31 2012 Mario Santagiuliana <fedora@marionline.it> 0.4.0-2
- Update spec file following Rex Dieter and Kevin Kofler suggestion
- Add obsolete and provide for devel subpkg

* Thu May 31 2012 Mario Santagiuliana <fedora@marionline.it> 0.4.0-1
- Update to new version 0.4.0
- Update to new licence GPLv2+
- Update to new name libkgapi
- Add obsolete and provide libkgoogle

* Wed May 30 2012 Mario Santagiuliana <fedora@marionline.it> 0.3.2-1.20120530gitf18d699
- Update spec comment to new git repository
- Update to new version 0.3.2
- Snapshot f18d699d9ef7ceceff06c2bb72fc00f34811c503

* Mon Apr 30 2012 Mario Santagiuliana <fedora@marionline.it> 0.3.1-1.20120430gitefb3215
- Rename package from akonadi-google to libkgoogle
- Update spec file
- Snapshot efb32159c283168cc2ab1a39e6fa3c8a30fbc941

* Mon Apr 30 2012 Mario Santagiuliana <fedora@marionline.it> 0.3.1-1
- New version 0.3.1

* Thu Apr 01 2012 Mario Santagiuliana <fedora@marionline.it> 0.3-1.20120402git3e0a93e
- New version 0.3
- Update to git snapshot 3e0a93e1b24cd7b6e394cf76d153c428246f9fa9
- Obsolete akonadi-google-tasks
- Fix error in changelog

* Thu Mar 01 2012 Mario Santagiuliana <fedora@marionline.it> 0.2-12.20120301git41cd7c5
- Update to git snapshot 41cd7c5d6e9cfb62875fd21f8a920a235b7a7d9c

* Wed Jan 20 2012 Mario Santagiuliana <fedora@marionline.it> 0.2-11.20120121gitbe021c6
- Update to git snapshot be021c6f12e6804976dcac203a1864686a219c26

* Wed Jan 20 2012 Mario Santagiuliana <fedora@marionline.it> 0.2-10.20120120git11bf6ad
- Update spec file follow comment 1:
https://bugzilla.redhat.com/show_bug.cgi?id=783317#c1
- Update to git snapshot 11bf6ad40dd93eda1f880a99d592009ea3ff47ac
- Include LICENSE

* Thu Jan 19 2012 Mario Santagiuliana <fedora@marionline.it> 0.2-9.20120119git754771b
- Create spec file for Fedora Review
- Source package create from git snapshot 754771b6081b194aedf750fac76a9af2709a5de3

* Wed Nov 16 2011 Dan Vratil <dan@progdan.cz> 0.2-8.1
- Initial SPEC
