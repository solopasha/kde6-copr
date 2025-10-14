%global commit0 a4f0711a8879a62c090f5ccd97bf7198682eff0b
%global shortcommit0 %{sub %{commit0} 1 7}
%global bumpver 7

%global framework karchive

Name:           kf6-%{framework}
Version:        6.20.0%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 1 addon with archive functions
License:        LGPL-2.0-or-later AND BSD-2-Clause
URL:            https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  cmake(Qt6Core)

BuildRequires:  bzip2-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  xz-devel
BuildRequires:  zlib-devel

%description
KDE Frameworks 6 Tier 1 addon with archive functions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files -f karchive6_qt.lang
%doc AUTHORS README.md
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6Archive.so.%{version_no_git}
%{_kf6_libdir}/libKF6Archive.so.6

%files devel
%{_kf6_includedir}/KArchive/
%{_kf6_libdir}/cmake/KF6Archive/
%{_kf6_libdir}/libKF6Archive.so

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

* Mon Oct 16 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231014.021837.b24e9b5-1
- Updated to latest git (And shortened the git commit version)

* Fri Sep 22 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.232718.8260e304c367377c16bf564cee43ee13479e66d5-1
- Initial Package
