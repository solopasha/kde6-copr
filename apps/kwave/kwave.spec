%global commit0 ba5b3c3c4168356f178287948cb0efd59b06cd66
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

# Opt out of https://fedoraproject.org/wiki/Changes/fno-omit-frame-pointer
# https://bugzilla.redhat.com/show_bug.cgi?id=2265381
%undefine _include_frame_pointers

Name:           kwave
Version:        24.12.0
Release:        1%{?dist}
Summary:        Sound Editor for KDE

# See the file LICENSES for the licensing scenario
License:        GPLv2+ and BSD and CC-BY-SA
URL:            https://invent.kde.org/multimedia/kwave
%apps_source

BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib

BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)

BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Multimedia)

BuildRequires:  alsa-lib-devel
BuildRequires:  audiofile-devel >= 0.3.0

BuildRequires:  fftw-devel >= 3.0
BuildRequires:  flac-devel
BuildRequires:  gettext
BuildRequires:  id3lib-devel >= 3.8.1

BuildRequires:  libmad-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libvorbis-devel
BuildRequires:  opus-devel
BuildRequires:  pulseaudio-libs-devel >= 0.9.16
# 'convert' needed for doc generation
BuildRequires:  ImageMagick

Requires:       %{name}-doc = %{version}-%{release}

%description
With Kwave you can record, play back, import and edit many sorts of audio files
including multi-channel files. Kwave includes some plugins to transform audio
files in several ways and presents a graphical view with a complete zoom- and
scroll capability.

%package doc
Summary:        User manuals for %{name}
License:        GFDL
BuildArch:      noarch

%description doc
This package contains arch-independent files for %{name}, especially the
HTML documentation.

%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1

%build
%cmake_kf6 \
   -DWITH_MP3=ON
%cmake_build

%install
%cmake_install
gzip -dS z %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/kwave.svgz

%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%doc AUTHORS README.md TODO CHANGES
%license GNU-LICENSE LICENSES
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/%{name}/
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}.*
%{_kf6_libdir}/lib%{name}.so.*
%{_kf6_libdir}/lib%{name}gui.so.*
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_qtplugindir}/%{name}/

