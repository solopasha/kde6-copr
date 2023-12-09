Name:    yakuake
Version: 24.01.80
Release: 1.1%{?dist}
Summary: A drop-down terminal emulator

# KDE e.V. may determine that future GPL versions are accepted
License: GPL-2.0-only OR GPL-3.0-only
URL: https://kde.org/applications/system/org.kde.yakuake
%apps_source

## upstream fixes

# konsolepart
Requires:       konsole6-part

BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6NotifyConfig)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KWayland)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}


%if 0%{?fedora}
%global appstream_validate 1
BuildRequires:  libappstream-glib
%endif

%description
Yakuake is a drop-down terminal emulator.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1


%build
%cmake_kf6

%cmake_build


%install
%cmake_install

%find_lang %{name}


%check
%if 0%{?appstream_validate}
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.yakuake.appdata.xml
%endif
desktop-file-validate  %{buildroot}%{_kf6_datadir}/applications/org.kde.yakuake.desktop


%files -f %{name}.lang
%doc AUTHORS ChangeLog TODO
%license LICENSES/*
%{_kf6_bindir}/yakuake
%{_kf6_datadir}/knsrcfiles/yakuake.knsrc
%{_kf6_metainfodir}/org.kde.yakuake.appdata.xml
%{_kf6_datadir}/applications/org.kde.yakuake.desktop
%{_kf6_datadir}/knotifications6/yakuake.notifyrc
%{_kf6_datadir}/yakuake/
%{_kf6_datadir}/icons/hicolor/*/apps/yakuake.*
%{_kf6_datadir}/dbus-1/services/org.kde.yakuake.service


%changelog
* Thu Oct 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.2-1
- 23.08.2

* Sat Sep 16 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.1-1
- 23.08.1

* Sat Aug 26 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.0-1
- 23.08.0

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.04.3-2
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

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.12.1-2
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

* Thu Aug 25 2022 Yaroslav Sidlovsky <zawertun@gmail.com> - 22.08.0-2
- BR: cmake(KF5Wayland)

* Fri Aug 19 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.0-1
- 22.08.0

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 07 2022 Than Ngo <than@redhat.com> - 22.04.3-1
- 22.04.3

* Fri Jun 24 2022 Than Ngo <than@redhat.com> - 22.04.2-1
- 22.04.2

* Thu May 12 2022 Justin Zobel <justin@1707.io> - 22.04.1-1
- Update to 22.04.1

* Mon May 09 2022 Justin Zobel <justin@1707.io> - 22.04.0-1
- Update to 22.04.0

* Wed Mar 02 2022 Marc Deop <marcdeop@fedoraproject.org> - 21.12.3-1
- 21.12.3

* Wed Feb 02 2022 Rex Dieter <rdieter@fedoraproject.org> - 21.12.2-1
- 21.12.2

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.12.1-2
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

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.04.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 08 2021 Rex Dieter <rdieter@fedoraproject.org> 21.04.2-2
- update URL (#1980317)

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

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 2021 Rex Dieter <rdieter@fedoraproject.org> - 20.12.1-1
- 20.12.1

* Wed Nov  4 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.3-1
- 20.08.3

* Tue Sep 15 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.1-1
- 20.08.1

* Mon Aug 17 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.0-1
- 20.08.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.3-2
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

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 14 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.1-1
- 19.12.1

* Mon Nov 11 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.3-1
- 19.08.3

* Thu Oct 17 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.2-1
- 19.08.2, part of kde-apps now

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 29 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.0.5-1
- 3.0.5

* Mon Feb 12 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.0.4-6
- use %%_kf5_metainfodir

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0.4-4
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr 03 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.4-1
- yakuake-3.0.4

* Fri Mar 31 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.3-2
- rebuild

* Fri Mar 31 2017 Rex Dieter <rdieter@fedoraproject.org> - 3.0.3-1
- yakuake-3.0.3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Mar 03 2016 Rex Dieter <rdieter@fedoraproject.org> 3.0.1-0.1
- yakuake-3.0.2, kf5 port

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 22 2015 Rex Dieter <rdieter@fedoraproject.org> - 2.9.9-9
- pull in upstream fixes (including appdata)
- trim changelog

* Sat Apr 18 2015 Jochen Schmitt <Jochen herr-schmitt de> - 2.9.9-8
- Fix height-handling issue (#810312)

* Sat Jan 31 2015 Rex Dieter <rdieter@fedoraproject.org> 2.9.9-7
- kde-apps cleanup

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.9.9-3
- Perl 5.18 rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 19 2012 Rex Dieter <rdieter@fedoraproject.org> 2.9.9-1
- yakuake-2.9.9

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 15 2011 Rex Dieter <rdieter@fedoraproject.org> 2.9.8-4
- Requires: konsole-part

* Sun Jul 24 2011 Jochen Schmitt <Jochen herr-schmitt de> 2.9.8-3
- Rebuild to fix dependecy issues

* Mon Jul 18 2011 Rex Dieter <rdieter@fedoraproject.org> 2.9.8-2
- Requires: konsole
- drop old cruft

* Wed Feb 09 2011 Rex Dieter <rdieter@fedoraproject.org> 2.9.8-1
- 2.9.8
- License: GPLv2 or GPLv3

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 20 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.9.7-2
- fix kdebase4 dep

* Sun Jul 18 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.9.7-1
- 2.9.7
- optimize scriptlets
- use _kde4_ macros

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 10 2009 Johan Cwiklinski <johan AT x-tnd DOT be> 2.9.6-1
- 2.9.6

* Sat Apr 17 2009 Johan Cwiklinski <johan AT x-tnd DOT be>  2.9.4-3
- Fix crash with QT 4.5

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Sep 4 2008 Johan Cwiklinski <johan AT x-tnd DOT be> - 2.9.4-1
- 2.9.4
- change BR from kdelibs4-devel to kdelibs-devel

* Fri Jun 20 2008 Johan Cwiklinski <johan AT x-tnd DOT be> - 2.9.3-1
- 2.9.3
- kdebase is required

* Sat Apr 05 2008 2008 Johan Cwiklinski <johan AT x-tnd DOT be> - 2.9.1-1
- 2.9.1
- use of %%{cmake_kde4} macro
- remove no longer needeed chrpath

* Wed Apr 02 2008 Rex Dieter <rdieter@fedoraproject.org> - 2.9-2.beta1
- BR: kdelibs4-devel
- description/summary: s/for KDE//

* Mon Feb 11 2008 Johan Cwiklinski <johan AT x-tnd DOT be> - 2.9-1.beta1
- upstream release for KDE4

* Mon Oct 30 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 2.7.5-4
- Add support for KonsoleScripts (#212862)

* Fri Sep 15 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 2.7.5-3
- Rebuild for FE6
- Update e-mail address
- Fix mixed-use-of-spaces-and-tabs rpmlint warning

* Sat May 20 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 2.7.5-2
- Add dist tag

* Sat May 20 2006 Dawid Gajownik <gajownik[AT]gmail.com> - 2.7.5-1
- Update to 2.7.5
- Add `--disable-dependency-tracking' and `--enable-final' options
- Include translations

* Mon Oct 24 2005 Mickael <dreadyman@gmail.com>
- initial release

