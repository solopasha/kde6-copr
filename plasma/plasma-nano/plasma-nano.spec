%global orig_name org.kde.plasma.nano

Name:    plasma-nano
Version: 5.92.0
Release: 1%{?dist}
License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later AND MIT
URL:     https://invent.kde.org/plasma/plasma-nano
%plasma_source

Summary: A minimalist Plasma shell for developing custom experiences on embedded devices.

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  libappstream-glib
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  hicolor-icon-theme
BuildRequires:  desktop-file-utils


BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KWayland)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KWinDBusInterface)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Svg)

Requires: kf6-plasma
Requires: kf6-kwayland
Requires: kf6-kwindowsystem
Requires: kf6-kservice
Requires: kf6-kcoreaddons
Requires: kf6-kpackage
Requires: qt6-qtdeclarative


%description
%{Summary}

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang plasma_shell_%{orig_name} --all-name

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.plasma.nano.desktoptoolbox.appdata.xml ||:


%files -f plasma_shell_%{orig_name}.lang
%license LICENSES/*.txt
%doc README.md

%{_kf6_metainfodir}/org.kde.plasma.nano.desktoptoolbox.appdata.xml
%{_kf6_qmldir}/org/kde/plasma/private/nanoshell
%{_kf6_datadir}/plasma/packages/%{orig_name}.desktoptoolbox
%{_kf6_datadir}/plasma/shells/%{orig_name}


%changelog
* Fri Nov 17 2023 Steve Cossette <farchord@gmail.com> - 5.27.80-1
- 5.27.80

* Tue Oct 24 2023 Steve Cossette <farchord@gmail.com> - 5.27.9-1
- 5.27.9

* Tue Sep 12 2023 justin.zobel@gmail.com - 5.27.8-1
- 5.27.8

* Tue Aug 01 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.7-1
- 5.27.7

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.27.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jun 25 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.6-1
- 5.27.6

* Wed May 10 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.5-1
- 5.27.5

* Tue Apr 04 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.4-1
- 5.27.4

* Tue Mar 14 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.3-1
- 5.27.3

* Tue Feb 28 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.2-1
- 5.27.2

* Tue Feb 21 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.1-1
- 5.27.1

* Thu Feb 09 2023 Marc Deop <marcdeop@fedoraproject.org> - 5.27.0-1
- 5.27.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.26.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 19 2023 Marc Deop <marcdeop@fedoraproject.org> - 5.26.90-1
- 5.26.90

* Sat Jan 07 2023 Marc Deop <marcdeop@fedoraproject.org> - 5.26.5-1
- 5.26.5

* Tue Nov 29 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.26.4-1
- 5.26.4

* Wed Nov 09 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.26.3-1
- 5.26.3

* Wed Oct 26 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.26.2-1
- 5.26.2

* Tue Oct 18 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.26.1-1
- 5.26.1

* Thu Oct 06 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.26.0-1
- 5.26.0

* Sat Sep 17 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.25.90-1
- 5.25.90

* Wed Sep 07 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.25.5-1
- 5.25.5

* Wed Aug 31 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 5.25.4-1
- 5.25.4

* Sat Apr 16 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 5.24.4-1
- 5.24.4

* Mon Jan 17 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 5.23.5-1
- Initial version of package

