%global commit0 44b38fc6c1d35729da030aef39ed36b408ddfb5b
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

%global base_name partitionmanager

%global kf6min 5.240.0
%global qt6min 6.5.0
%global kpmcoremin 24.01

Name:           kde-partitionmanager
Version:        24.08.0
Release:        1%{?dist}
Summary:        KDE Partition Manager

License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND MIT AND CC-BY-4.0 AND CC0-1.0 AND GFDL-1.2-or-later
URL:            https://apps.kde.org/partitionmanager/
%apps_source

BuildRequires:  cmake >= 3.16
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib

BuildRequires:  cmake(Qt6Core) >= %{qt6min}
BuildRequires:  cmake(Qt6Gui) >= %{qt6min}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6min}

BuildRequires:  cmake(KF6Config) >= %{kf6min}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6min}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6min}
BuildRequires:  cmake(KF6Crash) >= %{kf6min}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6min}
BuildRequires:  cmake(KF6I18n) >= %{kf6min}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6min}
BuildRequires:  cmake(KF6KIO) >= %{kf6min}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6min}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6min}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6min}
BuildRequires:  cmake(KF6DocTools) >= %{kf6min}

BuildRequires:  cmake(PolkitQt6-1)
BuildRequires:  cmake(KPMcore) >= %{kpmcoremin}

Requires:       kf6-filesystem

%description
KDE Partition Manager is a utility program to help you manage the disk devices,
partitions and file systems on your computer. It allows you to easily create,
copy, move, delete, resize without losing data, backup and restore partitions.

KDE Partition Manager supports a large number of file systems,
including ext2/3/4, reiserfs, NTFS, FAT16/32, jfs, xfs and more.

Starting from version 1.9.50 KDE Partition Manager has become the GUI part of
KPMcore (KDE PartitionManager core) which contain the libraries used to
manipulate filesystems.


%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang partitionmanager --with-kde --with-html


%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/*partitionmanager.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/*.appdata.xml


%files -f partitionmanager.lang
%license LICENSES/*
%{_kf6_bindir}/partitionmanager
%{_kf6_datadir}/applications/*partitionmanager.desktop
%{_kf6_datadir}/solid/actions/open_in_partitionmanager.desktop
%{_kf6_datadir}/config.kcfg/partitionmanager.kcfg
%{_datadir}/icons/hicolor/*/*/*
%{_kf6_metainfodir}/*partitionmanager.appdata.xml


%changelog
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
