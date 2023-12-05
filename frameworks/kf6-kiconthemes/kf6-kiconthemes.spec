%global framework kiconthemes

Name:    kf6-%{framework}
Version: 5.246.0
Release: 1.1%{?dist}
Summary: KDE Frameworks 6 Tier 3 integration module with icon themes

License: CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-GPL AND LicenseRef-KDE-Accepted-LGPL
URL:     https://invent.kde.org/frameworks/%{framework}

%frameworks_source

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtsvg-devel

BuildRequires:  cmake(KF6ColorScheme)

BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6UiPlugin)

BuildRequires:  pkgconfig(xkbcommon)

Requires:       hicolor-icon-theme

%description
KDE Frameworks 6 Tier 3 integration module with icon themes

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
%description    devel
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
%find_lang %{name} --all-name

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_bindir}/kiconfinder6
%{_kf6_libdir}/libKF6IconThemes.so.*
%{_kf6_libdir}/libKF6IconWidgets.so.*
%{_kf6_qtplugindir}/iconengines/KIconEnginePlugin.so
%{_kf6_qtplugindir}/designer/*6widgets.so
%{_kf6_libdir}/qt6/qml/org/kde/iconthemes

%files devel
%{_kf6_includedir}/KIconThemes
%{_kf6_includedir}/KIconWidgets
%{_kf6_libdir}/libKF6IconThemes.so
%{_kf6_libdir}/libKF6IconWidgets.so
%{_kf6_libdir}/cmake/KF6IconThemes/

%changelog
* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Tue Oct 17 2023 Jan Grulich <jgrulich@redhat.com> - 5.240.0^20231005.110037.668fdc1-2
- Rebuild (qt6)

* Mon Oct 09 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231005.110037.668fdc1-1
- Initial release
