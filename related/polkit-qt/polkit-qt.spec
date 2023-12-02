
%global rpm_macros_dir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

Name:            polkit-qt
Version:         0.175.0
Release:         1%{?dist}
Summary:         Qt bindings for PolicyKit

License:         LGPL-2.0-or-later AND GPL-2.0-or-later AND BSD-3-Clause
URL:             https://projects.kde.org/projects/kdesupport/polkit-qt-1 
Source0:         https://download.kde.org/unstable/polkit-qt-1/polkit-qt-1-%{version}.tar.xz
Source10:        macros.polkit-qt

BuildRequires:   cmake
BuildRequires:   gcc-c++
BuildRequires:   pkgconfig(polkit-agent-1) 
BuildRequires:   pkgconfig(polkit-gobject-1)
BuildRequires:   pkgconfig(Qt5DBus) 
BuildRequires:   pkgconfig(Qt5DBus) 
BuildRequires:   pkgconfig(Qt5Widgets)
BuildRequires:   pkgconfig(Qt6DBus) 
BuildRequires:   pkgconfig(Qt6DBus) 
BuildRequires:   pkgconfig(Qt6Widgets)

%description
Polkit-qt is a library that lets developers use the PolicyKit API
through a nice Qt-styled API.

%package        rpm-macros
Summary:        rpm-macros for %{name}
%description    rpm-macros
%{summary}.

%package        qt6
Summary:        Qt6 support library for %{name}
%description    qt6
%{summary}.

%package        qt6-devel
Summary:        Development files for %{name}-qt6
Requires:       %{name}-qt6%{?_isa} = %{version}-%{release}
Requires:       %{name}-rpm-macros
%description    qt6-devel
%{summary}.

%package        qt5
Summary:        Qt5 support library for %{name}
Obsoletes:      polkit-qt < 0.175.0-1
Provides:       polkit-qt = %{version}-%{release}
%description    qt5
%{summary}.

%package        qt5-devel
Summary:        Development files for %{name}-qt5
Requires:       %{name}-qt5%{?_isa} = %{version}-%{release}
Requires:       %{name}-rpm-macros
%description    qt5-devel
%{summary}.

%prep
%autosetup -n %{name}-1-%{version} -p1


%build
%global _vpath_builddir %{_target_platform}-qt5
%cmake
%cmake_build

%global _vpath_builddir %{_target_platform}-qt6
%cmake -DQT_MAJOR_VERSION=6
%cmake_build


%install
%global _vpath_builddir %{_target_platform}-qt5
%cmake_install

%global _vpath_builddir %{_target_platform}-qt6
%cmake_install

install -p -m644 -D %{SOURCE10} %{buildroot}%{rpm_macros_dir}/macros.polkit-qt


%files rpm-macros
%{rpm_macros_dir}/macros.polkit-qt

