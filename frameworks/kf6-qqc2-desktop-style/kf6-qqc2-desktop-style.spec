%global framework qqc2-desktop-style

Name:    kf6-%{framework}
Version: 5.246.0
Release: 1%{?dist}
Summary: QtQuickControls2 style for consistency between QWidget and QML apps 
License: CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only AND LicenseRef-KFQF-Accepted-GPL
URL:     https://invent.kde.org/frameworks/%{framework}
%frameworks_source

BuildRequires: extra-cmake-modules >= %{version}
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6ColorScheme)
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6Quick)
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: cmake(KF6Sonnet)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: qt6-qtbase-private-devel

Requires:      kf6-kirigami2

%description
This is a style for QtQuickControls 2 that uses QWidget's QStyle for
painting, making possible to achieve an higher degree of consistency
between QWidget-based and QML-based apps.


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
%{_kf6_libdir}/cmake/KF6QQC2DesktopStyle/
%{_qt6_qmldir}/org/kde/desktop/
%{_qt6_qmldir}/org/kde/qqc2desktopstyle/
%{_kf6_plugindir}/kirigami/platform/org.kde.desktop.so

%changelog
* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Tue Oct 17 2023 Jan Grulich <jgrulich@redhat.com> - 5.240.0^20231010.095318.b5f1e25-2
- Rebuild (qt6)

* Mon Oct 09 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231010.095318.b5f1e25-1
- Initial Import
