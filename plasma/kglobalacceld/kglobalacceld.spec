Name:    kglobalacceld
Summary: Daemon providing Global Keyboard Shortcut functionality
Version: 5.90.0
Release: 1.1%{?dist}

License: CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-LGPL
URL:     https://invent.kde.org/plasma/%{name}

%plasma_source

BuildRequires:  extra-cmake-modules
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires:  qt6-qtbase-gui
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xkbcommon) >= 0.5.0
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xcb-record)
BuildRequires:  pkgconfig(xcb-xtest)
BuildRequires:  systemd
Requires:  kf6-filesystem

%description
%{summary}.

%package devel
Summary:        Developer files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
%description    devel
%{summary}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%files
%license LICENSES/*.txt
%{_sysconfdir}/xdg/autostart/kglobalacceld.desktop
%{_userunitdir}/plasma-kglobalaccel.service
%{_libdir}/libKGlobalAccelD.so.*
%{_qt6_plugindir}/org.kde.kglobalacceld.platforms/KGlobalAccelDXcb.so
%{_libexecdir}/kglobalacceld

%files devel
%{_includedir}/KGlobalAccelD/
%{_libdir}/cmake/KGlobalAccelD/

%changelog
* Fri Nov 10 2023 Alessandro Astone <ales.astone@gmail.com> - 5.27.80-1
- 5.27.80

* Wed Oct 18 2023 Steve Cossette <farchord@gmail.com> - 5.27.80^20231009.021332.6933aae-3
- Added BuildDep for systemd

* Wed Oct 18 2023 Steve Cossette <farchord@gmail.com> - 5.27.80^20231009.021332.6933aae-2
- Fixed an issue with the systemd unit

* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.27.80^20231009.021332.6933aae-1
- Initial release
