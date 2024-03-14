#global tests 1

Name:    kdepim-runtime
Summary: KDE PIM Runtime Environment
Epoch:   1
Version: 24.02.1
Release: 1%{?dist}

License: GPLv2
URL:     https://invent.kde.org/pim/%{name}
%apps_source

BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6DAV)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6NotifyConfig)
BuildRequires:  cmake(KF6TextCustomEditor)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6DocTools)

BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6AkonadiCalendar)
BuildRequires:  cmake(KPim6AkonadiContactWidgets)
BuildRequires:  cmake(KPim6AkonadiMime)
BuildRequires:  cmake(KPim6AkonadiNotes)
BuildRequires:  cmake(KPim6CalendarUtils)
BuildRequires:  cmake(KPim6GAPI)
BuildRequires:  cmake(KPim6IdentityManagementWidgets)
BuildRequires:  cmake(KPim6IMAP)
BuildRequires:  cmake(KPim6LdapWidgets)
BuildRequires:  cmake(KPim6MailTransport)
BuildRequires:  cmake(KPim6Mbox)
BuildRequires:  cmake(KPim6Mime)

BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6NetworkAuth)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6TextToSpeech)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  boost-devel
BuildRequires:  cmake(Etebase)
BuildRequires:  cmake(libkolabxml)
BuildRequires:  cmake(Qca-qt6)
BuildRequires:  pkgconfig(libical)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(shared-mime-info)

%if 0%{?tests}
BuildRequires:  dbus-x11
BuildRequires:  akonadi-mysql
BuildRequires:  xorg-x11-server-Xvfb
%endif

Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description
%{summary}.

%package libs
Summary: %{name} runtime libraries
Obsoletes: kf5-kmailtransport-akonadi < 23.08.0
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: akonadi%{?_isa} >= %{version}
%description libs
%{summary}.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n kdepim-runtime-%{version}%{?pre} -p1


%build
%cmake_kf6 \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html


