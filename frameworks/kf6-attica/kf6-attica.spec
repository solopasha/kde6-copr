%global framework attica

Name:           kf6-%{framework}
Version:        5.248.0
Release:        1%{?dist}
Summary:        KDE Frameworks Tier 1 Addon with Open Collaboration Services API
License:        CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-LGPL.txt
URL:            https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel

Requires:       kf6-filesystem

%description
Attica is a Qt library that implements the Open Collaboration Services
API version 1.4.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       qt6-qtbase-devel
%description    devel
%{summary}.

%if 0%{?docs}
%package doc
Summary: API documentation for %{name}
BuildRequires: doxygen
BuildRequires: qt6-qdoc
BuildRequires: qt6-qhelpgenerator
BuildRequires: qt6-qtbase-doc
Requires: kf6-filesystem
BuildArch: noarch
%description doc
%{summary}.
%endif

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6 \
  %if 0%{?flatpak}
  %{?docs:-DBUILD_QCH:BOOL=OFF} \
  %else
  %{?docs:-DBUILD_QCH:BOOL=ON} \
  %endif

%cmake_build

%install
%cmake_install

%files
%doc AUTHORS ChangeLog README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Attica.so.*

%files devel
%{_kf6_libdir}/cmake/KF6Attica/
%{_kf6_includedir}/Attica/
%{_kf6_libdir}/libKF6Attica.so
%{_kf6_libdir}/pkgconfig/KF6Attica.pc


%changelog
* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Wed Sep 27 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230829.232558.4e09a15-1
- Initial Release
