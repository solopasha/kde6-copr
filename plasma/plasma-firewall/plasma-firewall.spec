%global commit0 e16c4d803d621624c2b0b5795341529ab65f59ad
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1


# Disable ufw for RHEL
%if 0%{?rhel}
%bcond_with ufw
%else
%bcond_without ufw
%endif

Name:    plasma-firewall
Version: 6.2.1
Release: 1%{?dist}
Summary: Control Panel for your system firewall

License: BSD-3-Clause AND CC0-1.0 AND FSFAP AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND LicenseRef-KDE-Accepted-GPL
URL:     https://invent.kde.org/plasma/%{name}
%plasma_source

BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: cmake

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6Auth)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KCMUtils)

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Test)

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

# Owns KCM directories
Requires: kf6-kcmutils%{?_isa}

Requires: %{name}-backend = %{version}-%{release}
Suggests: %{name}-firewalld

%description
%{summary}.

%package firewalld
Summary: FirewallD backend for Plasma Firewall
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-backend = %{version}-%{release}
Conflicts: %{name}-backend
Requires: firewalld

%description firewalld
This package provides the backend code for Plasma Firewall
to interface with FirewallD.

%if %{with ufw}
%package ufw
Summary: UFW backend for Plasma Firewall
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: %{name}-backend = %{version}-%{release}
Conflicts: %{name}-backend
Requires: ufw
# For dbus directories
Requires: dbus-common
# For polkit directories
Requires: polkit

%description ufw
This package provides the backend code for Plasma Firewall
to interface with the Uncomplicated Firewall (UFW).
%endif

%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name --with-html

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml || :
desktop-file-validate %{buildroot}%{_datadir}/applications/kcm_firewall.desktop

%if ! %{with ufw}
# Delete ufw stuff when we don't need it
rm -rfv %{buildroot}%{_qt6_plugindir}/kf6/plasma_firewall/ufwbackend.so
rm -rfv %{buildroot}%{_libexecdir}/kde_ufw_plugin_helper.py
rm -rfv %{buildroot}%{_datadir}/dbus-1/system-services/org.kde.ufw.service
rm -rfv %{buildroot}%{_datadir}/dbus-1/system.d/org.kde.ufw.conf
rm -rfv %{buildroot}%{_datadir}/kcm_ufw/defaults
rm -rfv %{buildroot}%{_datadir}/polkit-1/actions/org.kde.ufw.policy
rm -rfv %{buildroot}%{_kf6_libexecdir}/kauth/kde_ufw_plugin_helper
%endif

