## FIXME: many tests require GLX, which doesn't appear to work as-is under koji
#global tests 1
%global optflags %(echo %{optflags} | sed 's/-g /-g1 /')

Name:    konqueror
Version: 24.01.90
Release: 1%{?dist}
Summary: KDE File Manager and Browser

License: GPLv2+ and LGPLv2+ and GFDL
URL:     https://apps.kde.org/konqueror/
%apps_source

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

## upstream patches

## upstreamable patches
# toggle 'Always try to have one preloaded instance' to default off
# https://bugzilla.redhat.com/1523082
# https://bugs.kde.org/398996
Patch101: konqueror-18.12.2-preloaded.patch

## Fedora specific patches

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6WebEngineWidgets)
BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}

BuildRequires: cmake(KF6Parts)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Sonnet)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6Codecs)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(PlasmaActivities)
# libkonq
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(KF6Bookmarks)
BuildRequires: pkgconfig(zlib)
# webenginepart
BuildRequires: cmake(KF6Wallet)
BuildRequires: cmake(KF6Notifications)
# plugins
BuildRequires: cmake(Qt6TextToSpeech)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Su)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6XmlGui)
# sidebar
BuildRequires: cmake(KF6JobWidgets)

%if 0%{?tests}
BuildRequires: dbus-x11
BuildRequires: time
BuildRequires: xorg-x11-server-Xvfb
%endif

Requires:      kwebenginepart%{?_isa} = %{version}-%{release}
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}
Requires:      hicolor-icon-theme
Requires:      keditbookmarks

%description
Konqueror allows you to manage your files and browse the web in a
unified interface.

%package devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}
%description   devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package libs
Summary:       Runtime libraries for %{name}
Requires:      %{name} = %{version}-%{release}
%description libs
%{summary}.

%package -n kwebenginepart
Summary:  A KPart based on QtWebEngine
%description -n kwebenginepart
KWebEnginePart is a web browser component for KDE (KPart)
based on (Qt)WebEngine. You can use it for example for
browsing the web in Konqueror.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1


