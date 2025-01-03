%global commit0 3b79e6e2bae9b2a809fb4f8851ebd392c73aacf5
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

%global framework modemmanager-qt

Name:           kf6-%{framework}
Version:        6.9.0
Release:        1%{?dist}
Summary:        A Tier 1 KDE Frameworks module wrapping ModemManager DBus API
License:        GPL-2.0-only AND GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-GPL AND LicenseRef-KDE-Accepted-LGPL
URL:            https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Xml)

BuildRequires:  pkgconfig(ModemManager)

Requires:       kf6-filesystem

%description
A Qt 6 library for ModemManager.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ModemManager-devel
Requires:       cmake(Qt6Core)
Requires:       cmake(Qt6DBus)
%description    devel
Qt 6 libraries and header files for developing applications
that use ModemManager.

%qch_package

%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%files
%doc README README.md
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*.categories
%{_kf6_datadir}/qlogging-categories6/*.renamecategories
%{_kf6_libdir}/libKF6ModemManagerQt.so.%{version_no_git}
%{_kf6_libdir}/libKF6ModemManagerQt.so.6

%files devel
%{_kf6_includedir}/ModemManagerQt/
%{_kf6_libdir}/cmake/KF6ModemManagerQt/
%{_kf6_libdir}/libKF6ModemManagerQt.so
%{_qt6_docdir}/*.tags

%changelog
* Fri Dec 06 2024 Pavel Solovev <daron439@gmail.com> - 6.9.0-1
- Update to 6.9.0

* Sat Nov 02 2024 Pavel Solovev <daron439@gmail.com> - 6.8.0-1
- Update to 6.8.0

* Fri Oct 04 2024 Pavel Solovev <daron439@gmail.com> - 6.7.0-1
- Update to 6.7.0

* Fri Sep 06 2024 Pavel Solovev <daron439@gmail.com> - 6.6.0-1
- Update to 6.6.0

* Fri Aug 09 2024 Pavel Solovev <daron439@gmail.com> - 6.5.0-1
- Update to 6.5.0

* Fri Jul 12 2024 Pavel Solovev <daron439@gmail.com> - 6.4.0-1
- Update to 6.4.0

* Fri Jun 07 2024 Pavel Solovev <daron439@gmail.com> - 6.3.0-1
- Update to 6.3.0

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

* Wed Sep 27 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.233545.2b7a359714ce9f4a58b6372b68bd6e3a929886d2-48
- rebuilt

* Wed Sep 27 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.233545.2b7a359714ce9f4a58b6372b68bd6e3a929886d2-47
- rebuilt

* Tue Sep 26 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.233545.2b7a359714ce9f4a58b6372b68bd6e3a929886d2-46
- rebuilt

* Tue Sep 26 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.233545.2b7a359714ce9f4a58b6372b68bd6e3a929886d2-45
- rebuilt

* Tue Sep 26 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.233545.2b7a359714ce9f4a58b6372b68bd6e3a929886d2-44
- rebuilt

* Tue Sep 26 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.233545.2b7a359714ce9f4a58b6372b68bd6e3a929886d2-43
- rebuilt

* Mon Sep 25 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.233545.2b7a359714ce9f4a58b6372b68bd6e3a929886d2-42
- rebuilt

* Sun Sep 24 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.233545.2b7a359714ce9f4a58b6372b68bd6e3a929886d2-41
- rebuilt

* Sat Sep 23 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.233545.2b7a359714ce9f4a58b6372b68bd6e3a929886d2-40
- rebuilt

* Fri Sep 22 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.233545.2b7a359714ce9f4a58b6372b68bd6e3a929886d2-39
- rebuilt

* Thu Sep 21 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.233545.2b7a359714ce9f4a58b6372b68bd6e3a929886d2-38
- rebuilt

* Thu Sep 21 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.233545.2b7a359-37
- rebuilt

* Thu Sep 21 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.233545.2b7a359-36
- rebuilt

* Wed Sep 20 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.233545.2b7a359-35
- rebuilt

* Tue Aug 29 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230813.164311.fa71a4d-1
- Initial package
