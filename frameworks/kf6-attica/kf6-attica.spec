%global commit0 c1980d615a99dce67c8e8e5747ec98ad011ed1d9
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 2

%global framework attica

Name:           kf6-%{framework}
Version:        6.9.0%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
Summary:        Open Collaboration Service client library
License:        CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-LGPL.txt
URL:            https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)

Requires:       kf6-filesystem

%description
Attica is a Qt library that implements the Open Collaboration Services API
version 1.6.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       cmake(Qt6Core)
Requires:       cmake(Qt6Network)
%description    devel
%{summary}.

%qch_package

%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%files
%doc AUTHORS ChangeLog README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Attica.so.%{version_no_git}
%{_kf6_libdir}/libKF6Attica.so.6

%files devel
%{_kf6_includedir}/Attica/
%{_kf6_libdir}/cmake/KF6Attica/
%{_kf6_libdir}/libKF6Attica.so
%{_kf6_libdir}/pkgconfig/KF6Attica.pc
%{_qt6_docdir}/*.tags

%changelog
%{?kde_snapshot_changelog_entry}
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

* Wed Sep 27 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230829.232558.4e09a15-1
- Initial Release