%build
%cmake_kf6 \
  -DQT_MAJOR_VERSION=6 \
  -Wno-dev \
  %{?tests:-DBUILD_TESTING:BOOL=ON}

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/*.desktop || :
%if 0%{?tests}
xvfb-run -a bash -c "%ctest" || :
%endif


%files -f %{name}.lang
%license LICENSES/*
%doc AUTHORS ChangeLog
%{_kf6_bindir}/fsview
%{_kf6_bindir}/kcreatewebarchive
%{_kf6_bindir}/kfmclient
%{_kf6_bindir}/konqueror
%{_kf6_datadir}/akregator/pics/feed.png
%{_kf6_datadir}/applications/*.desktop
%{_kf6_datadir}/config.kcfg/*.kcfg
%{_kf6_datadir}/dbus-1/interfaces/*.xml
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_kf6_datadir}/kcmcss/
%{_kf6_datadir}/kcontrol/
%{_kf6_datadir}/kf6/kbookmark/
%{_kf6_datadir}/kio_bookmarks/
%{_kf6_datadir}/konqsidebartng/
%{_kf6_datadir}/konqueror/
%{_kf6_datadir}/qlogging-categories6/*
%{_kf6_metainfodir}/org.kde.konqueror.appdata.xml
%{_kf6_sysconfdir}/xdg/autostart/konqy_preload.desktop
%{_kf6_sysconfdir}/xdg/konqs*
%{_kf6_sysconfdir}/xdg/translaterc
%{_kf6_sysconfdir}/xdg/useragenttemplatesrc

%files libs
%{_kf6_libdir}/libKF6Konq.so.{7,*.*}
%{_kf6_libdir}/libkonqsidebarplugin.so.{6,*.*}
%{_kf6_libdir}/libkonquerorprivate.so.{5,*.*}
%{_kf6_plugindir}/kfileitemaction/akregatorplugin.so
%{_kf6_plugindir}/kio/bookmarks.so
%dir %{_kf6_plugindir}/parts/
%{_kf6_plugindir}/parts/fsviewpart.so
%{_kf6_plugindir}/parts/konq_sidebar.so
%{_kf6_qtplugindir}/*.so
%{_kf6_qtplugindir}/dolphinpart/kpartplugins/dirfilterplugin.so
%{_kf6_qtplugindir}/dolphinpart/kpartplugins/kimgallery.so
%{_kf6_qtplugindir}/dolphinpart/kpartplugins/konq_shellcmdplugin.so
%{_kf6_qtplugindir}/khtml/kpartplugins/
%{_kf6_qtplugindir}/konqueror_kcms/
%{_kf6_qtplugindir}/konqueror/kpartplugins/
%{_kf6_qtplugindir}/konqueror/sidebar/
%{_kf6_qtplugindir}/kwebkitpart/kpartplugins/
%{_kf6_qtplugindir}/webenginepart/kpartplugins/*

%files devel
#{_includedir}/konqsidebarplugin.h
%{_kf6_includedir}/asyncselectorinterface.h
%{_kf6_includedir}/konq*.h
%{_kf6_includedir}/libkonq_export.h
%{_kf6_libdir}/cmake/KF6Konq/
%{_kf6_libdir}/libKF6Konq.so
%{_kf6_libdir}/libkonqsidebarplugin.so

%files -n kwebenginepart
%{_kf6_datadir}/kconf_update/webengine*
%{_kf6_datadir}/webenginepart/
%{_kf6_libdir}/libkwebenginepart.so
%{_kf6_plugindir}/parts/webenginepart.so


%changelog
* Wed Dec 06 2023 Yaakov Selkowitz <yselkowitz@fedoraproject.org> - 24.01.80-1
- 24.01.80

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

* Thu Jul 07 2022 Than Ngo <than@redhat.com> - 22.04.3-1
- 22.04.3

* Thu Jun 23 2022 Than Ngo <than@redhat.com> - 22.04.2-1
- 22.04.2

* Thu May 12 2022 Justin Zobel <justin@1707.io> - 22.04.1-1
- Update to 22.04.1

* Mon May 09 2022 Justin Zobel <justin@1707.io> - 22.04.0-1
- Update to 22.04.0

* Wed Mar 02 2022 Marc Deop <marcdeop@fedoraproject.org> - 21.12.3-1
- 21.12.3

* Wed Feb 02 2022 Rex Dieter <rdieter@fedoraproject.org> - 21.12.2-1
- 21.12.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 06 2022 Rex Dieter <rdieter@fedoraproject.org> - 21.12.1-1
- 21.12.1

* Thu Dec 09 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.12.0-1
- 21.12.0

* Tue Nov 02 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.08.3-1
- 21.08.3

* Fri Oct 15 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.08.2-1
- 21.08.2

* Wed Sep 01 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.08.1-1
- 21.08.1

* Fri Aug 06 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.08.0-1
- 21.08.0

* Wed Jul 28 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.3-1
- 21.04.3

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 10 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.2-1
- 21.04.2

* Tue May 11 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.1-1
- 21.04.1

* Sat Apr 17 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.0-1
- 21.04.0

* Tue Mar 02 2021 Rex Dieter <rdieter@fedoraproject.org> - 20.12.3-1
- 20.12.3

* Tue Feb 02 2021 Rex Dieter <rdieter@fedoraproject.org> - 20.12.2-1
- 20.12.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 14:18:54 CST 2021 Rex Dieter <rdieter@fedoraproject.org> - 20.12.1-1
- 20.12.1

* Wed Nov  4 13:54:22 CST 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.3-1
- 20.08.3

* Tue Sep 15 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.1-1
- 20.08.1

* Mon Aug 17 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.0-1
- 20.08.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.3-1
- 20.04.3

* Fri Jun 12 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.2-1
- 20.04.2

* Tue May 26 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.1-1
- 20.04.1

* Thu Apr 23 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.0-1
- 20.04.0

* Thu Mar 05 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.3-1
- 19.12.3

* Tue Feb 04 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.2-1
- 19.12.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 08 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.1-1
- 19.12.1

* Mon Nov 11 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.3-1
- 19.08.3

* Thu Oct 17 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.2-1
- 19.08.2

* Sat Sep 28 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.1-1
- 19.08.1

* Tue Aug 13 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.0-1
- 19.08.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.04.3-1
- 19.04.3

* Tue Jun 04 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.04.2-1
- 19.04.2

* Tue May 07 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.04.1-1
- 19.04.1

* Thu Mar 07 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.3-1
- 18.12.3

* Thu Feb 21 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.2-2
- AlwaysHavePreloaded => false default (#1523082, kde#398996)

* Wed Feb 20 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.2-1
- 18.12.2
- optional ninja/tests support (not enabled by default)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 29 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.12.0-3
- revert back to kwebenginepart default, testing shows #1523082 occurs for all backends

* Sat Dec 29 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.12.0-2
- default to kwebkitpart until kwebenginepart works properly (#1523082,kde#401976)

* Sat Dec 08 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.12.0-1
- 18.12.0

* Tue Nov 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.3-1
- 18.08.3

* Wed Oct 10 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.2-1
- 18.08.2

* Fri Sep 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.1-1
- 18.08.1

* Wed Aug 15 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.0-1
- 18.08.0

* Thu Jul 12 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.3-1
- 18.04.3

* Tue Jun 05 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.2-1
- 18.04.2

* Tue May 08 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.1-1
- 18.04.1

* Sat Apr 14 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.0-1
- 18.04.0

* Wed Mar 21 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.3-2
- make buildable on all archs (#1474171)
- -kwebenginepart subpkg

* Tue Mar 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.3-1
- 17.12.3

* Tue Feb 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.2-1
- 17.12.2

* Thu Jan 11 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.1-1
- 17.12.1

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 17.12.0-2
- Remove obsolete scriptlets

* Tue Dec 12 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.12.0-1
- 17.12.0

* Tue Nov 21 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.3-2
- BR: Qt5TextToSpeech

* Wed Nov 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.3-1
- 17.08.3

* Wed Oct 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.2-1
- 17.08.2

* Tue Sep 05 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.1-1
- 17.08.1

* Sat Aug 26 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.0-2
- Requires: keditbookmarks (#1474248)

* Sat Aug 26 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.0-1
- 17.08.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Fri Jul 28 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.3-1
- 17.04.3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.2-1
- 17.04.2

* Wed May 10 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.1-1
- 17.04.1

* Sat Apr 22 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.0-2
- use %%find_lang for handbooks

* Tue Apr 18 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.0-1
- 17.04.0

* Wed Mar 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.3-1
- 16.12.3

* Wed Feb 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.2-1
- 16.12.2

* Fri Jan 20 2017 Christian Dersch <lupinix@mailbox.org> - 16.12.1-1
- initial package (review: RHBZ #1413020)
