Name:    kf6
# This version MUST remain in sync with KF6 versions!
# XXX: Yes, it's 5.x still, this is synced with the version set in extra-cmake-modules
Version: 6.2.0
Release: 1%{?dist}.1
Summary: Filesystem and RPM macros for KDE Frameworks 6
License: BSD-3-Clause
URL:     http://www.kde.org
Source0: macros.kf6
Source1: LICENSE
Source2: macros.kf6-srpm
Source3: kde_maps.lua
Source4: kde.lua

%description
Filesystem and RPM macros for KDE Frameworks 6

%package filesystem
Summary: Filesystem for KDE Frameworks 6
%if 0%{?fedora} >= 39 || 0%{?rhel} >= 10
Requires: kde-filesystem >= 5
%endif
%{?_qt6_version:Requires: qt6-qtbase >= %{_qt6_version}}
%description filesystem
Filesystem for KDE Frameworks 6.

%package rpm-macros
Summary: RPM macros for KDE Frameworks 6
Requires: cmake >= 3
Requires: qt6-rpm-macros >= 6
Requires: %{name}-srpm-macros = %{version}-%{release}
# misc build environment dependencies
Requires: gcc-c++
Requires: gnupg2
Requires: ninja-build
BuildArch: noarch
%description rpm-macros
RPM macros for building KDE Frameworks 6 packages.

%package srpm-macros
Summary: SRPM macros for KDE Frameworks 6
BuildArch: noarch
%description srpm-macros
RPM macros for building KDE SRPM packages.

%package qch
Summary: QCH metapackage
Recommends: qt6-doc
BuildArch: noarch
%description qch
QCH metapackage

%install
# See macros.kf6 where the directories are specified
mkdir -p %{buildroot}%{_prefix}/{lib,%{_lib}}/qt6/plugins/kf6/
mkdir -p %{buildroot}%{_prefix}/{lib,%{_lib}}/qt6/qml/org/kde/
mkdir -p %{buildroot}%{_includedir}/kf6
mkdir -p %{buildroot}%{_includedir}/KF6
mkdir -p %{buildroot}%{_datadir}/{kf6,kservices6,kservicetypes6}
mkdir -p %{buildroot}%{_datadir}/kio/servicemenus
mkdir -p %{buildroot}%{_datadir}/qlogging-categories6/
mkdir -p %{buildroot}%{_docdir}/qt6
mkdir -p %{buildroot}%{_libexecdir}/kf6
mkdir -p %{buildroot}%{_datadir}/kf6/
mkdir -p %{buildroot}%{_datadir}/locale/tok
%if ! (0%{?fedora} >= 39 || 0%{?rhel} >= 10)
mkdir -p %{buildroot}%{_prefix}/{lib,%{_lib}}/kconf_update_bin
mkdir -p %{buildroot}%{_datadir}/{config.kcfg,kconf_update}
mkdir -p %{buildroot}%{_datadir}/kpackage/{genericqml,kcms}
mkdir -p %{buildroot}%{_datadir}/knsrcfiles/
mkdir -p %{buildroot}%{_datadir}/solid/{actions,devices}
mkdir -p %{buildroot}%{_sysconfdir}/xdg/plasma-workspace/{env,shutdown}
%endif

install -Dpm644 %{_sourcedir}/macros.kf6 %{buildroot}%{_rpmconfigdir}/macros.d/macros.kf6
install -Dpm644 %{_sourcedir}/macros.kf6-srpm %{buildroot}%{_rpmconfigdir}/macros.d/macros.kf6-srpm
install -Dpm644 %{_sourcedir}/LICENSE %{buildroot}%{_datadir}/kf6/LICENSE
sed -i \
  -e "s|@@kf6_VERSION@@|%{version}|g" \
  %{buildroot}%{_rpmconfigdir}/macros.d/macros.kf6

install -Dpm0644 %{_sourcedir}/kde_maps.lua %{buildroot}%{_rpmluadir}/fedora/srpm/kde_maps.lua
install -Dpm0644 %{_sourcedir}/kde.lua %{buildroot}%{_rpmluadir}/fedora/srpm/kde.lua

%files filesystem
%{_datadir}/kf6/
%{_datadir}/kio/
%{_datadir}/kservices6/
%{_datadir}/kservicetypes6/
%{_datadir}/qlogging-categories6/
%{_docdir}/qt6/
%{_includedir}/kf6/
%{_includedir}/KF6/
%{_libexecdir}/kf6/
%{_prefix}/%{_lib}/qt6/plugins/kf6/
%{_prefix}/lib/qt6/plugins/kf6/
%{_prefix}/%{_lib}/qt6/qml/org/kde/
%{_prefix}/lib/qt6/qml/org/kde/
%{_datadir}/locale/tok
%if ! (0%{?fedora} >= 39 || 0%{?rhel} >= 10)
%{_datadir}/config.kcfg/
%{_datadir}/kconf_update/
%{_datadir}/knsrcfiles/
%{_datadir}/kpackage/
%{_datadir}/solid/
%{_prefix}/%{_lib}/kconf_update_bin/
%{_prefix}/lib/kconf_update_bin/
%{_sysconfdir}/xdg/plasma-workspace/
%endif

%files rpm-macros
%{_rpmconfigdir}/macros.d/macros.kf6

%files srpm-macros
%{_rpmconfigdir}/macros.d/macros.kf6-srpm
%{_rpmluadir}/fedora/srpm/kde*.lua

%files qch

%changelog
* Sun Jun 02 2024 Pavel Solovev <daron439@gmail.com> - 6.2.0-1.1
- rebuild for f40

* Sun May 12 2024 Pavel Solovev <daron439@gmail.com> - 6.2.0-1
- Update to 6.2.0

* Fri Apr 12 2024 Pavel Solovev <daron439@gmail.com> - 6.1.0-1
- Update to 6.1.0

* Fri Nov 24 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 5.245.0-2
- Update servicemenus path

* Fri Nov 10 2023 Alessandro Astone <ales.astone@gmail.com> - 5.245.0-1
- 5.245.0
- Fix macros for unstable releases

* Sun Nov 05 2023 Steve Cossette <farchord@gmail.com> - 5.240.0-4
- Migrated/copied framework version macros from the kf5 package

* Sun Oct 08 2023 Steve Cossette <farchord@gmail.com> - 5.240.0-3
- Added ownership of the Toki Pona locale to kf6-filesystem

* Thu Sep 21 2023 Neal Gompa <ngompa@fedoraproject.org> - 5.240.0-2
- Add KDE QML paths to -filesystem subpackage (#2239699)

* Sat Sep 16 2023 Neal Gompa <ngompa@fedoraproject.org> - 5.240.0-1
- Set version matching extra-cmake-modules base version

* Fri Sep 15 2023 Neal Gompa <ngompa@fedoraproject.org> - 0.0-1
- Version reset in preparation for kf6 initial release

* Thu Sep 14 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 7-2
- Use kde-filesystem for unversioned directories in F40+

* Fri Sep 8 2023 Justin Zobel <justin@1707.io> 7-1
- Create and own /usr/include/KF6

* Thu Mar 2 2023 Justin Zobel <justin@1707.io> 6-1
- Initial Version

