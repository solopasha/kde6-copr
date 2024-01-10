Name:          kontrast
Version:       24.01.90
Release:       1%{?dist}
Summary:       Color contrast checker
# BSD, CC0 are only for build files
License:       GPL-3.0-only AND GPL-3.0-or-later AND CC-BY-SA-4.0
URL:           https://apps.kde.org/kontrast/
%apps_source

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf6-rpm-macros
BuildRequires: libappstream-glib

BuildRequires: cmake(FutureSQL6)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(QCoro6Core)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Widgets)

Requires:      hicolor-icon-theme
Requires:      kf6-filesystem
# QML dependencies
Requires:      kf6-kirigami2%{?_isa}
Requires:      kf6-kirigami-addons%{?_isa}

%description
Kontrast is a color contrast checker and tell you if your color combinations
are accessible for people with color vision deficiencies.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%find_lang %{name} --with-html


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop


%files  -f %{name}.lang
%doc README.md
%license LICENSES/CC-BY* LICENSES/GPL-*
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/*/*/org.kde.%{name}.*
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml


%changelog
* Thu Nov 23 2023 Yaakov Selkowitz <yselkowitz@fedoraproject.org> - 24.01.75-1
- 24.01.75

* Fri Oct 13 2023 Yaakov Selkowitz <yselkowitz@fedoraproject.org> - 23.08.2-1
- Initial build
