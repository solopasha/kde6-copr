Name:           marknote
Version:        1.3.0
Release:        2%{?dist}
License:        GPL-3.0-or-later AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.0-only OR LGPL-3.0-only) AND BSD-3-Clause AND GPL-2.0-or-later
Summary:        A simple markdown note management app
URL:            https://invent.kde.org/office/marknote
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        signing-key.pgp

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib

BuildRequires:  cmake(KF6BreezeIcons)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Kirigami2)
BuildRequires:  cmake(KF6XmlGui)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  pkgconfig(md4c)

Requires:       qt6qml(org.kde.iconthemes)
Requires:       qt6qml(org.kde.kirigami)
Requires:       qt6qml(org.kde.kirigamiaddons.delegates)
Requires:       qt6qml(org.kde.kitemmodels)
Requires:       qt6qml(org.kde.sonnet)

%description
Francis uses the well-known pomodoro technique to help you get more productive.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/*.desktop

%find_lang %{name}

%files -f %{name}.lang
%license LICENSES/*.txt
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.%{name}.svg
%{_kf6_datadir}/qlogging-categories6/marknote.categories
%{_kf6_metainfodir}/org.kde.%{name}.metainfo.xml

%changelog
* Wed Aug 28 2024 Pavel Solovev <daron439@gmail.com> - 1.3.0-2
- rebuilt

* Wed Jul 17 2024 Pavel Solovev <daron439@gmail.com> - 1.3.0-1
- new version

* Wed May 22 2024 Pavel Solovev <daron439@gmail.com> - 1.2.1-1
- new version

* Mon Apr 01 2024 Pavel Solovev <daron439@gmail.com> - 1.1.1-1
- Update to 1.1.1

* Sat Mar 30 2024 Pavel Solovev <daron439@gmail.com> - 1.0.0-1
- Initial build
