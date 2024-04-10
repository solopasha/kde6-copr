%global commit0 1d9dd5f6fa0daac01ecab2313146ed62c225d902
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

%global framework prison

Name:		kf6-%{framework}
Summary:	KDE Frameworks 6 Tier 1 barcode library
Version:	6.3.0%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:	1%{?dist}
License:	BSD-3-Clause AND CC0-1.0 AND MIT
URL:		https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	extra-cmake-modules
BuildRequires:	kf6-rpm-macros
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Quick)
BuildRequires:	pkgconfig(Qt6Multimedia)
BuildRequires:	cmake(ZXing)
BuildRequires:	pkgconfig(libdmtx)
BuildRequires:	pkgconfig(libqrencode)

Requires:	kf6-filesystem

%description
Prison is a Qt-based barcode abstraction layer/library that provides
an uniform access to generation of barcodes with data.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
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
%doc README*
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Prison.so.%{lua: print((macros.version:gsub('[%^~].*', '')))}
%{_kf6_libdir}/libKF6Prison.so.6
%{_kf6_libdir}/libKF6PrisonScanner.so.%{lua: print((macros.version:gsub('[%^~].*', '')))}
%{_kf6_libdir}/libKF6PrisonScanner.so.6
%{_qt6_qmldir}/org/kde/prison/

%files devel
%{_qt6_docdir}/*.tags
%{_kf6_includedir}/Prison/
%{_kf6_includedir}/PrisonScanner/
%{_kf6_libdir}/libKF6Prison.so
%{_kf6_libdir}/libKF6PrisonScanner.so
%{_kf6_libdir}/cmake/KF6Prison/

%changelog
%{?kde_snapshot_changelog_entry}
* Wed Mar 20 2024 Pavel Solovev <daron439@gmail.com> - 6.0.0-2
- qmlcache rebuild

* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Tue Sep 26 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230925.220236.d99e5a2-1
- Initial release
