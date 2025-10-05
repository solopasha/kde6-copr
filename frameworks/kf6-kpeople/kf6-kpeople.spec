%global commit0 4be7be0a8c8a9728ce686abad37ef7e9b0384a6e
%global shortcommit0 %{sub %{commit0} 1 7}
%global bumpver 1

%global framework kpeople

Name:           kf6-%{framework}
Version:        6.20.0%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 3 library for contact and people aggregation

License:        CC0-1.0 AND LGPL-2.1-or-later
URL:            https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6WidgetsAddons)

BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Widgets)

%description
KDE Frameworks 6 Tier 3 library for interaction with XML RPC services.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core)
Requires:       cmake(Qt6Widgets)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6People.so.%{version_no_git}
%{_kf6_libdir}/libKF6People.so.6
%{_kf6_libdir}/libKF6PeopleBackend.so.%{version_no_git}
%{_kf6_libdir}/libKF6PeopleBackend.so.6
%{_kf6_libdir}/libKF6PeopleWidgets.so.%{version_no_git}
%{_kf6_libdir}/libKF6PeopleWidgets.so.6
%{_kf6_qmldir}/org/kde/people/
%{_qt6_plugindir}/kpeople/datasource/KPeopleVCard.so

%files devel
%{_kf6_includedir}/KPeople/
%{_kf6_libdir}/cmake/KF6People/
%{_kf6_libdir}/libKF6People.so
%{_kf6_libdir}/libKF6PeopleBackend.so
%{_kf6_libdir}/libKF6PeopleWidgets.so

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

* Mon Oct 09 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231003.021019.6f4b1b4c-1
- Initial release
