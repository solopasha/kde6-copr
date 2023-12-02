Name:    phonon-backend-vlc
Summary: VLC phonon backend
Version: 0.12.0
Release: 1%{?dist}
License: LGPL-2.0-or-later
URL:     http://phonon.kde.org/
Source0: http://download.kde.org/stable/phonon/phonon-backend-vlc/%{version}/phonon-backend-vlc-%{version}.tar.xz

## downstream patches

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: pkgconfig(libvlc)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(phonon4qt5)
BuildRequires: pkgconfig(phonon4qt6)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: pkgconfig(xcb)

%global phonon_ver %(pkg-config --modversion phonon4qt5 2>/dev/null || echo 4.12)
%global vlc_ver %(pkg-config --modversion libvlc 2>/dev/null || echo 1.1.10)

%description
%{summary}.

%package -n phonon-qt5-backend-vlc
Summary:  Vlc phonon-qt5 backend
Provides: phonon-qt5-backend%{?_isa} = %{phonon_ver}
Requires: (vlc-core%{?_isa} >= %{vlc_ver} or vlc-free-core%{?_isa} >= %{vlc_ver})
Requires: phonon-qt5%{?_isa} >= %{phonon_ver}
%description -n phonon-qt5-backend-vlc
%{summary}.

%package -n phonon-qt6-backend-vlc
Summary:  Vlc phonon-qt6 backend
Provides: phonon-qt6-backend%{?_isa} = %{phonon_ver}
Requires: (vlc-core%{?_isa} >= %{vlc_ver} or vlc-free-core%{?_isa} >= %{vlc_ver})
Requires: phonon-qt6%{?_isa} >= %{phonon_ver}
%description -n phonon-qt6-backend-vlc
%{summary}.

%prep
%autosetup -n phonon-backend-vlc-%{version} -p1

# reset initial preference below (fedora's default) gstreamer
sed -i -e 's|^InitialPreference=.*|InitialPreference=10|g' src/phonon-vlc.json.in


%build
%global _vpath_builddir %{_target_platform}-qt5
%cmake -DPHONON_BUILD_QT6=OFF
%cmake_build

%global _vpath_builddir %{_target_platform}-qt6
%cmake -DPHONON_BUILD_QT5=OFF
%cmake_build

%install
%global _vpath_builddir %{_target_platform}-qt5
%cmake_install

%global _vpath_builddir %{_target_platform}-qt6
%cmake_install

%find_lang phonon_vlc --with-qt


%files -n phonon-qt5-backend-vlc -f phonon_vlc.lang
%doc AUTHORS
%license COPYING.LIB
%{_qt5_plugindir}/phonon4qt5_backend/phonon_vlc_qt5.so

%files -n phonon-qt6-backend-vlc
%doc AUTHORS
%license COPYING.LIB
%{_qt6_plugindir}/phonon4qt6_backend/phonon_vlc_qt6.so

%changelog
* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.11.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.11.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 15 2021 Nicolas Chauvet <kwizart@gmail.com> - 0.11.3-1
- Update to 0.11.3

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Apr 25 2020 Rex Dieter <rdieter@fedoraproject.org> - 0.11.1-1
- 0.11.1, qt5 only

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.10.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 31 2019 Rex Dieter <rdieter@fedoraproject.org> - 0.10.3-1
- 0.10.3

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Rex Dieter <rdieter@fedoraproject.org> - 0.10.2-1
- 0.10.2

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.9.1-6
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.9.1-4
- .spec polish

* Thu Dec 07 2017 Nicolas Chauvet <kwizart@gmail.com> - 0.9.1-3
- Rebuilt for libvlc

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 12 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.9.1-1
- 0.9.1

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jul 17 2016 Leigh Scott <leigh123linux@googlemail.com> - 0.9.0-1
- 0.9.0
- patch to fix compile with vlc-3

* Sat Nov 14 2015 Nicolas Chauvet <kwizart@gmail.com> - 0.8.2-2
- https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Dec 12 2014 Rex Dieter <rdieter@fedoraproject.org> 0.8.2-1
- 0.8.2

* Mon Nov 17 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.8.1-2
- Rebuild for vlc 2.2.0

* Sat Nov 08 2014 Rex Dieter <rdieter@fedoraproject.org> 0.8.1-1
- 0.8.1

* Mon Sep 08 2014 Rex Dieter <rdieter@fedoraproject.org> 0.8.0-1
- 0.8.0

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Dec 06 2013 Rex Dieter <rdieter@fedoraproject.org> 0.7.1-1
- 0.7.1

* Wed Nov 06 2013 Rex Dieter <rdieter@fedoraproject.org> 0.7.0-1
- 0.7.0, Qt5 support

* Wed Oct 02 2013 Rex Dieter <rdieter@fedoraproject.org> 0.6.2-2
- rebuild (vlc)

* Wed Feb 13 2013 Rex Dieter <rdieter@fedoraproject.org> 0.6.2-1
- 0.6.2

* Tue Nov 13 2012 Rex Dieter <rdieter@fedoraproject.org> 0.6.1-1
- 0.6.1

* Mon Aug 20 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.6.0-3
- Rebuilt (branching)

* Sat Aug 11 2012 Rex Dieter <rdieter@fedoraproject.org> 0.6.0-1
- 0.6.0

* Fri Mar 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.5.0-2
- Rebuilt for c++ ABI breakage

* Sat Feb 18 2012 Rex Dieter <rdieter@fedoraproject.org> 0.5.0-1
- 0.5.0

* Sat Jan 07 2012 Rex Dieter <rdieter@fedoraproject.org> 0.5.0-0.2.20120107git
- 20120107 (master branch) snapshot

* Mon Dec 12 2011 Rex Dieter <rdieter@fedoraproject.org> 0.5.0-0.1.20111212git
- 20111212 (master branch) snapshot

* Fri Oct 21 2011 Rex Dieter <rdieter@fedoraproject.org> 0.4.55-0.1.20111021
- 20111021 snapshot
- pkgconfig-style deps

* Mon Aug 15 2011 Rex Dieter <rdieter@fedoraproject.org> 0.4.1-2
- rebuild

* Mon Aug 01 2011 Rex Dieter <rdieter@fedoraproject.org> 0.4.1-1
- 0.4.1

* Tue Apr 26 2011 Rex Dieter <rdieter@fedoraproject.org> - 0.4.0-1
- 0.4.0

* Wed Dec 01 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.3.1-1
- 0.3.1

* Tue Nov 30 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.3.0-1
- 0.3.0

* Sat Sep 11 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.2.0-2
- %%doc AUTHORS COPYING.LIB
- drop BR: pkgconfig

* Sun Jul 25 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.2.0-1
- phonon-backend-vlc-0.2.0 release

* Thu Jul 01 2010 Rex Dieter <rdieter@fedoraproject.org. - 0.2-0.7.20100701
- 20100701 snapshot

* Sun May 02 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.2-0.4.20100501
- 20100501 snapshot

* Mon Apr 26 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.2-0.3.20100420
- Provides: phonon-backend

* Tue Apr 20 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.2-0.2.20100420
- phonon-vlc 20100420 snapshot
