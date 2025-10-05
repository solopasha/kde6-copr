%global commit0 33684d109b0db3e885c5c6f01b5379a4ee1b3a06
%global shortcommit0 %{sub %{commit0} 1 7}
%global bumpver 1

%global framework ktextwidgets

Name:           kf6-%{framework}
Version:        6.20.0%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 3 addon with advanced text editing widgets

License:        CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-LGPL
URL:            https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Sonnet)
BuildRequires:  cmake(KF6WidgetsAddons)

BuildRequires:  cmake(Qt6TextToSpeech)
BuildRequires:  cmake(Qt6Widgets)

%description
KDE Frameworks 6 Tier 3 addon with advanced text edting widgets.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6I18n)
Requires:       cmake(KF6Sonnet)
Requires:       cmake(Qt6Widgets)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_libdir}/libKF6TextWidgets.so.%{version_no_git}
%{_kf6_libdir}/libKF6TextWidgets.so.6

%files devel
%{_kf6_includedir}/KTextWidgets/
%{_kf6_libdir}/cmake/KF6TextWidgets/
%{_kf6_libdir}/libKF6TextWidgets.so
%{_kf6_qtplugindir}/designer/ktextwidgets6widgets.so

%changelog
%{?kde_snapshot_changelog_entry}
* Fri Jan 03 2025 Pavel Solovev <daron439@gmail.com> - 6.10.0-1
- Update to 6.10.0

* Fri Dec 06 2024 Pavel Solovev <daron439@gmail.com> - 6.9.0-1
- Update to 6.9.0

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

* Mon Oct 09 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231003.060127.1cc7bdc-1
- Initial Release
