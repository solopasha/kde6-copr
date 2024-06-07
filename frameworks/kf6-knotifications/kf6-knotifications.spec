%global framework knotifications

Name:    kf6-%{framework}
Version: 6.3.0
Release: 1%{?dist}
Summary: KDE Frameworks 6 Tier 2 solution with abstraction for system notifications

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-LGPL
URL:     https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(KF6Config)

BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)

BuildRequires:  pkgconfig(libcanberra)

%description
KDE Frameworks 6 Tier 3 solution with abstraction for system
notifications.

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
%find_lang_kf6 knotifications6_qt
# We own the folder
mkdir -p %{buildroot}/%{_kf6_datadir}/knotifications6

%files -f knotifications6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Notifications.so.6
%{_kf6_libdir}/libKF6Notifications.so.%{version}
%{_kf6_qmldir}/org/kde/notification/
%dir %{_kf6_datadir}/knotifications6

%files devel
%{_qt6_docdir}/*.tags
%{_kf6_includedir}/KNotifications/
%{_kf6_libdir}/cmake/KF6Notifications/
%{_kf6_libdir}/libKF6Notifications.so

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

* Tue Oct 03 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231001.134620.703d04f-1
- Initial Release
