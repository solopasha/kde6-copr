%global base_name oxygen-icons

Name:    oxygen-icon-theme
Summary: Oxygen icon theme
Epoch:   1
Version: 6.0.0
Release: 1%{?dist}

License: LGPL-3.0-or-later
URL:     https://techbase.kde.org/Projects/Oxygen
BuildArch: noarch

Source0: https://download.kde.org/%{stable_kf6}/oxygen-icons/%{base_name}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/oxygen-icons/%{base_name}-%{version}.tar.xz.sig
Source2: kde-frameworks-signing-keys.pgp

## upstreamable patches

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel

BuildRequires:  hardlink
# for optimizegraphics
BuildRequires:  kde-dev-scripts
BuildRequires:  kde-filesystem
BuildRequires:  time

# inheritance, though could consider Recommends: if needed -- rex
Requires: hicolor-icon-theme

# upstream names
Provides:       oxygen-icons5 = %{epoch}:%{version}-%{release}
Provides:       oxygen-icons = %{epoch}:%{version}-%{release}
Provides:       kf6-oxygen-icons = %{epoch}:%{version}-%{release}

%description
%{summary}.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{base_name}-%{version} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

# optimize
pushd %{buildroot}%{_kf6_datadir}/icons/oxygen

du -s  .

hardlink -c -v %{buildroot}%{_kf6_datadir}/icons/oxygen

du -s .

time optimizegraphics

du -s .

## As of 15.04.3, hardlink reports
#Directories 78
#Objects 6926
#IFREG 6848
#Comparisons 901
#Linked 901
#saved 7737344
hardlink -c -v %{buildroot}%{_kf6_datadir}/icons/oxygen

du -s .
popd

# create/own all potential dirs
mkdir -p %{buildroot}%{_kf6_datadir}/icons/oxygen/{16x16,22x22,24x24,32x32,36x36,48x48,64x64,96x96,128x128,512x512,scalable}/{actions,apps,devices,mimetypes,places}


## trigger-based scriptlets
%transfiletriggerin -- %{_datadir}/icons/oxygen
gtk-update-icon-cache --force %{_datadir}/icons/oxygen &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/oxygen
gtk-update-icon-cache --force %{_datadir}/icons/oxygen &>/dev/null || :


%files
%doc AUTHORS CONTRIBUTING
%license COPYING
%dir %{_datadir}/icons/oxygen/
%{_datadir}/icons/oxygen/index.theme
%{_datadir}/icons/oxygen/base/
%{_datadir}/icons/oxygen/*x*/
%{_datadir}/icons/oxygen/scalable/


%changelog
* Wed Feb 21 2024 Alessandro Astone <ales.astone@gmail.com> - 1:6.0.0-1
- 6.0.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.245.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.245.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Nov 12 2023 Alessandro Astone <ales.astone@gmail.com> - 1:5.245.0-1
- 5.245.0
- This was moved upstream from frameworks release to an independent release

* Wed Oct 18 2023 Alessandro Astone <ales.astone@gmail.com> - 1:5.240.0^20230925.020636.8e9d99c-1
- Update to kf6

* Tue Oct 10 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:5.111.0-1
- 5.111.0

* Tue Sep 05 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:5.110.0-1
- 5.110.0

* Sat Aug 05 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:5.109.0-1
- 5.109.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.108.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:5.108.0-1
- 5.108.0

* Sat Jun 03 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:5.107.0-1
- 5.107.0

* Mon May 15 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:5.106.0-1
- 5.106.0

* Sun Apr 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:5.105.0-1
- 5.105.0

* Sat Mar 04 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:5.104.0-1
- 5.104.0

* Sun Feb 05 2023 Marc Deop <marcdeop@fedoraproject.org> - 1:5.103.0-1
- 5.103.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.102.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jan 14 2023 Marc Deop <marcdeop@fedoraproject.org> - 1:5.102.0-1
- 5.102.0

* Mon Dec 12 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:5.101.0-1
- whatever
- blaba

* Sun Nov 06 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:5.100.0-1
- 5.100.0

* Fri Oct 14 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:5.99.0-1
- 5.99.0

* Thu Sep 15 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:5.98.0-1
- 5.98.0

* Sat Aug 13 2022 Justin Zobel <justin@1707.io> - 5.97.0-1
- Update to 5.97.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.96.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 03 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:5.96.0-1
- 5.96.0

* Fri May 13 2022 Rex Dieter <rdieter@fedoraproject.org> - 1:5.94.0-1
- 5.94.0

