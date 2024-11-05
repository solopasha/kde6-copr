%global commit0 6a22af7d21b1091d6b9f00a291a692c4750c3d17
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

%global qt6minver 6.6.0
%global kf6minver 6.2

Name:           krdp
Version:        6.2.3
Release:        1%{?dist}
Summary:        Desktop sharing using RDP

License:        LGPL-2.1-only OR LGPL-3.0-only
URL:            https://invent.kde.org/plasma/krdp
%plasma_source

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules >= %{kf6minver}
BuildRequires:  gcc-c++
BuildRequires:  systemd-rpm-macros
BuildRequires:  qt6-qtbase-private-devel >= %{qt6minver}
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6StatusNotifierItem)

BuildRequires:  cmake(Qt6Core) >= %{qt6minver}
BuildRequires:  cmake(Qt6Gui) >= %{qt6minver}
BuildRequires:  cmake(Qt6Network) >= %{qt6minver}
BuildRequires:  cmake(Qt6DBus) >= %{qt6minver}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6minver}

BuildRequires:  (cmake(FreeRDP-Server) >= 2.10 with cmake(FreeRDP-Server) < 3)
BuildRequires:  (cmake(FreeRDP) >= 2.10 with cmake(FreeRDP) < 3)
BuildRequires:  (cmake(WinPR) >= 2.10 with cmake(WinPR) < 3)
BuildRequires:  cmake(KPipeWire) >= 5.27.80
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  /usr/bin/winpr-makecert
Requires:       /usr/bin/winpr-makecert

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-server < 6.0.90-3
Provides:       %{name}-server = %{version}-%{release}
Provides:       %{name}-server%{?_isa} = %{version}-%{release}

%description
%{summary}.

%package        libs
Summary:        Library for creating an RDP server
Requires:       /usr/bin/openssl

%description    libs
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
%{summary}.


%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name

%files -f %{name}.lang
%doc README.md
%{_kf6_bindir}/krdpserver
%{_kf6_datadir}/applications/kcm_krdpserver.desktop
%{_kf6_datadir}/applications/org.kde.krdp.desktop
%{_kf6_datadir}/qlogging-categories6/kcm_krdpserver.categories
%{_kf6_datadir}/qlogging-categories6/krdp.categories
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_krdpserver.so
%{_userunitdir}/plasma-krdp_server.service

%files libs
%license LICENSES/LGPL-*.txt LICENSES/LicenseRef-KDE-*
%{_kf6_libdir}/libKRdp.so.6{,.*}

%files devel
%{_kf6_libdir}/libKRdp.so
%{_kf6_libdir}/cmake/KRdp/


%post
%systemd_user_post plasma-krdp_server.service

%preun
%systemd_user_preun plasma-krdp_server.service

%postun
%systemd_user_postun plasma-krdp_server.service


%changelog
* Tue Nov 05 2024 Pavel Solovev <daron439@gmail.com> - 6.2.3-1
- Update to 6.2.3

* Thu Oct 31 2024 Pavel Solovev <daron439@gmail.com> - 6.2.2-2
- rebuilt

* Tue Oct 22 2024 Pavel Solovev <daron439@gmail.com> - 6.2.2-1
- Update to 6.2.2

* Tue Oct 15 2024 Pavel Solovev <daron439@gmail.com> - 6.2.1-1
- Update to 6.2.1

* Thu Oct 03 2024 Pavel Solovev <daron439@gmail.com> - 6.2.0-1
- Update to 6.2.0

* Tue Sep 10 2024 Pavel Solovev <daron439@gmail.com> - 6.1.5-1
- Update to 6.1.5

* Tue Aug 06 2024 Pavel Solovev <daron439@gmail.com> - 6.1.4-1
- Update to 6.1.4

* Tue Jul 16 2024 Pavel Solovev <daron439@gmail.com> - 6.1.3-1
- Update to 6.1.3

* Tue Jul 02 2024 Pavel Solovev <daron439@gmail.com> - 6.1.2-1
- Update to 6.1.2

* Tue Jun 25 2024 Pavel Solovev <daron439@gmail.com> - 6.1.1-1
- Update to 6.1.1

* Tue Jun 18 2024 Pavel Solovev <daron439@gmail.com> - 6.1.0-1
- Update to 6.1.0

* Sat Jun 01 2024 Pavel Solovev <daron439@gmail.com> - 6.0.90-2
- restructure (from fedora)

* Sat May 25 2024 Pavel Solovev <daron439@gmail.com> - 6.0.90-1
- new version

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.27.80~git20231227.4931015-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.27.80~git20231227.4931015-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Dec 31 2023 Neal Gompa <ngompa@fedoraproject.org> - 5.27.80~git20231227.4931015-1
- Initial package
