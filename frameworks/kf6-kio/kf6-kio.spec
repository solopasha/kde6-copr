%global commit0 d09989f93698a01aef719bfd19bd665269df091e
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 2

%global framework kio

Name:    kf6-%{framework}
Version: 6.9.0%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release: 1%{?dist}
Summary: KDE Frameworks 6 Tier 3 solution for filesystem abstraction

License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-GPL AND LicenseRef-KDE-Accepted-LGPL AND MIT
URL:     https://invent.kde.org/frameworks/%{framework}
%frameworks_meta
Patch:   0001-Give-the-kuriikwsfiltereng_private-a-VERSION-and-SOV.patch

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Auth)
BuildRequires:  cmake(KF6Bookmarks)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6KDED)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)

BuildRequires:  switcheroo-control

BuildRequires:  libacl-devel
%if !0%{?flatpak}
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
%endif
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(mount)
BuildRequires:  zlib-devel

BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires:  cmake(Qt6UiPlugin)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Core5Compat)

Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Requires:       %{name}-widgets%{?_isa} = %{version}-%{release}
Requires:       %{name}-file-widgets%{?_isa} = %{version}-%{release}
Requires:       %{name}-gui%{?_isa} = %{version}-%{release}

Requires: kf6-kded

%description
KDE Frameworks 6 Tier 3 solution for filesystem abstraction

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       cmake(KF6Bookmarks)
Requires:       cmake(KF6Completion)
Requires:       cmake(KF6Config)
Requires:       cmake(KF6CoreAddons)
Requires:       cmake(KF6ItemViews)
Requires:       cmake(KF6JobWidgets)
Requires:       cmake(KF6Service)
Requires:       cmake(KF6Solid)
Requires:       cmake(KF6WidgetsAddons)
Requires:       cmake(KF6WindowSystem)
Requires:       qt6-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation files for %{name}
Requires:       %{name}-core = %{version}-%{release}
BuildArch:      noarch
%description    doc
Documentation for %{name}.

%package        core
Summary:        Core components of the KIO Framework
Requires:       %{name}-core-libs%{?_isa} = %{version}-%{release}
Requires:       %{name}-doc = %{version}-%{release}
Requires:       kf6-filesystem
%if 0%{?fedora} < 40
Requires:       (kio-extras-kf5 if kf5-kio-core)
%else
Recommends:     (kio-extras-kf5 if kf5-kio-core)
%endif
%description    core
KIOCore library provides core non-GUI components for working with KIO.

%package        core-libs
Summary:        Runtime libraries for KIO Core
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
%description    core-libs
%{summary}.

%package        widgets
Summary:        Widgets for KIO Framework
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
%description    widgets
KIOWidgets contains classes that provide generic job control, progress
reporting, etc.

%package        widgets-libs
Summary:        Runtime libraries for KIO Widgets library
Requires:       %{name}-widgets%{?_isa} = %{version}-%{release}
%description    widgets-libs
%{summary}.

%package        file-widgets
Summary:        Widgets for file-handling for KIO Framework
Requires:       %{name}-widgets%{?_isa} = %{version}-%{release}
%description    file-widgets
The KIOFileWidgets library provides the file selection dialog and
its components.

%package        gui
Summary:        Gui components for the KIO Framework
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Recommends:     switcheroo-control
%description    gui
%{summary}.


%qch_package qch

%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name --with-man --with-html

%files
%license LICENSES/*.txt
%doc README.md

%files core
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libexecdir}/kioexec
%{_kf6_libexecdir}/kiod6
%{_kf6_libexecdir}/kioworker
%{_kf6_bindir}/ktelnetservice6
%{_kf6_bindir}/ktrash6
%{_kf6_plugindir}/kio/
%{_kf6_plugindir}/kded/
%{_kf6_plugindir}/kiod/
%{_kf6_datadir}/kf6/searchproviders/*.desktop
%{_kf6_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.kde.*.service

%files core-libs
%{_kf6_libdir}/libKF6KIOCore.so.6
%{_kf6_libdir}/libKF6KIOCore.so.%{version_no_git}

%files doc -f %{name}.lang

%files gui
%{_kf6_libdir}/libKF6KIOGui.so.6
%{_kf6_libdir}/libKF6KIOGui.so.%{version_no_git}

%files widgets
%dir %{_kf6_plugindir}/urifilters/
%{_kf6_plugindir}/urifilters/*.so

%files widgets-libs
%{_kf6_libdir}/libKF6KIOWidgets.so.6
%{_kf6_libdir}/libKF6KIOWidgets.so.%{version_no_git}
%{_kf6_libdir}/libkuriikwsfiltereng_private.so.6
%{_kf6_libdir}/libkuriikwsfiltereng_private.so.%{version_no_git}
%{_kf6_qtplugindir}/designer/*6widgets.so

%files file-widgets
%{_kf6_libdir}/libKF6KIOFileWidgets.so.6
%{_kf6_libdir}/libKF6KIOFileWidgets.so.%{version_no_git}

%files devel
%{_qt6_docdir}/*.tags
%{_kf6_datadir}/kdevappwizard/templates/kioworker6.tar.bz2
%{_kf6_includedir}/KIO/
%{_kf6_includedir}/KIOCore/
%{_kf6_includedir}/KIOFileWidgets/
%{_kf6_includedir}/KIOGui/
%{_kf6_includedir}/KIOWidgets/
%{_kf6_libdir}/cmake/KF6KIO/
%{_kf6_libdir}/libKF6KIOCore.so
%{_kf6_libdir}/libKF6KIOFileWidgets.so
%{_kf6_libdir}/libKF6KIOGui.so
%{_kf6_libdir}/libKF6KIOWidgets.so
%{_kf6_libdir}/libkuriikwsfiltereng_private.so

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

* Tue Jul 16 2024 Pavel Solovev <daron439@gmail.com> - 6.4.0-2
- pick upstream commit

* Fri Jul 12 2024 Pavel Solovev <daron439@gmail.com> - 6.4.0-1
- Update to 6.4.0

* Tue Jun 18 2024 Pavel Solovev <daron439@gmail.com> - 6.3.0-2
- change to recommends

* Fri Jun 07 2024 Pavel Solovev <daron439@gmail.com> - 6.3.0-1
- Update to 6.3.0

* Sun Jun 02 2024 Pavel Solovev <daron439@gmail.com> - 6.2.0-2.1
- rebuild for f40

* Sun May 12 2024 Pavel Solovev <daron439@gmail.com> - 6.2.0-1
- Update to 6.2.0

* Fri Apr 12 2024 Pavel Solovev <daron439@gmail.com> - 6.1.0-1
- Update to 6.1.0

* Wed Mar 20 2024 Pavel Solovev <daron439@gmail.com> - 6.0.0-3
- qmlcache rebuild

* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Tue Oct 17 2023 Jan Grulich <jgrulich@redhat.com> - 5.240.0^20231010.060359.1c34fd4-4
- Rebuild (qt6)

* Mon Oct 16 2023 Adam Williamson <awilliam@redhat.com> - 5.240.0^20231010.060359.1c34fd4-3

* Mon Oct 09 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231010.060359.1c34fd4-2
- Fixed a problem with the -doc subpackage building differently on different arches.

* Mon Oct 09 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231010.060359.1c34fd4-1
- Initial Release
