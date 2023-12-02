%global		framework kirigami

Name:		kf6-%{framework}2
Version:	5.246.0
Release:	1%{?dist}
Summary:	QtQuick plugins to build user interfaces based on the KDE UX guidelines
License:	BSD-3-Clause AND CC0-1.0 AND FSFAP AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-LGPL AND MIT
URL:		https://invent.kde.org/frameworks/%{framework}
%frameworks_source

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	extra-cmake-modules >= %{version}
BuildRequires:	kf6-rpm-macros
BuildRequires:	make
BuildRequires:	qt6-linguist
BuildRequires:	qt6-qtbase-devel
BuildRequires:	qt6-qtdeclarative-devel
BuildRequires:	qt6-qtsvg-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6ShaderTools)
BuildRequires:	cmake(Qt6Core5Compat)
BuildRequires:	pkgconfig(xkbcommon)

%description
%{summary}.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{framework}-%{version} -p1
# Some licenses are missing from the main LICENSES folder but are in the template folder, copying them over.
cp %{_builddir}/%{framework}-%{version}/templates/kirigami6/LICENSES/* %{_builddir}/%{framework}-%{version}/LICENSES/

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang_kf6 libkirigami6_qt

%files -f libkirigami6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/kirigami.categories
%{_kf6_libdir}/libKirigami.so.*
%{_kf6_libdir}/libKirigamiDelegates.so.*
%{_kf6_libdir}/libKirigamiPlatform.so.*
%{_kf6_qmldir}/org/kde/kirigami/

%files devel
%dir %{_kf6_datadir}/kdevappwizard/
%dir %{_kf6_datadir}/kdevappwizard/templates/
%{_kf6_datadir}/kdevappwizard/templates/kirigami6.tar.bz2
%{_kf6_includedir}/Kirigami/
%{_kf6_libdir}/cmake/KF6Kirigami/
%{_kf6_libdir}/cmake/KF6Kirigami2/
%{_kf6_libdir}/cmake/KF6KirigamiPlatform/
%{_kf6_libdir}/libKirigami.so
%{_kf6_libdir}/libKirigamiDelegates.so
%{_kf6_libdir}/libKirigamiPlatform.so


%changelog
* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Tue Oct 17 2023 Jan Grulich <jgrulich@redhat.com> - 5.240.0^20230927.203844.684c010-4
- Rebuild (qt6)

* Tue Oct 17 2023 Jan Grulich <jgrulich@redhat.com> - 5.240.0^20230927.203844.684c010-3
- Rebuild (qt6)

* Thu Oct 05 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230927.203844.684c010-2
- Rebuild for Qt Private API

* Wed Sep 27 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230927.203844.684c010-1
- Initial Release
