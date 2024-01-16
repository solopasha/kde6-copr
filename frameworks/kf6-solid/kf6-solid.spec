
%global framework solid

Name:           kf6-%{framework}
Version:        5.248.0
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 1 integration module that provides hardware information
License:        LGPL-2.1-or-later AND LGPL-2.1-only AND CCO-1.0 AND BSD-3-Clause AND LGPL-3.0-only
URL:            https://solid.kde.org/
%frameworks_meta

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Tools)
BuildRequires:  pkgconfig(libplist-2.0)
BuildRequires:  pkgconfig(libimobiledevice-1.0)
BuildRequires:  pkgconfig(mount)
BuildRequires:  libupnp-devel
BuildRequires:  systemd-devel
BuildRequires:  flex
BuildRequires:  bison
Recommends:     media-player-info
Recommends:     udisks2
Recommends:     upower

Requires:       kf6-filesystem

%description
Solid provides the following features for application developers:
 - Hardware Discovery
 - Power Management
 - Network Management

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6 \
    -DWITH_NEW_POWER_ASYNC_API:BOOL=ON \
    -DWITH_NEW_POWER_ASYNC_FREEDESKTOP:BOOL=ON \
    -DWITH_NEW_SOLID_JOB:BOOL=ON
%cmake_build

%install
%cmake_install
%find_lang_kf6 solid6_qt

%files -f solid6_qt.lang
%doc README.md TODO
%license LICENSES/*.txt
%{_kf6_bindir}/solid-hardware6
%{_kf6_bindir}/solid-power
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Solid.so.%{version}
%{_kf6_libdir}/libKF6Solid.so.6

%files devel
%{_kf6_includedir}/Solid/
%{_kf6_libdir}/cmake/KF6Solid/
%{_kf6_libdir}/libKF6Solid.so

%changelog
* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Tue Sep 19 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230911.192300.eaebf4a-1
- Initial Package
