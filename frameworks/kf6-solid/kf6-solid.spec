%global commit0 e0149417e45894a1a70982917144e47b611cbac9
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 3

%global _default_patch_fuzz 2

%global framework solid

Name:           kf6-%{framework}
Version:        6.9.0%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 1 integration module that provides hardware information
License:        LGPL-2.1-or-later AND LGPL-2.1-only AND CCO-1.0 AND BSD-3-Clause AND LGPL-3.0-only
URL:            https://invent.kde.org/frameworks/solid
%frameworks_meta

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Tools)
BuildRequires:  pkgconfig(libplist-2.0)
BuildRequires:  pkgconfig(libimobiledevice-1.0)
BuildRequires:  pkgconfig(mount)
BuildRequires:  libupnp-devel
BuildRequires:  systemd-devel
BuildRequires:  flex
BuildRequires:  bison
Recommends:     media-player-info
Recommends:     udisks2
Recommends:     upower

Requires:       kf6-filesystem

%description
Solid provides the following features for application developers:
 - Hardware Discovery
 - Power Management
 - Network Management

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%qch_package

%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang_kf6 solid6_qt

%files -f solid6_qt.lang
%doc README.md TODO
%license LICENSES/*.txt
%{_kf6_bindir}/solid-hardware6
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Solid.so.%{version_no_git}
%{_kf6_libdir}/libKF6Solid.so.6

%files devel
%{_qt6_docdir}/*.tags
%{_kf6_includedir}/Solid/
%{_kf6_libdir}/cmake/KF6Solid/
%{_kf6_libdir}/libKF6Solid.so

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

* Tue Sep 19 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230911.192300.eaebf4a-1
- Initial Package
