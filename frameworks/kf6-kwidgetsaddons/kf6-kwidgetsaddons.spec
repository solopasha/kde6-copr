%global		framework kwidgetsaddons

Name:		kf6-%{framework}
Version:	5.247.0
Release:	1%{?dist}
Summary:	KDE Frameworks 6 Tier 1 addon with various classes on top of QtWidgets
License:	BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND LGPL-3.0-or-later
URL:		https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:	cmake
BuildRequires:	extra-cmake-modules >= %{version}
BuildRequires:	fdupes
BuildRequires:	gcc-c++
BuildRequires:	kf6-rpm-macros

BuildRequires:	cmake(Qt6Widgets)

Requires:	kf6-filesystem

%description
KDE Frameworks 6 Tier 1 addon with various classes on top of QtWidgets.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	cmake(Qt6Widgets)
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
%find_lang_kf6 kwidgetsaddons6_qt
%fdupes %{buildroot}/%{_kf6_includedir}/KWidgetsAddons/
%fdupes LICENSES

%files -f kwidgetsaddons6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/kf6/kcharselect/
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6WidgetsAddons.so.*
%{_kf6_qtplugindir}/designer/*6widgets.so

%files devel
%{_kf6_includedir}/KWidgetsAddons/
%{_kf6_libdir}/cmake/KF6WidgetsAddons/
%{_kf6_libdir}/libKF6WidgetsAddons.so

%changelog
* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Sun Sep 24 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230917.131236.de81f37-1
- Initial release
