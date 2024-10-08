%global commit0 1b6c2c82b1e5d3e12012f25bedf6d62c144bf7e5
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

Name:    kirigami-gallery
Version: 24.08.2
Release: 1%{?dist}
Summary: Gallery application built using Kirigami
License: LGPL-2.1-or-later
URL:     https://apps.kde.org/kirigami2.gallery
%apps_source

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Widgets)

BuildRequires: cmake(KF6ItemModels)
BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KF5Package)

Requires:   kf6-kirigami%{?_isa}
Requires:   kf6-kitemmodels%{?_isa}
Requires:   breeze-icon-theme

%description
Example application which uses all features from kirigami,
including links to the source code, tips on how to use the
components and links to the corresponding HIG pages and
code examples on invent.


%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%find_lang kirigamigallery --with-qt


%check
# https://github.com/hughsie/appstream-glib/issues/360
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kirigami2.gallery.appdata.xml ||:
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.kirigami2.gallery.desktop


%files -f kirigamigallery.lang
%doc README.md
%license LICENSE.LGPL-2
%{_kf6_bindir}/kirigami2gallery
%{_kf6_datadir}/applications/org.kde.kirigami2.gallery.desktop
%{_kf6_metainfodir}/org.kde.kirigami2.gallery.appdata.xml


%changelog
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

* Sun Jan 07 2024 Alessandro Astone <ales.astone@gmail.com> - 24.01.85-1
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

* Fri Aug 19 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.0-1
- 22.08.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.04.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

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
- update BR's
- make runtime deps archful
- use %%cmake_kf5

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 11 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.04.3-1
- 21.04.3

* Thu Jun 10 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.2-1
- 21.04.2

* Tue May 11 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.1-1
- 21.04.1

* Wed Apr 28 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.0-1
- 21.04.0

* Mon Apr 12 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org>  21.03.90-3
- requirement : breeze-icon-theme added.

* Mon Apr 12 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org>  21.03.90-2
- F35FailsToInstall fix (#1948402)

* Sat Apr 10 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org>  21.03.90-1
- 21.03.90 (#1943793)

* Thu Mar 25 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org>  20.12.3-1
- Initial version of the package

