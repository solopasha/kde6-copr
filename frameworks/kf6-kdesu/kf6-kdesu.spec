%global framework kdesu

Name:    kf6-%{framework}
Version: 6.2.0
Release: 1%{?dist}.1
Summary: KDE Frameworks 6 Tier 3 integration with su

License: CC0-1.0 AND GPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-LGPL
URL:     https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Pty)
BuildRequires:  pkgconfig(x11)
BuildRequires:  qt6-qtbase-devel
Requires:  kf6-filesystem

%description

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6Pty)
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
%find_lang kdesu6_qt --all-name



%files -f kdesu6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*
%{_kf6_libdir}/libKF6Su.so.6
%{_kf6_libdir}/libKF6Su.so.%{version}
%{_kf6_libexecdir}/kdesu_stub
%attr(2755,root,nobody) %{_kf6_libexecdir}/kdesud

%files devel
%{_qt6_docdir}/*.tags
%{_kf6_includedir}/KDESu/
%{_kf6_libdir}/libKF6Su.so
%{_kf6_libdir}/cmake/KF6Su/

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

* Wed Sep 27 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231001.121632.8b7a35c-1
- Initial Release
