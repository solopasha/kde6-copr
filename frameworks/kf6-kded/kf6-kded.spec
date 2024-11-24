%global commit0 f7583bd3edcd573145714569da9a742e41879da8
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 2

%global framework kded

Name:           kf6-%{framework}
Version:        6.9.0%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 3 addon with extensible daemon for system-level services

License:        CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later
URL:            https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6Service)

BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  systemd-rpm-macros

Requires:       kf6-filesystem

%description
KDED stands for KDE Daemon which isn't very descriptive. KDED runs
in the background and performs a number of small tasks. Some of these
tasks are built in, others are started on demand.

Custom KDED modules can be provided by 3rd party frameworks and
applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang kded6 --with-man --without-mo
# create/own this
mkdir -p %{buildroot}%{_kf6_plugindir}/kded

%post
%systemd_user_post  plasma-kded6.service

%preun
%systemd_user_preun plasma-kded6.service

%files -f kded6.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_bindir}/kded6
%{_kf6_datadir}/applications/org.kde.kded6.desktop
%{_kf6_datadir}/dbus-1/services/*.service
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_mandir}/man8/kded6.8*
%{_userunitdir}/plasma-kded6.service
%dir %{_kf6_plugindir}/kded/

%files devel
%{_kf6_datadir}/dbus-1/interfaces/*.xml
%{_kf6_libdir}/cmake/KF6KDED/

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

* Mon Oct 09 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231005.021018.cbc5874-1
- Initial release
