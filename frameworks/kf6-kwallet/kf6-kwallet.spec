%global commit0 6c7c11f4354251924ff5f19b07a16033030756cc
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 3

%global framework kwallet

Name:    kf6-%{framework}
Version: 6.9.0%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release: 1%{?dist}
Summary: KDE Frameworks 6 Tier 3 solution for password management

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)

BuildRequires:  qt6-qtbase-devel

BuildRequires:  cmake(Gpgmepp)
BuildRequires:  cmake(Qca-qt6)
BuildRequires:  pkgconfig(libgcrypt)

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       kf6-filesystem
Requires:       pinentry-gui

%description
KWallet is a secure and unified container for user passwords.

%package        libs
Summary:        KWallet framework libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    libs
Provides API to access KWallet data from applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel

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

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_bindir}/kwallet-query
%{_kf6_bindir}/kwalletd6
%{_kf6_datadir}/applications/org.kde.kwalletd6.desktop
%{_kf6_datadir}/dbus-1/services/org.kde.kwalletd5.service
%{_kf6_datadir}/dbus-1/services/org.kde.kwalletd6.service
%{_kf6_datadir}/knotifications6/kwalletd6.notifyrc
%{_kf6_datadir}/qlogging-categories6/%{framework}*
%{_kf6_datadir}/xdg-desktop-portal/portals/kwallet.portal
%{_kf6_mandir}/man1/kwallet-query.1.*

%files libs
%{_kf6_libdir}/libKF6Wallet.so.%{version_no_git}
%{_kf6_libdir}/libKF6Wallet.so.6
%{_kf6_libdir}/libKF6WalletBackend.so.%{version_no_git}
%{_kf6_libdir}/libKF6WalletBackend.so.6

%files devel
%{_kf6_datadir}/dbus-1/interfaces/kf6_org.kde.KWallet.xml
%{_kf6_includedir}/KWallet/
%{_kf6_libdir}/cmake/KF6Wallet/
%{_kf6_libdir}/libKF6Wallet.so
%{_qt6_docdir}/*.tags


%changelog
%{?kde_snapshot_changelog_entry}
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

* Sun Jun 02 2024 Pavel Solovev <daron439@gmail.com> - 6.2.1-1.1
- rebuild for f40

* Sun May 12 2024 Pavel Solovev <daron439@gmail.com> - 6.2.0-1
- Update to 6.2.0

* Fri Apr 12 2024 Pavel Solovev <daron439@gmail.com> - 6.1.0-1
- Update to 6.1.0

* Wed Mar 20 2024 Pavel Solovev <daron439@gmail.com> - 6.0.0-2
- qmlcache rebuild

* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Sun Oct 15 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20231012.021308.7a2c863-1

* Mon Oct 09 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231003.213013.7c91f3d-1
- Initial Release