%files qt5
%license LICENSES/*
%{_libdir}/libpolkit-qt5-core-1.so.1*
%{_libdir}/libpolkit-qt5-gui-1.so.1*
%{_libdir}/libpolkit-qt5-agent-1.so.1*

%files qt5-devel
%{_includedir}/polkit-qt5-1/
%{_libdir}/libpolkit-qt5-core-1.so
%{_libdir}/libpolkit-qt5-gui-1.so
%{_libdir}/libpolkit-qt5-agent-1.so
%{_libdir}/pkgconfig/polkit-qt5-1.pc
%{_libdir}/pkgconfig/polkit-qt5-core-1.pc
%{_libdir}/pkgconfig/polkit-qt5-gui-1.pc
%{_libdir}/pkgconfig/polkit-qt5-agent-1.pc
%{_libdir}/cmake/PolkitQt5-1/

%files qt6
%license LICENSES/*
%{_libdir}/libpolkit-qt6-core-1.so.1*
%{_libdir}/libpolkit-qt6-gui-1.so.1*
%{_libdir}/libpolkit-qt6-agent-1.so.1*

%files qt6-devel
%{_includedir}/polkit-qt6-1/
%{_libdir}/libpolkit-qt6-core-1.so
%{_libdir}/libpolkit-qt6-gui-1.so
%{_libdir}/libpolkit-qt6-agent-1.so
%{_libdir}/pkgconfig/polkit-qt6-1.pc
%{_libdir}/pkgconfig/polkit-qt6-core-1.pc
%{_libdir}/pkgconfig/polkit-qt6-gui-1.pc
%{_libdir}/pkgconfig/polkit-qt6-agent-1.pc
%{_libdir}/cmake/PolkitQt6-1/


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.112.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.112.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.112.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.112.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.112.0-23
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.112.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 10 2020 Rex Dieter <rdieter@fedoraproject.org> - 0.112.0-21
- FTBFS, use %%cmake macros, drop qt5 support (moved to polkit-qt-1)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.112.0-20
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.112.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.112.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 Rex Dieter <rdieter@fedoraproject.org> - 0.112.0-17
- disable qt5 support (now packaged separately in polkit-qt-1 module)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.112.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.112.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.112.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 0.112.0-13
- BR: gcc-c++, use %%ldconfig_scriptlets %%license

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.112.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.112.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.112.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.112.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 26 2016 Helio Chissini de Castro <helio@kde.org> - 0.112.0-8
- Fix polkit-qt5-devel dependency.

* Mon Feb 29 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.112.0-7
- pull in some upstream fixes
- -qt5: Obsoletes: polkit-qt5-1 (#1294471)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.112.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.112.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.112.0-4
- Rebuilt for GCC 5 C++11 ABI change

* Fri Oct 24 2014 Rex Dieter <rdieter@fedoraproject.org> 0.112.0-3
- build polkit-qt5-1(-devel) here 

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.112.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 10 2014 Martin Bříza <mbriza@redhat.com> - 0.112.0-1
- polkit-qt-1-0.112.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.103.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Feb 01 2014 Rex Dieter <rdieter@fedoraproject.org> - 0.103.0-10
- -devel: use %%_rpmconfigdir/macros.d (where supported)
- .spec cleanup

* Thu Dec 19 2013 Rex Dieter <rdieter@fedoraproject.org> 0.103.0-9
- pull in some more upstream fixes (from mbriza)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.103.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 11 2013 Rex Dieter <rdieter@fedoraproject.org> - 0.103.0-7
- pull in some upstream patches
- .spec cleanup

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.103.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 09 2012 Than Ngo <than@redhat.com> - 0.103.0-5
- fix url

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.103.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 20 2012 Than Ngo <than@redhat.com> - 0.103.0-3
- fix build issue with doxygen-1.8.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.103.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 15 2011 Jaroslav Reznik <jreznik@redhat.com> 0.103.0-1
- polkit-qt-1-0.103.0

* Mon Dec 12 2011 Rex Dieter <rdieter@fedoraproject.org> 0.99.0-3
- upstream crash patch (kde#258916,#684625)
- pull a couple more upstream patches
- -devel: drop Req: polkit-devel

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 09 2010 Jaroslav Reznik <jreznik@redhat.com> - 0.99.0-1
- polkit-qt-1-0.99.0

* Sat Nov 20 2010 Rex Dieter <rdieter@fedoraproject.org> -  0.98.1-1.20101120
- polkit-qt-1-0.98.1-20101120 snapshot

* Fri Oct 15 2010 Radek Novacek <rnovacek@redhat.com> - 0.96.1-4
- Next attempt of fix-deprecated-warnings patch

* Thu Oct 14 2010 Jaroslav Reznik <jreznik@redhat.com> - 0.96.1-3
- Revert fix-deprecated-warnings as it causes kde#254150

* Thu Oct 07 2010 Radek Novacek <rnovacek@redhat.com> 0.96.1-2
- Fixed deprecation warning with polkit-0.98
- Fixed typo in url
- Null checking patch (might be fix for #637064)

* Tue Sep 07 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.96.1-1
- polkit-qt-1-0.96.1

* Thu Jan 14 2010 Rex Dieter <rdieter@fedoraproject.org> - 0.95.1-3
- macros.polkit-qt : %%_polkit_qt_policydir, %%_polkit_qt

* Thu Jan 14 2010 Jaroslav Reznik <jreznik@redhat.com> - 0.95.1-2
- Installs FindPolkitQt-1.cmake

* Tue Jan 05 2010 Jaroslav Reznik <jreznik@redhat.com> - 0.95.1-1
- Update to release version

* Sun Dec 27 2009 Rex Dieter <rdieter@fedoraproject.org> - 0.95-0.3.20091119svn
- Provides: polkit-qt-1(-devel) ...
- doc: make noarch

* Wed Dec 09 2009 Kevin Kofler <Kevin@tigcc.ticalc.org>  - 0.95-0.2.20091119svn
- Obsoletes: polkit-qt-examples < 0.10 for upgrade path

* Mon Nov 23 2009 Radek Novacek <rnovacek@redhat.com> - 0.95-0.1.20091119svn
- Added -doc subpackage
- Added command to obtaining the source code

* Fri Nov 20 2009 Jaroslav Reznik <jreznik@redhat.com> - 0.95-0.1.20091119svn
- SPEC file fixes
- removed -examples subpackage

* Thu Nov 19 2009 Radek Novacek <rnovacek@redhat.com> - 0.1.20091119svn
- Initial build of snapshot from svn
