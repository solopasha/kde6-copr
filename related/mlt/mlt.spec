%if 0%{?rhel} >= 8
%bcond_with     ruby
%bcond_with     php
%bcond_with     opencv
%else
%bcond_without  ruby
%bcond_without  php
%bcond_without  opencv
%endif

# needs nonfree/ndi-sdk
%bcond_with  ndi

Name:           mlt
Version:        7.22.0
Release:        4%{?dist}
Summary:        Toolkit for broadcasters, video editors, media players, transcoders

# mlt/src/win32/fnmatch.{c,h} are BSD-licensed.
# but is not used in Linux
License:        GPLv3 and LGPLv2+
URL:            http://www.mltframework.org/
Source0:        https://github.com/mltframework/mlt/releases/download/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/mltframework/mlt/pull/963
# Support compilation with libxml2 2.12.0
Patch0:         mlt-pr963-libxml2_2_12.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  sed
BuildRequires:  frei0r-devel
BuildRequires:  opencv-devel
BuildRequires:  cmake(Qt6CoreTools)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6GuiTools)
BuildRequires:  cmake(Qt6DBusTools)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6WidgetsTools)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  SDL-devel
BuildRequires:  SDL2-devel
%if ! (0%{?rhel} >= 8)
BuildRequires:  SDL_image-devel
BuildRequires:  SDL2_image-devel
%endif
BuildRequires:  gtk2-devel
BuildRequires:  pipewire-jack-audio-connection-kit-devel
BuildRequires:  libatomic
BuildRequires:  libogg-devel
#Deprecated dv and kino modules are not built.
#https://github.com/mltframework/mlt/commit/9d082192a4d79157e963fd7f491da0f8abab683f
#BuildRequires:  libdv-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  ladspa-devel
BuildRequires:  libxml2-devel
BuildRequires:  sox-devel
# verion 3.0.11 needed for php7 IIRC
BuildRequires:  swig >= 3.0.11
BuildRequires:  python3-devel
BuildRequires:  freetype-devel
BuildRequires:  libexif-devel
BuildRequires:  fftw-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  vid.stab-devel
BuildRequires:  movit-devel
BuildRequires:  eigen3-devel
BuildRequires:  libebur128-devel
BuildRequires:  rubberband-devel
BuildRequires:  ffmpeg-free-devel
BuildRequires:  xine-lib-devel
Provides:  mlt-freeworld = %{version}-%{release}
Obsoletes: mlt-freeworld < %{version}-%{release}

%if %{with ndi}
BuildRequires:  libndi-devel
BuildRequires:  ndi-sdk-devel
%endif
%if %{with opencv}
BuildRequires:  opencv-devel
%endif
BuildRequires:  pkgconfig(libarchive)

%if %{with ruby}
BuildRequires:  ruby-devel
BuildRequires:  ruby
%else
Obsoletes: mlt-ruby < %{version}-%{release}
%endif

%if %{with php}
BuildRequires: php-devel
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}%{php_extdir}/.*\\.so$
%endif


%description
MLT is an open source multimedia framework, designed and developed for
television broadcasting.

It provides a toolkit for broadcasters, video editors,media players,
transcoders, web streamers and many more types of applications. The
functionality of the system is provided via an assortment of ready to use
tools, xml authoring components, and an extendible plug-in based API.

%if %{with ndi}
%package ndi
Summary:        NDI support for MLT
%description ndi
This package adds NDI support through the NDI SDK to MLT.
%endif

%package devel
Summary:        Libraries, includes to develop applications with %{name}
License:        LGPLv2+
Requires:       pkgconfig
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains the header files and static libraries for
building applications which use %{name}.

%package -n python3-mlt
%{?python_provide:%python_provide python3-mlt}
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: Python package to work with MLT

%description -n python3-mlt
This module allows to work with MLT using python 3.

%package ruby
Requires: %{name}%{_isa} = %{version}-%{release}
Summary: Ruby package to work with MLT

%description ruby
This module allows to work with MLT using ruby.