%files -f %{name}.lang
%license LICENSES/*.txt
%{_libdir}/libkcm_firewall_core.so
%{_qt6_plugindir}/plasma/kcms/systemsettings/kcm_firewall.so
%dir %{_qt6_plugindir}/kf6/plasma_firewall
%{_datadir}/applications/kcm_firewall.desktop
%{_metainfodir}/org.kde.plasma.firewall.metainfo.xml

%files firewalld
%{_qt6_plugindir}/kf6/plasma_firewall/firewalldbackend.so

%if %{with ufw}
%files ufw
%{_qt6_plugindir}/kf6/plasma_firewall/ufwbackend.so
%{_libexecdir}/kde_ufw_plugin_helper.py
%{_kf6_libexecdir}/kauth/kde_ufw_plugin_helper
%{_datadir}/dbus-1/system-services/org.kde.ufw.service
%{_datadir}/dbus-1/system.d/org.kde.ufw.conf
%dir %{_datadir}/kcm_ufw
%{_datadir}/kcm_ufw/defaults
%{_datadir}/polkit-1/actions/org.kde.ufw.policy
%endif


%changelog
* Tue Oct 15 2024 Pavel Solovev <daron439@gmail.com> - 6.2.1-1
- Update to 6.2.1

* Thu Oct 03 2024 Pavel Solovev <daron439@gmail.com> - 6.2.0-1
- Update to 6.2.0

* Tue Sep 10 2024 Pavel Solovev <daron439@gmail.com> - 6.1.5-1
- Update to 6.1.5

* Tue Aug 06 2024 Pavel Solovev <daron439@gmail.com> - 6.1.4-1
- Update to 6.1.4

* Tue Jul 16 2024 Pavel Solovev <daron439@gmail.com> - 6.1.3-1
- Update to 6.1.3

* Tue Jul 02 2024 Pavel Solovev <daron439@gmail.com> - 6.1.2-1
- Update to 6.1.2

* Tue Jun 25 2024 Pavel Solovev <daron439@gmail.com> - 6.1.1-1
- Update to 6.1.1

* Tue Jun 18 2024 Pavel Solovev <daron439@gmail.com> - 6.1.0-1
- Update to 6.1.0

* Fri May 24 2024 Pavel Solovev <daron439@gmail.com> - 6.0.90-1
- Update to 6.0.90

* Tue May 21 2024 Pavel Solovev <daron439@gmail.com> - 6.0.5-1
- Update to 6.0.5

* Tue Apr 16 2024 Pavel Solovev <daron439@gmail.com> - 6.0.4-1
- Update to 6.0.4

* Tue Mar 26 2024 Pavel Solovev <daron439@gmail.com> - 6.0.3-1
- Update to 6.0.3

* Wed Mar 20 2024 Pavel Solovev <daron439@gmail.com> - 6.0.2-2
- qmlcache rebuild

* Sun Nov 12 2023 Steve Cossette <farchord@gmail.com> - 5.27.80-1
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

* Thu Jan 05 2023 Justin Zobel <justin@1707.io> - 5.26.5-1
- Update to 5.26.5

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

* Wed Aug 03 2022 Justin Zobel <justin@1707.io> - 5.25.4-1
- Update to 5.25.4

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.25.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 12 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.25.3-1
- 5.25.3

* Tue Jun 28 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.25.2-1
- 5.25.2

* Tue Jun 21 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.25.1-1
- 5.25.1

* Thu Jun 09 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.25.0-1
- 5.25.0

* Fri May 20 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.24.90-1
- 5.24.90

* Tue May 03 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.24.5-1
- 5.24.5

* Thu Mar 31 2022 Justin Zobel <justin@1707.io> - 5.24.4-1
- Update to 5.24.4

* Tue Mar 08 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.24.3-1
- 5.24.3

* Tue Feb 22 2022 Rex Dieter <rdieter@fedoraproject.org> - 5.24.2-1
- 5.24.2

* Tue Feb 15 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.24.1-1
- 5.24.1

* Thu Feb 03 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.24.0-1
- 5.24.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.23.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 13 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.23.90-1
- 5.23.90

* Tue Jan 04 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.23.5-1
- 5.23.5

* Tue Dec 14 2021 Marc Deop <marcdeop@fedoraproject.org> - 5.23.4-1
- 5.23.4

* Wed Nov 10 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.23.3-1
- 5.23.3

* Tue Oct 26 2021 Rex Dieter <rdieter@fedoraproject.org> - 5.23.2-1
- 5.23.2

* Sat Oct 23 2021 Marc Deop <marcdeop@fedoraproject.org> - 5.23.1-1
- 5.23.1

* Fri Oct 08 2021 Marc Deop <marcdeop@fedoraproject.org> - 5.23.0-1
- 5.23.0

* Fri Sep 17 2021 Marc Deop <marcdeop@fedoraproject.org> - 5.22.90-1
- 5.22.90

* Tue Aug 31 2021 Jan Grulich <jgrulich@redhat.com> - 5.22.5-1
- 5.22.5

* Tue Jul 27 2021 Jan Grulich <jgrulich@redhat.com> - 5.22.4-1
- 5.22.4

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.22.3-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 12 2021 Jan Grulich <jgrulich@redhat.com> - 5.22.3-1
- 5.22.3

* Tue Jun 22 2021 Jan Grulich <jgrulich@redhat.com> - 5.22.2.1-1
- 5.22.2.1

* Tue Jun 22 2021 Jan Grulich <jgrulich@redhat.com> - 5.22.2-1
- 5.22.2

* Tue Jun 15 2021 Jan Grulich <jgrulich@redhat.com> - 5.22.1-1
- 5.22.1

* Sun Jun 06 2021 Jan Grulich <jgrulich@redhat.com> - 5.22.0-1
- 5.22.0

* Tue May 04 2021 Jan Grulich <jgrulich@redhat.com> - 5.21.5-1
- 5.21.5

* Tue Apr 06 2021 Jan Grulich <jgrulich@redhat.com> - 5.21.4-1
- 5.21.4

* Tue Mar 16 2021 Jan Grulich <jgrulich@redhat.com> - 5.21.3-1
- 5.21.3

* Tue Mar 02 2021 Jan Grulich <jgrulich@redhat.com> - 5.21.2-1
- 5.21.2

* Tue Feb 23 2021 Jan Grulich <jgrulich@redhat.com> - 5.21.1-1
- 5.21.1

* Thu Feb 11 2021 Jan Grulich <jgrulich@redhat.com> - 5.21.0-1
- 5.21.0

* Fri Jan 29 2021 Neal Gompa <ngompa13@gmail.com> - 5.20.90-4
- Subpackage firewall backends
- Ensure directory ownership is correct

* Thu Jan 28 2021 Marc Deop <marcdeop@fedoraproject.org> - 5.20.90-3
- Add BuildRequires for gcc-c++, make and cmake

* Wed Jan 27 2021 Marc Deop <marcdeop@fedoraproject.org> - 5.20.90-2
- Fix License

* Wed Jan 27 2021 Marc Deop <marcdeop@fedoraproject.org> - 5.20.90-1
- 5.20.90 (beta)
