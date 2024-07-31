Name:           rkward
Version:        0.8.0
Release:        1%{?dist}
Summary:        Graphical frontend for R language

License:        GPL-2.0-or-later AND MIT
URL:            https://%{name}.kde.org/
Source:         https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.gz
Source:         https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.gz.sig
Source:         signing-key.pgp

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  kf6-rpm-macros
BuildRequires:  R-core-devel

BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6BreezeIcons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6TextEditor)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)

Requires:       hicolor-icon-theme
Requires:       shared-mime-info

Provides:       bundled(kdsingleapplication)

%description
RKWard aims to provide an easily extensible, easy to use IDE/GUI for the
R-project. RKWard tries to combine the power of the R-language with the
(relative) ease of use of commercial statistics tools. Long term plans
include integration with office suites

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop

%find_lang %{name} --all-name --with-kde --with-html --with-man

%files -f %{name}.lang
%license LICENSES/GPL-2.0-or-later.txt LICENSES/MIT.txt
%doc README
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/%{name}/
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}.*
%{_kf6_datadir}/kio/servicemenus/%{name}.protocol
%{_kf6_datadir}/ktexteditor_snippets/data/RKWard*.xml
%{_kf6_datadir}/metainfo/org.kde.%{name}.metainfo.xml
%{_kf6_datadir}/mime/packages/vnd.kde.rkward-output.xml
%{_kf6_datadir}/mime/packages/vnd.kde.rmarkdown.xml
%{_kf6_datadir}/mime/packages/vnd.rkward.r.xml
%{_kf6_libdir}/librkward.rbackend.lib.so
%{_kf6_mandir}/man1/%{name}.1*
%{_libexecdir}/%{name}.rbackend

%changelog
* Wed Jul 31 2024 Pavel Solovev <daron439@gmail.com> - 0.8.0-1
- new version

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 25 2024 Iñaki Úcar <iucar@fedoraproject.org> - 0.7.5-4
- R-maint-sig mass rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Sep 09 2023 Iñaki Úcar <iucar@fedoraproject.org> - 0.7.5-1
- update to 0.7.5
- switch to SPDX

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild
