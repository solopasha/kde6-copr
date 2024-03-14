Name:          kde-inotify-survey
Version:       24.02.1
Release:       1%{?dist}
Summary:       Monitors inotify limits and lets the user know when exceeded

# Complete license breakdown can be found in the "LICENSE-BREAKDOWN" file
License:       BSD-3-Clause and CC0-1.0 and FSFAP and GPL-2.0-only and GPL-3.0-only
URL:           https://invent.kde.org/system/%{name}
%apps_source


Requires:      kf6-kded
Requires:      dbus-common
Requires:      polkit
BuildRequires: kf6-rpm-macros
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gettext
BuildRequires: qt6-qtbase-devel
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6Auth)

%description
%{summary}.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build


%install
%cmake_install
%find_lang %{name} --with-kde --with-man --all-name

%files -f %{name}.lang
%license LICENSES/* screenshot.png.license
%doc README.md screenshot.png
%{_bindir}/kde-inotify-survey
%{_kf6_plugindir}/kded/inotify.so
%{_kf6_libexecdir}/kauth/kded-inotify-helper
%{_datadir}/dbus-1/system-services/org.kde.kded.inotify.service
%{_datadir}/dbus-1/system.d/org.kde.kded.inotify.conf
%{_datadir}/knotifications6/org.kde.kded.inotify.notifyrc
%{_datadir}/metainfo/org.kde.inotify-survey.metainfo.xml
%{_datadir}/polkit-1/actions/org.kde.kded.inotify.policy

%changelog
* Thu Mar 21 2024 Pavel Solovev <daron439@gmail.com> - 24.02.1-1
- Update to 24.02.1

* Sun Nov 19 2023 Steve Cossette <farchord@gmail.com> - 24.01.75-1
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

* Thu Jun 8 2023 Steve Cossette <farchord@gmail.com> - 23.04.2-3
- Update to 23.04.2
- Fixed changelog mistake

* Mon May 29 2023 Steve Cossette <farchord@gmail.com> - 23.04.1-1
- Initial release
