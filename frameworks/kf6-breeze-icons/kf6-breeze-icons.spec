%global commit0 edd81c9dd18fb4a8a382be5cfec8edd703a6aa8e
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

# If KF7 still provides these icons, then their installation should then
# be disabled in KF6 builds.
%bcond install_icons 1
# for compatibility, to be removed once Kexi (and others?) are ported
%bcond install_rcc 1

%global framework breeze-icons

Name:    kf6-%{framework}
Summary: Breeze icon theme library
Version: 6.9.0%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release: 1%{?dist}

# skladnik.svg is CC-BY-SA-4.0
# folder-edit-sign-encrypt.svg is LGPL-2.1-or-later
# src/lib/ is LGPL-2.0-or-later
# all other icons are LGPL-3.0-or-later
License: LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later AND CC-BY-SA-4.0
URL:     https://api.kde.org/frameworks/breeze-icons/html/
%frameworks_meta

## upstream patches

## upstreamable patches


BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
# icon optimizations
BuildRequires: hardlink
# for generate-24px-versions.py
BuildRequires: python3-lxml

%if %{with install_icons}
Requires: breeze-icon-theme = %{version}-%{release}
%else
Requires: breeze-icon-theme
%endif

%description
%{summary}.

%if %{with install_icons}
%package -n breeze-icon-theme
Summary:     Breeze icon theme
# analysis above
License:     LGPL-2.1-or-later AND LGPL-3.0-or-later AND CC-BY-SA-4.0
BuildArch:   noarch
Requires:    hicolor-icon-theme
# Needed for proper Fedora logo
Requires:    system-logos
# upstream name
Provides:    breeze-icons = %{version}-%{release}
%description -n breeze-icon-theme
%{summary}.
%endif

%if %{with install_rcc}
%package -n breeze-icon-theme-rcc
Summary:     Breeze Qt resource files
# analysis above
License:     LGPL-2.1-or-later AND LGPL-3.0-or-later AND CC-BY-SA-4.0
BuildArch:   noarch
%description -n breeze-icon-theme-rcc
%{summary}.
%endif

%package     devel
Summary:     Breeze icon theme development files
Requires:    %{name} = %{version}-%{release}
# renamed for https://pagure.io/fedora-kde/SIG/issue/530
Provides:    breeze-icon-theme-devel = %{version}-%{release}
Obsoletes:   breeze-icon-theme-devel < 6.3.0-2
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1


%build
%cmake_kf6 \
  -DBINARY_ICONS_RESOURCE:BOOL=%{?with_install_rcc:ON}%{!?with_install_rcc:OFF} \
  -DSKIP_INSTALL_ICONS:BOOL=%{?with_install_icons:OFF}%{!?with_install_icons:ON} \
  %{nil}

%cmake_build


%install
%cmake_install

%if %{with install_icons}

# Do not use Fedora logo from upstream
rm -rf %{buildroot}%{_datadir}/icons/breeze-dark/apps/48/org.fedoraproject.AnacondaInstaller.svg
rm -rf %{buildroot}%{_datadir}/icons/breeze/apps/48/org.fedoraproject.AnacondaInstaller.svg
# Use copy found in fedora-logos
pushd %{buildroot}%{_datadir}/icons/breeze-dark/apps/48/
ln -s ../../../hicolor/48x48/apps/org.fedoraproject.AnacondaInstaller.svg org.fedoraproject.AnacondaInstaller.svg
popd
pushd %{buildroot}%{_datadir}/icons/breeze/apps/48/
ln -s ../../../hicolor/48x48/apps/org.fedoraproject.AnacondaInstaller.svg org.fedoraproject.AnacondaInstaller.svg
popd

## icon optimizations
du -s .
hardlink -c -v %{buildroot}%{_datadir}/icons/
du -s .

# %%ghost icon.cache
touch %{buildroot}%{_kf6_datadir}/icons/{breeze,breeze-dark}/icon-theme.cache


## trigger-based scriptlets
%transfiletriggerin -n breeze-icon-theme -- %{_datadir}/icons/breeze
gtk-update-icon-cache --force %{_datadir}/icons/breeze &>/dev/null || :

