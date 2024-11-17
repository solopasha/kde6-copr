%global commit0 76fd74a9ab178e32f9443731ed653432f1a333e1
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 2

%global		framework kcalendarcore

Name:		kf6-%{framework}
Version:	6.9.0%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:	1%{?dist}
Summary:	KDE Frameworks 6 Tier 1 KCalendarCore Library
License:	BSD-3-Clause AND LGPL-2.0-or-later AND LGPL-3.0-or-later
URL:		https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:	cmake
BuildRequires:	extra-cmake-modules
BuildRequires:	gcc-c++
BuildRequires:	kf6-rpm-macros
BuildRequires:	libical-devel
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	qt6-qtbase-devel
BuildRequires:  cmake(Qt6Qml)

%description
%{summary}.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = :%{version}-%{release}
Requires:	libical-devel
%description	devel
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

%files
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*kcalendarcore.*
%{_kf6_libdir}/libKF6CalendarCore.so.%{version_no_git}
%{_kf6_libdir}/libKF6CalendarCore.so.6
%{_kf6_qmldir}/org/kde/calendarcore/

%files devel
%{_qt6_docdir}/*.tags
%{_kf6_includedir}/KCalendarCore/
%{_kf6_libdir}/libKF6CalendarCore.so
%{_kf6_libdir}/cmake/KF6CalendarCore/
%{_kf6_libdir}/pkgconfig/KF6CalendarCore.pc

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

* Tue Sep 26 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230829.232751.2905599-1
- Initial release
