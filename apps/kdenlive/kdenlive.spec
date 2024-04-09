%global _lto_cflags %{nil}

Name:    kdenlive
Summary: Non-linear video editor
Version: 24.02.2
Release: 1%{?dist}

License: (GPL-2.0-only or GPL-3.0-only) and GPL-2.0-or-later and GPL-3.0-or-later and LGPL-3.0-only and BSD-3-Clause and CC0-1.0
URL:     http://www.kdenlive.org
%apps_source


BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: gettext

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Bookmarks)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6ItemViews)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6JobWidgets)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6NotifyConfig)
BuildRequires: cmake(KF6Plotting)
BuildRequires: cmake(KF6Purpose)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6FileMetaData)

BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: cmake(Qt6OpenGL)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6UiPlugin)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt6NetworkAuth)

BuildRequires: librttr-devel
BuildRequires: pkgconfig(libv4l2)
BuildRequires: pkgconfig(mlt++-7) >= 7.12.0


Requires: dvdauthor
Requires: /usr/bin/ffmpeg
# Require version of mlt with qt6 support
Requires: mlt%{?_isa} >= 7.22.0-4
Suggests: dvgrab
#qt5-qtquickcontrols is still required rfbz #5701 and #5702
Requires: frei0r-plugins
Requires: kf6-qqc2-desktop-style
Requires: kf6-kirigami2

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval            
ExcludeArch: %{ix86}

%description
Kdenlive is an intuitive and powerful multi-track video editor, including most
recent video technologies.

%package        doc
Summary:        Developer Documentation files for %{name}
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1


%build
# disabling QCH as some files don't seem to end up installed in the right place
%{cmake_kf6} \
  -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON -Wno-dev \
  -DQT_MAJOR_VERSION=6 \
  -DBUILD_QCH:BOOL=OFF

%cmake_build


%install
%cmake_install

## unpackaged files
rm -rfv  %{buildroot}%{_datadir}/doc/Kdenlive/

%find_lang %{name} --with-html --all-name


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop


