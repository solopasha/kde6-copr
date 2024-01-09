%global framework kservice

Name:    kf6-%{framework}
Summary: KDE Frameworks 6 Tier 3 solution for advanced plugin and service introspection
Version: 5.247.0
Release: 1%{?dist}

# The following licenses are in the LICENSES folder but go unused: GPL-2.0-only, GPL-2.0-or-later, GPL-3.0-only, LicenseRef-KDE-Accepted-GPL
License: CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-LGPL
URL:     https://invent.kde.org/frameworks/%{framework}

%frameworks_meta

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)

BuildRequires:  qt6-qtbase-devel

# for the Administration category
# Recommends:       redhat-menus

Requires:       kf6-filesystem

%description
KDE Frameworks 6 Tier 3 solution for advanced plugin and service
introspection.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6Config)
Requires:       cmake(KF6CoreAddons)
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
%find_lang %{name} --all-name --with-man
mkdir -p %{buildroot}%{_kf6_datadir}/kservices6
mkdir -p %{buildroot}%{_kf6_datadir}/kservicetypes6

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_bindir}/kbuildsycoca6
%{_kf6_datadir}/kservices6/
%{_kf6_datadir}/kservicetypes6/
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Service.so.5*
%{_kf6_libdir}/libKF6Service.so.6*
%{_kf6_mandir}/man8/*.8*

%files devel
%{_kf6_includedir}/KService/
%{_kf6_libdir}/cmake/KF6Service/
%{_kf6_libdir}/libKF6Service.so

%changelog
* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Tue Oct 03 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231006.002016.a60f060-1
- Initial Release
