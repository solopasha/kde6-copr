%global framework bluez-qt

Name:           kf6-%{framework}
Summary:        A Qt wrapper for Bluez
Version:        6.3.0
Release:        1%{?dist}

License:        CC0-1.0 AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only
URL:            https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  gcc-c++
BuildRequires:  cmake

# For %%{_udevrulesdir}
BuildRequires:  systemd

Requires:       kf6-filesystem >= %{version}
Recommends:     bluez >= 5

%description
BluezQt is Qt-based library written handle all Bluetooth functionality.

%package        devel
Summary:        Development files for %{name}

Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
%description    devel
Development files for %{name}.



%qch_package

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{framework}-%{version}


%build
 %{cmake_kf6} \
  -DUDEV_RULES_INSTALL_DIR:PATH="%{_udevrulesdir}"
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6BluezQt.so.6
%{_kf6_libdir}/libKF6BluezQt.so.%{version}
%{_kf6_qmldir}/org/kde/bluezqt/

%files devel
%{_qt6_docdir}/*.tags
%{_kf6_includedir}/BluezQt/
%{_kf6_libdir}/libKF6BluezQt.so
%{_kf6_libdir}/cmake/KF6BluezQt/
%{_kf6_libdir}/pkgconfig/KF6BluezQt.pc

%changelog
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

* Fri Sep 22 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230901.202319.fe828b8-1
- Initial build