* Sun Apr 10 2022 Justin Zobel <justin@1707.io> - 5.93-1
- Update to 5.93

* Thu Mar 10 2022 Rex Dieter <rdieter@fedoraproject.org> - 1:5.92.0-1
- 5.92.0

* Fri Feb 11 2022 Rex Dieter <rdieter@fedoraproject.org> - 1:5.91.0-1
- 5.91.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.90.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 04 2022 Marc Deop i Argemí (Private) <marc@marcdeop.com> - 1:5.90.0-1
- 5.90.0

* Wed Dec 08 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:5.89.0-1
- 5.89.0

* Mon Nov 08 2021 Marc Deop <marcdeop@fedoraproject.org> - 1:5.88.0-1
- 5.88.0

* Tue Oct 05 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:5.87.0-1
- 5.87.0

* Tue Sep 14 2021 Marc Deop <marcdeop@fedoraproject.org> - 1:5.86.0-1
- 5.86.0

* Thu Aug 12 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:5.85.0-1
- 5.85.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.83.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 08 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:5.83.0-1
- 5.83.0

* Mon May 03 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:5.82.0-1
- 5.82.0

* Tue Apr 06 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:5.81.0-1
- 5.81.0

* Tue Mar 09 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:5.80.0-1
- 5.80.0

* Sat Feb 06 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:5.79.0-2
- respin

* Sat Feb 06 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:5.79.0-1
- 5.79.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.78.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan  4 08:31:21 CST 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:5.78.0-1
- 5.78.0

* Tue Dec 29 2020 Marc Deop <marcdeop@fedoraproject.org> - 1:5.77.0-2
- Fix Source0 url

* Sun Dec 13 14:23:11 CST 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:5.77.0-1
- 5.77.0

* Thu Nov 19 09:17:26 CST 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:5.76.0-1
- 5.76.0

* Wed Oct 14 10:11:25 CDT 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:5.75.0-1
- 5.75.0

* Fri Sep 18 2020 Jan Grulich <jgrulich@redhat.com> - 1:5.74.0-1
- 5.74.0

* Mon Aug 03 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:5.73.0-1
- 5.73.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.72.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.72.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:5.72.0-1
- 5.72.0

* Tue Jun 16 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:5.71.0-1
- 5.71.0

* Mon May 04 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:5.70.0-1
- 5.70.0

* Fri Mar 20 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:5.68.0-1
- 5.68.0

* Sun Feb 02 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:5.67.0-1
- 5.67.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.66.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:5.66.0-1
- 5.66.0

* Tue Dec 17 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:5.65.0-1
- 5.65.0

* Fri Nov 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:5.64.0-1
- 5.64.0

* Tue Oct 22 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:5.63.0-1
- 5.63.0

* Mon Sep 16 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:5.62.0-1
- 5.62.0

* Wed Aug 07 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:5.61.0-1
- 5.61.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.60.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:5.60.0-1
- 5.60.0

* Thu Jun 06 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:5.59.0-1
- 5.59.0

* Tue May 07 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:5.58.0-1
- 5.58.0

* Sat Apr 13 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:5.57.0-1
- 5.57.0

* Sat Apr 13 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:5.56.0-2
- simpler scriptlets

* Tue Mar 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:5.56.0-1
- 5.56.0

* Mon Feb 04 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:5.55.0-1
- 5.55.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.54.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:5.54.0-1
- 5.54.0

* Sun Dec 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:5.53.0-1
- 5.53.0

* Sun Nov 04 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:5.52.0-1
- 5.52.0

* Wed Oct 10 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:5.51.0-1
- 5.51.0

* Tue Sep 04 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:5.50.0-1
- 5.50.0

* Tue Aug 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:5.49.0-1
- 5.49.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.48.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:5.48.0-1
- 5.48.0

* Sat Jun 02 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:5.47.0-1
- 5.47.0

* Sat May 05 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:5.46.0-1
- 5.46.0

* Sun Apr 08 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:5.45.0-1
- 5.45.0

* Sat Mar 03 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:5.44.0-1
- 5.44.0

* Wed Feb 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:5.43.0-1
- 5.43.0

* Fri Jan 19 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:5.42.0-2
- Requires: hicolor-icon-theme

* Mon Jan 08 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:5.42.0-1
- 5.42.0

* Mon Dec 04 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:5.41.0-1
- 5.41.0

