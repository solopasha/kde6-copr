Name:           klevernotes
Version:        1.1.0
Release:        1%{?dist}
License:        LGPL-2.0-or-later AND BSD-3-Clause AND GPL-2.0-or-later AND CC0-1.0
Summary:        A note-taking and management application using markdown
URL:            https://invent.kde.org/office/klevernotes
Source0:        https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz.sig
Source2:        signing-key.pgp

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Kirigami)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6WebEngineQuick)

Requires:       qt6qml(org.kde.kirigami)
Requires:       qt6qml(org.kde.kirigamiaddons.components)
Requires:       qt6qml(org.kde.kitemmodels)

Provides:       bundled(md4qt) = 4.0.0

%description
%{summary}.

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
%{_kf6_metainfodir}/org.kde.%{name}.metainfo.xml

%changelog
* Mon Oct 14 2024 Pavel Solovev <daron439@gmail.com> - 1.1.0-1
- Initial build
