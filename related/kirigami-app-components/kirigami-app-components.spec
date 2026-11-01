%global commit0 cb794aef2974c754e4c6398f0ebcde8e64d09bee
%global shortcommit0 %{sub %{commit0} 1 7}
%global bumpver 2

Name:           kirigami-app-components
Version:        1.1.1%{?bumpver:^%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
Summary:        Kirigami addons and modules necessary to do a full featured KDE application
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://invent.kde.org/libraries/kirigami-app-components
%kde_meta

BuildSystem:    cmake_kf6

BuildRequires:  cmake(KF6Config) 
BuildRequires:  cmake(KF6GuiAddons) 
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KirigamiPlatform) 

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Quick) 
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Widgets) 

%description
Kirigami addons and modules necessary to do a full featured KDE application, 
such as integration with configurable keyboard shortcuts and standard actions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core)
%description    devel
%{summary}.

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_libdir}/libKirigamiActionCollection.so.1*
%{_kf6_libdir}/libKirigamiActionCollection.so.6
%{_kf6_qmldir}/org/kde/kirigami/actioncollection/

%files devel
%{_kf6_includedir}/Kirigami/ActionCollection/
%{_kf6_libdir}/cmake/KF6KirigamiAppComponents/
%{_kf6_libdir}/libKirigamiActionCollection.so

%changelog
%{?kde_snapshot_changelog_entry}
