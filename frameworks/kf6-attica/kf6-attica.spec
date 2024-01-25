%global commit0 8b5cb3c72a046a895dcd8a025d4ee2a090cb0dd2
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

%global framework attica

Name:           kf6-%{framework}
Version:        6.0.0%{?bumpver:^%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
Summary:        KDE Frameworks Tier 1 Addon with Open Collaboration Services API
License:        CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-LGPL.txt
URL:            https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel

Requires:       kf6-filesystem

%description
Attica is a Qt library that implements the Open Collaboration Services
API version 1.4.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       qt6-qtbase-devel
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
%{_kf6_libdir}/libKF6Attica.so.%{lua: print((macros.version:gsub('[%^~].*', '')))}
%{_kf6_libdir}/libKF6Attica.so.6

%files devel
%{_qt6_docdir}/*.tags
%{_kf6_includedir}/Attica/
%{_kf6_libdir}/cmake/KF6Attica/
%{_kf6_libdir}/libKF6Attica.so
%{_kf6_libdir}/pkgconfig/KF6Attica.pc


%changelog
* Wed Mar 20 2024 Pavel Solovev <daron439@gmail.com> - 6.0.0-2
- qmlcache rebuild

* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Wed Sep 27 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230829.232558.4e09a15-1
- Initial Release
