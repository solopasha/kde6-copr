%global commit0 f6dc52fa5853b4f68c3c53716847675f5a6394c3
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 2

%global framework baloo

Name:           kf6-%{framework}
Summary:        A Tier 3 KDE Frameworks 6 module that provides indexing and search functionality
Version:        6.10.0%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
License:        BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-GPL AND LicenseRef-KDE-Accepted-LGPL AND bzip2-1.0.6
URL:            https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

Patch100:       baloo-5.67.0-baloofile_config.patch

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6FileMetaData)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IdleTime)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Solid)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  lmdb-devel

# for systemd-related macros
BuildRequires:  systemd-rpm-macros

Requires:       %{name}-file%{?_isa} = %{version}-%{release}

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6CoreAddons)
Requires:       cmake(KF6FileMetaData)
Requires:       cmake(Qt6Core)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        file
Summary:        File indexing and search for Baloo
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:      kf5-baloo-file < 6
%description    file
%{summary}.

%package        libs
Summary:        Runtime libraries for %{name}
%description    libs
%{summary}.

%qch_package

%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%find_lang baloodb6
%find_lang baloo_file6
%find_lang baloo_file_extractor6
%find_lang balooctl6
%find_lang balooengine6
%find_lang baloosearch6
%find_lang balooshow6
%find_lang kio6_baloosearch
%find_lang kio6_tags
%find_lang kio6_timeline

cat kio6_tags.lang kio6_baloosearch.lang kio6_timeline.lang \
    balooctl6.lang balooengine6.lang baloosearch6.lang \
    balooshow6.lang baloodb6.lang \
    > %{name}.lang

cat baloo_file6.lang baloo_file_extractor6.lang \
    > %{name}-file.lang

%files -f %{name}.lang
%license LICENSES/*.txt
%{_kf6_bindir}/balooctl6
%{_kf6_bindir}/baloosearch6
%{_kf6_bindir}/balooshow6
%{_kf6_datadir}/qlogging-categories6/%{framework}*

%files file -f %{name}-file.lang
%config(noreplace) %{_kf6_sysconfdir}/xdg/autostart/baloo_file.desktop
%{_kf6_libexecdir}/baloo_file
%{_kf6_libexecdir}/baloo_file_extractor
%{_userunitdir}/kde-baloo.service

%files libs
%license LICENSES/*
%{_kf6_libdir}/libKF6Baloo.so.%{version_no_git}
%{_kf6_libdir}/libKF6Baloo.so.6
%{_kf6_libdir}/libKF6BalooEngine.so.%{version_no_git}
%{_kf6_libdir}/libKF6BalooEngine.so.6
%{_kf6_plugindir}/kded/baloosearchmodule.so
%{_kf6_plugindir}/kio/baloosearch.so
%{_kf6_plugindir}/kio/tags.so
%{_kf6_plugindir}/kio/timeline.so
%{_kf6_qmldir}/org/kde/baloo/

%files devel
%{_kf6_datadir}/dbus-1/interfaces/org.kde.baloo.*.xml
%{_kf6_datadir}/dbus-1/interfaces/org.kde.Baloo*.xml
%{_kf6_includedir}/Baloo/
%{_kf6_libdir}/cmake/KF6Baloo/
%{_kf6_libdir}/libKF6Baloo.so
%{_kf6_libdir}/pkgconfig/KF6Baloo.pc
%{_qt6_docdir}/*.tags

%changelog
%{?kde_snapshot_changelog_entry}
* Fri Dec 06 2024 Pavel Solovev <daron439@gmail.com> - 6.9.0-1
- Update to 6.9.0

* Sun Nov 24 2024 Pavel Solovev <daron439@gmail.com> - 6.8.0-2
- Obsolete any version of kf5-baloo-file

* Sat Nov 02 2024 Pavel Solovev <daron439@gmail.com> - 6.8.0-1
- Update to 6.8.0

* Fri Oct 04 2024 Pavel Solovev <daron439@gmail.com> - 6.7.0-1
- Update to 6.7.0

* Fri Sep 06 2024 Pavel Solovev <daron439@gmail.com> - 6.6.0-1
- Update to 6.6.0

* Fri Aug 09 2024 Pavel Solovev <daron439@gmail.com> - 6.5.0-1
- Update to 6.5.0

* Fri Jul 12 2024 Pavel Solovev <daron439@gmail.com> - 6.4.0-1
- Update to 6.4.0

* Sun Jun 09 2024 Pavel Solovev <daron439@gmail.com> - 6.3.0-2
- require baloo-file

* Fri Jun 07 2024 Pavel Solovev <daron439@gmail.com> - 6.3.0-1
- Update to 6.3.0

* Sun Jun 02 2024 Pavel Solovev <daron439@gmail.com> - 6.2.0-2.1
- rebuild for f40

* Sat Jun 01 2024 Pavel Solovev <daron439@gmail.com> - 6.2.0-2
- Obsolete kf5-baloo-file

* Sun May 12 2024 Pavel Solovev <daron439@gmail.com> - 6.2.0-1
- Update to 6.2.0

* Fri Apr 12 2024 Pavel Solovev <daron439@gmail.com> - 6.1.0-1
- Update to 6.1.0

* Wed Mar 20 2024 Pavel Solovev <daron439@gmail.com> - 6.0.0-2
- qmlcache rebuild

* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231011.023811.02a2bd6-1
- Initial release
