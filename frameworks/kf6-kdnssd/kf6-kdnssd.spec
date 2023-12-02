%global		framework kdnssd

Name:		kf6-%{framework}
Version:	5.246.0
Release:	1%{?dist}
Summary:	KDE Frameworks 6 Tier 1 integration module for DNS-SD services (Zeroconf)
License:	BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later
URL:		https://invent.kde.org/frameworks/%{framework}
%frameworks_source

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	avahi-devel
BuildRequires:	extra-cmake-modules >= %{version}
BuildRequires:	kf6-rpm-macros
BuildRequires:	qt6-qtbase-devel
BuildRequires:	qt6-qttools-devel

Requires:	nss-mdns
Requires:	kf6-filesystem

%description
KDE Frameworks 6 Tier 1 integration module for DNS-SD services (Zeroconf)

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	qt6-qtbase-devel
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang_kf6 kdnssd6_qt

%files -f kdnssd6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_libdir}/libKF6DNSSD.so.*

%files devel
%{_kf6_includedir}/KDNSSD/
%{_kf6_libdir}/libKF6DNSSD.so
%{_kf6_libdir}/cmake/KF6DNSSD/


%changelog
* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Mon Sep 25 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230829.232959.124d7db-1
- Initial Release
