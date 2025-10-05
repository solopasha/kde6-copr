%global commit0 f136f3e561e6a607c205f242db52134aa1513e5d
%global shortcommit0 %{sub %{commit0} 1 7}
%global bumpver 1

%global framework kglobalaccel

Name:           kf6-%{framework}
Version:        6.20.0%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 3 integration module for global shortcuts

# The following are in the LICENSES folder but go unused: LGPL-2.1-only, LGPL-3.0-only, LicenseRef-KDE-Accepted-LGPL
License:        CC0-1.0 AND LGPL-2.0-or-later
URL:            https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  qt6-qtbase-private-devel

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       cmake(Qt6DBus)
Requires:       cmake(Qt6Widgets)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files -f kglobalaccel6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}*
%{_kf6_libdir}/libKF6GlobalAccel.so.%{version_no_git}
%{_kf6_libdir}/libKF6GlobalAccel.so.6

%files devel
%{_kf6_datadir}/dbus-1/interfaces/*
%{_kf6_includedir}/KGlobalAccel/
%{_kf6_libdir}/cmake/KF6GlobalAccel/
%{_kf6_libdir}/libKF6GlobalAccel.so

%changelog
%{?kde_snapshot_changelog_entry}
* Fri Jan 03 2025 Pavel Solovev <daron439@gmail.com> - 6.10.0-1
- Update to 6.10.0

* Fri Dec 06 2024 Pavel Solovev <daron439@gmail.com> - 6.9.0-1
- Update to 6.9.0

* Mon Dec 02 2024 Pavel Solovev <daron439@gmail.com> - 6.8.0-2
- Remove Qt6 version constraints

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

* Tue Oct 17 2023 Jan Grulich <jgrulich@redhat.com> - 5.240.0^20231003.060644.9b93514-3
- Rebuild (qt6)

* Mon Oct 09 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231003.060644.9b93514-2
- Removed -libs from the required installs at runtime (Unneeded)

* Tue Oct 03 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231003.060644.9b93514-1
- Initial Release
