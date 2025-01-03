%global commit0 f419e5fa8c38721c828092fc2eb9c05d538e682f
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

%global framework ki18n

Name:           kf6-%{framework}
Version:        6.10.0
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 1 addon for localization
License:        BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-LGPL AND ODbL-1.0
URL:            https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  gettext
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  python3

Requires:       kf6-filesystem
Requires:       iso-codes

%description
KDE Frameworks 6 Tier 1 addon for localization.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gettext
Requires:       python3
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%qch_package

%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*%{framework}*
%{_kf6_libdir}/libKF6I18n.so.%{version_no_git}
%{_kf6_libdir}/libKF6I18n.so.6
%{_kf6_libdir}/libKF6I18nLocaleData.so.%{version_no_git}
%{_kf6_libdir}/libKF6I18nLocaleData.so.6
%{_kf6_libdir}/libKF6I18nQml.so.%{version_no_git}
%{_kf6_libdir}/libKF6I18nQml.so.6
%{_kf6_qmldir}/org/kde/i18n/
%{_kf6_qtplugindir}/kf6/ktranscript.so
%lang(ca) %{_datadir}/locale/ca/LC_SCRIPTS/ki18n6/
%lang(ca@valencia) %{_datadir}/locale/ca@valencia/LC_SCRIPTS/ki18n6/
%lang(fi) %{_datadir}/locale/fi/LC_SCRIPTS/ki18n6/
%lang(gd) %{_datadir}/locale/gd/LC_SCRIPTS/ki18n6/
%lang(ja) %{_datadir}/locale/ja/LC_SCRIPTS/ki18n6/
%lang(ko) %{_datadir}/locale/ko/LC_SCRIPTS/ki18n6/
%lang(nb) %{_datadir}/locale/nb/LC_SCRIPTS/ki18n6/
%lang(nn) %{_datadir}/locale/nn/LC_SCRIPTS/ki18n6/
%lang(ru) %{_datadir}/locale/ru/LC_SCRIPTS/ki18n6/
%lang(sr) %{_datadir}/locale/sr/LC_SCRIPTS/ki18n6/
%lang(sr) %{_datadir}/locale/uk/LC_SCRIPTS/ki18n6/
%lang(sr@ijekavian) %{_datadir}/locale/sr@ijekavian/LC_SCRIPTS/ki18n6/
%lang(sr@ijekavianlatin) %{_datadir}/locale/sr@ijekavianlatin/LC_SCRIPTS/ki18n6/
%lang(sr@latin) %{_datadir}/locale/sr@latin/LC_SCRIPTS/ki18n6/

%files devel
%{_kf6_includedir}/KI18n/
%{_kf6_includedir}/KI18nLocaleData/
%{_kf6_libdir}/cmake/KF6I18n/
%{_kf6_libdir}/libKF6I18n.so
%{_kf6_libdir}/libKF6I18nLocaleData.so
%{_kf6_libdir}/libKF6I18nQml.so
%{_qt6_docdir}/*.tags

%changelog
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

* Tue Oct 17 2023 Jan Grulich <jgrulich@redhat.com> - 5.240.0^20230829.233059.7042d58-3
- Rebuild (qt6)

* Thu Oct 05 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.233059.7042d58-2
- Rebuild for Qt Private API

* Wed Sep 27 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230829.233059.7042d58-1
- Initial Release
