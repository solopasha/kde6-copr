# build Python plugins (disabled by default due to #2048781)
%bcond_with python

Name:           falkon
Version:        24.02.1
Release:        1%{?dist}
Summary:        Modern web browser

# Files in src/lib/opensearch and src/lib/3rdparty are GPLv2+
# Files in src/plugins/MouseGestures/3rdparty are BSD (2 clause)
License:        GPLv3+ and BSD
URL:            https://www.falkon.org/
%apps_source

# reenable native scrollbars by default (upstream disabled them in 2.1.2)
Patch0:         falkon-3.1.0-native-scrollbars.patch

## upstream patches

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6WebChannel)
BuildRequires:  cmake(Qt6WebEngineCore)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  qt6-qtbase-private-devel

BuildRequires:  cmake(KF6Archive)

BuildRequires:  openssl-devel
BuildRequires:  xcb-util-devel

%if 0%{?with_python}
BuildRequires:  python3-devel
BuildRequires:  cmake(PySide6)
BuildRequires:  cmake(Shiboken6)
BuildRequires:  cmake(Shiboken6Tools)
BuildRequires:  cmake(KF6I18n)
%endif

# require the correct minimum versions of Qt, symbol versioning does not work
Requires:       qt6-qtbase%{?_isa} >= %(echo %{_qt6_version} | cut -d. -f-2)
%global qtwebengine_version %(pkg-config --modversion Qt6WebEngineCore 2>/dev/null || echo 6.6)
Requires:       qt6-qtwebengine%{?_isa} >= %(echo %{qtwebengine_version} | cut -d. -f-2)

# directory ownership
Requires:       hicolor-icon-theme

# forked version that uses D-Bus instead of lock files (see also #1551678)
Provides:       bundled(qtsingleapplication-qt6)

%global __provides_exclude_from ^%{_kf6_qtplugindir}/falkon/.*$

%package gnome-keyring
Summary: gnome-keyring plugin for %{name}
BuildRequires:  pkgconfig(gnome-keyring-1)
Requires: %{name}%{?_isa} = %{version}-%{release}

%description gnome-keyring
%{summary}.

%package kde
Summary: KDE Frameworks Integration plugin for %{name}
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Purpose)
BuildRequires:  cmake(KF6JobWidgets)
Requires: %{name}%{?_isa} = %{version}-%{release}

%description kde
Plugin for Falkon adding support for:
- storing passwords securely in KWallet,
- additional URL protocols using KIO (e.g., man:, info:, gopher:, etc.),
- a "Share page" menu using the KDE Purpose Framework,
- intercepting crashes with KCrash, bringing up the DrKonqi crash handler.


