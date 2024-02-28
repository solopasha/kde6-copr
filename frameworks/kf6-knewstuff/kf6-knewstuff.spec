%global framework knewstuff

Name:    kf6-%{framework}
Version: 6.0.0
Release: 1%{?dist}
Summary: KDE Frameworks 6 Tier 3 module for downloading application assets
License: BSD-2-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-GPL AND LicenseRef-KDE-Accepted-LGPL
URL:     https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Attica)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6Syndication)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6Package)

BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel

Requires:  kf6-filesystem

%description
KDE Frameworks 6 Tier 3 module for downloading and sharing additional
application data like plugins, themes, motives, etc.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6Attica)
Requires:       cmake(KF6CoreAddons)
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
%find_lang %{name} --all-name

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_bindir}/knewstuff*
%{_kf6_datadir}/applications/org.kde.knewstuff-dialog6.desktop
%{_kf6_datadir}/qlogging-categories6/%{framework}*
%{_kf6_libdir}/libKF6NewStuffCore.so.6
%{_kf6_libdir}/libKF6NewStuffCore.so.%{version}
%{_kf6_libdir}/libKF6NewStuffWidgets.so.6
%{_kf6_libdir}/libKF6NewStuffWidgets.so.%{version}
%{_kf6_qmldir}/org/kde/newstuff/

%files devel
%{_qt6_docdir}/*.tags
%{_kf6_includedir}/KNewStuff/
%{_kf6_includedir}/KNewStuffCore/
%{_kf6_includedir}/KNewStuffWidgets/
%{_kf6_libdir}/cmake/KF6NewStuff/
%{_kf6_libdir}/cmake/KF6NewStuffCore/
%{_kf6_libdir}/libKF6NewStuffCore.so
%{_kf6_libdir}/libKF6NewStuffWidgets.so
%{_kf6_libdir}/qt6/plugins/designer/knewstuff6widgets.so


%changelog
* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Tue Oct 17 2023 Jan Grulich <jgrulich@redhat.com> - 5.240.0^20231011.024051.03d9e05-2
- Rebuild (qt6)

* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231011.024051.03d9e05-1
- Initial release
