Name:           kde-rounded-corners
Version:        0.6.7
Release:        8%{?dist}
Summary:        Rounds the corners of your windows in KDE Plasma

License:        GPL-3.0-only
URL:            https://github.com/matinlotfali/KDE-Rounded-Corners
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6WindowSystem)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  qt6-qtbase-private-devel

BuildRequires:  cmake(KWin)
BuildRequires:  cmake(KWinDBusInterface)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(xcb)

%description
%{summary}.

%prep
%autosetup -n KDE-Rounded-Corners-%{version} -p1

%build
%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_kf6_datadir}/kwin/shaders/shapecorners*.frag
%{_qt6_plugindir}/kwin/effects/configs/kwin_shapecorners_config.so
%{_qt6_plugindir}/kwin/effects/plugins/kwin4_effect_shapecorners.so

%changelog
* Thu Oct 31 2024 Pavel Solovev <daron439@gmail.com> - 0.6.7-8
- rebuilt

* Wed Oct 23 2024 Pavel Solovev <daron439@gmail.com> - 0.6.7-7
- rebuilt

* Tue Oct 15 2024 Pavel Solovev <daron439@gmail.com> - 0.6.7-6
- rebuilt

* Fri Oct 04 2024 Pavel Solovev <daron439@gmail.com> - 0.6.7-5
- rebuilt

* Tue Sep 10 2024 Pavel Solovev <daron439@gmail.com> - 0.6.7-4
- rebuilt

* Thu Aug 29 2024 Pavel Solovev <daron439@gmail.com> - 0.6.7-3
- rebuilt

* Wed Jul 17 2024 Pavel Solovev <daron439@gmail.com> - 0.6.7-2
- rebuilt

* Sat Jul 06 2024 Pavel Solovev <daron439@gmail.com> - 0.6.7-1
- new version

* Sun May 26 2024 Pavel Solovev <daron439@gmail.com> - 0.6.6-1
- new version

* Thu May 23 2024 Pavel Solovev <daron439@gmail.com> - 0.6.5-2
- rebuilt

* Tue Apr 16 2024 Pavel Solovev <daron439@gmail.com> - 0.6.1-7
- rebuilt

* Wed Mar 27 2024 Pavel Solovev <daron439@gmail.com> - 0.6.1-6
- rebuilt

* Fri Jan 12 2024 Pavel Solovev <daron439@gmail.com>
- Initial build