%description
Falkon is a modern web browser based on QtWebEngine (which is itself based on
the Chromium core, i.e., Blink) and the Qt framework. It is designed to be
lightweight and fast and offers advanced functions such as
- an integrated advertisement blocker,
- a search engine manager,
- a SSL certificate manager,
- speed dial
- theming support, and
- seamless integration into your desktop environment.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%if 0%{?with_python}
# delete falkon_hellopython and falkon_helloqml translations, those plugins are
# not shipped
rm -f po/*/falkon_hello*.po
%else
# delete all Python plugins' and falkon_helloqml translations, those plugins are
# not shipped
rm -rf po
%endif


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

# translations (find_lang_kf6 does not support --all-name, so adapt it)
find %{buildroot}/%{_datadir}/locale/ -name "*.qm" -type f | sed 's:%{buildroot}/::;s:%{_datadir}/locale/\([a-zA-Z_\@]*\)/LC_MESSAGES/\([^/]*\.qm\):%lang(\1) %{_datadir}/locale/\1/LC_MESSAGES/\2:' >%{name}.lang
%if 0%{?with_python}
find %{buildroot}/%{_datadir}/locale/ -name "*.mo" -type f | sed 's:%{buildroot}/::;s:%{_datadir}/locale/\([a-zA-Z_\@]*\)/LC_MESSAGES/\([^/]*\.mo\):%lang(\1) %{_datadir}/locale/\1/LC_MESSAGES/\2:' >>%{name}.lang
%endif

desktop-file-install \
    --add-mime-type="x-scheme-handler/http;x-scheme-handler/https;" \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}/%{_datadir}/applications/org.kde.falkon.desktop


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.falkon.appdata.xml



%files -f %{name}.lang
%doc README.md CHANGELOG
%license COPYING
%{_kf6_bindir}/falkon
%{_kf6_libdir}/libFalkonPrivate.so.*
%dir %{_kf6_qtplugindir}/falkon/
%{_kf6_qtplugindir}/falkon/AutoScroll.so
%{_kf6_qtplugindir}/falkon/FlashCookieManager.so
%{_kf6_qtplugindir}/falkon/GreaseMonkey.so
%{_kf6_qtplugindir}/falkon/MouseGestures.so
%{_kf6_qtplugindir}/falkon/PIM.so
%{_kf6_qtplugindir}/falkon/StatusBarIcons.so
%{_kf6_qtplugindir}/falkon/TabManager.so
%{_kf6_qtplugindir}/falkon/VerticalTabs.so
%if 0%{?with_python}
%{_kf6_qtplugindir}/falkon/i18n.py
%{_kf6_qtplugindir}/falkon/middleclickloader/
%{_kf6_qtplugindir}/falkon/runaction/
%endif
%{_kf6_metainfodir}/org.kde.falkon.appdata.xml
%{_kf6_datadir}/applications/org.kde.falkon.desktop
%{_kf6_datadir}/bash-completion/
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_kf6_datadir}/falkon/

%files gnome-keyring
%{_kf6_qtplugindir}/falkon/GnomeKeyringPasswords.so

%files kde
%{_kf6_qtplugindir}/falkon/KDEFrameworksIntegration.so


%changelog
* Thu Mar 21 2024 Pavel Solovev <daron439@gmail.com> - 24.02.1-1
- Update to 24.02.1

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.0-1
- 24.02.0

* Fri Feb 16 2024 Jan Grulich <jgrulich@redhat.com> - 24.01.95-2
- Rebuild (qt6)

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.95-1
- 24.01.95

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90

* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Mon Dec 04 2023 Yaakov Selkowitz <yselkowitz@fedoraproject.org> - 24.01.80-1
- 24.01.80

* Thu Oct 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.2-1
- 23.08.2

* Sat Sep 16 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.1-1
- 23.08.1

* Sat Aug 26 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.0-1
- 23.08.0

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.04.3-2
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

* Wed Jan 04 2023 Justin Zobel <justin@1707.io> - 22.12.1-1
- Update to 22.12.1

* Wed Dec 21 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.12.0-1
- 22.12.0

* Fri Nov 04 2022 Marc Deop i Argemí (Private) <marc@marcdeop.com> - 22.08.3-1
- 22.08.3

* Fri Sep 09 2022 Marc Deop marcdeop@fedoraproject.org - 22.08.1-1
- 22.08.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.2.0-3
- use new CMake macros (the transitional -B. hack no longer works)

* Mon Jan 31 2022 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.2.0-2
- add optional Python plugin support (--with python) (#1749896)
- keep it disabled by default though because of shiboken2 bug (#2048781)

* Mon Jan 31 2022 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.2.0-1
- update to 3.2.0 (new upstream feature release), drop upstream patches
- add BuildRequires: kf5-karchive-devel, dependency added upstream

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 3.1.0-10
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb 01 2021 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.1.0-8
- Pass -B. to cmake to work around incompatible RPM macro change (#1863525)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.1.0-4
- fix FTBFS with Qt 5.14/5.15 due to missing #includes (thanks to loise)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 22 2019 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.1.0-1
- update to 3.1.0 (new upstream feature release)
- drop upstreamed mixed-versions and password-migration patches
- drop system-qtsingleapplication patch, Falkon's copy now uses D-Bus (#1551678)
- rebase native-scrollbars patch
- rename falkon-kwallet subpackage to falkon-kde
- update BuildRequires and file list

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 13 2018 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.0.1-2
- implement migration of passwords stored in KWallet or GNOME Keyring

* Sat May 12 2018 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.0.1-1.1
- fix the fix for kde#391300 to require only QtWebEngine 5.10, not Qt 5.10

* Thu May 10 2018 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.0.1-1
- update to 3.0.1 (includes QupZilla profile migration, bug fixes)
- unconditionally Obsolete/Provide qupzilla now that configuration is migrated
- drop qtbug-65223-workaround patch, upstream made the workaround unconditional
- rebase system-qtsingleapplication patch

* Wed Apr 04 2018 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.0.0-4
- update URL tag to https://www.falkon.org/

* Sun Mar 25 2018 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.0.0-3
- add Requires: hicolor-icon-theme for directory ownership
- add obsolete_qupzilla flag to Obsolete/Provide qupzilla, enable it on F28+

* Mon Mar 05 2018 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.0.0-2
- don't use braces for the cmake_kf5 command macro
- remove obsolete scriptlets, add ldconfig_scriptlets transitional macro for now

* Mon Mar 05 2018 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.0.0-1
- renamed from QupZilla to Falkon
- the obsolete commented out AccessKeysNavigation plugin was completely removed
- new VerticalTabs plugin
- add BuildRequires: cmake extra-cmake-modules gcc-c++ kf5-rpm-macros
- build system changed from QMake to CMake
- update %%doc and %%license file lists
- rebase qtbug-65223-workaround patch and fix typo in the bug ID
- redo the unbundling of QtSingleApplication for CMake
- port the Provides filter to the native RPM Provides filtering

* Thu Feb 01 2018 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.2.5-2
- unconditionally enable the QTBUG-65223 workaround so that it actually works

* Mon Jan 29 2018 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.2.5-1
- update to 2.2.5 (now requires Qt 5.9)

* Sat Dec 23 2017 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.2.3-1
- update to 2.2.3 (bugfix release)
- appdata is now in /usr/share/metainfo

* Thu Dec 14 2017 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.2.2-1
- update to 2.2.2 (bugfix release)

* Tue Nov 07 2017 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.2.1-1
- update to 2.2.1 (bugfix release)
- drop appdata file name typo workaround, fixed upstream

* Mon Oct 16 2017 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.2.0-1
- update to 2.2.0 (now requires Qt 5.8)
- drop openssl11 patch, fixed upstream
- rebase native-scrollbars patch
- drop obsolete mixed-versions patch (Qt 5.8 conditionals are gone)
- .desktop and appdata files renamed by upstream
- backport a typo fix in the appdata file name

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.1.2-5
- Rebuild due to bug in RPM (RHBZ #1468476)

* Sun Apr 16 2017 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.1.2-4
- add versioned qt5-qtbase and qt5-qtwebengine Requires

* Sat Apr 15 2017 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.1.2-3
- require only QtWebEngine 5.8 for spell checking etc., not all of Qt 5.8

* Fri Mar 31 2017 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.1.2-2
- rebuild against Qt 5.8 to pick up spell checking from QtWebEngine 5.8

* Fri Mar 24 2017 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.1.2-1
- update to 2.1.2 (bugfix release)
- reenable native scrollbars by default (upstream disabled them in 2.1.2)

* Mon Feb 20 2017 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.1.1-1
- update to 2.1.1 (bugfix release)
- drop backported speeddial patch, already in 2.1.1

* Wed Feb 08 2017 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.1.0-2
- backport upstream fix for adding/editing SpeedDial entries (#1419915)

* Sun Feb 05 2017 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.1.0-1
- update to 2.1.0 (now requires Qt 5.7)
- drop upstreamed printing patch
- drop support for Fedora <= 24, Qt is too old there (5.6.x)

* Sat Dec 10 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.0.2-2
- rebuild against fixed Qt (moc) to fix KWallet support

* Sun Oct 30 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.0.2-1
- update to 2.0.2 (bugfix release)

* Fri Oct 28 2016 Than Ngo <than@redhat.com> - 2.0.1-9
- uses %%qt5_qtwebengine_arches

* Tue Oct 18 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.0.1-8
- fix FTBFS with OpenSSL 1.1 (patch by Bernhard Rosenkränzer (bero))

* Thu Sep 08 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.0.1-7
- printing patch: FilePrinter: do not pass margins to lpr, the PDF has margins
- printing patch: enable options handled by FilePrinter in the print dialog

* Tue Sep 06 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.0.1-6
- printing patch: adapt the FilePrinter from Okular to pass correct lpr args

* Tue Sep 06 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.0.1-5
- printing patch: use async QProcess API instead of QProcess::execute to run lpr

* Fri Aug 26 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.0.1-4
- printing patch: use the callback version of printToPdf instead of the file one

* Fri Aug 26 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.0.1-3
- printing patch: let lpr autoremove the file instead of QTemporaryFile

* Fri Jul 29 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.0.1-2
- add experimental printing support

* Sat Jun 11 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.0.1-1
- update to 2.0.1 (bugfix release)

* Thu Mar 31 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.0.0-1
- update to 2.0.0 (official release)
- remove unused BR pkgconfig(hunspell) (not used since the QtWebEngine switch)

* Sat Mar 26 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.9.99-0.10.20160321git91e6c2eb71590
- new snapshot with Greasemonkey improvements and minor bugfixes elsewhere

* Thu Feb 25 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.9.99-0.9.20160225gitff0a8898616e1
- new snapshot, fixes FTBFS (bad bash-completion path), some more UI tweaks

* Wed Feb 24 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.9.99-0.8.20160220git844f439526150
- new snapshot, updated for QtWebEngine 5.6.0 RC API changes, some UI tweaks

* Tue Feb 02 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.9.99-0.7.20160127git06b2414d801eb
- bump Release for official Rawhide build (#1298145)

* Wed Jan 27 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.9.99-0.6.20160127git06b2414d801eb
- new snapshot with some theming, high DPI and usability improvements
- add ExclusiveArch matching the one in qt5-qtwebengine (see #1298011)

* Wed Jan 27 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.9.99-0.5.20160125git3ab21c1c2c2cd
- new snapshot with some bugfixes and theming improvements

* Fri Jan 22 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.9.99-0.4.20160120git95f10443ef895
- new snapshot, adds image finder plugin
- drop my patches that were both upstreamed
- fix/update %%description to refer to QtWebEngine/Chromium/Blink, not WebKit

* Thu Jan 14 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.9.99-0.3.20160102git3e0583377d825
- fix crash from autosearch-optional patch

* Thu Jan 14 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.9.99-0.2.20160102git3e0583377d825
- default to NoProxy instead of HttpProxy so that the default just works
- make automatic searching from the address bar optional

* Fri Jan 08 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.9.99-0.1.20160102git3e0583377d825
- update to QtWebEngine-based git snapshot (from git master)
- BR Qt >= 5.6
- remove BR qt5-qtwebkit-devel and qt5-qtscript-devel
- add BR qt5-qtwebengine-devel and xcb-util-devel
- update file list: no AccessKeysNavigation plugin for now

* Wed Dec 16 2015 Rex Dieter <rdieter@fedoraproject.org> 1.8.9-3
- BR: qt5-linguist (instead of all of qt5-qttools-devel)

* Wed Dec 09 2015 Rex Dieter <rdieter@fedoraproject.org> 1.8.9-2
- -kwallet, -gnome-keyring subpkgs (#1285034)

* Mon Nov 30 2015 Rex Dieter <rdieter@fedoraproject.org> 1.8.9-1
- 1.8.9 (#1285034)

* Tue Nov 10 2015 Rex Dieter <rdieter@fedoraproject.org> - 1.8.8-2
- enable kwallet plugin (#1279972)
- track plugins closer
- filter plugin provides
- .spec cosmetics

* Sat Nov 07 2015 Rex Dieter <rdieter@fedoraproject.org> 1.8.8-1
- 1.8.8

* Mon Oct 12 2015 Rex Dieter <rdieter@fedoraproject.org> 1.8.7-2
- workaround qtwebkit-5.5.1 dropping QTWEBKIT_VERSION_CHECK macro (#1270602)
- revert use of %%make_install (qmake supports INSTALL_ROOT, not DESTDIR)
- %%check: appstream validation

* Sun Oct 11 2015 Raphael Groner <projects.rg@smart.ms> - 1.8.7-1
- new version

* Mon Oct 05 2015 Rex Dieter <rdieter@fedoraproject.org> 1.8.6-7
- qupzilla FTBFS (#1247953)

* Mon Jul 20 2015 Raphael Groner <projects.rg@smart.ms> - 1.8.6-6
- unbundle qtsingleapplication (rhbz#1091704)
- remove qt4 build (f20 went EOL)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 12 2015 Helio Chissini de Castro <helio@kde.org> - 1.8.6-4
- Remove some non legal icons from tarball.

* Wed Mar 11 2015 Helio Chissini de Castro <helio@kde.org> - 1.8.6-3
- Add missing build requires

* Wed Mar 11 2015 Helio Chissini de Castro <helio@kde.org> - 1.8.6-2
- Add missing build requires

* Wed Mar 11 2015 Helio Chissini de Castro <helio@kde.org> - 1.8.6-1
- New pustream version - Repackaged replacing invalid icons
- Make Qt5 as default
- Compile Qt4 only in Fedora 20 or less
- Remove invalid flags

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 18 2014 Christoph Wickert <cwickert@fedoraproject.org> - 1.6.3-1
- Update to 1.6.3

* Fri Sep 27 2013 Christoph Wickert <cwickert@fedoraproject.org> - 1.4.4-1
- Update to 1.4.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 19 2013 Christoph Wickert <cwickert@fedoraproject.org> - 1.4.3-1
- Update to 1.4.3
- Include new bash-completion file

* Mon Apr 01 2013 Christoph Wickert <cwickert@fedoraproject.org> - 1.4.1-1
- Update to 1.4.1

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Oct 20 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.3.5-2
- Use new filter setup
- Build with --as-needed
- Preserve timestamps during install
- Add comment about license of the source files

* Sat Oct 06 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.3.5-1
- Update to 1.3.5
- Enable WebGL (USE_WEBGL)
- Enable geolocation and notifications API (USE_QTWEBKIT_2_2)
- Change icense tag to "GPLv3+ and BSD" (some plugins are BSD licensed)
- Add x-scheme-handlers so qupzilla can be set as default browser
- Filter out private requires and provides
- Include README.md in %%doc

* Mon Apr 30 2012 Christoph Wickert <cwickert@fedoraproject.org> - 1.2.0-1
- Initial package
