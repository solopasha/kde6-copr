%global commit0 8b27375b2553e1093390441ea3c7588719c912dc
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

Name:    ffmpegthumbs
Version: 24.12.0
Release: 1%{?dist}
Summary: KDE ffmpegthumbnailer service

License: GPL-2.0-or-later
URL:     https://apps.kde.org/%{name}/
%apps_source

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: libappstream-glib

BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6KIO)

BuildRequires: ffmpeg-free-devel

Provides: kffmpegthumbnailer = %{version}-%{release}
Provides: kdemultimedia-extras-freeworld = %{version}-%{release}

%description
%{summary}.


%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1


%build
%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build


%install
%cmake_install


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.metainfo.xml


%files
%license LICENSES/GPL-2.0-or-later.txt
%{_kf6_datadir}/config.kcfg/ffmpegthumbnailersettings5.kcfg
%{_kf6_datadir}/qlogging-categories6/ffmpegthumbs.categories
%{_kf6_metainfodir}/org.kde.%{name}.metainfo.xml
%{_kf6_plugindir}/thumbcreator/ffmpegthumbs.so


%changelog
* Fri Dec 06 2024 Pavel Solovev <daron439@gmail.com> - 24.12.0-1
- Update to 24.12.0

* Tue Nov 05 2024 Pavel Solovev <daron439@gmail.com> - 24.08.3-1
- Update to 24.08.3

* Mon Oct 07 2024 Pavel Solovev <daron439@gmail.com> - 24.08.2-1
- Update to 24.08.2

* Sat Oct 05 2024 Pavel Solovev <daron439@gmail.com> - 24.08.1-2
- rebuilt

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

* Tue Mar 21 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.80-1
- 23.03.80

* Tue Mar 21 2023 Sérgio Basto <sergio@serjux.com> - 22.12.3-3
- Rebuild to fix bodhi override of releasever 2 to 1

* Sun Mar 12 2023 Neal Gompa <ngompa@fedoraproject.org> - 22.12.3-2
- Rebuild for ffmpeg 6.0

* Thu Mar 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 22.12.3-1
- 22.12.3

* Tue Jan 31 2023 Marc Deop <marcdeop@fedoraproject.org> - 22.12.2-1
- 22.12.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Justin Zobel <justin@1707.io> - 22.12.1-1
- Update to 22.12.1

* Thu Dec 29 2022 Neal Gompa <ngompa@fedoraproject.org> - 22.12.0-1
- Update to 22.12.0 and move to Fedora

* Sat Nov 19 2022 Sérgio Basto <sergio@serjux.com> - 22.08.3-1
- Update ffmpegthumbs to 22.08.3

* Sat Sep 24 2022 Sérgio Basto <sergio@serjux.com> - 22.08.1-1
- Update ffmpegthumbs to 22.08.1

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 22.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Thu Aug 04 2022 Leigh Scott <leigh123linux@gmail.com> - 22.04.3-1
- Update ffmpegthumbs to 22.04.3

* Tue Apr 26 2022 Leigh Scott <leigh123linux@gmail.com> - 22.04.0-1
- Update ffmpegthumbs to 22.04.0

* Sat Feb 26 2022 Sérgio Basto <sergio@serjux.com> - 21.12.2-1
- Update ffmpegthumbs to 21.12.2
- Add ffmpeg-5 PR
- lang has disappear from the package

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 21.04.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 11 2021 Leigh Scott <leigh123linux@gmail.com> - 21.04.2-3
- Rebuilt for new ffmpeg snapshot

* Mon Aug 02 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 21.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 12 2021 Sérgio Basto <sergio@serjux.com> - 21.04.2-1
- Update ffmpegthumbs to 21.04.2

* Sun Feb 21 2021 Sérgio Basto <sergio@serjux.com> - 20.12.2-1
- Update ffmpegthumbs to 20.12.2
- Add missing dependency on taglib

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 20.08.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 31 2020 Leigh Scott <leigh123linux@gmail.com> - 20.08.1-2
- Rebuilt for new ffmpeg snapshot

* Mon Sep 14 2020 Sérgio Basto <sergio@serjux.com> - 20.08.1-1
- Update ffmpegthumbs to 20.08.1

* Mon Aug 17 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 19.12.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 22 2020 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 19.12.1-3
- Rebuild for ffmpeg-4.3 git

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 19.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Sérgio Basto <sergio@serjux.com> - 19.12.1-1
- Update ffmpegthumbs to 19.12.1
- Fix build

* Wed Sep 25 2019 Leigh Scott <leigh123linux@googlemail.com> - 19.08.1-1
- 19.08.1

* Tue Aug 06 2019 Leigh Scott <leigh123linux@gmail.com> - 18.12.3-2
- Rebuild for new ffmpeg version

* Thu Mar 14 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.3-1
- 18.12.3

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 18.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Feb 28 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.2-1
- 18.12.2

* Mon Sep 17 2018 Sérgio Basto <sergio@serjux.com> - 18.08.1-1
- Update ffmpegthumbs to 18.08.1

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 17.12.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 08 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 17.12.0-4
- Rebuilt for new ffmpeg snapshot

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 17.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Leigh Scott <leigh123linux@googlemail.com> - 17.12.0-2
- Rebuilt for ffmpeg-3.5 git

* Fri Dec 29 2017 Sérgio Basto <sergio@serjux.com> - 17.12.0-1
- Update ffmpegthumbs to 17.12.0

* Tue Oct 17 2017 Leigh Scott <leigh123linux@googlemail.com> - 17.08.1-2
- Rebuild for ffmpeg update

