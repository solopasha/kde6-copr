%global commit0 36174521fa65b83e91fcd2682cf7b27fd08e4868
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 3

%global framework frameworkintegration

Name:           kf6-%{framework}
Version:        6.9.0%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 4 workspace and cross-framework integration plugins
License:        CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-LGPL
URL:            https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6NewStuffCore)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6WidgetsAddons)

BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake(AppStreamQt)
BuildRequires:  cmake(packagekitqt6)

Requires:       kf6-filesystem

%description
Framework Integration is a set of plugins responsible for better integration of
Qt applications when running on a KDE Plasma workspace.

Applications do not need to link to this directly.

%package        libs
Summary:        Runtime libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    libs
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6ColorScheme)
Requires:       cmake(KF6IconThemes)
Requires:       cmake(KF6WidgetsAddons)
%description    devel
The %{name}-devel package contains files to develop for %{name}.

%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/knotifications6/plasma_workspace.notifyrc
%dir %{_kf6_libexecdir}/kpackagehandlers
%{_kf6_libexecdir}/kpackagehandlers/appstreamhandler
%{_kf6_libexecdir}/kpackagehandlers/knshandler

%files libs
%{_kf6_libdir}/libKF6Style.so.%{version_no_git}
%{_kf6_libdir}/libKF6Style.so.6
%{_kf6_plugindir}/FrameworkIntegrationPlugin.so

%files devel
%{_kf6_includedir}/FrameworkIntegration/
%{_kf6_includedir}/KStyle/
%{_kf6_libdir}/cmake/KF6FrameworkIntegration/
%{_kf6_libdir}/libKF6Style.so

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

* Tue Oct 17 2023 Jan Grulich <jgrulich@redhat.com> - 5.240.0^20231003.064310.c062482-2
- Rebuild (qt6)

* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231003.064310.c062482-1
- Initial release