* Fri Nov 10 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:5.40.0-1
- 5.40.0

* Sun Oct 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:5.39.0-1
- 5.39.0

* Fri Sep 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:5.38.0-2
- use scriptlet triggers

* Sun Sep 03 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:5.38.0-1
- 5.38.0

* Fri Aug 25 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:5.37.0-1
- 5.37.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:5.36.0-1
- 5.36.0

* Sun Jun 04 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:5.35.0-1
- 5.35.0

* Mon May 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:5.34.0-1
- 5.34.0

* Mon Apr 03 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:5.33.0-1
- 5.33.0

* Sat Mar 04 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:5.32.0-1
- 5.32.0

* Mon Feb 06 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.31.0-1
- 5.31.0, update URL

* Fri Dec 16 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:5.29.0-1
- 5.29.0

* Mon Oct 03 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.27.0-1
- 5.27.0

* Wed Sep 21 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.26.0-1
- 5.26.0

* Sun Aug 07 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.25.0-1
- 5.25.0

* Wed Jul 06 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.24.0-1
- KDE Frameworks 5.24.0

* Tue Jun 07 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.23.0-1
- 5.23.0

* Mon May 09 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.22.0-1
- 5.22.0

* Mon Apr 04 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.21.0-2
- (re)enable icon optimizations, support bootstrapping

* Mon Apr 04 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.21.0-1
- KDE Frameworks 5.21.0
- update URL, drop %%ghost index-theme.cache hacks, disable icon optimizations (temporary)

* Mon Mar 14 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.20.0-1
- KDE Frameworks 5.20.0

