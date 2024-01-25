%global kf6_min_version 5.240.0

Name:           kasts
Version:        24.01.95
Release:        1%{?dist}
License:        GPLv2 and GPLv2+ and GPLv3+ and BSD and LGPLv3+
Summary:        A mobile podcast application
Url:            https://apps.kde.org/%{name}
%apps_source

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  taglib-devel
BuildRequires:  pkgconfig(libvlc)
BuildRequires:  pkgconfig(gstreamer-1.0)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Multimedia)

BuildRequires:  cmake(KF6I18n)           >= %{kf6_min_version}
BuildRequires:  cmake(KF6CoreAddons)     >= %{kf6_min_version}
BuildRequires:  cmake(KF6Kirigami)      >= %{kf6_min_version}
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6Syndication)    >= %{kf6_min_version}
BuildRequires:  cmake(KF6Config)         >= %{kf6_min_version}
BuildRequires:  cmake(KF6ThreadWeaver)   >= %{kf6_min_version}
BuildRequires:  cmake(KF6ColorScheme)    >= %{kf6_min_version}
BuildRequires:  kf6-rpm-macros           >= %{kf6_min_version}

# QML module dependencies
Requires:  kf6-kirigami2%{?_isa}
Requires:  kf6-kirigami-addons%{?_isa}
Requires:  qt6-qt5compat%{?_isa}
Requires:  qt6-qtmultimedia%{?_isa}

%description
%{summary}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml

%files -f %{name}.lang
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/scalable/actions/media-playback-cloud.svg
%{_kf6_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_kf6_datadir}/icons/hicolor/scalable/apps/%{name}-tray-dark.svg
%{_kf6_datadir}/icons/hicolor/scalable/apps/%{name}-tray-light.svg
%{_kf6_libdir}/libKMediaSession.so
%{_kf6_qmldir}/org/kde/kmediasession/libkmediasession-qmlplugin.so
%{_kf6_qmldir}/org/kde/kmediasession/qmldir
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%license LICENSES/*


%changelog
* Mon Nov 27 2023 Yaakov Selkowitz <yselkowitz@fedoraproject.org> - 24.01.75-1
- 24.01.75

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

* Wed Sep 28 2022 Justin Zobel <justin@1707.io> - 22.09.2-1
- Update to 22.09.2

* Thu Aug 25 2022 Justin Zobel <justin@1707.io> - 22.06-1
- Update to 22.06

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Apr 19 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 22.02-1
- Update to 22.02

* Sun Jan 16 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.12-1
- Initial package
