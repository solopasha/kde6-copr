%global commit0 e0c555ebb70f305345ff18d5d70a4ee14475ec28
%global shortcommit0 %{sub %{commit0} 1 7}
%global bumpver 3

Name:           knighttime
Version:        6.5.80%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
Summary:        Helpers for scheduling the dark-light cycle

License:        BSD-3-Clause AND LGPL-2.1-only AND GPL-2.0-only AND CC0-1.0
URL:            https://invent.kde.org/plasma/%{name}
%plasma_source

BuildRequires:  desktop-file-utils
BuildRequires:  systemd-rpm-macros

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Holidays)
BuildRequires:  cmake(KF6I18n)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Positioning)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core)
%description    devel
%{summary}.

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/*.desktop

%post
%systemd_user_post plasma-knighttimed.service

%files
%license LICENSES
%{_kf6_datadir}/applications/org.kde.knighttimed.desktop
%{_kf6_datadir}/dbus-1/interfaces/org.kde.NightTime.xml
%{_kf6_datadir}/dbus-1/services/org.kde.NightTime.service
%{_kf6_datadir}/qlogging-categories6/knighttime.categories
%{_kf6_libdir}/libKNightTime.so.%{version_no_git}
%{_kf6_libdir}/libKNightTime.so.0
%{_libexecdir}/knighttimed
%{_userunitdir}/plasma-knighttimed.service

%files devel
%{_includedir}/KNightTime/
%{_kf6_libdir}/cmake/KNightTime/
%{_kf6_libdir}/libKNightTime.so

%changelog
%{?kde_snapshot_changelog_entry}
* Mon Jul 07 2025 Pavel Solovev <daron439@gmail.com> - 6.4.80~1.git137d8cc-1
- Initial package