%files doc
%{_kf6_docdir}/HTML/*/%{name}

%changelog
* Fri Dec 06 2024 Pavel Solovev <daron439@gmail.com> - 24.12.0-1
- Update to 24.12.0

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

* Sat Feb 24 2024 Alessandro Astone <ales.astone@gmail.com> - 24.02.0-2
- Disable frame pointers

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.0-1
- 24.02.0

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.95-1
- 24.01.95

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90

* Mon Jan 08 2024 Steve Cossette <farchord@gmail.com> - 24.01.85-1
- 24.01.85 (Qt5)

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

* Wed Jan 04 2023 Justin Zobel <justin@1707.io> - 22.12.1-1
- Update to 22.12.1

* Mon Dec 19 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.12.0-1
- 22.12.0

* Fri Nov 04 2022 Marc Deop i Argemí (Private) <marc@marcdeop.com> - 22.08.3-1
- 22.08.3

* Fri Oct 14 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.2-1
- 22.08.2

* Wed Sep 14 2022 Michel Alexandre Salim <salimma@fedoraproject.org> - 22.08.1-2
- Rebuilt for flac 1.4.0

* Thu Sep 08 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.1-1
- 22.08.1

* Fri Aug 19 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.0-1
- 22.08.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 11 2022 Than Ngo <than@redhat.com> - 22.04.3-1
- 22.04.3

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

* Thu Jan 06 2022 Rex Dieter <rdieter@fedoraproject.org> - 21.12.1-1
- 21.12.1

* Mon Dec 27 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.12.0-1
- 21.12.0

* Tue Nov 02 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.08.3-1
- 21.08.3

* Thu Oct 21 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.08.2-1
- 21.08.2

* Wed Jul 28 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.3-1
- 21.04.3

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 10 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.2-1
- 21.04.2

* Fri Jun 04 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.1-2
- .spec cleanup, drop extraneous patch, build deps

* Tue May 11 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.1-1
- 21.04.1

* Mon Apr 19 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.0-1
- 21.04.0

* Wed Mar 03 2021 Rex Dieter <rdieter@fedoraproject.org> - 20.12.3-1
- 20.12.3

* Wed Feb 03 2021 Rex Dieter <rdieter@fedoraproject.org> - 20.12.2-1
- 20.12.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 2021 Sérgio Basto <sergio@serjux.com> - 20.12.1-1
- Update kwave to 20.12.1

* Fri Nov  6 15:03:05 CST 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.3-1
- 20.08.3

* Thu Oct 15 2020 Jeff Law <law@redhat.com> - 20.08.1-2
- Fix missing #include for gcc-11

* Tue Sep 15 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.1-1
- 20.08.1

* Tue Aug 18 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.0-1
- 20.08.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 12 2020 Marie Loise Nolden <loise@kde.org> - 20.04.3-1
- Update kwave to 20.04.3

* Fri Jun 12 2020 Marie Loise Nolden <loise@kde.org> - 20.04.2-1
- Update kwave to 20.04.2

* Tue May 26 2020 Sérgio Basto <sergio@serjux.com> - 20.04.1-1
- Update kwave to 20.04.1

* Thu Mar 26 2020 Sérgio Basto <sergio@serjux.com> - 19.12.3-1
- Update kwave to 19.12.3

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Sérgio Basto <sergio@serjux.com> - 19.12.1-1
- Update kwave to 19.12.1

* Wed Sep 25 2019 Sérgio Basto <sergio@serjux.com> - 19.08.1-1
- Update kwave to 19.08.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 07 2019 Sérgio Basto <sergio@serjux.com> - 18.12.3-1
- Update kwave to 18.12.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.08.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 16 2018 Sérgio Basto <sergio@serjux.com> - 18.08.1-1
- Update kwave to 18.08.1
- Reenable doc package.

* Thu Aug 02 2018 Sérgio Basto <sergio@serjux.com> - 18.04.3-2
- Decompressicons, icons should not be gzipped

* Fri Jul 27 2018 Sérgio Basto <sergio@serjux.com> - 18.04.3-1
- Update kwave to 18.04.3
- Disable doc as workaround.

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 17.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 11 2018 Sérgio Basto <sergio@serjux.com> - 17.12.3-1
- Update kwave to 17.12.3

* Thu Feb 22 2018 Sérgio Basto <sergio@serjux.com> - 17.12.2-1
- Update kwave to 17.12.2

* Tue Jan 30 2018 Sérgio Basto <sergio@serjux.com> - 17.12.1-1
- Update kwave to 17.12.1

* Tue Jan 02 2018 Sérgio Basto <sergio@serjux.com> - 17.12.0-2
- Use _kf5_metainfodir to fix appdata directory issue

* Fri Dec 29 2017 Sérgio Basto <sergio@serjux.com> - 17.12.0-1
- Update kwave to 17.12.0

* Sun Oct 08 2017 Sérgio Basto <sergio@serjux.com> - 17.08.1-1
- Update kwave to 17.08.1

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 17.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 12 2017 Leigh Scott <leigh123linux@googlemail.com> - 17.04.2-1
- Update to 17.04.2

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 16.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 18 2017 Leigh Scott <leigh123linux@googlemail.com> - 16.12.2-1
- Initial port to kf5

* Sun Feb 15 2015 Mario Blättermann <mario.blaettermann@gmail.com> - 0.8.99-7
- Add BSD license

* Sat Feb 07 2015 Mario Blättermann <mario.blaettermann@gmail.com> - 0.8.99-6
- Add mp3 support via libmad

* Tue Feb 03 2015 Mario Blättermann <mario.blaettermann@gmail.com> - 0.8.99-5
- Remove gcc-c++ from BR
- Fix %%post and %%postun
- Move lsm file to the -doc subpackage

* Mon Feb 02 2015 Mario Blättermann <mario.blaettermann@gmail.com> - 0.8.99-4
- Move the documentation to a noarch subpackage

* Sat Jan 31 2015 Mario Blättermann <mario.blaettermann@gmail.com> - 0.8.99-3
- Add update-desktop-database scriptlet

* Wed Jan 28 2015 Mario Blättermann <mario.blaettermann@gmail.com> - 0.8.99-2
- Generate png icons

* Fri Jan 16 2015 Mario Blättermann <mario.blaettermann@gmail.com> - 0.8.99-1
- Initial package
