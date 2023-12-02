
%undefine __cmake_in_source_build

%global framework kplotting

Name:           kf6-%{framework}
Version:        5.246.0
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 1 addon for plotting
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://invent.kde.org/frameworks/%{framework}
%frameworks_source

# Compile Tools
BuildRequires:  cmake
BuildRequires:  gcc-c++

# Fedora
BuildRequires:  kf6-rpm-macros
Requires:       kf6-filesystem

# KDE Frameworks
BuildRequires:  extra-cmake-modules >= %{version}

# Other
BuildRequires:  pcre2-devel
BuildRequires:  perl-interpreter

# Qt
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6UiPlugin)

%description
KPlotting provides classes to do plotting.

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
%{cmake_kf6}
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_libdir}/libKF6Plotting.so.*
%{_kf6_qtplugindir}/designer/kplotting6widgets.so

%files devel
%{_kf6_includedir}/KPlotting/
%{_kf6_libdir}/libKF6Plotting.so
%{_kf6_libdir}/cmake/KF6Plotting/

%changelog
* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Tue Oct 03 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230829.233317.aea878d-129
- Fixed some issues in the spec stated during the review

* Tue Sep 19 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.233317.aea878d-128
- Initial Package
