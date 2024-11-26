Name:           ruqola
Version:        2.3.2
Release:        1%{?dist}
Summary:        KDE client for Rocket Chat

License:        LGPL-2.0-or-later
URL:            https://invent.kde.org/network/ruqola
Source:         https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
Source:         https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz.sig
Source:         kde-frameworks-signing-keys.pgp

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib

BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6IdleTime)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NetworkManagerQt)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6NotifyConfig)
BuildRequires:  cmake(KF6Prison)
BuildRequires:  cmake(KF6Purpose)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6Sonnet)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6UserFeedback)
BuildRequires:  cmake(KF6XmlGui)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6MultimediaWidgets)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6NetworkAuth)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6WebSockets)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake(KF6TextAutoCorrectionWidgets)
BuildRequires:  cmake(KF6TextCustomEditor)
BuildRequires:  cmake(KF6TextEditTextToSpeech)
BuildRequires:  cmake(KF6TextEmoticonsWidgets)
BuildRequires:  cmake(KF6TextTranslator)
BuildRequires:  cmake(KF6TextUtils)
# BuildRequires:  cmake(KLLMWidgets)
BuildRequires:  cmake(PlasmaActivities)
BuildRequires:  cmake(Qt6Keychain)

%description
%{summary}.

%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -p1

%build
%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-html

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%license LICENSES/LGPL-2.0-or-later.txt
%doc README.md
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}.png
%{_kf6_datadir}/knotifications6/%{name}.notifyrc
%{_kf6_datadir}/messageviewer/openurlwith/ruqola.openurl
%{_kf6_datadir}/qlogging-categories6/%{name}.*
%{_kf6_libdir}/libcmark-rc-copy.so.0*
%{_kf6_libdir}/librocketchatrestapi-qt.so.{0,%{version}}
%{_kf6_libdir}/libruqolacore.so.{0,%{version}}
%{_kf6_libdir}/libruqolawidgets.so.{0,%{version}}
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_qt6_plugindir}/ruqolaplugins/

%changelog
%autochangelog