* Tue Feb 16 2016 Rex Dieter <rdieter@fedoraproject.org> 5.19.0-3
- kdenlive conflicts (#1308932), -BR: cmake

* Mon Feb 15 2016 Rex Dieter <rdieter@fedoraproject.org> 5.19.0-2
- add versioned Conflicts: kmail (#1308475, #1308358)

* Thu Feb 11 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.19.0-1
- KDE Frameworks 5.19.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 03 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.18.0-1
- KDE Frameworks 5.18.0

* Fri Dec 18 2015 Rex Dieter <rdieter@fedoraproject.org> 1:5.17.0-2
- .spec cosmetics, use %%license, fix %%changelog, update URL, drop Provides: system-kde-icon-theme

* Tue Dec 08 2015 Daniel Vrátil <dvratil@fedoraproject.org> - 1:5.17.0-1
- KDE Frameworks 5.17.0

* Sun Nov 08 2015 Daniel Vrátil <dvratil@fedoraproject.org> - 1:5.16.0-1
- KDE Frameworks 5.16.0

* Sun Nov 08 2015 Daniel Vrátil <dvratil@fedoraproject.org> - 1:5.16.0-1
- Moved to KDE Frameworks 5

* Fri Aug 14 2015 Rex Dieter <rdieter@fedoraproject.org> 15.04.3-2
- use optimizegraphics (from kde-dev-scripts)

* Sun Jun 28 2015 Rex Dieter <rdieter@fedoraproject.org> - 15.04.3-1
- 15.04.3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 01 2015 Rex Dieter <rdieter@fedoraproject.org> 15.04.2-1
- 15.04.2

* Thu May 14 2015 Rex Dieter <rdieter@fedoraproject.org> 15.04.1-1
- 15.04.1

* Fri Apr 10 2015 Rex Dieter <rdieter@fedoraproject.org> 15.04.0-1
- 15.04.0

* Sat Feb 28 2015 Rex Dieter <rdieter@fedoraproject.org> 14.12.3-1
- 14.12.3

* Mon Feb 23 2015 Rex Dieter <rdieter@fedoraproject.org> 14.12.2-1
- 14.12.2

* Sat Jan 10 2015 Rex Dieter <rdieter@fedoraproject.org> 14.12.1-1
- 14.12.1, drop cmake hacks

* Sun Dec 07 2014 Rex Dieter <rdieter@fedoraproject.org> 14.11.97-1
- 14.11.97

* Sat Nov 08 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.3-1
- 4.14.3

* Sat Oct 11 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.2-1
- 4.14.2

* Mon Sep 15 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.1-1
- 4.14.1

* Thu Aug 14 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.14.0-1
- 4.14.0

* Tue Aug 05 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.97-1
- 4.13.97

* Sun Jul 13 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.3-1
- 4.13.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Jun 07 2014 Rex Dieter <rdieter@fedoraproject.org> 4.13.2-1
- 4.13.2

* Fri May 09 2014 Rex Dieter <rdieter@fedoraproject.org> 4.13.1-1
- 4.13.1

* Fri Apr 11 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.13.0-1
- 4.13.0

* Mon Mar 31 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.97-1
- 4.12.97

* Sat Mar 22 2014 Rex Dieter <rdieter@fedoraproject.org> 4.12.95-1
- 4.12.95

* Mon Mar 17 2014 Rex Dieter <rdieter@fedoraproject.org> 4.12.90-1
- 4.12.90

* Fri Feb 28 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.3-1
- 4.12.3

* Fri Jan 31 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.2-1
- 4.12.2

* Fri Jan 10 2014 Rex Dieter <rdieter@fedoraproject.org> - 4.12.1-1
- 4.12.1

* Wed Dec 18 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.12.0-1
- 4.12.0

* Sun Dec 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.97-1
- 4.11.97

* Thu Nov 21 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.95-1
- 4.11.95

* Fri Nov 15 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.90-1
- 4.11.90

* Fri Nov 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.3-1
- 4.11.3

* Sat Sep 28 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.11.2-1
- 4.11.2

* Tue Sep 03 2013 Rex Dieter <rdieter@fedoraproject.org> 4.11.1-1
- 4.11.1

* Thu Aug 08 2013 Than Ngo <than@redhat.com> - 4.11.0-1
- 4.11.0

* Thu Jul 25 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.97-1
- 4.10.97

* Tue Jul 23 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.95-1
- 4.10.95

* Thu Jun 27 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.90-1
- 4.10.90

* Sat Jun 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.4-1
- 4.10.4

* Mon May 06 2013 Than Ngo <than@redhat.com> - 4.10.3-1
- 4.10.3

* Sat Mar 30 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.2-1
- 4.10.2

* Sat Mar 02 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.1-1
- 4.10.1

* Thu Jan 31 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.0-1
- 4.10.0

* Sat Jan 19 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.9.98-1
- 4.9.98

* Thu Jan 03 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.9.97-1
- 4.9.97

* Wed Dec 19 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.95-1
- 4.9.95

* Mon Dec 03 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.90-1
- 4.9.90 (4.10beta2)

* Fri Nov 02 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.3-1
- 4.9.3

* Fri Sep 28 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.2-1
- 4.9.2

* Mon Sep 03 2012 Than Ngo <than@redhat.com> - 4.9.1-1
- 4.9.1

* Sun Aug 12 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.0-2
- remove .spec cruft
- fancify Source0 handling

* Thu Jul 26 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.0-1
- 4.9.0

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.97-1
- 4.8.97

* Wed Jun 27 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.95-1
- 4.8.95

* Fri Jun 08 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.90-1
- 4.8.90

* Fri May 25 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.80-1
- 4.8.80

* Mon Apr 30 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.3-1
- 4.8.3

* Fri Mar 30 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.2-1
- 4.8.2

* Mon Mar 05 2012 Radek Novacek <rnovacek@redhat.com> 4.8.1-1
- 4.8.1

* Sun Jan 22 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.0-1
- 4.8.0

* Wed Jan 11 2012 Rex Dieter <rdieter@fedoraproject.org> 4.7.97-2
- icon theme cache not removed on uninstall (#771487)
- try harder to own all related dirs

* Wed Jan 04 2012 Radek Novacek <rnovacek@redhat.com> - 4.7.97-1
- 4.7.97

* Fri Dec 23 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.95-2
- Provides: oxygen-icons

* Wed Dec 21 2011 Radek Novacek <rnovacek@redhat.com> - 4.7.95-1
- 4.7.95

* Sat Dec 03 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.90-1
- 4.7.90

* Fri Nov 18 2011 Jaroslav Reznik <jreznik@redhat.com> 4.7.80-1
- 4.7.80 (beta 1)

* Fri Oct 28 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.3-1
- 4.7.3

* Tue Oct 04 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.2-1
- 4.7.2

* Wed Sep 14 2011 Radek Novacek <rnovacek@redhat.com> 4.7.1-1
- 4.7.1

* Tue Jul 26 2011 Jaroslav Reznik <jreznik@redhat.com> - 4.7.0-1
- 4.7.0

* Fri Jul 08 2011 Jaroslav Reznik <jreznik@redhat.com> - 4.6.95-1
- 4.6.95 (rc2)

* Tue Jun 28 2011 Than Ngo <than@redhat.com> - 4.6.90-1
- 4.6.90 (rc1)

* Fri May 27 2011 Jaroslav Reznik <jreznik@redhat.com> 4.6.80-1
- 4.6.80 (beta1)

* Thu Apr 28 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.3-1
- 4.6.3

* Wed Apr 06 2011 Jaroslav Reznik <jreznik@redhat.com> 4.6.2-1
- 4.6.2

* Sat Feb 26 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.1-1
- 4.6.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 21 2011 Jaroslav Reznik <jreznik@redhat.com> 4.6.0-1
- 4.6.0

* Wed Jan 05 2011 Jaroslav Reznik <jreznik@redhat.com> 4.5.95-1
- 4.5.95 (4.6rc2)

* Wed Dec 22 2010 Rex Dieter <rdieter@fedoraproject.org> 4.5.90-1
- 4.5.90 (4.6rc1)

* Fri Dec 03 2010 Thomas Janssen <thomasj@fedoraproject.org> 4.5.85-1
- 4.5.85 (4.6beta2)

* Sat Nov 20 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.80-1
- 4.5.80 (4.6beta1)

* Sun Oct 31 2010 Than Ngo <than@redhat.com> - 4.5.3-1
- 4.5.3

* Fri Oct 01 2010 Rex Dieter <rdieter@fedoraproject.org> -  4.5.2-1
- 4.5.2

* Tue Sep 28 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.1-2
- Obsoletes: fedora-kde-icon-theme (f13+)
- Provides:  system-kde-icon-theme (f13+)

* Fri Aug 27 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.1-1
- 4.5.1

* Thu Aug 05 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.5.0-1
- 4.5.0

* Sun Jul 25 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.95-1
- 4.5 RC3 (4.4.95)

* Wed Jul 07 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.92-1
- 4.5 RC2 (4.4.92)

* Fri Jun 25 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.90-1
- 4.5 RC 1 (4.4.90)

* Mon Jun 07 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.4.85-1
- 4.5 Beta 2 (4.4.85)

* Fri May 21 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.4.80-1
- 4.5 Beta 1 (4.4.80)

* Fri Apr 30 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.4.3-1
- 4.4.3

* Mon Mar 29 2010 Lukas Tinkl <ltinkl@redhat.com> - 4.4.2-1
- 4.4.2

* Sat Feb 27 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.1-1
- 4.4.1

* Tue Feb 09 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.0-2
- hardlink dup'd icons

* Fri Feb 05 2010 Than Ngo <than@redhat.com> - 4.4.0-1
- 4.4.0

* Sun Jan 31 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.3.98-1
- KDE 4.3.98 (4.4rc3)

* Thu Jan 21 2010 Lukas Tinkl <ltinkl@redhat.com> - 4.3.95-1
- KDE 4.3.95 (4.4rc2)

* Wed Jan  6 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.3.90-1
- 4.3.90 (4.4 rc1)

* Fri Dec 18 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.85-1
- 4.3.85 (4.4 beta2)

* Tue Dec  1 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.3.80-1
- KDE 4.4 beta1 (4.3.80)

* Sat Nov 21 2009 Ben Boeckel <MathStuf@gmail.com> - 4.3.75-0.1.svn1048496
- Update to 4.3.75 snapshot

* Sat Oct 31 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.3-1
- 4.3.3

* Mon Oct 05 2009 Than Ngo <than@redhat.com> - 4.3.2-1
- 4.3.2

* Fri Aug 28 2009 Than Ngo <than@redhat.com> - 4.3.1-1
- 4.3.1

* Thu Jul 30 2009 Than Ngo <than@redhat.com> - 4.3.0-1
- 4.3.0

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.98-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Than Ngo <than@redhat.com> - 4.2.98-1
- 4.3rc3

* Mon Jul 13 2009 Than Ngo <than@redhat.com> - 4.2.96-1
- 4.3rc2

* Fri Jun 26 2009 Than Ngo <than@redhat.com> - 4.2.95-1
- 4.3rc1

* Wed Jun 03 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.90-1
- KDE-4.3 beta2 (4.2.90)

* Fri May 08 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.85-1
- oxygen-icons-4.2.85

* Tue Mar 31 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.2-1
- kde-4.2.2

* Mon Mar 30 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.1-11
- License: LGPLv3+
- %%doc: AUTHORS CONTRIBUTING COPYING TODO*

* Fri Mar 27 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.1-10
- standalone (noarch) oxygen-icon-theme