%files -f %{name}.lang
%doc AUTHORS README.md
%license COPYING LICENSES/*
%{_kf6_bindir}/kdenlive_render
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/kdenlive/
%{_kf6_datadir}/mime/packages/org.kde.kdenlive.xml
%{_kf6_datadir}/mime/packages/westley.xml
%{_kf6_datadir}/icons/*/*/*/*
%{_kf6_datadir}/config.kcfg/kdenlivesettings.kcfg
%{_kf6_datadir}/knotifications6/kdenlive.notifyrc
%{_datadir}/knsrcfiles/*.knsrc
%{_kf6_datadir}/qlogging-categories6/kdenlive.categories
%{_kf6_mandir}/man1/kdenlive.1*
%{_kf6_mandir}/man1/kdenlive_render.1*
# consider subpkg for multilib
%{_kf6_plugindir}/thumbcreator/mltpreview.so


%changelog
* Thu Apr 11 2024 Pavel Solovev <daron439@gmail.com> - 24.02.2-1
- Update to 24.02.2

* Thu Mar 21 2024 Pavel Solovev <daron439@gmail.com> - 24.02.1-1
- Update to 24.02.1

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.0-1
- 24.02.0

* Fri Feb 02 2024 Andrew Bauer <zonexpertconsulting@outlook.com> - 24.01.95-2
- Drop i686 per fedora leaf package policy

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.95-1
- 24.01.95

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90

* Sun Dec 31 2023 Marie Loise Nolden <loise@kde.org> - 24.01.85-1
- 24.01.85 using Qt6/KF6

* Fri Oct 13 2023 Steve Cossette <farchord@gmail.com> - 23.08.2-2
- Added qqc2-desktop-style and kf5-kirigami as runtime requirements

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

* Mon Jan 23 2023 Neal Gompa <ngompa@fedoraproject.org> - 22.12.1-1
- Update to 22.12.1
- Adapt for Fedora

* Mon Dec 19 2022 Sérgio Basto <sergio@serjux.com> - 22.12.0-1
- Update kdenlive to 22.12.0

* Sat Nov 19 2022 Sérgio Basto <sergio@serjux.com> - 22.08.3-1
- Update kdenlive to 22.08.3

* Fri Sep 23 2022 Sérgio Basto <sergio@serjux.com> - 22.08.1-1
- Update kdenlive to 22.08.1
- Just requires mlt-freeworld, should be enough because mlt-freeworld requires same version of mlt

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 22.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Thu Aug 04 2022 Leigh Scott <leigh123linux@gmail.com> - 22.04.3-1
- Update kdenlive to 22.04.3

* Tue Apr 26 2022 Leigh Scott <leigh123linux@gmail.com> - 22.04.0-1
- Update kdenlive to 22.04.0

* Wed Apr 13 2022 Sérgio Basto <sergio@serjux.com> - 21.12.3-1
- Update kdenlive to 21.12.3

* Mon Feb 14 2022 Sérgio Basto <sergio@serjux.com> - 21.12.2-1
- Update kdenlive to 21.12.2

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 21.04.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 20 2021 Nicolas Chauvet <kwizart@gmail.com> - 21.04.3-3
- rebuilt

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 21.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 18 2021 Sérgio Basto <sergio@serjux.com> - 21.04.3-1
- Update kdenlive to 21.04.3

* Tue Jun 22 2021 Leigh Scott <leigh123linux@gmail.com> - 21.04.2-2
- Fix startup crash on Wayland (rfbz#5945)

* Thu Jun 10 2021 Sérgio Basto <sergio@serjux.com> - 21.04.2-1
- Update kdenlive to 21.04.2

* Mon May 17 2021 Sérgio Basto <sergio@serjux.com> - 21.04.1-1
- Update kdenlive to 21.04.1

* Sat Apr 24 2021 Leigh Scott <leigh123linux@gmail.com> - 20.12.3-3
- Rebuilt for removed libstdc++ symbol (#1937698)

* Fri Mar 12 2021 Sérgio Basto <sergio@serjux.com> - 20.12.3-2
- git rm rttr.CMakeLists.txt

* Mon Mar 08 2021 Sérgio Basto <sergio@serjux.com> - 20.12.3-1
- Update kdenlive to 20.12.3
- Use rttr package

* Sat Feb 20 2021 Sérgio Basto <sergio@serjux.com> - 20.12.2-1
- Update kdenlive to 20.12.2

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 20.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Sérgio Basto <sergio@serjux.com> - 20.12.1-1
- Update kdenlive to 20.12.1

* Mon Dec 28 2020 Sérgio Basto <sergio@serjux.com> - 20.12.0-1
- Update kdenlive to 20.12.0

* Fri Nov 06 2020 Sérgio Basto <sergio@serjux.com> - 20.08.3-1
- Update kdenlive to 20.08.3

* Mon Sep 21 2020 Sérgio Basto <sergio@serjux.com> - 20.08.1-1
- Update kdenlive to 20.08.1

* Mon Aug 31 2020 Sérgio Basto <sergio@serjux.com> - 20.08.0-2
- Use modern cmake macros and disable LTO (rfbz #5733)

* Tue Aug 25 2020 Sérgio Basto <sergio@serjux.com> - 20.08.0-1
- Update kdenlive to 20.08.0

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 20.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Sérgio Basto <sergio@serjux.com> - 20.04.3-1
- Update kdenlive to 20.04.3

* Mon Jul 20 2020 Sérgio Basto <sergio@serjux.com> - 20.04.2-2
- qt5-qtquickcontrols is still required rfbz #5701 and #5702

* Fri Jun 12 2020 Sérgio Basto <sergio@serjux.com> - 20.04.2-1
- Update kdenlive to 20.04.2

* Mon May 18 2020 Sérgio Basto <sergio@serjux.com> - 20.04.1-3
- Add requires frei0r-plugins
- Sort requires alphabetically

* Mon May 18 2020 Sérgio Basto <sergio@serjux.com> - 20.04.1-2
- Add -Wno-dev

* Mon May 18 2020 Sérgio Basto <sergio@serjux.com> - 20.04.1-1
- Update kdenlive to 20.04.1

* Thu Mar 26 2020 Sérgio Basto <sergio@serjux.com> - 19.12.3-1
- Update kdenlive to 19.12.3

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 19.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Sérgio Basto <sergio@serjux.com> - 19.12.1-2
- Use released sources that have po files

* Tue Jan 14 2020 Sérgio Basto <sergio@serjux.com> - 19.12.1-1
- Update kdenlive to 19.12.1

* Thu Oct 31 2019 Sérgio Basto <sergio@serjux.com> - 19.08.2-1
- Update kdenlive to 19.08.2

* Tue Oct 01 2019 Leigh Scott <leigh123linux@googlemail.com> - 19.04.3-2
- Add requires qt5-qtquickcontrols2 (rfbz#5401)

* Wed Sep 18 2019 Sérgio Basto <sergio@serjux.com> - 19.04.3-1
- Update kdenlive to 19.04.3

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 18.12.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 12 2019 Leigh Scott <leigh123linux@gmail.com> - 18.12.3-4
- Rebuild for new mlt version

* Fri Mar 29 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.3-3
- respin melt.patch for real this time

* Fri Mar 29 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.3-2
- respin melt patch to give mlt-melt priority over melt

* Thu Mar 28 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.3-1
- 18.12.3
- backport upstream fix for mlt-melt (kde#405564)

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 18.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Feb 28 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.2-1
- 18.12.2

* Tue Oct 23 2018 Leigh Scott <leigh123linux@googlemail.com> - 18.08.2-1
- Update kdenlive to 18.08.2

* Mon Sep 17 2018 Sérgio Basto <sergio@serjux.com> - 18.08.1-1
- Update kdenlive to 18.08.1

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 18.04.3-2
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 Sérgio Basto <sergio@serjux.com> - 18.04.3-1
- Update kdenlive to 18.04.3

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 18.04.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun May 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.1-1
- 18.04.1
- .spec cosmetics
- omit scriptlets on fedora (all handled via system triggers now)

* Sun May 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.3-4
- rebuild (mlt)

* Wed Mar 21 2018 Sérgio Basto <sergio@serjux.com> - 17.12.3-3
- recordmydesktop is not used since 0.9.something

* Mon Mar 19 2018 Sérgio Basto <sergio@serjux.com> - 17.12.3-2
- Add a fix to build in el7

* Sun Mar 11 2018 Sérgio Basto <sergio@serjux.com> - 17.12.3-1
- Update kdenlive to 17.12.3

* Thu Feb 22 2018 Sérgio Basto <sergio@serjux.com> - 17.12.2-1
- Update kdenlive to 17.12.2

* Tue Jan 30 2018 Sérgio Basto <sergio@serjux.com> - 17.12.1-1
- Update kdenlive to 17.12.1

* Tue Jan 02 2018 Sérgio Basto <sergio@serjux.com> - 17.12.0-2
- Use _kf5_metainfodir to fix appdata directory issue

* Fri Dec 29 2017 Sérgio Basto <sergio@serjux.com> - 17.12.0-1
- Update kdenlive to 17.12.0

* Thu Nov 02 2017 Sérgio Basto <sergio@serjux.com> - 17.08.2-1
- Update kdenlive to 17.08.2

* Sun Oct 08 2017 Sérgio Basto <sergio@serjux.com> - 17.08.1-1
- Update to 17.08.1

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 17.04.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 16 2017 Sérgio Basto <sergio@serjux.com> - 17.04.2-3
- yet another fix for gcc7

* Sun Jun 11 2017 Sérgio Basto <sergio@serjux.com> - 17.04.2-2
- Add a new gcc7.patch
- Add find_lang macro

* Sun Jun 11 2017 Sérgio Basto <sergio@serjux.com> - 17.04.2-1
- Update to 17.04.2

* Sat Apr 01 2017 Sérgio Basto <sergio@serjux.com> - 16.12.3-1
- Update to 16.12.3

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 16.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 22 2017 Leigh Scott <leigh123linux@googlemail.com> - 16.12.2-2
- Add build fix for gcc-7 changes

* Tue Feb 21 2017 Sérgio Basto <sergio@serjux.com> - 16.12.2-1
- Update kdenlive to 16.12.2 following Fedora KDE applications

* Tue Jan 31 2017 Sérgio Basto <sergio@serjux.com> - 16.08.3-2
- Requires mlt-freeworld on el7

* Tue Jan 31 2017 Sérgio Basto <sergio@serjux.com> - 16.08.3-1
- Update kdenlive to 16.08.3 like kde-baseapps

* Fri Jan 06 2017 Leigh Scott <leigh123linux@googlemail.com> - 16.12.0-1
- Update to 16.12.0

* Thu Oct 13 2016 Sérgio Basto <sergio@serjux.com> - 16.08.2-1
- Update to 16.08.2
- Scriplets fixed by upstream

* Fri Sep 16 2016 Sérgio Basto <sergio@serjux.com> - 16.08.1-1
- Update to 16.08.1
- Requires mlt-freeworld on F25+

* Tue Aug 23 2016 Sérgio Basto <sergio@serjux.com> - 16.08.0-1
- Kdenlive 16.08.0 is here

* Thu Jul 28 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.3-1
- 16.04.3, add missing 'touch' to %%postun, document kinit workaround

* Fri Jul 08 2016 Leigh Scott <leigh123linux@googlemail.com> - 16.04.2-2
- Use marcos for files
- Fix scriptlets

* Wed Jun 15 2016 Sérgio Basto <sergio@serjux.com> - 16.04.2-1
- Update kdenlive to 16.04.2

* Fri May 27 2016 David Vásquez <davidjeremias82 AT gmail DOT com> 16.04.1-2
- Added missing dependencies
- Disabled, build testing
- Automatic qt system path

* Fri May 13 2016 Sérgio Basto <sergio@serjux.com> - 16.04.1-1
- Update to 16.04.1

* Thu Mar 24 2016 Sérgio Basto <sergio@serjux.com> - 15.12.2-2
- Fix rfbz #4015

* Wed Feb 17 2016 Rex Dieter <rdieter@fedoraproject.org> 15.12.2-1
- 15.12.2

* Mon Nov 09 2015 Rex Dieter <rdieter@fedoraproject.org> 15.08.2-1
- 15.08.2

* Mon Dec 22 2014 Rex Dieter <rdieter@fedoraproject.org> 0.9.10-1
- 0.9.10

* Wed Aug 06 2014 Rex Dieter <rdieter@fedoraproject.org> 0.9.8-2
- optimize mime scriptlets

* Wed May 14 2014 Rex Dieter <rdieter@fedoraproject.org> 0.9.8-1
- 0.9.8

* Mon Apr 07 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.9.6-4
- Rebuilt for rfbz#3209

* Wed Oct 09 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.9.6-3
- rebuilt for mlt

* Sun May 26 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.9.6-2
- Rebuilt for x264/FFmpeg

* Sun Apr 07 2013 Rex Dieter <rdieter@fedoraproject.org> 0.9.6-1
- 0.9.6

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.9.4-2
- Mass rebuilt for Fedora 19 Features

* Tue Jan 29 2013 Rex Dieter <rdieter@fedoraproject.org> 0.9.4-1
- 0.9.4

* Tue Jun 19 2012 Richard Shaw <hobbes1069@gmail.com> - 0.9.2-2
- Rebuild for updated mlt.

* Thu May 31 2012 Rex Dieter <rdieter@fedoraproject.org> 0.9.2-1
- 0.9.2

* Tue May 15 2012 Rex Dieter <rdieter@fedoraproject.org> 0.9-1
- 0.9
- pkgconfig-style deps

* Fri Mar 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.8.2.1-3
- Rebuilt for c++ ABI breakage

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.8.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 10 2011 Rex Dieter <rdieter@fedoraproject.org> 0.8.2.1-1
- 0.8.2.1

* Tue Nov 15 2011 Rex Dieter <rdieter@fedoraproject.org> 0.8.2-2
- rebuild

* Fri Nov 11 2011 Rex Dieter <rdieter@fedoraproject.org> 0.8.2-1
- 0.8.2
- tighten mlt deps

* Thu Jul 21 2011 Ryan Rix <ry@n.rix.si> 0.8-1
- New version
- Add patch to fix FTBFS

* Fri Apr 15 2011 Rex Dieter <rdieter@fedoraproject.org> 0.7.8-2
- update scriptlets, %%_kde4_... macros/best-practices
- +Requires: kdebase-runtime (versioned)
- fix ftbfs

* Thu Apr 07 2011 Ryan Rix <ry@n.rix.si> - 0.7.8-1
- new version

* Mon Mar 01 2010 Zarko <zarko.pintar@gmail.com> - 0.7.7.1-1
- new version

* Thu Feb 18 2010 Zarko <zarko.pintar@gmail.com> - 0.7.7-1
- new version

* Mon Sep 07 2009 Zarko <zarko.pintar@gmail.com> - 0.7.5-1
- new version

* Sat May 30 2009 Zarko <zarko.pintar@gmail.com> - 0.7.4-2
- added updating of mime database
- changed dir of .desktop file

* Fri May 22 2009 Zarko <zarko.pintar@gmail.com> - 0.7.4-1
- new release
- spec cleaning

* Thu Apr 16 2009 Zarko <zarko.pintar@gmail.com> - 0.7.3-2
- some clearing
- added doc files

* Wed Apr 15 2009 Zarko <zarko.pintar@gmail.com> - 0.7.3-1
- new release

* Sun Apr 12 2009 Zarko <zarko.pintar@gmail.com> - 0.7.2.1-2
- spec convert to kde4 macros

* Mon Mar 16 2009 Zarko <zarko.pintar@gmail.com> - 0.7.2.1-1
- update to 0.7.2.1
- spec cleaned
- Resolve RPATHs

* Sun Nov 16 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 0.7-1
- update to 0.7

* Wed Nov  5 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 0.7-0.1.20081104svn2622
- update to last svn revision

* Tue Nov  4 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 0.7-0.beta1
- clean up spec

* Fri Oct 17 2008 jeff <moe@blagblagblag.org> - 0.7-1.beta1
- Add URL
- Full URL for Source:
- Remove all Requires:
- Update BuildRoot
- Remove Packager: Brixton Linux Action Group
- Add BuildRequires: ffmpeg-devel kdebindings-devel soprano-devel
- Update %%files
- %%doc with only effects/README
- GPLv2+
- Add lang files

* Tue Jul  8 2008 jeff <moe@blagblagblag.org> - 0.6-1.svn2298.0blag.f9
- Update to KDE4 branch
  https://kdenlive.svn.sourceforge.net/svnroot/kdenlive/branches/KDE4

* Tue Jul  8 2008 jeff <moe@blagblagblag.org> - 0.6-1.svn2298.0blag.f9
- Update to svn r2298
- New Requires
- kdenlive-svn-r2298-renderer-CMakeLists.patch 

* Sun Nov 11 2007 jeff <moe@blagblagblag.org> - 0.5-1blag.f7
- Update to 0.5 final

* Tue Apr 17 2007 jeff <moe@blagblagblag.org> - 0.5-0svn20070417.0blag.fc6
- svn to 20070417

* Fri Apr  6 2007 jeff <moe@blagblagblag.org> - 0.5-0svn20070406.0blag.fc6
- svn to 20070406

* Tue Apr  3 2007 jeff <moe@blagblagblag.org> - 0.5-0svn20070403.0blag.fc6
- svn to 20070403

* Thu Mar 22 2007 jeff <moe@blagblagblag.org> - 0.5-0svn20070322.0blag.fc6
- svn to 20070322

* Thu Mar 15 2007 jeff <moe@blagblagblag.org> - 0.5-0svn20070316.0blag.fc6
- BLAG'd

* Sun Apr 27 2003 Jason Wood <jasonwood@blueyonder.co.uk> 0.2.2-1mdk
- First stab at an RPM package.
- This is taken from kdenlive-0.2.2 source package.
