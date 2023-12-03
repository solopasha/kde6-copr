Name:     skanpage
Version:  24.01.80
Release:  1%{?dist}
Summary:  Utility to scan images and multi-page documents
# For a breakdown of the licensing, see PACKAGE-LICENSING
License:  GPLv3 and GPLv2 and CC0-1.0 and BSD
URL:      https://invent.kde.org/utilities/%{name}
%apps_source

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6Purpose)
BuildRequires:  cmake(KF6XmlGui)

BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Widgets)

Recommends: sane-backends-drivers-scanners

%description
Skanpage is a multi-page scanning application built
using the libksane library and a QML interface.
It supports saving to image and PDF files.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%find_lang %{name}


%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml


%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_kf6_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_kf6_datadir}/qlogging-categories6/%{name}.categories
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml

%changelog
* Wed Oct 25 2023 Vasiliy Glazov <vascom2@gmail.com> - 23.08.2-2
- Added requires kquickimageeditor

* Thu Oct 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.2-1
- 23.08.2

* Sat Sep 16 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.1-1
- 23.08.1

* Sat Aug 26 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.0-1
- 23.08.0

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.3-1
- 23.04.3

* Tue Jun 06 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.2-1
- 23.04.2

* Sat May 13 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.1-1
- 23.04.1

* Fri Apr 14 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.0-1
- 23.04.0

* Fri Mar 31 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.90-1
- 23.03.90

* Mon Mar 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.80-1
- 23.03.80

* Thu Mar 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 22.12.3-1
- 22.12.3

* Tue Jan 31 2023 Marc Deop <marcdeop@fedoraproject.org> - 22.12.2-1
- 22.12.2

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 Justin Zobel <justin@1707.io> - 22.12.1-1
- Update to 22.12.1

* Sun Dec 25 2022 Justin Zobel <justin@1707.io> - 22.12.0-1
- Update to 22.12.0

* Thu Jul 28 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 22.04.3-3
- sane-backends-drivers-scanners recommendation for additional scanner added.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Than Ngo <than@redhat.com> - 22.04.3-1
- 22.04.3

* Sun May 15 2022 Justin Zobel <justin@1707.io> - 22.04.1-1
- Update to 22.04.1

* Sun Feb 27 2022 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 1.0-1
- Initial package for skapage 1.0
