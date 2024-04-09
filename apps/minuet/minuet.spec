Name:           minuet
Version:        24.02.2
Release:        1%{?dist}
Summary:        A KDE Software for Music Education
#OFL license for bundled Bravura.otf font
#and BSD license for cmake/FindFluidSynth.cmake
License:        GPL-2.0-or-later AND OFL-1.1
URL:            http://www.kde.org
%apps_source

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules >= 5.15.0
BuildRequires:  kf6-rpm-macros
BuildRequires:  kf6-filesystem
BuildRequires:  desktop-file-utils

BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Svg)

BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  libappstream-glib
# Runtime requirement
Requires:       hicolor-icon-theme
Requires:       %{name}-data

Provides:       bundled(font(bravura))

%description
Application for Music Education.

Minuet aims at supporting students and teachers in many aspects
of music education, such as ear training, first-sight reading,
solfa, scales, rhythm, harmony, and improvisation.
Minuet makes extensive use of MIDI capabilities to provide a
full-fledged set of features regarding volume, tempo, and pitch
changes, which makes Minuet a valuable tool for both novice and
experienced musicians.

%package devel
Summary:        Minuet: Build Environment
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development headers and libraries for Minuet.

%package data
Summary:        Minuet: Data files
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description data
Data files for Minuet.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
chmod -x src/app/org.kde.%{name}.desktop

%build
%cmake_kf6 \
	-DQT_MAJOR_VERSION=6

%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name --with-html

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.%{name}.desktop


%files -f %{name}.lang
%doc README*
%license COPYING*
%{_datadir}/applications/org.kde.%name.desktop
%{_kf6_metainfodir}/org.kde.%{name}.metainfo.xml
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_kf6_libdir}/libminuetinterfaces.so.*
%{_qt6_plugindir}/%{name}

%files devel
%doc README*
%license COPYING*
%{_includedir}/%{name}
%{_kf6_libdir}/libminuetinterfaces.so

%files data
%{_kf6_datadir}/%{name}


%changelog
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

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90

* Thu Dec 28 2023 Marie Loise Nolden <loise@kde.org> - 24.01.85-1
- 24.01.85

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

* Mon Apr 24 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 23.04.0-2
- Fix license

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

* Sun Aug 21 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 22.08.0-1
- Update to 22.08.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Than Ngo <than@redhat.com> - 22.04.3-1
- 22.04.3

* Tue Apr 26 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 22.04.0-1
- Update to 22.04.0

* Thu Mar 03 2022 Marc Deop <marcdeop@fedoraproject.org> - 21.12.3-1
- 21.12.3

* Fri Feb 04 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 21.12.2-1
- Update to 21.12.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 11 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 21.12.1-1
- Update to 21.12.1

* Mon Dec 13 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 21.12.0-1
- Update to 21.12.0

* Fri Sep 24 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 21.08.1-1
- Update to 21.08.1

* Mon Aug 23 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 21.08.0-1
- Update to 21.08.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 15 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 21.04.3-1
- Update to 21.04.3

* Wed Jun 16 2021 Vasiliy Glazov <vascom2@gmail.com> - 21.04.2-2
- fluidsynth so bump

* Fri Jun 11 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 21.04.2-1
- Update to 21.04.2

* Wed May 19 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 21.04.1-1
- Update to 21.04.1

* Thu Apr 22 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 21.04.0-1
- Update to 21.04.0

* Mon Mar 15 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 20.12.3-1
- Update to 20.12.3

* Mon Feb 22 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 20.12.2-1
- Update to 20.12.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.08.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 07 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.08.3-1
- Update to 20.08.3

* Wed Oct 21 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.08.2-1
- Update to 20.08.2

* Wed Sep 23 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.08.1-1
- Update to 20.08.1

* Thu Aug 20 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.08.0-1
- Update to 20.08.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.04.3-1
- Update to 20.04.3

* Sat Jun 13 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.04.2-1
- Update to 20.04.2

* Thu May 21 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.04.1-1
- Update to 20.04.1

* Mon Feb 17 2020 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 19.12.1-3
- Rebuild against fluidsynth2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 19.12.1-1
- Update to 19.12.1

* Thu Nov 07 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 19.08.2-1
- Update to 19.08.2
- Enable LTO

* Fri Sep 06 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 19.08.1-1
- Update to 19.08.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.04.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 15 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 19.04.1-2
- Added gcc-c++ to BR
- Data in separate subpackage
- Correct licensing

* Mon May 13 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 19.04.1-1
- First release for fedora
