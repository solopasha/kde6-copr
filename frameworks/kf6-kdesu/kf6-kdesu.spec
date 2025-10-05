%global commit0 0971f9c8d5ab014afb7efa74bf7155ba5b2d408c
%global shortcommit0 %{sub %{commit0} 1 7}
%global bumpver 1

%global framework kdesu

Name:           kf6-%{framework}
Version:        6.20.0%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
Summary:        User interface for running shell commands with root privileges

License:        CC0-1.0 AND GPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-LGPL
URL:            https://invent.kde.org/frameworks/%{framework}
%frameworks_meta
BuildOption: -DKDESU_USE_SUDO_DEFAULT:BOOL=TRUE

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Pty)

BuildRequires:  cmake(Qt6Core)

BuildRequires:  pkgconfig(x11)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6Pty)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/ksu.categories
%{_kf6_libdir}/libKF6Su.so.%{version_no_git}
%{_kf6_libdir}/libKF6Su.so.6
%{_kf6_libexecdir}/kdesu_stub
%{_kf6_libexecdir}/kdesud

%files devel
%{_kf6_includedir}/KDESu/
%{_kf6_libdir}/cmake/KF6Su/
%{_kf6_libdir}/libKF6Su.so

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

* Wed Sep 27 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231001.121632.8b7a35c-1
- Initial Release
