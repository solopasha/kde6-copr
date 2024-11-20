%global commit0 39822d1cbeb67e1d76d5ef21f990c95347e24e4f
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 5

%global framework kcmutils

Name:    kf6-%{framework}
Version: 6.9.0%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release: 1%{?dist}
Summary: KDE Frameworks 6 Tier 3 addon with extra API to write KConfigModules

License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-LGPL
URL:     https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel

Requires: kf6-filesystem

%description
KCMUtils provides various classes to work with KCModules. KCModules can be
created with the KConfigWidgets framework.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6ConfigWidgets)
Requires:       cmake(KF6CoreAddons)
Requires:       cmake(Qt6Qml)
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
%find_lang %{name} --all-name
# create/own dirs
mkdir -p %{buildroot}%{_kf6_qtplugindir}/kcms

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_bindir}/kcmshell6
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6KCMUtils.so.%{version_no_git}
%{_kf6_libdir}/libKF6KCMUtils.so.6
%{_kf6_libdir}/libKF6KCMUtilsCore.so.%{version_no_git}
%{_kf6_libdir}/libKF6KCMUtilsCore.so.6
%{_kf6_libdir}/libKF6KCMUtilsQuick.so.%{version_no_git}
%{_kf6_libdir}/libKF6KCMUtilsQuick.so.6
%{_kf6_qmldir}/org/kde/kcmutils/
%{_kf6_qtplugindir}/kcms/

%files devel
%{_qt6_docdir}/*.tags
%{_kf6_includedir}/KCMUtils/
%{_kf6_includedir}/KCMUtilsCore/
%{_kf6_includedir}/KCMUtilsQuick/
%{_kf6_libdir}/cmake/KF6KCMUtils/
%{_kf6_libdir}/libKF6KCMUtils.so
%{_kf6_libdir}/libKF6KCMUtilsCore.so
%{_kf6_libdir}/libKF6KCMUtilsQuick.so
%{_kf6_libexecdir}/kcmdesktopfilegenerator

%changelog
%{?kde_snapshot_changelog_entry}
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

* Tue Oct 17 2023 Jan Grulich <jgrulich@redhat.com> - 5.240.0^20231009.021630.3e10cd2-2
- Rebuild (qt6)

* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231009.021630.3e10cd2-1
- Initial release
