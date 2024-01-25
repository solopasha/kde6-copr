%global klockd_name org.kde.kclockd
%global orig_name org.kde.kclock

Name:           kclock
Version:        24.01.95
Release:        1%{?dist}
License:        GPLv2+ and LGPLv2.1+ and CC-BY and GPLv3+
Summary:        Clock app for Plasma Mobile
URL:            https://apps.kde.org/kclock/
%apps_source

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6KirigamiAddons)

BuildRequires:  cmake(Plasma)

Requires:       hicolor-icon-theme
# QML module dependencies
Requires:       kf6-kcoreaddons%{?_isa}
Requires:       kf6-kirigami%{?_isa}
Requires:       kf6-kirigami-addons%{?_isa}
Requires:       kf6-ksvg%{?_isa}
Requires:       qt6-qtmultimedia%{?_isa}


%description
A convergent clock application for Plasma.


%package plasma-applet
Summary:        Plasma applet for kclock
Requires:       %{name}%{?_isa} = %{version}-%{release}
# QML module dependencies
Requires:       kf6-kcmutils%{?_isa}
Requires:       kf6-kirigami%{?_isa}
Requires:       libplasma%{?_isa}

%description plasma-applet
%{summary}.


%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -p1


%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop


%files -f %{name}.lang
%doc README.md
%license LICENSES/*
%{_kf6_bindir}/%{name}
%{_kf6_bindir}/%{name}d
%{_kf6_datadir}/applications/%{orig_name}.desktop
%{_kf6_datadir}/dbus-1/interfaces/*.xml
%{_kf6_datadir}/dbus-1/services/org.kde.%{name}d.service
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.%{name}.svg
%{_kf6_datadir}/knotifications6/%{name}d.notifyrc
%{_kf6_metainfodir}/%{orig_name}.appdata.xml
%{_kf6_sysconfdir}/xdg/autostart/%{klockd_name}-autostart.desktop

%files plasma-applet
%{_kf6_datadir}/icons/hicolor/scalable/apps/%{name}_plasmoid_1x2.svg
%{_kf6_datadir}/plasma/plasmoids/org.kde.plasma.%{name}_1x2/
%{_kf6_metainfodir}/org.kde.plasma.%{name}_1x2.appdata.xml
%{_qt6_plugindir}/plasma/applets/org.kde.plasma.%{name}_1x2.so


%changelog
* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90

* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Mon Dec 04 2023 Yaakov Selkowitz <yselkowitz@fedoraproject.org> - 24.01.80-1
- 24.01.80

* Thu Oct 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.2-1
- 23.08.2

* Tue Oct 10 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 23.08.1-1
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

* Thu Apr 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.0-1
- 23.04.0

* Fri Mar 31 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.90-1
- 23.03.90

* Mon Mar 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.80-1
- 23.03.80

* Mon Jan 30 2023 Justin Zobel <justin@1707.io> - 23.01.0-1
- Update to 23.01.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 01 2022 Justin Zobel <justin@1707.io> - 22.11-1
- Update to 22.11

* Wed Sep 28 2022 Justin Zobel <justin@1707.io> - 22.09-1
- Update to 22.09

* Thu Aug 25 2022 Justin Zobel <justin@1707.io> - 22.06-1
- Update to 22.06

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 10 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 22.02-1
- Plasma mobile version 22.02

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 16 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.12-1
- 21.12

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jun 13 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.06-1
- version update : 21.06

* Sun Jun 06 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.05-2
- BR: appstream added

* Sat May 15 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.05-1
- initial version of package
