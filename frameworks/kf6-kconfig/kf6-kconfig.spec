%global commit0 2447c7c4eea625288bc94f83d46abd44f474b89e
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

%global		framework kconfig


Name:		  kf6-%{framework}
Version:	6.7.0
Release:	1%{?dist}
Summary:	KDE Frameworks 6 Tier 1 addon with advanced configuration system
License:	BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND MIT
URL:		  https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:	cmake
BuildRequires:	extra-cmake-modules
BuildRequires:	gcc-c++
BuildRequires:	kf6-rpm-macros
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Xml)

Requires:	kf6-filesystem

%description
KDE Frameworks 6 Tier 1 addon with advanced configuration system made of two
parts: KConfigCore and KConfigGui.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	cmake(Qt6DBus)
Requires:	cmake(Qt6Qml)
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
%find_lang_kf6 kconfig6_qt

%files -f kconfig6_qt.lang
%doc DESIGN README.md TODO
%license LICENSES/*.txt
%{_kf6_bindir}/kreadconfig6
%{_kf6_bindir}/kwriteconfig6
%{_kf6_datadir}/qlogging-categories6/%{framework}*
%{_kf6_libdir}/libKF6ConfigCore.so.%{version_no_git}
%{_kf6_libdir}/libKF6ConfigCore.so.6
%{_kf6_libdir}/libKF6ConfigGui.so.%{version_no_git}
%{_kf6_libdir}/libKF6ConfigGui.so.6
%{_kf6_libdir}/libKF6ConfigQml.so.%{version_no_git}
%{_kf6_libdir}/libKF6ConfigQml.so.6
%{_kf6_libdir}/qt6/qml/org/kde/config/
%{_kf6_libexecdir}/kconf_update
%{_kf6_libexecdir}/kconfig_compiler_kf6

%files devel
%{_qt6_docdir}/*.tags
%{_kf6_includedir}/KConfig/
%{_kf6_includedir}/KConfigCore/
%{_kf6_includedir}/KConfigGui/
%{_kf6_includedir}/KConfigQml/
%{_kf6_libdir}/cmake/KF6Config/
%{_kf6_libdir}/libKF6ConfigCore.so
%{_kf6_libdir}/libKF6ConfigGui.so
%{_kf6_libdir}/libKF6ConfigQml.so

%changelog
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

* Mon Oct 16 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231016.020925.5cd23ad-1
- Updated git version and prettied up the version string

* Wed Sep 27 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230925.220329.8ff33136df67fddc9dd5bd979acf81592bfe4f98-1
- Initial Package
