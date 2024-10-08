%global commit0 5e97db1d03ec93bb0602d39ecfeb0e370fd00122
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

Name:           alligator
Version:        24.08.2
Release:        1%{?dist}
License:        GPLv2 or GPLv3
Summary:        Kirigami-based RSS reader
URL:            https://invent.kde.org/plasma-mobile/alligator
%apps_source

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6Syndication)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Test)

Requires:       hicolor-icon-theme
# QML module dependencies
Requires:       kf6-kirigami2%{?_isa}
Requires:       kf6-kirigami-addons%{?_isa}

%description
Alligator is a convergent RSS/Atom feed reader.

%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml


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

* Wed Mar 20 2024 Pavel Solovev <daron439@gmail.com> - 24.02.0-2
- qmlcache rebuild

* Thu Oct 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.2-1
- 23.08.2

* Sat Sep 16 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.1-1
- 23.08.1

* Sat Aug 26 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.0-1
- 23.08.0

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.3-1
- 23.04.3

* Tue Jun 06 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.2-1
- 23.04.2

* Sat May 13 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.1-1
- 23.04.1

* Thu Apr 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.0-1
- 23.04.0

* Fri Mar 31 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.90-1
- 23.03.90

* Mon Mar 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.80-1
- 23.03.80

* Mon Jan 30 2023 Justin Zobel <justin@1707.io> - 23.01.0-1
- Update to 23.01.0

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 01 2022 Justin Zobel <justin@1707.io> - 22.11-1
- Update to 22.11

* Wed Sep 28 2022 Justin Zobel <justin@1707.io> - 22.09-1
- Update to 22.09

* Thu Aug 25 2022 Justin Zobel <justin@1707.io> - 22.06-1
- Update to 22.06

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 10 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 22.02-1
- Plasma mobile version 22.02

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 16 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.12-1
- 21.12

* Sun Sep 12 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.08-2
- Source1 removed

* Sun Sep 12 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.08-1
- 21.08

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jul 16 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.06-1
- 21.06

* Sat May 22 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.05-2
- License section fixed

* Sun May 16 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.05-1
- initial version of package

