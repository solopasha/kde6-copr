%global		framework kitemviews

Name:		kf6-%{framework}
Version:	5.248.0
Release:	1%{?dist}
Summary:	KDE Frameworks 6 Tier 1 addon with item views
License:	CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later
URL:		https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:	fdupes
BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	extra-cmake-modules >= %{version}
BuildRequires:	kf6-rpm-macros
BuildRequires:	qt6-qtbase-devel
BuildRequires:	qt6-qttools-devel

Requires:	kf6-filesystem

%description
KDE Frameworks 6 Tier 1 addon with item views.

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
%find_lang_kf6 kitemviews6_qt
%fdupes LICENSES

%files -f kitemviews6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6ItemViews.so.*
%{_kf6_qtplugindir}/designer/*6widgets.so

%files devel
%{_kf6_includedir}/KItemViews/
%{_kf6_libdir}/cmake/KF6ItemViews/
%{_kf6_libdir}/libKF6ItemViews.so

%changelog
* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Mon Sep 25 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230829.233208.77b6030-1
- Initial Release