%check
%if 0%{?tests}
xvfb-run -a bash -c "%ctest" || :
%endif
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/akonadi_*
%{_kf6_bindir}/gidmigrator
%{_kf6_datadir}/akonadi/agents/*
%{_kf6_datadir}/akonadi/firstrun/*
%{_kf6_datadir}/akonadi/davgroupware-providers/*
%{_kf6_datadir}/applications/org.kde.akonadi_*.desktop
%{_kf6_datadir}/dbus-1/interfaces/*.xml
%{_kf6_datadir}/icons/hicolor/*/apps/*
%{_kf6_datadir}/knotifications6/*
%{_kf6_datadir}/mime/packages/kdepim-mime.xml
%{_kf6_datadir}/qlogging-categories6/*%{name}.*


%files libs
%{_kf6_libdir}/libakonadi-filestore.so.*
%{_kf6_libdir}/libakonadi-singlefileresource.so.*
%{_kf6_libdir}/libfolderarchivesettings.so.*
%{_kf6_libdir}/libkmindexreader.so.*
%{_kf6_libdir}/libmaildir.so.*
%{_kf6_libdir}/libnewmailnotifier.so.*
%{_kf6_plugindir}/kio/akonadi.so
# todo: enumerate akonadi config plugins -- rdieter
%{_kf6_qtplugindir}/pim6/akonadi/config/
%{_kf6_qtplugindir}/pim6/kcms/kaddressbook/kcm_ldap.so
%{_kf6_qtplugindir}/pim6/mailtransport/mailtransport_akonadiplugin.so


%changelog
* Thu Mar 21 2024 Pavel Solovev <daron439@gmail.com> - 1:24.02.1-1
- Update to 24.02.1

* Thu Oct 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:23.08.2-1
- 23.08.2

* Mon Sep 25 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:23.08.1-3
- Add Obsoletes: kf5-kmailtransport-akonadi < 23.08.0

* Wed Sep 20 2023 Alessandro Astone <ales.astone@gmail.com> - 1:23.08.1-2
- Backport fixes for Google integration

* Sat Sep 16 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:23.08.1-1
- 23.08.1

* Sat Aug 26 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:23.08.0-1
- 23.08.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:23.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:23.04.3-1
- 23.04.3

* Tue Jun 06 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:23.04.2-1
- 23.04.2

* Sat May 13 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:23.04.1-1
- 23.04.1

* Fri Apr 14 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:23.04.0-1
- 23.04.0

* Fri Mar 31 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:23.03.90-1
- 23.03.90

* Mon Mar 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:23.03.80-1
- 23.03.80

* Thu Mar 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:22.12.3-1
- 22.12.3

* Tue Jan 31 2023 Marc Deop <marcdeop@fedoraproject.org> - 1:22.12.2-1
- 22.12.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:22.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 Justin Zobel <justin@1707.io> - 22.12.1-1
- Update to 22.12.1

* Tue Jan 03 2023 Justin Zobel <justin@1707.io> - 22.12.1-1
- Update to 22.12.1

* Mon Dec 19 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:22.12.0-1
- 22.12.0

* Fri Nov 04 2022 Marc Deop i Argemí (Private) <marc@marcdeop.com> - 1:22.08.3-1
- 22.08.3

* Fri Oct 14 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:22.08.2-1
- 22.08.2

* Thu Sep 08 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:22.08.1-1
- 22.08.1

* Fri Aug 19 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:22.08.0-1
- 22.08.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:22.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Than Ngo <than@redhat.com> - 22.04.3-1
- 22.04.3

* Thu May 12 2022 Justin Zobel <justin@1707.io> - 22.04.1-1
- Update to 22.04.1

* Mon May 09 2022 Justin Zobel <justin@1707.io> - 22.04.0-1
- Update to 22.04.0

* Wed Mar 02 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:21.12.3-1
- 21.12.3

* Sun Feb 13 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 1:21.12.2-3
- Adding upstream patch "disable sync contact patch

* Sat Feb 12 2022 Jeff Law <jeffreyalaw@gmail.com> - 1:21.12.2-2
- Re-enable LTO

* Fri Feb 04 2022 Rex Dieter <rdieter@fedoraproject.org> - 1:21.12.2-1
- 21.12.2

* Thu Feb 03 2022 Than Ngo <than@redhat.com> - 21.12.1-3
- Fix build with GCC 12- require new kf5-kmailtransport-21.12.1-3

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:21.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 06 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:21.12.1-1
- 21.12.1

* Mon Dec 20 2021 Marc Deop <marcdeop@fedoraproject.org> - 1:21.12.0-1
- 21.12.0

* Tue Nov 02 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:21.08.3-1
- 21.08.3

* Thu Oct 21 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:21.08.2-1
- 21.08.2

* Wed Jul 28 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:21.04.3-1
- 21.04.3

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:21.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:21.04.2-1
- 21.04.2

* Tue May 11 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:21.04.1-1
- 21.04.1

* Tue Apr 27 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:21.04.0-1
- 21.04.0

* Wed Mar 03 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:20.12.3-1
- 20.12.3

* Thu Feb 04 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:20.12.2-1
- 20.12.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:20.08.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov  6 15:33:01 CST 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:20.08.3-1
- 20.08.3

* Tue Sep 15 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:20.08.1-1
- 20.08.1

* Tue Aug 18 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:20.08.0-1
- 20.08.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:20.04.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:20.04.3-2
- rebuild (kdav)

* Fri Jul 10 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:20.04.3-1
- 20.04.3

* Fri Jun 12 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:20.04.2-1
- 20.04.2

* Wed May 27 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:20.04.1-1
- 20.04.1

* Fri Apr 24 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:20.04.0-1
- 20.04.0

* Sat Mar 07 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:19.12.3-1
- 19.12.3

* Tue Feb 04 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:19.12.2-1
- 19.12.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:19.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:19.12.1-1
- 19.12.1

* Mon Nov 11 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:19.08.3-1
- 19.08.3

* Fri Oct 18 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:19.08.2-1
- 19.08.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:19.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:19.04.3-1
- 19.04.3

* Wed Jun 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:19.04.2-1
- 19.04.2

* Tue Apr 30 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:18.12.3-2
- fix URL (#1704749)

* Fri Mar 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:18.12.3-1
- 18.12.3

* Tue Feb 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:18.12.2-1
- 18.12.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:18.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:18.12.1-1
- 18.12.1

* Thu Jan 03 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:18.12.0-2
- add versioned  Requires: libkgapi (#1662756)

* Fri Dec 14 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:18.12.0-1
- 18.12.0

* Tue Nov 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:18.08.3-1
- 18.08.3

* Wed Oct 10 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:18.08.2-1
- 18.08.2

* Mon Oct 01 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:18.08.1-1
- 18.08.1

* Fri Jul 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:18.04.3-1
- 18.04.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:18.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:18.04.2-1
- 18.04.2

* Wed May 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:18.04.1-1
- 18.04.1

* Fri Apr 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:18.04.0-1
- 18.04.0

* Tue Mar 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:17.12.3-1
- 17.12.3

* Tue Feb 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:17.12.2-1
- 17.12.2

* Thu Jan 11 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:17.12.1-1
- 17.12.1

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:17.12.0-4
- Remove obsolete scriptlets

* Thu Dec 21 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:17.12.0-3
- Provides: bundled(libkolab)

* Thu Dec 14 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:17.12.0-2
- respin

* Tue Dec 12 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:17.12.0-1
- 17.12.0

* Wed Dec 06 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:17.11.90-1
- 17.11.90

* Wed Nov 22 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:17.11.80-1
- 17.11.80

* Tue Nov 21 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:17.08.3-2
- BR: Qt5TextToSpeech

* Wed Nov 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:17.08.3-1
- 17.08.3

* Mon Sep 25 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:17.08.1-1
- 17.08.1

* Fri Jul 28 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:17.04.3-1
- 17.04.3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:17.04.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Björn Esser <besser82@fedoraproject.org> - 1:17.04.2-2
- Rebuilt for Boost 1.64

* Thu Jun 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:17.04.2-1
- 17.04.2

* Tue May 30 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:17.04.1-2
- backport upstream fixes

* Sun May 14 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:17.04.1-1
- 17.04.1

* Thu Mar 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:16.12.3-1
- 16.12.3

* Thu Feb 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:16.12.2-1
- 16.12.2

* Wed Feb 08 2017 Adam Williamson <awilliam@redhat.com> - 1:16.12.1-2
- Rebuild for new boost

* Mon Jan 16 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:16.12.1-1
- 16.12.1

* Mon Dec 05 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:16.08.3-1
- 16.08.3

* Fri Oct 28 2016 Than Ngo <than@redhat.com> - 1:16.08.2-2
- don't build on ppc64/s390x as qtwebengine is not supported yet

* Thu Oct 13 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:16.08.2-1
- 16.08.2

* Tue Oct 04 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:16.08.1-2
- pull in upstream fixes

* Thu Sep 08 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:16.08.1-1
- 16.08.1

* Sun Sep 04 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:16.08.0-1
- 16.08.0

* Sun Jul 10 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:16.04.3-1
- 16.04.3

* Tue Jun 28 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:16.04.2-2
- BR: libkolab libkolabxml

* Sun Jun 12 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:16.04.2-1
- 16.04.2

* Thu May 26 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:16.04.1-1
- 16.04.1

* Mon May 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:16.04.0-1
- 16.04.0, update URL, support bootstrap, add %%check, -libs: move plugins here

* Tue Mar 15 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:15.12.3-1
- 15.12.3

* Sun Feb 14 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:15.12.2-1
- 15.12.2

* Sat Feb 06 2016 Rex Dieter <rdieter@fedoraproject.org> 1:15.12.1-1
- 15.12.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:15.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 23 2016 Robert Scheck <robert@fedoraproject.org> - 1:15.12.0-2
- Rebuild for libical 2.0.0

* Tue Dec 15 2015 Jan Grulich <jgrulich@redhat.com> - 1:15.12.0-1
- Update to 15.12.0

* Sun Dec 13 2015 Rex Dieter <rdieter@fedoraproject.org> 1:15.11.90-2
- drop %%kde_runtime_requires (kde4)

* Fri Dec 11 2015 Jan Grulich <jgrulich@redhat.com> - 1:15.11.90-1
- Update to 15.11.90 (KF5 based)

* Fri Oct 02 2015 Rex Dieter <rdieter@fedoraproject.org> 1:4.14.10-5
- drop use of kde4-only /usr/share/autostart, use %%license, update URL

* Tue Sep 15 2015 Rex Dieter <rdieter@fedoraproject.org> 1:4.14.10-4
- -libs: drop versioned kdepimlibs-akonadi dep

* Sun Sep 13 2015 Rex Dieter <rdieter@fedoraproject.org> 1:4.14.10-3
- rebuild (boost)

* Fri Jul 31 2015 Rex Dieter <rdieter@fedoraproject.org> 1:4.14.10-2
- (explicitly) BR: boost-devel

* Mon Jun 29 2015 Rex Dieter <rdieter@fedoraproject.org> - 1:4.14.10-1
- 4.14.10

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.14.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Rex Dieter <rdieter@fedoraproject.org> - 1:4.14.9-1
- 4.14.9

* Fri May 15 2015 Rex Dieter <rdieter@fedoraproject.org> - 1:4.14.8-1
- 4.14.8

* Fri Apr 10 2015 Rex Dieter <rdieter@fedoraproject.org> - 1:4.14.7-1
- 4.14.7

* Sun Mar 01 2015 Rex Dieter <rdieter@fedoraproject.org> - 1:4.14.6-1
- 4.14.6

* Tue Feb 24 2015 Rex Dieter <rdieter@fedoraproject.org> - 1:4.14.5-1
- 4.14.5

* Fri Feb 06 2015 Rex Dieter <rdieter@fedoraproject.org> 1:4.14.4-2
- rebuild (boost)

* Fri Jan 16 2015 Rex Dieter <rdieter@fedoraproject.org> - 1:4.14.4-1
- 4.14.4

* Sun Nov 09 2014 Rex Dieter <rdieter@fedoraproject.org> - 1:4.14.3-1
- 4.14.3

* Sun Oct 12 2014 Rex Dieter <rdieter@fedoraproject.org> - 1:4.14.2-1
- 4.14.2

* Tue Sep 16 2014 Rex Dieter <rdieter@fedoraproject.org> 1:4.14.1-2
- bump build deps for libkgapi, libkolab, BR: libaccounts-qt-devel

* Tue Sep 16 2014 Rex Dieter <rdieter@fedoraproject.org> - 1:4.14.1-1
- 4.14.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 15 2014 Rex Dieter <rdieter@fedoraproject.org> - 1:4.14.0-1
- 4.14.0

* Tue Aug 05 2014 Rex Dieter <rdieter@fedoraproject.org> - 1:4.13.97-1
- 4.13.97

* Tue Jul 15 2014 Rex Dieter <rdieter@fedoraproject.org> - 1:4.13.3-1
- 4.13.3

* Thu Jul 03 2014 Rex Dieter <rdieter@fedoraproject.org> 1:4.13.2-3
- optimize mimeinfo scriptlet

* Thu Jun 19 2014 Rex Dieter <rdieter@fedoraproject.org> - 1:4.13.2-2
- BR: kdelibs4-webkit-devel (google calendar resource)

* Mon Jun 09 2014 Rex Dieter <rdieter@fedoraproject.org> - 1:4.13.2-1
- 4.13.2

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.13.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 1:4.13.1-2
- rebuild for boost 1.55.0

* Sun May 11 2014 Rex Dieter <rdieter@fedoraproject.org> - 1:4.13.1-1
- 4.13.1

* Sat Apr 12 2014 Rex Dieter <rdieter@fedoraproject.org> - 1:4.13.0-1
- 4.13.0

* Fri Apr 04 2014 Rex Dieter <rdieter@fedoraproject.org> - 1:4.12.97-1
- 4.12.97

* Sun Mar 23 2014 Rex Dieter <rdieter@fedoraproject.org> - 1:4.12.95-1
- 4.12.95

* Wed Mar 19 2014 Rex Dieter <rdieter@fedoraproject.org> - 1:4.12.90-2
- (re)enable kolab support

* Wed Mar 19 2014 Rex Dieter <rdieter@fedoraproject.org> - 1:4.12.90-1
- 4.12.90

* Sun Mar 02 2014 Rex Dieter <rdieter@fedoraproject.org> - 1:4.12.3-1
- 4.12.3

* Fri Jan 31 2014 Rex Dieter <rdieter@fedoraproject.org> - 1:4.12.2-1
- 4.12.2

* Sat Jan 11 2014 Rex Dieter <rdieter@fedoraproject.org> - 1:4.12.1-2
- %%build: use %%{?_smp_mflags}

* Fri Jan 10 2014 Rex Dieter <rdieter@fedoraproject.org> - 1:4.12.1-1
- 4.12.1

* Thu Dec 19 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:4.12.0-1
- 4.12.0

* Sun Dec 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:4.11.97-1
- 4.11.97

* Thu Nov 21 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:4.11.95-1
- 4.11.95

* Sat Nov 16 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:4.11.90-1
- 4.11.90

* Sat Nov 02 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:4.11.3-1
- 4.11.3

* Sat Sep 28 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:4.11.2-1
- 4.11.2

* Wed Sep 04 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:4.11.1-1
- 4.11.1

* Mon Aug 19 2013 Rex Dieter <rdieter@fedoraproject.org> 4.11.0-2
- BR: libkfbapi-devel

* Thu Aug 08 2013 Than Ngo <than@redhat.com> - 4.11.0-1
- 4.11.0

* Mon Jul 29 2013 Petr Machata <pmachata@redhat.com> - 1:4.10.97-2
- Rebuild for boost 1.54.0

* Thu Jul 25 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:4.10.97-1
- 4.10.97

* Tue Jul 23 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:4.10.95-1
- 4.10.95

* Fri Jun 28 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:4.10.90-1
- 4.10.90

* Mon Jun 03 2013 Rex Dieter <rdieter@fedoraproject.org> 1:4.10.4-2
- rebuild (libkgapi)

* Sat Jun 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:4.10.4-1
- 4.10.4

* Wed May 22 2013 Daniel Vrátil <dvratil@redhat.com> 1:4.10.3-3
- Rebuild for libkgapi-2.0.0

* Fri May 10 2013 Rex Dieter <rdieter@fedoraproject.org> 1:4.10.3-2
- pull in some upstream fixes, particularly: imap folder acls (kollab#1816)

* Mon May 06 2013 Than Ngo <than@redhat.com> - 1:4.10.3-1
- 4.10.3

* Mon Apr 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:4.10.2-1
- 4.10.2

* Sat Mar 02 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:4.10.1-1
- 4.10.1

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1:4.10.0-4
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1:4.10.0-3
- Rebuild for Boost-1.53.0

* Fri Feb 08 2013 Rex Dieter <rdieter@fedoraproject.org> 1:4.10.0-2
- pull in a few upstream patches

* Fri Feb 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:4.10.0-1
- 4.10.0

* Tue Jan 22 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:4.9.98-1
- 4.9.98

* Fri Jan 04 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:4.9.97-1
- 4.9.97

* Thu Dec 20 2012 Rex Dieter <rdieter@fedoraproject.org> - 1:4.9.95-1
- 4.9.95

* Tue Dec 04 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.90-1
- 4.9.90

* Mon Dec 03 2012 Than Ngo <than@redhat.com> - 4.9.4-1
- 4.9.4

* Thu Nov 29 2012 Jan Grulich <jgrulich@redhat.com> - 1:4.9.3-3
- Rebuild (qjson)

* Fri Nov 23 2012 Dan Vratil <dvratil@redhat.com> - 1:4.9.3-2
- Rebuild against qjson 0.8.0

* Sat Nov 03 2012 Rex Dieter <rdieter@fedoraproject.org> - 1:4.9.3-1
- 4.9.3

* Sat Sep 29 2012 Rex Dieter <rdieter@fedoraproject.org> - 1:4.9.2-1
- 4.9.2

* Mon Sep 03 2012 Than Ngo <than@redhat.com> - 1:4.9.1-1
- 4.9.1

* Mon Aug 06 2012 Than Ngo <than@redhat.com> - 1:4.9.0-2
- add rhel/fedora condition

* Thu Jul 26 2012 Lukas Tinkl <ltinkl@redhat.com> - 1:4.9.0-1
- 4.9.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.8.97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Rex Dieter <rdieter@fedoraproject.org> - 1:4.8.97-1
- 4.8.97

* Thu Jun 28 2012 Rex Dieter <rdieter@fedoraproject.org> 1:4.8.95-2
- missing Kolab Resource (#835904)

* Wed Jun 27 2012 Jaroslav Reznik <jreznik@redhat.com> - 1:4.8.95-1
- 4.8.95

* Wed Jun 13 2012 Rex Dieter <rdieter@fedoraproject.org> 1:4.8.90-2
- rebuild (shared-desktop-ontologies)

* Sun Jun 10 2012 Rex Dieter <rdieter@fedoraproject.org> - 1:4.8.90-1
- 4.8.90

* Sun Jun 03 2012 Jaroslav Reznik <jreznik@redhat.com> - 1:4.8.80-1
- 4.8.80

* Mon Apr 30 2012 Rex Dieter <rdieter@fedoraproject.org> 1:4.8.3-2
- s/kdebase-runtime/kde-runtime/

* Mon Apr 30 2012 Jaroslav Reznik <jreznik@redhat.com> - 1:4.8.3-1
- 4.8.3

* Tue Apr 03 2012 Lukas Tinkl <ltinkl@redhat.com> 1:4.8.2-3
- 4.8.2 tarball respin

* Sun Apr 01 2012 Rex Dieter <rdieter@fedoraproject.org> 1:4.8.2-2
- KAlarmCal::EventAttribute::commandError makes Kontact crash (kde#297039)

* Fri Mar 30 2012 Rex Dieter <rdieter@fedoraproject.org> - 1:4.8.2-1
- 4.8.2

* Mon Mar 12 2012 Jaroslav Reznik <jreznik@redhat.com> - 1:4.8.1-2
- fix version

* Mon Mar 05 2012 Jaroslav Reznik <jreznik@redhat.com> - 1:4.8.1-1
- 4.8.1

* Wed Feb 08 2012 Rex Dieter <rdieter@fedoraproject.org> 1:4.8.0-2
- use akonadi_kcm_sqlite patch referenced on reviewboard instead

* Sun Jan 22 2012 Rex Dieter <rdieter@fedoraproject.org> - 1:4.8.0-1
- 4.8.0

* Wed Jan 04 2012 Radek Novacek <rnovacek@redhat.com> - 1:4.7.97-1
- 4.7.97

* Wed Dec 21 2011 Radek Novacek <rnovacek@redhat.com> - 1:4.7.95-1
- 4.7.95
- drop fix linking wrt convenience lib nepomukfeederpluginlib patch

* Wed Dec 07 2011 Rex Dieter <rdieter@fedoraproject.org> 1:4.7.90-4
- fix Obsoletes: kdepim-runtime-devel versioning (missing epoch)

* Wed Dec 07 2011 Rex Dieter <rdieter@fedoraproject.org> 1:4.7.90-3
- drop useless -devel pkg

* Mon Dec 05 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1:4.7.90-2
- move unversioned libnepomukdatamanagement-copy.so from -devel to -libs

* Sun Dec 04 2011 Rex Dieter <rdieter@fedoraproject.org> - 1:4.7.90-1
- 4.7.90

* Fri Nov 25 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.80-1
- 4.7.80

* Sat Oct 29 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.3-1
- 4.7.3

* Sat Oct 15 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.7.2-5.1
- rebuild against known working Qt headers for F16 final

* Thu Oct 13 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.2-5
- sqlite-support.patch, s/QSQLITE/QSQLITE3/

* Thu Oct 13 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.2-4
- disable akonadi nepomuk/strigi notification spam

* Wed Oct 12 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.2-3
- akonadi_maildispatcher_agent crashes when sending email (kde#283364)

* Sat Oct 08 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.2-2
- Kmail has duplicated folders after migration from previous version (kde#283467)

* Tue Oct 04 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.2-1
- 4.7.2

* Wed Sep 21 2011 Rex Dieter <rdieter@fedoraproject.org> 1:4.7.1-4
- pkgconfig-style deps

* Wed Sep 21 2011 Rex Dieter <rdieter@fedoraproject.org> 1:4.7.1-3
- upstream Ignore-items-with-empty-remote-ids-here patch

* Tue Sep 20 2011 Radek Novacek <rnovacek@redhat.com> 1:4.7.1-2
- Enable SQLite support in akonadi

* Fri Sep 02 2011 Than Ngo <than@redhat.com> - 1:4.7.1-1
- 4.7.1

* Tue Jul 26 2011 Jaroslav Reznik <jreznik@redhat.com> 1:4.7.0-1
- 4.7.0

* Mon Jul 11 2011 Jaroslav Reznik <jreznik@redhat.com> 1:4.6.95-1
- 4.6.95 (rc2)

* Thu Jun 30 2011 Rex Dieter <rdieter@fedoraproject.org> 1:4.6.90-1
- 4.6.90

* Fri Jun 10 2011 Rex Dieter <rdieter@fedoraproject.org> 1:4.6.0-1
- 4.6.0
