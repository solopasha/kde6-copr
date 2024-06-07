%global framework threadweaver

Name:		kf6-%{framework}
Version:	6.3.0
Release:	1%{?dist}
Summary:	KDE Frameworks 6 Tier 1 addon for advanced thread management
License:	CC0-1.0 AND LGPL-2.0-or-later
URL:		https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:	cmake
BuildRequires:	extra-cmake-modules >= %{version}
BuildRequires:	gcc-c++
BuildRequires:	kf6-rpm-macros

BuildRequires:	qt6-qtbase-devel

Requires:	kf6-filesystem

%description
KDE Frameworks 6 Tier 1 addon for advanced thread management.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	qt6-qtbase-devel
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


%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_libdir}/libKF6ThreadWeaver.so.6
%{_kf6_libdir}/libKF6ThreadWeaver.so.%{version}

%files devel
%{_qt6_docdir}/*.tags
%{_kf6_includedir}/ThreadWeaver/
%{_kf6_libdir}/cmake/KF6ThreadWeaver/
%{_kf6_libdir}/libKF6ThreadWeaver.so


%changelog
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

* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230920.171345.39c665c-1
- Initial release
