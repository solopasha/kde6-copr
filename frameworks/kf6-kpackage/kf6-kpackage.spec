%global framework kpackage

Name:           kf6-%{framework}
Version:        6.2.0
Release:        1%{?dist}.1
Summary:        KDE Frameworks 6 Tier 2 library to load and install packages as plugins
License:        CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  qt6-qtbase-devel

Requires:  kf6-filesystem

%description
KDE Frameworks 6 Tier 2 library to load and install non-binary packages as
if they were plugins.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
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
%find_lang %{name} --all-name --with-man

# create/own dirs
mkdir -p %{buildroot}%{_kf6_qtplugindir}/kpackage/packagestructure/
mkdir -p %{buildroot}%{_kf6_datadir}/kpackage/

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_bindir}/kpackagetool6
%{_kf6_datadir}/kpackage/
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Package.so.6
%{_kf6_libdir}/libKF6Package.so.%{version}
%{_kf6_qtplugindir}/kpackage/
%{_mandir}/man1/kpackagetool6.1*

%files devel
%{_qt6_docdir}/*.tags
%{_kf6_includedir}/KPackage/
%{_kf6_libdir}/cmake/KF6Package/
%{_kf6_libdir}/libKF6Package.so


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

* Tue Oct 03 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231003.152541.40b9c7e-1
- Initial Release
