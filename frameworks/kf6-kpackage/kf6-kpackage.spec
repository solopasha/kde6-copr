%global commit0 f5f205d9fd9294d2b129e44d43a3d8ba1105a797
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

%global framework kpackage

Name:           kf6-%{framework}
Version:        6.3.0%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 2 library to load and install packages as plugins
License:        CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
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
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1

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
%{_kf6_libdir}/libKF6Package.so.%{lua: print((macros.version:gsub('[%^~].*', '')))}
%{_kf6_qtplugindir}/kpackage/
%{_mandir}/man1/kpackagetool6.1*

%files devel
%{_qt6_docdir}/*.tags
%{_kf6_includedir}/KPackage/
%{_kf6_libdir}/cmake/KF6Package/
%{_kf6_libdir}/libKF6Package.so


%changelog
%{?kde_snapshot_changelog_entry}
* Wed Mar 20 2024 Pavel Solovev <daron439@gmail.com> - 6.0.0-2
- qmlcache rebuild

* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Tue Oct 03 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231003.152541.40b9c7e-1
- Initial Release
