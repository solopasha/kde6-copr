%global commit0 721b2440f4c111a9a68672580d2cfac7c9934eab
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 3

Name:           kde-rounded-corners
Version:        0.6.0%{?bumpver:^%{bumpver}.git%{shortcommit0}}
Release:        2%{?dist}
Summary:        Rounds the corners of your windows in KDE Plasma

License:        GPL-3.0-only
URL:            https://github.com/matinlotfali/KDE-Rounded-Corners
Source:         %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

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
%autosetup -n KDE-Rounded-Corners-%{commit0} -p1

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
* Fri Jan 12 2024 Pavel Solovev <daron439@gmail.com>
- Initial build
