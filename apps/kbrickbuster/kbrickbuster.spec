Name:    kbrickbuster
Summary: Destroy bricks with a ball
Version: 24.01.80
Release: 1%{?dist}

License: GPLv2+ and GFDL
URL:     https://invent.kde.org/games/kbreakout

%global stable     %stable_kf6
%global majmin_ver %majmin_ver_kf6

# Upstream source. Cannot be used because we need to *PATCH* the sources
#Source0: https://download.kde.org/%{stable}/release-service/%{version}/src/kbreakout-%{version}.tar.xz
Source0: kbrickbuster-24.01.75.tar.xz
# This patch is needed to modify upstream sources. They must be uploaded to the
# side-cache
Source1: patch.sh

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf6-rpm-macros
BuildRequires: kf6-kcompletion-devel
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-kdbusaddons-devel
BuildRequires: kf6-kdeclarative-devel
BuildRequires: kf6-kguiaddons-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kiconthemes-devel
BuildRequires: kf6-kitemviews-devel
BuildRequires: kf6-kio-devel
BuildRequires: kf6-kjobwidgets-devel
BuildRequires: kf6-knewstuff-devel
BuildRequires: kf6-knotifyconfig-devel
BuildRequires: kf6-knewstuff-devel
BuildRequires: kf6-kservice-devel
BuildRequires: kf6-kwindowsystem-devel
BuildRequires: kf6-kwidgetsaddons-devel
BuildRequires: kf6-kxmlgui-devel
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DocTools)
BuildRequires: pkgconfig(Qt6Widgets) pkgconfig(Qt6Qml) pkgconfig(Qt6Quick) pkgconfig(Qt6QuickWidgets)  pkgconfig(Qt6Svg)
BuildRequires: libkdegames-devel >= %{majmin_ver}

Obsoletes: kbreakout < 1:4.14.3-1
Provides:  kbreakout = 1:%{version}-%{release}

%description
The objective KBrickbuster game is to destroy as many bricks as possible
without losing the ball.


%prep
%autosetup -p1


%build
%{cmake_kf6}
%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html


%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop ||:


%files -f %{name}.lang
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}.*
%{_kf6_datadir}/%{name}/
%{_kf6_datadir}/metainfo/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/qlogging-categories6/%{name}.categories


%changelog
* Fri Nov 17 2023 Justin Zobel <justin.zobel@gmail.com> - 24.01.75-1
- Update to 24.01.75

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 02 2023 Marc Deop marcdeop@fedoraproject.org - 22.12.0-2
- Bring back patch.sh (and modify it)
- Use proper sources ( modified upstream with patch.sh)

* Mon Jan 02 2023 Marc Deop marcdeop@fedoraproject.org - 22.12.0-1
- 22.12.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 18.08.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 18.08.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 18.08.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 18.08.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 18.08.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 18.08.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.08.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.08.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.3-1
- 18.08.3

* Mon Nov 05 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.2-1
- 18.08.2

* Sun Sep 16 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.1-1
- 18.08.1

* Mon Aug 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.3-1
- 18.04.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.04.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.1-1
- 18.04.1

* Tue Mar 13 2018 Yaakov Selkowitz <yselkowi@redhat.com> - 17.12.3-1
- 17.12.3
- Fix renaming of docs and translations (#1555071)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.08.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 17.08.3-2
- Remove obsolete scriptlets

* Wed Nov 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.3-1
- 17.08.3

* Wed Oct 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.2-1
- 17.08.2

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.12.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.3-1
- 16.12.3, update URL

* Thu Feb 23 2017 Than Ngo <than@redhat.com> - 16.12.2-1
- fixed bz#1423803 - kbrickbuster: FTBFS in rawhide
- updated patch.sh

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.07.80-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 29 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.07.80-1
- 16.07.80

* Sat Jul 09 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.3-1
- 16.04.3

* Sun Jun 12 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.2-1
- 16.04.2

* Sun May 08 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.1-1
- 16.04.1

* Sat Apr 23 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.0-1
- 16.04.0

* Tue Mar 15 2016 Rex Dieter <rdieter@fedoraproject.org> - 15.12.3-1
- 15.12.3

* Sun Feb 14 2016 Rex Dieter <rdieter@fedoraproject.org> 15.12.2-1
- 15.12.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 15.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Rex Dieter <rdieter@fedoraproject.org> 15.12.1-1
- 15.12.1

* Wed Dec 23 2015 Rex Dieter <rdieter@fedoraproject.org> 15.12.0-2
- bump libkdegames dep

* Sat Dec 19 2015 Rex Dieter <rdieter@fedoraproject.org> 15.12.0-1
- 15.12.0, .spec cosmetics

* Wed Aug 26 2015 Daniel VrÃ¡til <dvratil@redhat.com> 15.08.0-1
- 15.08.0

* Thu Jul 02 2015 Rex Dieter <rdieter@fedoraproject.org> 15.04.3-1
- 15.04.3

* Thu Jul 02 2015 Rex Dieter <rdieter@fedoraproject.org> 15.04.2-3
- less-strict deps

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Rex Dieter <rdieter@fedoraproject.org> 15.04.2-1
- 15.04.2

* Thu Apr 16 2015 Rex Dieter <rdieter@fedoraproject.org> 15.04.0-1
- 15.04.0

* Thu Feb 12 2015 Than Ngo <than@redhat.com> 14.12.1-1
- rename kbreakout to KBrickbuster 

* Sat Jan 17 2015 Rex Dieter <rdieter@fedoraproject.org> - 14.12.1-1
- 14.12.1

* Tue Dec 09 2014 Rex Dieter <rdieter@fedoraproject.org> - 14.11.97-1
- 14.11.97

* Sun Nov 09 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.3-1
- 4.14.3

* Sun Oct 12 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.2-1
- 4.14.2

* Tue Sep 16 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.1-1
- 4.14.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 15 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.0-1
- 4.14.0

* Tue Aug 05 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.97-1
- 4.13.97

* Tue Jul 15 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.3-1
- 4.13.3

* Mon Jun 09 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.2-1
- 4.13.2

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 11 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.1-1
- 4.13.1

* Sat Apr 12 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.0-1
- 4.13.0

* Fri Apr 04 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.97-1
- 4.12.97

* Sun Mar 23 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.95-1
- 4.12.95

* Wed Mar 19 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.90-1
- 4.12.90

* Sun Mar 02 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.3-1
- 4.12.3

* Fri Jan 31 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.2-1
- 4.12.2

* Fri Jan 10 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.1-1
- 4.12.1

* Thu Dec 19 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.12.0-1
- 4.12.0

* Sun Dec 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.97-1
- 4.11.97

* Thu Nov 21 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.95-1
- 4.11.95

* Sat Nov 16 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.90-1
- 4.11.90

* Sat Nov 02 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.3-1
- 4.11.3

* Sat Sep 28 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.2-1
- 4.11.2

* Wed Sep 04 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.1-1
- 4.11.1

* Thu Aug 08 2013 Than Ngo <than@redhat.com> - 4.11.0-1
- 4.11.0

* Thu Jul 25 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.97-1
- 4.10.97

* Tue Jul 23 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.95-1
- 4.10.95

* Fri Jun 28 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.90-1
- 4.10.90

* Sat Jun 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.4-1
- 4.10.4

* Mon May 06 2013 Than Ngo <than@redhat.com> - 4.10.3-1
- 4.10.3

* Sun Mar 31 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.2-1
- 4.10.2

* Sat Mar 02 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.1-1
- 4.10.1

* Fri Feb 15 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.0-2
- update license, summary/description

* Thu Feb 07 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.0-1
- first try