* Sun Oct 08 2017 Sérgio Basto <sergio@serjux.com> - 17.08.1-1
- Update to 17.08.1

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 17.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 11 2017 Sérgio Basto <sergio@serjux.com> - 17.04.2-1
- Update to 17.04.2

* Sat Apr 29 2017 Leigh Scott <leigh123linux@googlemail.com> - 16.12.3-2
- Rebuild for ffmpeg update

* Wed Mar 29 2017 Sérgio Basto <sergio@serjux.com> - 16.12.3-1
- Update to 16.12.3

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 16.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 21 2017 Sérgio Basto <sergio@serjux.com> - 16.12.2-1
- Update ffmpegthumbs to 16.12.2 following Fedora KDE applications

* Thu Oct 13 2016 Sérgio Basto <sergio@serjux.com> - 16.08.2-1
- Update to 16.08.2

* Thu Sep 15 2016 Sérgio Basto <sergio@serjux.com> - 16.08.1-1
- Update to 16.08.1
- Drop Port-to-libavfilter-for-deinterlacing.patch is upstreamed.

* Sat Aug 20 2016 Sérgio Basto <sergio@serjux.com> - 16.04.3-1
- Update to 16.04.3, rfbz #4164, following kdemultimedia of Fedora proper,
  the ffmpegthumbs package is not ffmpegthumbnailer, neither kffmpegthumbnailer
  packages, these 3 packages have a very similar names but just ffmpegthumbs is
  part of kdemultimedia.

* Sat Jul 30 2016 Julian Sikorski <belegdol@fedoraproject.org> - 16.04.2-3
- Rebuilt for ffmpeg-3.1.1

* Fri Jul 08 2016 Leigh Scott <leigh123linux@googlemail.com> - 16.04.2-2
- fix f23 build

* Fri Jul 08 2016 Leigh Scott <leigh123linux@googlemail.com> - 16.04.2-1
- Update to 16.04.2 release
- patch for ffmpeg-3.0

* Sun Oct 19 2014 Sérgio Basto <sergio@serjux.com> - 4.13.97-3
- Rebuilt for FFmpeg 2.4.3

* Fri Sep 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 4.13.97-2
- Rebuilt for FFmpeg 2.4.x

* Wed Aug 06 2014 Rex Dieter <rdieter@fedoraproject.org> 4.13.97-1
- 4.13.97

* Wed Aug 06 2014 Rex Dieter <rdieter@fedoraproject.org> 4.13.3-1
- 4.13.3

* Sat Mar 29 2014 Sérgio Basto <sergio@serjux.com> - 4.11.3-2
- Rebuilt for ffmpeg-2.2

* Wed Nov 27 2013 Rex Dieter <rdieter@fedoraproject.org> 4.11.3-1
- 4.11.3

* Tue Oct 01 2013 Rex Dieter <rdieter@fedoraproject.org> 4.11.1-1
- 4.11.1

* Thu Aug 15 2013 Nicolas Chauvet <kwizart@gmail.com> - 4.10.1-3
- Rebuilt for FFmpeg 2.0.x

* Sun May 26 2013 Nicolas Chauvet <kwizart@gmail.com> - 4.10.1-2
- Rebuilt for x264/FFmpeg

* Fri Apr 05 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.1-1
- 4.10.1

* Wed Jan 16 2013 Rex Dieter <rdieter@fedoraproject.org> 4.9.97-1
- 4.9.97

* Sat Nov 24 2012 Nicolas Chauvet <kwizart@gmail.com> - 4.9.3-2
- Rebuilt for FFmpeg 1.0

* Thu Nov 08 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.3-1
- 4.9.3

* Wed Sep 12 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.1-1
- 4.9.1

* Thu Aug 30 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.0-1
- 4.9.0

* Mon Jun 18 2012 Rex Dieter <rdieter@fedoraproject.org> 4.8.90-4
- ffmpegthumbs

* Fri Mar 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 4.7.2-4
- Rebuilt for c++ ABI breakage

* Tue Feb 28 2012 Nicolas Chauvet <kwizart@gmail.com> - 4.7.2-3
- Rebuilt for x264/FFmpeg

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 4.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 01 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.2-1
- 4.7.2

* Mon Sep 26 2011 Nicolas Chauvet <kwizart@gmail.com> - 4.7.0-2
- Rebuilt for FFmpeg-0.8

* Fri Aug 12 2011 Magnus Tuominen magnus.tuominen@gmail.com> 4.7.0-1
- 4.7.0
- patch50 no longer needed

* Fri Apr 08 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.1-1
- 4.6.1

* Sun Jan 23 2011 Rex Dieter <rdieter@fedoraproject.org> - 4.6.0-1
- 4.6.0

* Thu Dec 09 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.85-1
- 4.5.85 (4.6beta2)
- drop Obsoletes/Provides ffmpegthumnailer

* Mon Nov 22 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.80-1
- 4.5.80 (4.6beta1)

* Mon Nov 22 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.3-2
- Obsoletes: ffmpegthumbnailer-devel too

* Thu Nov 18 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.3-1
- 4.5.3

* Fri Oct 15 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.2-1
- 4.5.2

* Sun Sep 19 2010 Magnus Tuominen <magnus.tuominen@gmail.com> - 4.5.1-2
- drop patch
- obsolete < 15

* Mon Sep 13 2010 Magnus Tuominen <magnus.tuominen@gmail.com> - 4.5.1-1
- first attempt on kdemultimedia-extras-freeworld