%transfiletriggerin -n breeze-icon-theme -- %{_datadir}/icons/breeze-dark
gtk-update-icon-cache --force %{_datadir}/icons/breeze-dark &>/dev/null || :

%transfiletriggerpostun -n breeze-icon-theme -- %{_datadir}/icons/breeze
gtk-update-icon-cache --force %{_datadir}/icons/breeze &>/dev/null || :

%transfiletriggerpostun -n breeze-icon-theme -- %{_datadir}/icons/breeze-dark
gtk-update-icon-cache --force %{_datadir}/icons/breeze-dark &>/dev/null || :

%endif

%files
%license COPYING.LIB
%doc README.md
%{_kf6_libdir}/libKF6BreezeIcons.so.6
%{_kf6_libdir}/libKF6BreezeIcons.so.%{version_no_git}

%files devel
%{_kf6_includedir}/BreezeIcons/
%{_kf6_libdir}/cmake/KF6BreezeIcons/
%{_kf6_libdir}/libKF6BreezeIcons.so

%if %{with install_icons}
%files -n breeze-icon-theme
%license COPYING-ICONS
%doc README.md
%ghost %{_datadir}/icons/breeze/icon-theme.cache
%{_datadir}/icons/breeze/index.theme
%{_datadir}/icons/breeze/*/
%ghost %{_datadir}/icons/breeze-dark/icon-theme.cache
%{_datadir}/icons/breeze-dark/index.theme
%{_datadir}/icons/breeze-dark/*/
%exclude %{_datadir}/icons/breeze/breeze-icons.rcc
%endif

%if %{with install_rcc}
%files -n breeze-icon-theme-rcc
%{_datadir}/icons/breeze/breeze-icons.rcc
%endif

%changelog
%{?kde_snapshot_changelog_entry}
* Fri Oct 04 2024 Pavel Solovev <daron439@gmail.com> - 6.7.0-1
- Update to 6.7.0

* Fri Sep 06 2024 Pavel Solovev <daron439@gmail.com> - 6.6.0-1
- Update to 6.6.0

* Fri Aug 09 2024 Pavel Solovev <daron439@gmail.com> - 6.5.0-1
- Update to 6.5.0

* Fri Jul 12 2024 Pavel Solovev <daron439@gmail.com> - 6.4.0-1
- Update to 6.4.0

* Mon Jun 10 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 6.3.0-2
- Renamed to kf6-breeze-icons with breeze-icon-theme subpackage

* Sat Jun 01 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.3.0-1
- 6.3.0

* Sat May 04 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.2.0-1
- 6.2.0

* Wed Apr 10 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.0-1
- 6.1.0

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.0.0-1
- 6.0.0

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.249.0-1
- 5.249.0

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.248.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.248.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 10 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.248.0-1
- 5.248.0

* Wed Dec 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.247.0-1
- 5.247.0

* Sat Dec 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.246.0-1
- 5.246.0

* Sun Nov 12 2023 Alessandro Astone <ales.astone@gmail.com> - 5.245.0-1
- 5.245.0

* Wed Oct 18 2023 Alessandro Astone <ales.astone@gmail.com> - 5.240.0^20231010.120657.8ac0648-1
- Update to kf6

* Tue Oct 10 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.111.0-1
- 5.111.0

* Wed Oct 04 2023 Neal Gompa <ngompa@fedoraproject.org> - 5.110.0-2
- Fix CMakeLists to use noarch cmake package install path

* Tue Sep 05 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.110.0-1
- 5.110.0

* Sat Aug 05 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.109.0-1
- 5.109.0

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.108.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.108.0-1
- 5.108.0

* Sat Jun 03 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.107.0-1
- 5.107.0

* Mon May 15 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.106.0-1
- 5.106.0

* Sun Apr 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.105.0-1
- 5.105.0

* Sat Mar 04 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.104.0-1
- 5.104.0

* Sun Feb 05 2023 Marc Deop <marcdeop@fedoraproject.org> - 5.103.0-1
- 5.103.0

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.102.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jan 14 2023 Marc Deop <marcdeop@fedoraproject.org> - 5.102.0-1
- 5.102.0

