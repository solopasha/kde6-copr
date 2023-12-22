Name:    kopeninghours
Version: 24.01.85
Release: 1%{?dist}
Summary: Library for parsing and evaluating OSM opening hours expressions

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later
URL:     https://invent.kde.org/libraries/%{name}
%apps_source

BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake
BuildRequires:  cmake(KF6Holidays)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  python3-devel
BuildRequires:  boost-devel
Requires:       kf6-filesystem

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1


%build
%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build


%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%license LICENSES/*.txt
%doc README.md
%{_kf6_datadir}/qlogging-categories6/org_kde_kopeninghours.categories
%{_kf6_libdir}/libKOpeningHours.so.1
%{_kf6_libdir}/libKOpeningHours.so.24*
%{_qt6_qmldir}/org/kde/kopeninghours/
%{python3_sitelib}/PyKOpeningHours/

%files devel
%{_includedir}/kopeninghours_version.h
%{_includedir}/kopeninghours/
%{_includedir}/KOpeningHours/
%{_kf6_libdir}/cmake/KOpeningHours/
%{_kf6_libdir}/libKOpeningHours.so

%changelog
* Mon Dec 18 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80

* Mon Oct 09 2023 Steve Cossette <farchord@gmail.com> - 23.08.2-1
- Initial Release
