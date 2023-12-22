%global orig_name kirigami-addons

Name:           kirigami-addons
Version:        0.11.76
Release:        3.5%{?dist}
License:        BSD-2-Clause AND CC-BY-SA-4.0 AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-GPL AND LicenseRef-KDE-Accepted-LGPL AND LicenseRef-KFQF-Accepted-GPL
Summary:        Convergent visual components ("widgets") for Kirigami-based applications
Url:            https://invent.kde.org/libraries/kirigami-addons
Source:         https://invent.kde.org/libraries/%{orig_name}/-/archive/v%{version}/%{orig_name}-v%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Kirigami)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)

Requires:       kf6-kitemmodels

Provides:       kf6-kirigami2-addons
Provides:       kf6-kirigami2-addons%{?_isa}
Provides:       kf6-kirigami2-addons-dateandtime
Provides:       kf6-kirigami2-addons-dateandtime%{?_isa}
Provides:       kf6-kirigami2-addons-treeview
Provides:       kf6-kirigami2-addons-treeview%{?_isa}
Provides:       kf6-kirigami-addons
Provides:       kf6-kirigami-addons%{?_isa}
Provides:       kf6-kirigami-addons-dateandtime
Provides:       kf6-kirigami-addons-dateandtime%{?_isa}
Provides:       kf6-kirigami-addons-treeview
Provides:       kf6-kirigami-addons-treeview%{?_isa}

%description
A set of "widgets" i.e visual end user components along with a
code to support them. Components are usable by both touch and
desktop experiences providing a native experience on both, and
look native with any QQC2 style (qqc2-desktop-theme, Material
or Plasma).


%prep
%autosetup -n %{orig_name}-v%{version}
find ./po -type f -execdir mv {} kirigami-addons6.po \;

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{orig_name}6 --all-name

%files -f %{orig_name}6.lang
%doc README.md
%license LICENSES/*
%{_kf6_qmldir}/org/kde/kirigamiaddons/
%{_kf6_libdir}/cmake/KF6KirigamiAddons/


%changelog
* Fri Aug 18 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:0.11.0-1
- Update to 0.11.0

* Sat Aug 05 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:0.10.0-1
- Update to 0.10.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 19 2023 Marc Deop marcdeop@fedoraproject.org - 1:0.8.0-1
- Update to 0.8.0

* Wed Mar 08 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:0.7.2-1
- Update to 0.7.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 30 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:0.6-1
- 0.6

* Wed Sep 28 2022 Justin Zobel <justin@1707.io> - 0.4-1
- Update to 0.4

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.05-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Jan Grulich <jgrulich@redhat.com> - 21.05-6
- Rebuild (qt5)

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 21.05-5
- Rebuild (qt5)

* Fri Mar 11 2022 Jan Grulich <jgrulich@redhat.com> - 21.05-4
- Rebuild (qt5)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 15 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.05-1
- initial version of package
