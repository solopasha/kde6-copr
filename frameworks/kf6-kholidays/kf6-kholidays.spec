%global		framework kholidays

Name:		kf6-%{framework}
Version:	6.0.0
Release:	2%{?dist}
Summary:	The KHolidays Library

License:	BSD-2-Clause AND CC0-1.0 AND GPL-3.0-or-later AND LGPL-2.0-or-later WITH Bison-exception-2.2
URL:		https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:	cmake
BuildRequires:	extra-cmake-modules >= %{version}
BuildRequires:	gcc-c++
BuildRequires:	kf6-rpm-macros

BuildRequires: 	cmake(Qt6Core)
BuildRequires: 	cmake(Qt6Qml)

%description
The KHolidays library provides a C++ API that determines holiday
and other special events for a geographical region.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires: 	cmake(Qt6Core)
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%qch_package

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang_kf6 libkholidays6_qt

%files -f libkholidays6_qt.lang
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6Holidays.so.6
%{_kf6_libdir}/libKF6Holidays.so.%{version}
%{_kf6_qmldir}/org/kde/kholidays/

%files devel
%{_qt6_docdir}/*.tags
%{_kf6_includedir}/KHolidays/
%{_kf6_libdir}/cmake/KF6Holidays/
%{_kf6_libdir}/libKF6Holidays.so

%changelog
* Wed Mar 20 2024 Pavel Solovev <daron439@gmail.com> - 6.0.0-2
- qmlcache rebuild

* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230901.194437.d42ac5f-1
- Initial release