* Mon Dec 12 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.101.0-1
- 5.101.0
- use new macros to simplify code

* Sun Nov 06 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.100.0-1
- 5.100.0

* Fri Oct 14 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.99.0-1
- 5.99.0

* Thu Sep 15 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.98.0-1
- 5.98.0

* Mon Aug 15 2022 Yaroslav Sidlovsky <zawertun@gmail.com> - 5.97.0-2
- BR: python3-lxml

* Sat Aug 13 2022 Justin Zobel <justin@1707.io> - 5.97.0-1
- Update to 5.97.0

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.96.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 03 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.96.0-1
- 5.96.0

* Fri May 13 2022 Rex Dieter <rdieter@fedoraproject.org> - 5.94.0-1
- 5.94.0

* Sun Apr 10 2022 Justin Zobel <justin@1707.io> - 5.93-1
- Update to 5.93

* Thu Mar 10 2022 Rex Dieter <rdieter@fedoraproject.org> - 5.92.0-1
- 5.92.0

* Fri Feb 11 2022 Rex Dieter <rdieter@fedoraproject.org> - 5.91.0-1
- 5.91.0

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.90.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 04 2022 Marc Deop i Argemí (Private) <marc@marcdeop.com> - 5.90.0-1
- 5.90.0

* Wed Dec 08 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.89.0-1
- 5.89.0

* Mon Nov 08 2021 Marc Deop <marcdeop@fedoraproject.org> - 5.88.0-1
- 5.88.0

* Tue Oct 05 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.87.0-1
- 5.87.0

* Tue Sep 14 2021 Marc Deop <marcdeop@fedoraproject.org> - 5.86.0-1
- 5.86.0

* Thu Aug 12 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.85.0-1
- 5.85.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.83.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 08 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.83.0-1
- 5.83.0

* Mon May 03 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.82.0-1
- 5.82.0

* Thu Apr 29 2021 Tom Callaway <spot@fedoraproject.org> - 5.81.0-3
- use fedora logo image from fedora-logos (not upstream copy)

* Fri Apr 09 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.81.0-2
- respin

* Tue Apr 06 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.81.0-1
- 5.81.0

* Tue Mar 09 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.80.0-1
- 5.80.0

* Sat Feb 06 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.79.0-2
- respin

* Sat Feb 06 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.79.0-1
- 5.79.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.78.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan  4 08:30:16 CST 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.78.0-1
- 5.78.0

* Sun Dec 13 14:06:11 CST 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.77.0-1
- 5.77.0

* Thu Nov 19 08:51:38 CST 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.76.0-1
- 5.76.0

* Wed Oct 14 09:42:50 CDT 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.75.0-1
- 5.75.0

* Fri Sep 18 2020 Jan Grulich <jgrulich@redhat.com> - 5.74.0-1
- 5.74.0

* Mon Aug 03 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.73.0-1
- 5.73.0, use %%cmake_build %%cmake_install

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.72.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.72.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.72.0-1
- 5.72.0

* Tue Jun 16 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.71.0-1
- 5.71.0

* Mon May 04 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.70.0-1
- 5.70.0

* Tue Apr 21 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.69.0-1
- 5.69.0

* Fri Mar 20 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.68.0-1
- 5.68.0

* Sun Feb 02 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.67.0-1
- 5.67.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.66.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Rex Dieter <rdieter@fedoraproject.org> - 5.66.0-1
- 5.66.0

* Tue Dec 17 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.65.0-1
- 5.65.0

* Fri Nov 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.64.0-1
- 5.64.0

* Tue Oct 22 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.63.0-1
- 5.63.0

* Mon Sep 16 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.62.0-1
- 5.62.0

* Wed Aug 07 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.61.0-1
- 5.61.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.60.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 13 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.60.0-1
- 5.60.0

* Thu Jun 06 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.59.0-1
- 5.59.0

* Tue May 07 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.58.0-1
- 5.58.0

