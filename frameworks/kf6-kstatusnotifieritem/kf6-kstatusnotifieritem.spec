%global commit0 9f480b0d323001167e6b0c71efde9d91f7d7a23f
%global shortcommit0 %{sub %{commit0} 1 7}
%global bumpver 1

%global framework kstatusnotifieritem

Name:           kf6-%{framework}
Version:        6.20.0%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
Summary:        Implementation of Status Notifier Items

License:        CC0-1.0 AND LGPL-2.0-or-later
URL:            https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  cmake(KF6WindowSystem)

BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  qt6-qtbase-private-devel

BuildRequires:  pkgconfig(x11)

%description
%summary.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6DBus)
Requires:       cmake(Qt6Gui)
Requires:       cmake(Qt6Widgets)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%kf6_python_bindings_package

%files -f kstatusnotifieritem6_qt.lang
%{_kf6_datadir}/dbus-1/interfaces/kf6_org.kde.StatusNotifierItem.xml
%{_kf6_datadir}/dbus-1/interfaces/kf6_org.kde.StatusNotifierWatcher.xml
%{_kf6_datadir}/qlogging-categories6/kstatusnotifieritem.categories
%{_kf6_libdir}/libKF6StatusNotifierItem.so.%{version_no_git}
%{_kf6_libdir}/libKF6StatusNotifierItem.so.6

%files devel
%{_kf6_includedir}/KStatusNotifierItem/
%{_kf6_libdir}/cmake/KF6StatusNotifierItem/
%{_kf6_libdir}/libKF6StatusNotifierItem.so

%changelog
%{?kde_snapshot_changelog_entry}
* Fri Jan 03 2025 Pavel Solovev <daron439@gmail.com> - 6.10.0-1
- Update to 6.10.0

* Fri Dec 06 2024 Pavel Solovev <daron439@gmail.com> - 6.9.0-1
- Update to 6.9.0

* Mon Dec 02 2024 Pavel Solovev <daron439@gmail.com> - 6.8.0-2
- Remove Qt6 version constraints

* Sat Nov 02 2024 Pavel Solovev <daron439@gmail.com> - 6.8.0-1
- Update to 6.8.0

* Thu Oct 31 2024 Pavel Solovev <daron439@gmail.com> - 6.7.0-2
- rebuilt

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

* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231011.024138.6035342-1
- Initial release