%package php
Requires: php(zend-abi) = %{php_zend_api}
Requires: php(api) = %{php_core_api}
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: PHP package to work with MLT

%description php
This module allows to work with MLT using PHP.


%prep
%autosetup -p1

chmod 644 src/modules/qt/kdenlivetitle_wrapper.cpp
chmod 644 src/modules/kdenlive/filter_freeze.c
chmod -x demo/demo

# mlt/src/win32/fnmatch.{c,h} are BSD-licensed.
# be sure that aren't used
rm -r src/win32/


%build
%cmake -DCMAKE_SKIP_RPATH:BOOL=ON           \
       -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON   \
       %{?with_php: -DSWIG_PHP:BOOL=ON}     \
       -DSWIG_PYTHON:BOOL=ON                \
       %{?with_ruby: -DSWIG_RUBY:BOOL=ON}   \
       %{?with_opencv: -DMOD_OPENCV:BOOL=ON}  \
       -DMOD_GLAXNIMATE:BOOL=ON \
       -DMOD_GLAXNIMATE_QT6:BOOL=ON  \
       -DMOD_QT6:BOOL=ON \
       %{?with_ndi: -DMOD_NDI:BOOL=ON -DNDI_SDK_INCLUDE_PATH=%{_includedir}/ndi-sdk -DNDI_SDK_LIBRARY_PATH=%{_libdir} -DNDI_INCLUDE_DIR=%{_includedir}/ndi-sdk -DNDI_LIBRARY_DIR=%{_libdir}}

%cmake_build

%install
%cmake_install

%if %{with php}
install -d %{buildroot}%{_sysconfdir}/php.d
cat > %{buildroot}%{_sysconfdir}/php.d/mlt.ini << 'EOF'
; Enable mlt extension module
extension=mlt.so
EOF
%endif

# maintain binary /usr/bin/mlt-melt
mv %{buildroot}%{_bindir}/melt %{buildroot}%{_bindir}/mlt-melt

# Remove rpath file '/usr/bin/melt-7' contains an invalid rpath '/home/martin/rpmbuild/BUILD/mlt-7.0.1/x86_64-redhat-linux-gnu/out/lib' in [/home/martin/rpmbuild/BUILD/mlt-7.0.1/x86_64-redhat-linux-gnu/out/lib]
#chrpath --delete %{buildroot}%{_bindir}/melt-7

%check
# verify pkg-config version sanity
export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion mlt-framework-7)" = "%{version}"
test "$(pkg-config --modversion mlt++-7)" = "%{version}"

%ldconfig_scriptlets

%files
%doc AUTHORS NEWS README*
%doc demo/
%license COPYING GPL
%{_bindir}/mlt-melt
%{_bindir}/melt-7
%{_libdir}/mlt-7/
%{_libdir}/libmlt++-7.so.*
%{_libdir}/libmlt-7.so.*
%{_datadir}/mlt-7/
%{_mandir}/man1/melt-7.1*
%if %{with ndi}
%exclude %{_libdir}/mlt-7/libmltndi.so

%files ndi
%{_libdir}/mlt-7/libmltndi.so
%endif

%files -n python3-mlt
%{python3_sitearch}/mlt7.py*
%{python3_sitearch}/_mlt7.so
%{python3_sitearch}/__pycache__/mlt7.*

%if %{with ruby}
%files ruby
%{ruby_vendorarchdir}/mlt.so
%endif

%if %{with php}
%files php
%config(noreplace) %{_sysconfdir}/php.d/mlt.ini
%{php_extdir}/mlt.so
%if ! (0%{?fedora} > 37)
%{_libdir}/php/modules/mlt.php
%endif
%endif

%files devel
%{_libdir}/pkgconfig/mlt-framework-7.pc
%{_libdir}/pkgconfig/mlt++-7.pc
%{_libdir}/libmlt-7.so
%{_libdir}/libmlt++-7.so
%{_libdir}/cmake/Mlt7/Mlt7*.cmake
%{_includedir}/mlt-7/


