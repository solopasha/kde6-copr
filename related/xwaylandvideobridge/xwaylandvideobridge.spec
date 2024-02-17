Name:           xwaylandvideobridge
Version:        0.4.0
Release:        2%{?dist}
Summary:        Utility to allow streaming Wayland windows to X applications

License:        (GPL-2.0-only or GPL-3.0-only) and LGPL-2.0-or-later and BSD-3-Clause
URL:            https://invent.kde.org/system/xwaylandvideobridge
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        kde-frameworks-signing-keys.pgp

BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-event)
BuildRequires:  pkgconfig(xcb-record)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  cmake(KPipeWire)

Requires:       hicolor-icon-theme

%description
By design, X11 applications can't access window or screen contents
for wayland clients. This is fine in principle, but it breaks screen
sharing in tools like Discord, MS Teams, Skype, etc and more.

This tool allows us to share specific windows to X11 clients,
but within the control of the user at all times.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1


%build
%cmake_kf6 -DBUILD_WITH_QT6=ON
%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop


%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}.*
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/qlogging-categories6/%{name}.categories
%{_sysconfdir}/xdg/autostart/org.kde.%{name}.desktop


%changelog
* Sat Nov 18 2023 Alessandro Astone <ales.astone@gmail.com> - 0.3.0-2
- Build against Qt6/KF6

* Thu Nov 09 2023 Alessandro Astone <ales.astone@gmail.com> - 0.3.0-1
- Update to 0.3
- Autostart on login

* Fri Oct 27 2023 Alessandro Astone <ales.astone@gmail.com> - 0.2-1
- Update to tagged release 0.2

* Mon Sep 18 2023 Neal Gompa <ngompa@fedoraproject.org> - 0~git20230917.9b27c3f-1
- Bump to new git snapshot

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0~git20230504.3445aff-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 15 2023 Neal Gompa <ngompa@fedoraproject.org> - 0~git20230504.3445aff-2
- Add dependency on hicolor-icon-theme

* Wed May 10 2023 Neal Gompa <ngompa@fedoraproject.org> - 0~git20230504.3445aff-1
- Initial package
