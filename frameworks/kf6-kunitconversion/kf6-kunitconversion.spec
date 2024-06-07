%global framework kunitconversion

Name:    kf6-%{framework}
Version: 6.3.0
Release: 1%{?dist}
Summary: KDE Frameworks 6 Tier 2 addon for unit conversions

License: CC0-1.0 AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(KF6I18n)
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel

Requires:  kf6-filesystem

%description
KDE Frameworks 6 Tier 2 addon for unit conversions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
%description    devel
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
%find_lang %{name} --all-name --with-man

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_libdir}/libKF6UnitConversion.so.6
%{_kf6_libdir}/libKF6UnitConversion.so.%{version}
%{_kf6_datadir}/qlogging-categories6/%{framework}.*

%files devel
%{_qt6_docdir}/*.tags
%{_kf6_includedir}/KUnitConversion/
%{_kf6_libdir}/libKF6UnitConversion.so
%{_kf6_libdir}/cmake/KF6UnitConversion/

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

* Tue Oct 03 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231001.122451.d7e3a49-1
- Initial Release
