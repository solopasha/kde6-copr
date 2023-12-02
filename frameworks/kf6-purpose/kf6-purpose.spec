%global framework purpose

Name:    kf6-purpose
Summary: Framework for providing abstractions to get the developer's purposes fulfilled
Version: 5.246.0
Release: 1%{?dist}

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

%frameworks_source

BuildRequires: extra-cmake-modules >= %{version}
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: cmake
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6Prison)
BuildRequires: cmake(KF6Declarative)
BuildRequires: pkgconfig(Qt6Network)
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: pkgconfig(xkbcommon)
Requires: hicolor-icon-theme

%description
Purpose offers the possibility to create integrate services and actions on
any application without having to implement them specifically. Purpose will
offer them mechanisms to list the different alternatives to execute given the
requested action type and will facilitate components so that all the plugins
can receive all the information they need.

%package  devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(KF6CoreAddons)
%description devel
%{summary}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Purpose.so.5*
%{_kf6_libdir}/libKF6Purpose.so.6
%{_kf6_libdir}/libKF6PurposeWidgets.so.5*
%{_kf6_libdir}/libKF6PurposeWidgets.so.6
%{_kf6_libdir}/libPhabricatorHelpers.so.5*
%{_kf6_libdir}/libPhabricatorHelpers.so.6
%{_kf6_libdir}/libReviewboardHelpers.so.5*
%{_kf6_libdir}/libReviewboardHelpers.so.6
%{_kf6_libexecdir}/purposeprocess
%{_kf6_datadir}/kf6/purpose/
%{_kf6_plugindir}/purpose/
%dir %{_kf6_plugindir}/kfileitemaction/
%{_kf6_plugindir}/kfileitemaction/sharefileitemaction.so
%{_kf6_qmldir}/org/kde/purpose/
%{_datadir}/icons/hicolor/*/apps/*-purpose.*

%files devel
%{_kf6_libdir}/libKF6Purpose.so
%{_kf6_libdir}/libKF6PurposeWidgets.so
%{_kf6_includedir}/Purpose/
%{_kf6_includedir}/PurposeWidgets/
%{_kf6_libdir}/cmake/KF6Purpose/

%changelog
* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231011.004242.c0f1138-1
- Initial release
