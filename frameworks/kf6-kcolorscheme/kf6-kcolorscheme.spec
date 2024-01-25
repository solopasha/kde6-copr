%global framework kcolorscheme

Name:    kf6-%{framework}
Version: 5.249.0
Release: 1%{?dist}
Summary: Classes to read and interact with KColorScheme
License: BSD-2-Clause and CC0-1.0 and LGPL-2.0-or-later and LGPL-2.1-only and LGPL-3.0-only and LicenseRef-KDE-Accepted-LGPL
URL:     https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)

Requires:       kf6-filesystem

%description
%summary.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       cmake(KF6Config)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%qch_package

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang kcolorscheme6 --all-name

%files -f kcolorscheme6.lang
%doc README.md
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/kcolorscheme.categories
%{_kf6_libdir}/libKF6ColorScheme.so.%{version}
%{_kf6_libdir}/libKF6ColorScheme.so.6

%files devel
%{_qt6_docdir}/*.tags
%{_kf6_includedir}/KColorScheme/
%{_kf6_libdir}/cmake/KF6ColorScheme/
%{_kf6_libdir}/libKF6ColorScheme.so

%changelog
* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Tue Oct 03 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231001.103550.783d488-1
- Initial Release
