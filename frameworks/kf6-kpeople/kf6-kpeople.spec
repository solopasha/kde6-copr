%global framework kpeople

Name:    kf6-%{framework}
Version: 5.246.0
Release: 1%{?dist}
Summary: KDE Frameworks 6 Tier 3 library for contact and people aggregation

License: CC0-1.0 AND LGPL-2.1-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

%frameworks_source

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel

Requires:  kf6-filesystem

%description
KDE Frameworks 6 Tier 3 library for interaction with XML RPC services.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

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
%{_kf6_libdir}/libKF6People.so.*
%{_kf6_libdir}/libKF6PeopleWidgets.so.*
%{_kf6_libdir}/libKF6PeopleBackend.so.*
%{_kf6_qmldir}/org/kde/people/

%files devel
%{_kf6_includedir}/KPeople/
%{_kf6_libdir}/libKF6People.so
%{_kf6_libdir}/libKF6PeopleWidgets.so
%{_kf6_libdir}/libKF6PeopleBackend.so
%{_kf6_libdir}/cmake/KF6People/

%changelog
* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Mon Oct 09 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231003.021019.6f4b1b4c-1
- Initial release
