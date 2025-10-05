%global commit0 dc25509afc119fbd139ab23a1c000b745541d84c
%global shortcommit0 %{sub %{commit0} 1 7}
%global bumpver 1

%global framework purpose

Name:           kf6-purpose
Summary:        Framework for providing abstractions to get the developer's purposes fulfilled
Version:        6.20.0%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}

License:        CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Prison)
BuildRequires:  cmake(KF6Declarative)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  accounts-qml-module-qt6
BuildRequires:  cmake(KAccounts6)
BuildRequires:  intltool

Requires:       accounts-qml-module-qt6%{?_isa}
Requires:       kf6-bluez-qt%{?_isa}
Requires:       kf6-kcmutils%{?_isa}
Requires:       kf6-kirigami%{?_isa}
Requires:       kf6-kitemmodels%{?_isa}
Requires:       kf6-prison%{?_isa}

Requires:       hicolor-icon-theme

%description
Purpose offers the possibility to create integrate services and actions on
any application without having to implement them specifically. Purpose will
offer them mechanisms to list the different alternatives to execute given the
requested action type and will facilitate components so that all the plugins
can receive all the information they need.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6CoreAddons)
%description    devel
%{summary}.

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/accounts/services/kde/google-youtube.service
%{_kf6_datadir}/accounts/services/kde/nextcloud-upload.service
%{_kf6_datadir}/icons/hicolor/*/apps/*-purpose6.*
%{_kf6_datadir}/kf6/purpose/
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Purpose.so.%{version_no_git}
%{_kf6_libdir}/libKF6Purpose.so.6
%{_kf6_libdir}/libKF6PurposeWidgets.so.%{version_no_git}
%{_kf6_libdir}/libKF6PurposeWidgets.so.6
%{_kf6_libexecdir}/purposeprocess
%dir %{_kf6_plugindir}/kfileitemaction
%{_kf6_plugindir}/kfileitemaction/sharefileitemaction.so
%{_kf6_plugindir}/purpose/
%{_kf6_qmldir}/org/kde/purpose/

%files devel
%{_kf6_includedir}/Purpose/
%{_kf6_includedir}/PurposeWidgets/
%{_kf6_libdir}/cmake/KF6Purpose/
%{_kf6_libdir}/libKF6Purpose.so
%{_kf6_libdir}/libKF6PurposeWidgets.so

%changelog
%{?kde_snapshot_changelog_entry}
* Fri Jan 03 2025 Pavel Solovev <daron439@gmail.com> - 6.10.0-1
- Update to 6.10.0

* Fri Dec 06 2024 Pavel Solovev <daron439@gmail.com> - 6.9.0-1
- Update to 6.9.0

* Sat Nov 02 2024 Pavel Solovev <daron439@gmail.com> - 6.8.0-1
- Update to 6.8.0

* Fri Oct 04 2024 Pavel Solovev <daron439@gmail.com> - 6.7.0-1
- Update to 6.7.0

* Fri Sep 06 2024 Pavel Solovev <daron439@gmail.com> - 6.6.0-1
- Update to 6.6.0

* Fri Aug 09 2024 Pavel Solovev <daron439@gmail.com> - 6.5.0-1
- Update to 6.5.0

* Fri Jul 12 2024 Pavel Solovev <daron439@gmail.com> - 6.4.0-1
- Update to 6.4.0

* Fri Jun 07 2024 Pavel Solovev <daron439@gmail.com> - 6.3.0-1
- Update to 6.3.0

* Sun Jun 02 2024 Pavel Solovev <daron439@gmail.com> - 6.2.0-1.1
- rebuild for f40

* Sun May 12 2024 Pavel Solovev <daron439@gmail.com> - 6.2.0-1
- Update to 6.2.0

* Fri Apr 12 2024 Pavel Solovev <daron439@gmail.com> - 6.1.0-1
- Update to 6.1.0

* Wed Mar 20 2024 Pavel Solovev <daron439@gmail.com> - 6.0.0-2
- qmlcache rebuild

* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231011.004242.c0f1138-1
- Initial release
