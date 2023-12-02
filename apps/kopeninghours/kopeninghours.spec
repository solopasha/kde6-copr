Name:    kopeninghours
Version: 24.01.80
Release: 1%{?dist}
Summary: Library for parsing and evaluating OSM opening hours expressions

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later
URL:     https://invent.kde.org/libraries/%{name}
%apps_source

BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros


%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%license LICENSES/*.txt
%doc README.md
%{_kf6_libdir}/libKOpeningHours.so.*
%{_qt6_qmldir}/org/kde/kopeninghours
%{_datadir}/qlogging-categories6/org_kde_kopeninghours.categories
%{python3_sitelib}/PyKOpeningHours/

%files devel
%{_includedir}/KOpeningHours
%{_kf6_libdir}/cmake/KOpeningHours
%{_kf6_libdir}/libKOpeningHours.so
%{_includedir}/kopeninghours
%{_includedir}/kopeninghours_version.h

%changelog
* Mon Oct 09 2023 Steve Cossette <farchord@gmail.com> - 23.08.2-1
- Initial Release