%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.22.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild
- Workaround https://gcc.gnu.org/bugzilla/show_bug.cgi?id=113205
- Rebuild for opencv 4.9.0

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 01 2024 Marie Loise Nolden <loise@kde.org> - 7.22.0-2
- use Qt6 instead of Qt5, otherwise kdenlive won't work with Qt6/KF6

* Thu Dec 07 2023 Sérgio Basto <sergio@serjux.com> - 7.22.0-1
- Update mlt to 7.22.0 (#2252089)

* Thu Nov 30 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 7.20.0-2
- Backport upstream PR for compilation with libxml2 2.12.0

* Tue Oct 03 2023 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 7.20.0-1
- Update to 7.20.0 (#2241895)

* Tue Oct 03 2023 Remi Collet <remi@remirepo.net> - 7.18.0-4
- rebuild for https://fedoraproject.org/wiki/Changes/php83

* Sat Sep 23 2023 Sérgio Basto <sergio@serjux.com> - 7.18.0-3
- Rebuild to use new movit and vid.stab packages

* Mon Aug 07 2023 Sérgio Basto <sergio@serjux.com> - 7.18.0-2
- Rebuild for opencv 4.8.0

* Sat Jul 29 2023 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 7.18.0-1
- Update to 7.18.0 (#2227469)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jun 17 2023 Python Maint <python-maint@redhat.com> - 7.16.0-2
- Rebuilt for Python 3.12

* Mon May 08 2023 Sérgio Basto <sergio@serjux.com> - 7.16.0-1
- Update mlt to 7.16.0 (#2196232)

* Mon Mar 13 2023 Sérgio Basto <sergio@serjux.com> - 7.14.0-2
- Effectively enables xine module

* Sun Mar 12 2023 Neal Gompa <ngompa@fedoraproject.org> - 7.14.0-1
- Update to 7.14.0 for ffmpeg 6 compatibility

* Mon Jan 23 2023 Neal Gompa <ngompa@fedoraproject.org> - 7.12.0-4
- Build the ffmpeg and xine plugins in the main package
- Rename freeworld to ndi subpackage since it has only ndi plugin

* Mon Jan 16 2023 Sérgio Basto <sergio@serjux.com> - 7.12.0-3
- Rebuild for opencv 4.7.0

* Mon Jan 16 2023 Sérgio Basto <sergio@serjux.com> - 7.12.0-2
- Enable module glaxnimate

* Sun Nov 20 2022 Sérgio Basto <sergio@serjux.com> - 7.12.0-1
- Update mlt to 7.12.0

* Fri Nov 04 2022 Sérgio Basto <sergio@serjux.com> - 7.10.0-1
- Update mlt to 7.10.0 (#2137811 2139196)

* Wed Oct 05 2022 Remi Collet <remi@remirepo.net> - 7.8.0-3
- rebuild for https://fedoraproject.org/wiki/Changes/php82

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 10 2022 Sérgio Basto <sergio@serjux.com> - 7.8.0-1
- Update mlt to 7.8.0 (#2100308)

* Tue Jun 21 2022 Sérgio Basto <sergio@serjux.com> - 7.6.0-3
- Rebuilt for opencv 4.6.0

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 7.6.0-2
- Rebuilt for Python 3.11

* Fri Apr 01 2022 Sérgio Basto <sergio@serjux.com> - 7.6.0-1
- Update mlt to 7.6.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 12 2022 Sérgio Basto <sergio@serjux.com> - 7.4.0-2
- Rework freeworld sub-package
- Add NDI option

* Fri Jan 07 2022 Sérgio Basto <sergio@serjux.com> - 7.4.0-1
- Update mlt to 7.4.0
- On epel8 disable php and ruby plugins and not BR SDL_images

* Wed Dec 15 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 6.26.1-5
- rebuild for new vid.stab

* Thu Oct 28 2021 Remi Collet <remi@remirepo.net> - 6.26.1-4
- rebuild for https://fedoraproject.org/wiki/Changes/php81

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.26.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 6.26.1-2
- Rebuilt for Python 3.10

* Fri May 28 2021 Sérgio Basto <sergio@serjux.com> - 6.26.1-1
- Update mlt to 6.26.1

* Sun Mar 28 2021 Sérgio Basto <sergio@serjux.com> - 6.24.0-4
- Renable php and ruby plugins on epel8

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.24.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild
- On epel8 disable php and ruby plugins and not BR SDL_images

* Wed Jan 06 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 6.24.0-2
- F-34: rebuild against ruby 3.0

* Sat Dec 26 2020 Sérgio Basto <sergio@serjux.com> - 6.24.0-1
- Update mlt to 6.24.0 (#1904918)

* Thu Oct 22 2020 Nicolas Chauvet <kwizart@gmail.com> - 6.22.1-2
- Rebuilt for OpenCV

* Thu Aug 20 2020 Sérgio Basto <sergio@serjux.com> - 6.22.1-1
- Update to 6.22.1

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.20.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.20.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 6.20.0-2
- Rebuilt for Python 3.9
- Rebuild for OpenCV 4.3

* Mon Feb 17 2020 Martin Gansser <martinkg@fedoraproject.org> - 6.20.0-1
- Update to 6.20.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.18.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 6.18.0-3
- F-32: rebuild against ruby27

* Mon Dec 23 2019 Sérgio Basto <sergio@serjux.com> - 6.18.0-2
- Remove python2-mlt subpackage once flowblade is switched to Python 3 (#1738074)
- Nothing provides python3-mlt needed by flowblade-2.4 on F30 (#1785934)
- Enable audio support with vorbis (#1724862)

* Tue Nov 12 2019 Sérgio Basto <sergio@serjux.com> - 6.18.0-1
- Update to 6.18.0

* Sun Nov 03 2019 Sérgio Basto <sergio@serjux.com> - 6.16.0-4
- Fix build on rawhide with Python 3.8

* Tue Oct 22 2019 Sérgio Basto <sergio@serjux.com> - 6.16.0-3
- Couple of fixes from upstream for kdenlive
- Add python3-mlt in addition to python2-mlt, document Python 2 exception

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 11 2019 Sérgio Basto <sergio@serjux.com> - 6.16.0-1
- Update MLT to 6.16.0

* Tue May 07 2019 Sérgio Basto <sergio@serjux.com> - 6.14.0-2
- Flowblade requires python2-mlt until version 2.4, 2.4 will be the first
  Python3 supporting version https://github.com/jliljebl/flowblade/issues/597

* Sun Apr 28 2019 Sérgio Basto <sergio@serjux.com> - 6.14.0-1
- Update to 6.14.0 and switch to python3 on F30+

* Mon Mar 04 2019 Martin Gansser <martinkg@fedoraproject.org> - 6.12.0-7
- Add mlt-null-pointer-crash.patch again

* Sun Mar 03 2019 Martin Gansser <martinkg@fedoraproject.org> - 6.12.0-6
- Re-Add mlt-python2 subpackage

* Sat Feb 02 2019 Martin Gansser <martinkg@fedoraproject.org> - 6.12.0-5
- Add mlt-null-pointer-crash.patch fixes (RHBZ #1669010)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 6.12.0-3
- F-30: rebuild against ruby26

* Fri Jan 04 2019 Miro Hrončok <mhroncok@redhat.com> - 6.12.0-2
- Remove the Python 2 subpackage (#1628684)

* Thu Nov 29 2018 Martin Gansser <martinkg@fedoraproject.org> - 6.12.0-1
- Update to 6.12.0

* Thu Oct 11 2018 Remi Collet <remi@remirepo.net> - 6.10.0-5
- Rebuild for https://fedoraproject.org/wiki/Changes/php73

* Wed Aug 22 2018 Martin Gansser <martinkg@fedoraproject.org> - 6.10.0-4
- Rebuilt

* Wed Aug 22 2018 Sérgio Basto <sergio@serjux.com> - 6.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 13 2018 Martin Gansser <martinkg@fedoraproject.org> - 6.10.0-2
- Revert Revert-Prefer-qimage-over-pixbuf.patch
- Add 'if' conditions to fix missing python2 on Fedora 29

* Tue Jul 03 2018 Martin Gansser <martinkg@fedoraproject.org> - 6.10.0-1
- Update to 6.10.0

* Sat Jun 16 2018 Martin Gansser <martinkg@fedoraproject.org> - 6.8.0-2
- Add Revert-Prefer-qimage-over-pixbuf.patch to prevent flowblade segfault

* Sat May 12 2018 Martin Gansser <martinkg@fedoraproject.org> - 6.8.0-1
- Update to 6.8.0

* Mon Mar 05 2018 Adam Williamson <awilliam@redhat.com> - 6.6.0-7
- Rebuild for opencv soname bump

* Fri Mar 02 2018 Sérgio Basto <sergio@serjux.com> - 6.6.0-6
- Enable SDL1 and SDL2 as requested by flowblade authors
  https://github.com/jliljebl/flowblade/blob/master/flowblade-trunk/docs/SDL_2_AND_MLT_6_6_0.md

* Sun Feb 11 2018 Iryna Shcherbina <ishcherb@redhat.com> - 6.6.0-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Sérgio Basto <sergio@serjux.com> - 6.6.0-3
- Rebuild (movit-1.6.0)

* Sun Jan 28 2018 Sérgio Basto <sergio@serjux.com> - 6.6.0-2
- Try a fix for kdenlive: There is "Use GPU processing (Movit library)... "
  GPU processing needs MLT compiled with Movit and RTaudio modules
  It is greyed, can not select.

* Thu Jan 25 2018 Sérgio Basto <sergio@serjux.com> - 6.6.0-1
- Update to 6.6.0

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 6.5.0-0.9.20171213gitea973eb
- Rebuilt for switch to libxcrypt

* Fri Jan 05 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 6.5.0-0.8.20171213gitea973eb
- F-28: rebuild for ruby25

* Sat Dec 23 2017 Sérgio Basto <sergio@serjux.com> - 6.5.0-0.7.20171213gitea973eb
- Update snapshot

* Fri Nov 17 2017 Sérgio Basto <sergio@serjux.com> - 6.5.0-0.6.20171114git73bfefd
- Update snapshot

* Sun Nov 05 2017 Sérgio Basto <sergio@serjux.com> - 6.5.0-0.5.20171105gitddc40aa
- Update snapshot

* Tue Oct 10 2017 Sérgio Basto <sergio@serjux.com> - 6.5.0-0.4
- Add vid.stab support

* Tue Oct 03 2017 Remi Collet <remi@fedoraproject.org> - 6.5.0-0.3
- rebuild for https://fedoraproject.org/wiki/Changes/php72

* Sat Sep 30 2017 Sérgio Basto <sergio@serjux.com> - 6.5.0-0.2
- Enable movit support

* Sat Sep 30 2017 Sérgio Basto <sergio@serjux.com> - 6.5.0-0.1
- Update to 6.5.0 pre-version also fix some bugs (#1497386)
- Switch to SDL2

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 6.4.1-10
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 6.4.1-9
- Python 2 binary package renamed to python2-mlt
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 03 2017 Sérgio Basto <sergio@serjux.com> - 6.4.1-6
- Rebuild (opencv)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Sérgio Basto <sergio@serjux.com> - 6.4.1-4
- Better swig handler for el7 support

* Sat Jan 14 2017 Sérgio Basto <sergio@serjux.com> - 6.4.1-3
- Enable php extension, swig already support php7 (#1356985)

* Thu Jan 12 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 6.4.1-2
- F-26: rebuild for ruby24

* Tue Nov 29 2016 Sérgio Basto <sergio@serjux.com> - 6.4.1-1
- New upstream vesion, 6.4.1
- Fix license, win32 not used in Linux
- Clean trailing white spaces
- Move provides_exclude_from php into php clause

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jun 30 2016 Sérgio Basto <sergio@serjux.com> - 6.2.0-2
- Disable the php extension, for now, the PHP 7 landed in rawhide

* Wed May 25 2016 Sérgio Basto <sergio@serjux.com> - 6.2.0-1
- Initial MLT spec on Fedora.

* Tue Mar 29 2016 Sérgio Basto <sergio@serjux.com> - 6.0.0-3
- Use upstream patch to compile Ruby bindings

* Sun Feb 21 2016 Sérgio Basto <sergio@serjux.com> - 6.0.0-2
- Add license tag.
- More spec modernizations and rpmlint fixes.
- Configure conditional build for Ruby.
- Remove old BuilRequires that aren't needed anymore.
- Remove old config options (avformat-swscale and qimage-libdir) that no longer
  exist in configure.
- Fix Ruby build.

* Fri Feb 19 2016 Sérgio Basto <sergio@serjux.com> - 6.0.0-1
- Update 6.0.0 (This is a bugfix and minor enhancement release. Note that our
  release versioning scheme has changed. We were approaching 1.0 but decided to
  synchronize release version with the C library ABI version, which is currently
  at v6)
- Switch to qt5 to fix rfbz #3810 and copy some BRs from Debian package.

* Wed Nov 18 2015 Sérgio Basto <sergio@serjux.com> - 0.9.8-1
- Update MLT to 0.9.8

* Mon May 11 2015 Sérgio Basto <sergio@serjux.com> - 0.9.6-2
- Workaround #3523

* Thu May 07 2015 Sérgio Basto <sergio@serjux.com> - 0.9.6-1
- Update mlt to 0.9.6 .
- Added BuildRequires of libexif-devel .

* Thu May 07 2015 Sérgio Basto <sergio@serjux.com> - 0.9.2-4
- Added BuildRequires of opencv-devel, rfbz #3523 .

* Mon Oct 20 2014 Sérgio Basto <sergio@serjux.com> - 0.9.2-3
- Rebuilt for FFmpeg 2.4.3

* Fri Sep 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.9.2-2
- Rebuilt for FFmpeg 2.4.x

* Mon Sep 15 2014 Sérgio Basto <sergio@serjux.com> - 0.9.2-1
- New upstream release.

* Thu Aug 07 2014 Sérgio Basto <sergio@serjux.com> - 0.9.0-6
- Rebuilt for ffmpeg-2.3

* Sat Jul 26 2014 Sérgio Basto <sergio@serjux.com> - 0.9.0-5
- Rebuild for new php, need by mlt-php

* Sun Mar 30 2014 Sérgio Basto <sergio@serjux.com> - 0.9.0-4
- Rebuilt for ffmpeg-2.2 and fix for freetype2 changes.

* Wed Dec 04 2013 Sérgio Basto <sergio@serjux.com> - 0.9.0-3
- Update License tag .

* Wed Nov 20 2013 Sérgio Basto <sergio@serjux.com> - 0.9.0-2
- Enable gplv3 as asked in rfbz #3040
- Fix a changelog date.
- Fix Ruby warning with rpmbuild "Use RbConfig instead of obsolete and deprecated Config".
- Remove obsolete tag %%clean and rm -rf

* Mon Oct 07 2013 Sérgio Basto <sergio@serjux.com> - 0.9.0-1
- Update to 0.9.0

* Wed Oct 02 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.8.8-7
- Rebuilt

* Thu Aug 15 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.8.8-6
- Rebuilt for FFmpeg 2.0.x

* Mon Jun 10 2013 Rex Dieter <rdieter@fedoraproject.org> 0.8.8-5
- mlt-ruby FTBFS, omit until fixed (#2816)

* Sun May 26 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.8.8-4
- Rebuilt for x264/FFmpeg

* Sun Apr 28 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.8.8-3
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Feb 1  2013 Ryan Rix <ry@n.rix.si> - 0.8.8-1
- Fix ABI requirement to Ruby 1.9

* Fri Feb 1  2013 Ryan Rix <ry@n.rix.si> - 0.8.8-1
- Update to 0.8.8

* Wed Jan 30 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.8.6-2
- Rebuilt for ffmpeg

* Sun Dec 30 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.8.6-1
- Update to 0.8.6

* Sat Nov 24 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.8.0-3
- Rebuilt for FFmpeg 1.0

* Tue Jun 26 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.8.0-2
- Rebuilt for FFmpeg

* Tue Jun 19 2012 Richard Shaw <hobbes1069@gmail.com> - 0.8.0-1
- Update to latest upstream release.

* Thu Jun 14 2012 Remi Collet <remi@fedoraproject.org> 0.7.8-3
- fix filter

* Thu Jun 14 2012 Remi Collet <remi@fedoraproject.org> 0.7.8-2
- update PHP requirement for PHP Guildelines
- add php extension configuration file
- filter php private shared so

* Tue May 08 2012 Rex Dieter <rdieter@fedoraproject.org> 0.7.8-1
- 0.7.8

* Tue May 08 2012 Rex Dieter <rdieter@fedoraproject.org> 0.7.6-8
- rebuild (sox)

* Fri Mar 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.7.6-7
- Rebuilt for c++ ABI breakage

* Tue Feb 28 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.7.6-6
- Rebuilt for x264/FFmpeg

* Fri Jan 27 2012 Ryan Rix <ry@n.rix.si> 0.7.6-5
- Include patch to fix building on gcc47 (upstreaming)

* Wed Jan 25 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.7.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 29 2011 Ryan Rix <ry@n.rix.si> 0.7.6-3
- s/%%[?_isa}/%%{?_isa}

* Tue Nov 15 2011 Rex Dieter <rdieter@fedoraproject.org> 0.7.6-2
- rebuild

* Fri Nov 11 2011 Rex Dieter <rdieter@fedoraproject.org> 0.7.6-1
- 0.7.6
- track files/sonames closer
- tighten subpkg deps via %%{?_isa}
- drop dup'd %%doc items

* Mon Sep 26 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.7.4-2
- Rebuilt for ffmpeg-0.8

* Thu Jul 21 2011 Ryan Rix <ry@n.rix.si> - 0.7.4-1
- New upstream

* Sun Apr 10 2011 Ryan Rix <ry@n.rix.si> - 0.7.0-2
- Add SDL_image-devel BR per Kdenlive wiki page

* Thu Apr 7 2011 Ryan Rix <ry@n.rix.si> - 0.7.0-1
- New upstream

* Tue Dec 21 2010 Ryan Rix <ry@n.rix.si> - 0.5.4-2
- Fix build, needed a patch from mlt's git repo.

* Sat Nov 20 2010 Nicolas Chauvet <kwizart@gmail.com> - 0.5.4-1.1
- rebuilt - was missing in repo

* Wed Apr 21 2010 Ryan Rix <ry@n.rix.si> - 0.5.4-1
- New upstream version to fix reported crashes against Kdenlive

* Fri Feb 19 2010 Zarko Pintar <zarko.pintar@gmail.com> - 0.5.0-2
- disabled xine module for PPC arch.

* Thu Feb 18 2010 Zarko Pintar <zarko.pintar@gmail.com> - 0.5.0-1
- new version

* Wed Dec 09 2009 Zarko Pintar <zarko.pintar@gmail.com> - 0.4.10-1
- new version
- added subpackage for ruby

* Wed Oct 07 2009 Zarko Pintar <zarko.pintar@gmail.com> - 0.4.6-1
- new version
- added subpackages for: python, PHP

* Mon Sep 07 2009 Zarko Pintar <zarko.pintar@gmail.com> - 0.4.4-1
- new version
- renamed melt binary to mlt-melt

* Wed May 20 2009 Zarko Pintar <zarko.pintar@gmail.com> - 0.4.2-1
- new version
- removed obsolete patches

* Wed May 20 2009 Zarko Pintar <zarko.pintar@gmail.com> - 0.4.0-3
- added linker and license patches
- set license of MLT devel subpackage to LGPLv2+

* Wed May 20 2009 Zarko Pintar <zarko.pintar@gmail.com> - 0.4.0-2
- some PPC clearing

* Mon May 18 2009 Zarko Pintar <zarko.pintar@gmail.com> - 0.4.0-1
- update to 0.4.0

* Wed May 13 2009 Zarko Pintar <zarko.pintar@gmail.com> - 0.3.9-2
- spec cleaning

* Mon May 11 2009 Zarko Pintar <zarko.pintar@gmail.com> - 0.3.9-1
- new release
- MLT++  is now a part of this package

* Fri May  8 2009 Zarko Pintar <zarko.pintar@gmail.com> - 0.3.8-3
- unused-direct-shlib-dependency fix

* Fri Apr 17 2009 Zarko Pintar <zarko.pintar@gmail.com> - 0.3.8-2
- spec clearing
- added patches for resolving broken lqt-config, lib64 and execstack

* Wed Apr 15 2009 Zarko Pintar <zarko.pintar@gmail.com> - 0.3.8-1
- New release

* Thu Apr  9 2009 Zarko Pintar <zarko.pintar@gmail.com> - 0.3.6-3
- Enabled MMX support (not for PPC & PPC64)
- include demo files
- some spec cosmetics

* Thu Mar 12 2009 Zarko Pintar <zarko.pintar@gmail.com> - 0.3.6-2
- Change URL address
- devel Requires: pkgconfig

* Fri Feb 20 2009 Levente Farkas <lfarkas@lfarkas.org> - 0.3.6-1
- Update to 0.3.6

* Wed Nov  5 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 0.3.1-0.1.svn1180
- update to upstream r1180
- add --avformat-swscale configure option

* Tue Nov  4 2008 Arkady L. Shane <ashejn@yandex-team.ru> - 0.3.0-5
- rebuilt with proper qt4 paths

* Mon Oct 13 2008 jeff <moe@blagblagblag.org> - 0.3.0-4
- Build without fomit-frame-pointer ffmath
- Add BuildRequires: prelink
- clear-execstack libmltgtk2.so
- Don't strip binaries
- Group: Development/Libraries
- Prefix albino, humperdink, and miracle binaries with mlt-

* Sun Oct  5 2008 jeff <moe@blagblagblag.org> - 0.3.0-3
- License: GPLv2+ and LGPLv2+
- Group: Development/Tools
- ExcludeArch: x86_64 s390 s390x ppc ppc64
- %%defattr(-,root,root)
- %%doc docs/
- %%{_libdir}/%%{name} to main package


* Sun Aug 24 2008 jeff <moe@blagblagblag.org> - 0.3.0-2
- Change BuildRoot:
- Full source URL
- ExcludeArch: x86_64
- -devel Requires: pkgconfig, Requires: %%{name} = %%{version}-%%{release}

* Sun Aug 24 2008 jeff <moe@blagblagblag.org> - 0.3.0-1
- Update to 0.3.0
- --enable-gpl
- mlt-filehandler.patch

* Tue Jul  8 2008 jeff <moe@blagblagblag.org> - 0.2.5-0.svn1155.0blag.f10
- Build for blaghead

* Mon Jul  7 2008 jeff <moe@blagblagblag.org> - 0.2.5-0.svn1155.0blag.f9
- Update to svn r1155
- Remove sox-st.h.patch
- Add configure --disable-sox as it breaks build

* Sun Nov 11 2007 jeff <moe@blagblagblag.org> - 0.2.4-0blag.f7
- Update to 0.2.4
- Clean up spec

* Sat Jun 23 2007 jeff <moe@blagblagblag.org> - 0.2.3-0blag.f7
- Update to 0.2.3

* Sat Dec 30 2006 jeff <moe@blagblagblag.org> - 0.2.2-0blag.fc6
- Rebuild for 60k
- Remove --disable-sox
- Add mlt-0.2.2-sox-st.h.patch

* Sat Oct 21 2006 jeff <moe@blagblagblag.org> - 0.2.2-0blag.fc5
- Update to 0.2.2

* Sat Oct 21 2006 jeff <moe@blagblagblag.org> - 0.2.1-0blag.fc5
- BLAG'd
- Removed "olib" from path, name, etc.
- Add changelog
- Update summary/description

