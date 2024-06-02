
%global framework kplotting

Name:           kf6-%{framework}
Version:        6.2.0
Release:        1%{?dist}.1
Summary:        KDE Frameworks 6 Tier 1 addon for plotting
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6UiPlugin)

Requires:       kf6-filesystem

%description
KPlotting provides classes to do plotting.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%qch_package

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{framework}-%{version} -p1

%build
%{cmake_kf6}
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_libdir}/libKF6Plotting.so.6
%{_kf6_libdir}/libKF6Plotting.so.%{version}
%{_kf6_qtplugindir}/designer/kplotting6widgets.so

%files devel
%{_qt6_docdir}/*.tags
%{_kf6_includedir}/KPlotting/
%{_kf6_libdir}/cmake/KF6Plotting/
%{_kf6_libdir}/libKF6Plotting.so

%changelog
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

* Tue Oct 03 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230829.233317.aea878d-129
- Fixed some issues in the spec stated during the review

* Tue Sep 19 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.233317.aea878d-128
- Initial Package
