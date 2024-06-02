%global framework networkmanager-qt

Name:           kf6-%{framework}
Version:        6.2.0
Release:        1%{?dist}.1
Summary:        A Tier 1 KDE Frameworks 6 module that wraps NetworkManager DBus API
License:        LGPL-2.0-or-later AND GPL-2.0-only AND GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-GPL AND LicenseRef-KDE-Accepted-LGPL AND CC0-1.0
URL:            https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

# Compile Tools
BuildRequires:  cmake
BuildRequires:  gcc-c++

# KDE Frameworks
BuildRequires:  extra-cmake-modules

# Fedora
Requires:       kf6-filesystem
BuildRequires:  kf6-rpm-macros

# Qt
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Qml)

# Other
BuildRequires:  pkgconfig(libnm)
Recommends:     NetworkManager

%description
A Tier 1 KDE Frameworks 6 Qt library for NetworkManager.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core)
Requires:       pkgconfig(libnm)
%description    devel
Qt libraries and header files for developing applications
that use NetworkManager.


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
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6NetworkManagerQt.so.%{version}
%{_kf6_libdir}/libKF6NetworkManagerQt.so.6
%{_kf6_libdir}/qt6/qml/org/kde/networkmanager/kde-qmlmodule.version
%{_kf6_libdir}/qt6/qml/org/kde/networkmanager/libnetworkmanagerqtqml.so
%{_kf6_libdir}/qt6/qml/org/kde/networkmanager/networkmanagerqtqml.qmltypes
%{_kf6_libdir}/qt6/qml/org/kde/networkmanager/qmldir

%files devel
%{_qt6_docdir}/*.tags
%{_kf6_includedir}/NetworkManagerQt/
%{_kf6_libdir}/libKF6NetworkManagerQt.so
%{_kf6_libdir}/cmake/KF6NetworkManagerQt/

%changelog
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

* Wed Sep 27 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230920.135708.7f4e3a34bbe3c7db7f2d090e1bfc572a21f834a2-135
- Initial Package
