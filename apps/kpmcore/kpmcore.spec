%global commit0 5e2cd7eb6066a7922e4a29346d86ecc03d027e7c
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

%global kf6min 5.240.0
%global qt6min 6.5.0
%global sover 12

Name:           kpmcore
Version:        24.08.1
Release:        1%{?dist}
Summary:        Library for managing partitions by KDE programs
License:        GPL-3.0-or-later AND MIT AND CC-BY-4.0 AND CC0-1.0
URL:            https://github.com/KDE/kpmcore
%apps_source

BuildRequires:  cmake >= 3.16
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(Qt6Core) >= %{qt6min}
BuildRequires:  cmake(Qt6DBus) >= %{qt6min}
BuildRequires:  cmake(Qt6Gui) >= %{qt6min}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6min}

BuildRequires:  cmake(KF6CoreAddons) >= %{kf6min}
BuildRequires:  cmake(KF6I18n) >= %{kf6min}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6min}

BuildRequires:  cmake(PolkitQt6-1)

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(blkid) >= 2.33.2

Requires:       e2fsprogs
Requires:       kf6-filesystem

Recommends:     dosfstools
Recommends:     exfatprogs
Recommends:     f2fs-tools
Recommends:     fatresize
Recommends:     hfsutils
Recommends:     hfsplus-tools
Recommends:     jfsutils
Recommends:     nilfs-utils
Recommends:     ocfs2-tools
Recommends:     udftools

%description
KPMcore contains common code for managing partitions by KDE Partition Manager
and other KDE projects


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core) >= %{qt6min}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}


%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1

%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name}
%find_lang %{name}._policy_


%files -f %{name}.lang -f %{name}._policy_.lang
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libkpmcore.so.%{sover}
%{_kf6_libdir}/libkpmcore.so.%{version_no_git}
%{_kf6_qtplugindir}/kpmcore
%{_libexecdir}/kpmcore_externalcommand
%{_datadir}/dbus-1/system.d/org.kde.kpmcore.*.conf
%{_datadir}/dbus-1/system-services/org.kde.kpmcore.*.service
%{_datadir}/polkit-1/actions/org.kde.kpmcore.externalcommand.policy

%files devel
%{_includedir}/%{name}/
%{_kf6_libdir}/cmake/KPMcore
%{_kf6_libdir}/libkpmcore.so


%changelog
* Tue Sep 10 2024 Pavel Solovev <daron439@gmail.com> - 24.08.1-1
- Update to 24.08.1

* Fri Aug 16 2024 Pavel Solovev <daron439@gmail.com> - 24.08.0-1
- Update to 24.08.0

* Fri Aug 09 2024 Pavel Solovev <daron439@gmail.com> - 24.07.90-1
- Update to 24.07.90

* Thu Jul 25 2024 Pavel Solovev <daron439@gmail.com> - 24.07.80-1
- Update to 24.07.80

* Thu Jul 04 2024 Pavel Solovev <daron439@gmail.com> - 24.05.2-1
- Update to 24.05.2

* Thu Jun 13 2024 Pavel Solovev <daron439@gmail.com> - 24.05.1-1
- Update to 24.05.1

* Thu May 23 2024 Pavel Solovev <daron439@gmail.com> - 24.05.0-1
- Update to 24.05.0

* Fri Apr 26 2024 Pavel Solovev <daron439@gmail.com> - 24.04.80-1
- Update to 24.04.80

* Thu Apr 11 2024 Pavel Solovev <daron439@gmail.com> - 24.02.2-1
- Update to 24.02.2

* Thu Mar 21 2024 Pavel Solovev <daron439@gmail.com> - 24.02.1-1
- Update to 24.02.1
