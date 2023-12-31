%global		framework kquickcharts

Name:		kf6-%{framework}
Summary:	A QtQuick module providing high-performance charts
Version:	5.247.0
Release:	1%{?dist}

License:	BSD-2-Clause AND CC0-1.0 AND LGPL-2.1-only AND LGPL-3.0-only AND MIT
URL:		https://invent.kde.org/frameworks/%{framework}

%frameworks_meta

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	extra-cmake-modules >= %{version}
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6ShaderTools)

%description
The Quick Charts module provides a set of charts that can be used from QtQuick
applications. They are intended to be used for both simple display of data as
well as continuous display of high-volume data (often referred to as plotters).
The charts use a system called distance fields for their accelerated rendering,
which provides ways of using the GPU for rendering 2D shapes without loss of
quality.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	cmake(Qt6Core)
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

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_qmldir}/org/kde/quickcharts/
%{_libdir}/libQuickCharts.so.*
%{_libdir}/libQuickChartsControls.so*

%files devel
%{_kf6_libdir}/cmake/KF6QuickCharts/
%{_libdir}/libQuickCharts.so
%{_libdir}/libQuickChartsControls.so

%changelog
* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Mon Sep 25 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230906.190341.34bbef0-1
- Initial release
