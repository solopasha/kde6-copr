%bcond_without qt5
%bcond_without qt6

Name:           qtkeychain
Version:        0.14.2
Release:        1%{?dist}
Summary:        A password store library

License:        BSD
Url:            https://github.com/frankosterfeld/qtkeychain
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Fix qt6 detection broken by including ECMGeneratePriFile
#Patch0:         qtkeychain-qt6.patch

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig(libsecret-1)

%description
The qtkeychain library allows you to store passwords easily and securely.


%if %{with qt5}
%package qt5
Summary:        %{summary}

%description qt5
The qt5keychain library allows you to store passwords easily and securely.


%package qt5-devel
Summary:        Development files for %{name}-qt5
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5LinguistTools)
Requires:       %{name}-qt5%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       qt5-qtbase-devel%{?_isa}
# deps referenced in Qt5KeychainLibraryDepends-relwithdebinfo.cmake:  IMPORTED_LINK_INTERFACE_LIBRARIES_RELWITHDEBINFO "Qt5::Core;secret-1;gio-2.0;gobject-2.0;glib-2.0;Qt5::DBus"
# *probably* overlinking and can be pruned, but requires closer inspection
Requires:       pkgconfig(libsecret-1)

%description qt5-devel
This package contains development files for qt5keychain.
%endif


%if %{with qt6}
%package qt6
Summary:        %{summary}

%description qt6
The qt6keychain library allows you to store passwords easily and securely.


%package qt6-devel
Summary:        Development files for %{name}-qt6
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6LinguistTools)
Requires:       %{name}-qt6%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       qt6-qtbase-devel%{?_isa}
# deps referenced in Qt6KeychainLibraryDepends-relwithdebinfo.cmake:  IMPORTED_LINK_INTERFACE_LIBRARIES_RELWITHDEBINFO "Qt6::Core;secret-1;gio-2.0;gobject-2.0;glib-2.0;Qt6::DBus"
# *probably* overlinking and can be pruned, but requires closer inspection
Requires:       pkgconfig(libsecret-1)

%description qt6-devel
This package contains development files for qt6keychain.
%endif


%prep
%autosetup -p1


%build
%if %{with qt5}
%define _vpath_builddir %{_target_platform}-qt5
%cmake \
  -DBUILD_WITH_QT6:BOOL=OFF \
  -DECM_MKSPECS_INSTALL_DIR=%{_qt5_archdatadir}/mkspecs/modules \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build
%endif

%if %{with qt6}
%define _vpath_builddir %{_target_platform}-qt6
%cmake \
  -DBUILD_WITH_QT6:BOOL=ON \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build
%endif


%install
%if %{with qt5}
%define _vpath_builddir %{_target_platform}-qt5
%cmake_install
%endif

%if %{with qt6}
%define _vpath_builddir %{_target_platform}-qt6
%cmake_install
%endif

%find_lang %{name} --with-qt

grep %{_datadir}/qt5keychain/translations %{name}.lang > %{name}-qt5.lang
grep %{_datadir}/qt6keychain/translations %{name}.lang > %{name}-qt6.lang


%if %{with qt5}
%files qt5 -f %{name}-qt5.lang
%license COPYING
%{_libdir}/libqt5keychain.so.1
%{_libdir}/libqt5keychain.so.0*

%files qt5-devel
%{_includedir}/qt5keychain/
%{_libdir}/cmake/Qt5Keychain/
%{_libdir}/libqt5keychain.so
%{_qt5_archdatadir}/mkspecs/modules/qt_Qt5Keychain.pri
%endif

%if %{with qt6}
%files qt6 -f %{name}-qt6.lang
%license COPYING
%{_libdir}/libqt6keychain.so.1
%{_libdir}/libqt6keychain.so.0*

%files qt6-devel
%{_includedir}/qt6keychain/
%{_libdir}/cmake/Qt6Keychain/
%{_libdir}/libqt6keychain.so
%{_libdir}/qt6/mkspecs/modules/qt_Qt6Keychain.pri
%endif

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 30 2022 Sandro Mani <manisandro@gmail.com> - 0.13.2-3
- Add qt6 build

* Tue Dec 13 2022 Troy Dawson <tdawson@redhat.com> - 0.13.2-2
- Clean up qt4 build dependencies

* Sat Aug 20 2022 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.13.2-1
- Update to 0.13.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 08 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.11.1-1
- Update to 0.11.1

* Mon Aug 31 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.10.0-4
- Fix for CMake macro changes
- Add ability to disable Qt4 build (makes it easier to maintain EPEL8 branch)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 18 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.10.0-1
- Update to 0.10.0
- Drop upstreamed patches

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 31 2019 Rex Dieter <rdieter@fedoraproject.org> - 0.9.1-3
- -devel: +Requires: pkgconfig(libsecret-1)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 28 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.9.1-1
- Release 0.9.1 (#1601122, #1481589)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jul 23 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.7.0-2
- Fix packaging problems

* Mon May 23 2016 nikos roussos <comzeradd@fedoraproject.org> 0.7.0-1
- update to 0.7.0

* Sun May 22 2016 Nikos Roussos <comzeradd@fedoraproject.org> 0.6.2-2
- Bump release

* Thu Apr 28 2016 Nikos Roussos <comzeradd@fedoraproject.org> 0.6.2-1
- update to 0.6.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 29 2015 Rex Dieter <rdieter@fedoraproject.org> 0.5.0-1
- qtkeychain-0.5.0 (#1136285), enable Qt5 support

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.90-6.20140405git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.90-5.20140405git
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.90-4.20140405git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.90-3.20140405git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 06 2014 Rex Dieter <rdieter@fedoraproject.org> 0.3.90-2.20140405git
- track libqtkeychain soname
- use %%find_lang
- omit dup'd cmake defines

* Sun May 04 2014 <jmarrero@fedoraproject.org> 0.3.90-1
- Update to latest github commit.

* Sun Mar 16 2014 <jmarrero@fedoraproject.org> 0.3.0-1
- Update to latest upstream version

* Tue Jan 07 2014 <jmarrero@fedoraproject.org> 0.1.0-4.20130805git
- Remove gcc-c++ dep
- Fix Requires
- Remove unneeded line in devel description
- Leave black line between changelogs

* Sat Jan 04 2014 <jmarrero@fedoraproject.org> 0.1.0-3.20130805git
- Fix Version and Release
- Fix %%files devel's cmake ownership by pointing the subfiles
- Fix Changelog to reflect version and release changes

* Tue Dec 24 2013 <jmarrero@fedoraproject.org> 0.1.0-2.20130805git
- Fix descriptions

* Mon Dec 23 2013 <jmarrero@fedoraproject.org> 0.1.0-1.20130805git
- Initial Packaging
