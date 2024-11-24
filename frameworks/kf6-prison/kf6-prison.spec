%global commit0 6f3d86f0bf4f571cc71ffe2063eed356d8ad979c
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 2

%global framework prison

Name:           kf6-%{framework}
Summary:        KDE Frameworks 6 Tier 1 barcode library
Version:        6.9.0%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
License:        BSD-3-Clause AND CC0-1.0 AND MIT
URL:            https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Quick)

BuildRequires:  cmake(ZXing)
BuildRequires:  pkgconfig(libdmtx)
BuildRequires:  pkgconfig(libqrencode)

Requires:       kf6-filesystem

%description
Prison is a Qt-based barcode abstraction layer/library that provides
an uniform access to generation of barcodes with data.

%package        devel
Summary:        Development files for %{name}
Requires:	    %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Gui)
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

%files
%doc README*
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Prison.so.%{version_no_git}
%{_kf6_libdir}/libKF6Prison.so.6
%{_kf6_libdir}/libKF6PrisonScanner.so.%{version_no_git}
%{_kf6_libdir}/libKF6PrisonScanner.so.6
%{_qt6_qmldir}/org/kde/prison/

%files devel
%{_kf6_includedir}/Prison/
%{_kf6_includedir}/PrisonScanner/
%{_kf6_libdir}/cmake/KF6Prison/
%{_kf6_libdir}/libKF6Prison.so
%{_kf6_libdir}/libKF6PrisonScanner.so
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

* Tue Sep 26 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230925.220236.d99e5a2-1
- Initial release