* Sat Apr 13 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.57.0-2
- simplify scriptlets (bug #1699280)

* Mon Apr 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.57.0-1
- 5.57.0

* Tue Mar 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.56.0-1
- 5.56.0

* Mon Feb 04 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.55.0-1
- 5.55.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.54.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 5.54.0-1
- 5.54.0

* Sun Dec 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.53.0-1
- 5.53.0

* Sun Nov 04 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.52.0-1
- 5.52.0

* Wed Oct 10 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.51.0-1
- 5.51.0

* Tue Sep 04 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.50.0-1
- 5.50.0

* Tue Aug 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.49.0-1
- 5.49.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.48.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.48.0-1
- 5.48.0

* Sat Jun 02 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.47.0-1
- 5.47.0

* Sat May 05 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.46.0-1
- 5.46.0

* Sun Apr 08 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.45.0-1
- 5.45.0

* Sat Mar 03 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.44.0-1
- 5.44.0

* Wed Feb 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.43.0-1
- 5.43.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.42.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.42.0-2
- Requires: hicolor-icon-theme

* Mon Jan 08 2018 Rex Dieter <rdieter@fedoraproject.org> - 5.42.0-1
- 5.42.0

* Mon Dec 04 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.41.0-1
- 5.41.0

* Fri Nov 10 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.40.0-1
- 5.40.0

* Wed Oct 25 2017 Troy Dawson <tdawson@redhat.com> - 5.39.0-2
- Cleanup spec file conditionals

* Sun Oct 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.39.0-1
- 5.39.0

* Wed Sep 27 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.38.0-2
- use scriptlet triggers (f26+)

* Sun Sep 03 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.38.0-1
- 5.38.0

* Fri Aug 25 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.37.0-1
- 5.37.0

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.36.0-1
- 5.36.0

* Sun Jun 04 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.35.0-1
- 5.35.0

* Sat May 20 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.34.0-2
- summary typo

* Mon May 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.34.0-1
- 5.34.0

* Tue Apr 25 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.33.0-2
- -rcc subpkg
- drop creating/owning extra dirs (layout has changed since)
- .spec cosmetics

* Mon Apr 03 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.33.0-1
- 5.33.0

* Sat Mar 04 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.32.0-1
- 5.32.0

* Mon Feb 06 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.31.0-1
- 5.31.0, update URL

* Fri Dec 16 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.29.0-1
- 5.29.0

* Fri Nov 18 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.27.0-2
- Breeze Dark is listed as Breeze in System Settings (kde#370213)

* Mon Oct 03 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.27.0-1
- 5.27.0

* Wed Sep 07 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.26.0-1
- KDE Frameworks 5.26.0

* Sun Aug 07 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.25.0-1
- 5.25.0

* Wed Jul 06 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.24.0-1
- KDE Frameworks 5.24.0

* Tue Jun 07 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.23.0-1
- 5.23.0

* Mon May 16 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.22.0-2
- backport fix for gtk warnings (kde#362041)

* Mon May 16 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.22.0-1
- KDE Frameworks 5.22.0

* Thu Apr 14 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.21.0-3
- Obsoletes: breeze-icon-theme < 5.17.0

* Thu Apr 14 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.21.0-2
- make Requires: breeze-cursor-theme fedora only
- update URL, -BR: cmake

* Mon Apr 04 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.21.0-1
- KDE Frameworks 5.21.0

* Mon Mar 14 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.20.0-1
- KDE Frameworks 5.20.0

* Thu Feb 11 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.19.0-1
- KDE Frameworks 5.19.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 03 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.18.0-1
- KDE Frameworks 5.18.0

* Tue Dec 08 2015 Daniel Vrátil <dvratil@fedoraproject.org> - 5.17.0-1
- KDE Frameworks 5.17.0

* Sun Nov 15 2015 Rex Dieter <rdieter@fedoraproject.org> - 5.16.0-2
- Requires: breeze-cursor-theme (#1282203)
- use hardlink optimizer
- fix breeze dark inheritance (again)

* Sun Nov 08 2015 Daniel Vrátil <dvratil@fedoraproject.org> - 5.16.0-1
- KDE Frameworks 5.16.0

* Sun Nov 08 2015 Daniel Vrátil <dvratil@fedoraproject.org> - 5.16.0-1
- Moved to KDE Frameworks 5
