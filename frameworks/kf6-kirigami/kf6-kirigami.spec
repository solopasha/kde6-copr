%global commit0 95c13740d42b963711821fff94efbb36bec675f8
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 10

%global framework kirigami

Name:           kf6-%{framework}
Version:        6.9.0%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
Summary:        QtQuick plugins to build user interfaces based on the KDE UX guidelines
License:        BSD-3-Clause AND CC0-1.0 AND FSFAP AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-LGPL AND MIT
URL:            https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6ShaderTools)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}

# Renamed from kf6-kirigami2
Obsoletes:      kf6-kirigami2 < 5.246.0-2
Provides:       kf6-kirigami2 = %{version}-%{release}
Provides:       kf6-kirigami2%{?_isa} = %{version}-%{release}

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      kf6-kirigami2-devel < 5.246.0-2
Provides:       kf6-kirigami2-devel = %{version}-%{release}
%description    devel
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
%find_lang_kf6 libkirigami6_qt

%files -f libkirigami6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/kirigami.categories
%{_kf6_libdir}/libKirigami.so.%{version_no_git}
%{_kf6_libdir}/libKirigami.so.6
%{_kf6_libdir}/libKirigamiDelegates.so.%{version_no_git}
%{_kf6_libdir}/libKirigamiDelegates.so.6
%{_kf6_libdir}/libKirigamiDialogs.so.%{version_no_git}
%{_kf6_libdir}/libKirigamiDialogs.so.6
%{_kf6_libdir}/libKirigamiLayouts.so.%{version_no_git}
%{_kf6_libdir}/libKirigamiLayouts.so.6
%{_kf6_libdir}/libKirigamiPlatform.so.%{version_no_git}
%{_kf6_libdir}/libKirigamiPlatform.so.6
%{_kf6_libdir}/libKirigamiPrimitives.so.%{version_no_git}
%{_kf6_libdir}/libKirigamiPrimitives.so.6
%{_kf6_libdir}/libKirigamiPrivate.so.%{version_no_git}
%{_kf6_libdir}/libKirigamiPrivate.so.6
%{_kf6_qmldir}/org/kde/kirigami/

%files devel
%{_kf6_datadir}/kdevappwizard/templates/kirigami6.tar.bz2
%{_kf6_includedir}/Kirigami/
%{_kf6_libdir}/cmake/KF6Kirigami/
%{_kf6_libdir}/cmake/KF6Kirigami2/
%{_kf6_libdir}/cmake/KF6KirigamiPlatform/
%{_kf6_libdir}/libKirigami.so
%{_kf6_libdir}/libKirigamiDelegates.so
%{_kf6_libdir}/libKirigamiDialogs.so
%{_kf6_libdir}/libKirigamiLayouts.so
%{_kf6_libdir}/libKirigamiPlatform.so
%{_kf6_libdir}/libKirigamiPrimitives.so
%{_kf6_libdir}/libKirigamiPrivate.so
%{_qt6_docdir}/*.tags

%changelog
%{?kde_snapshot_changelog_entry}
* Thu Oct 31 2024 Pavel Solovev <daron439@gmail.com> - 6.7.0-2
- rebuilt

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

* Sun Jun 02 2024 Pavel Solovev <daron439@gmail.com> - 6.2.1-1.1
- rebuild for f40

* Sun May 12 2024 Pavel Solovev <daron439@gmail.com> - 6.2.0-1
- Update to 6.2.0

* Fri Apr 12 2024 Pavel Solovev <daron439@gmail.com> - 6.1.0-1
- Update to 6.1.0

* Fri Mar 29 2024 Pavel Solovev <daron439@gmail.com> - 6.0.0-3
- fix assert

* Wed Mar 20 2024 Pavel Solovev <daron439@gmail.com> - 6.0.0-2
- qmlcache rebuild

* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Tue Oct 17 2023 Jan Grulich <jgrulich@redhat.com> - 5.240.0^20230927.203844.684c010-4
- Rebuild (qt6)

* Tue Oct 17 2023 Jan Grulich <jgrulich@redhat.com> - 5.240.0^20230927.203844.684c010-3
- Rebuild (qt6)

* Thu Oct 05 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230927.203844.684c010-2
- Rebuild for Qt Private API

* Wed Sep 27 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230927.203844.684c010-1
- Initial Release
