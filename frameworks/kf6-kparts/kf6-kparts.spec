%global framework kparts

Name:    kf6-%{framework}
Version: 6.0.0
Release: 2%{?dist}
Summary: KDE Frameworks 6 Tier 3 solution for KParts

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-LGPL
URL:     https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  qt6-qtbase-devel

Requires:  kf6-filesystem

%description
KDE Frameworks 6 Tier 3 solution for KParts

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6KIO)
Requires:       cmake(KF6Service)
Requires:       cmake(KF6XmlGui)
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
%find_lang %{name} --all-name --with-html
# create/own parts plugin dir
mkdir -p %{buildroot}%{_kf6_plugindir}/parts/

%files -f %{name}.lang
%doc README.md AUTHORS
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Parts.so.6
%{_kf6_libdir}/libKF6Parts.so.%{version}
%dir %{_kf6_plugindir}/parts/

%files devel
%{_qt6_docdir}/*.tags
%dir %{_kf6_datadir}/kdevappwizard/
%dir %{_kf6_datadir}/kdevappwizard/templates/
%{_kf6_datadir}/kdevappwizard/templates/kparts6-app.tar.bz2
%{_kf6_includedir}/KParts/
%{_kf6_libdir}/cmake/KF6Parts/
%{_kf6_libdir}/libKF6Parts.so


%changelog
* Wed Mar 20 2024 Pavel Solovev <daron439@gmail.com> - 6.0.0-2
- qmlcache rebuild

* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231011.024115.17e9362-1
- Initial release
