%global commit0 ccdab74966a63ced83d7ac76aff60a88c82ea421
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

%global framework kauth

Name:    kf6-%{framework}
Version: 6.9.0%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release: 1%{?dist}
Summary: KDE Frameworks 6 module to perform actions as privileged user
# LGPL-2.0-or-later is also in the project's LICENSES, but is unused according to reuse.
License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.1-or-later
URL:     https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  kf6-rpm-macros
BuildRequires:  polkit-qt6-1-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6WindowSystem)

Requires:  kf6-filesystem

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6CoreAddons)
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
%find_lang_kf6 kauth6_qt

%files -f kauth6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/dbus-1/system.d/org.kde.kf6auth.conf
%{_kf6_datadir}/kf6/kauth/
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6AuthCore.so.%{version_no_git}
%{_kf6_libdir}/libKF6AuthCore.so.6
%{_kf6_qtplugindir}/kf6/kauth/

%files devel
%{_qt6_docdir}/*.tags
%{_kf6_includedir}/KAuth/
%{_kf6_includedir}/KAuthCore/
%{_kf6_libdir}/cmake/KF6Auth/
%{_kf6_libdir}/libKF6AuthCore.so
%{_kf6_libexecdir}/kauth/

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

* Tue Oct 03 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231003.060844.0b37b02-1
- Initial Release
