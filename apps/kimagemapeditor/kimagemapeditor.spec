Name:    kimagemapeditor
Summary: HTML Image Map Editor
Version: 24.02.1
Release: 1%{?dist}

License: GPL-2.0-or-later
URL:     https://invent.kde.org/graphics/kimagemapeditor
%apps_source

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: libappstream-glib

BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Crash)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5GuiAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Parts)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5XmlGui)

BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5WebEngineWidgets)
BuildRequires: cmake(Qt5Widgets)

%description
A tool to edit image maps of HTML files.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1


%build
%cmake_kf5
%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/*.desktop


%files -f %{name}.lang
%license COPYING
%{_kf5_bindir}/kimagemapeditor
%{_kf5_datadir}/applications/org.kde.kimagemapeditor.desktop
%{_kf5_datadir}/icons/hicolor/*/apps/kimagemapeditor.png
%{_kf5_datadir}/icons/hicolor/22x22/actions/*.png
%{_kf5_datadir}/icons/hicolor/scalable/apps/kimagemapeditor.svgz
%{_kf5_datadir}/kimagemapeditor/
%{_kf5_datadir}/kservices5/kimagemapeditorpart.desktop
%{_kf5_datadir}/qlogging-categories5/kimagemapeditor.categories
%{_kf5_metainfodir}/org.kde.kimagemapeditor.appdata.xml
%{_kf5_plugindir}/parts/kimagemapeditorpart.so


%changelog
* Thu Mar 21 2024 Pavel Solovev <daron439@gmail.com> - 24.02.1-1
- Update to 24.02.1
