%global framework kauth

Name:    kf6-%{framework}
Version: 6.0.0
Release: 2%{?dist}
Summary: KDE Frameworks 6 module to perform actions as privileged user
# LGPL-2.0-or-later is also in the project's LICENSES, but is unused according to reuse.
License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.1-or-later
URL:     https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  kf6-rpm-macros
BuildRequires:  polkit-qt6-1-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6WindowSystem)

Requires:  kf6-filesystem

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6CoreAddons)
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
%find_lang_kf6 kauth6_qt

%files -f kauth6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/dbus-1/system.d/org.kde.kf6auth.conf
%{_kf6_datadir}/kf6/kauth/
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6AuthCore.so.%{version}
%{_kf6_libdir}/libKF6AuthCore.so.6
%{_kf6_qtplugindir}/kf6/kauth/

%files devel
%{_qt6_docdir}/*.tags
%{_kf6_includedir}/KAuth/
%{_kf6_includedir}/KAuthCore/
%{_kf6_libdir}/cmake/KF6Auth/
%{_kf6_libdir}/libKF6AuthCore.so
%{_kf6_libexecdir}/kauth/

%changelog
* Wed Mar 20 2024 Pavel Solovev <daron439@gmail.com> - 6.0.0-2
- qmlcache rebuild

* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Tue Oct 03 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231003.060844.0b37b02-1
- Initial Release
