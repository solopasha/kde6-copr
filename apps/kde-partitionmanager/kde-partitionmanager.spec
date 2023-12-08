%global base_name partitionmanager

%global kf6min 5.240.0
%global qt6min 6.5.0
%global kpmcoremin 24.01

Name:           kde-partitionmanager
Version:        24.01.80
Release:        %autorelease
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
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n partitionmanager-%{version}


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
%autochangelog
