Name: ksnip
Version: 1.10.1
Release: 3%{?dist}

License: GPL-2.0-or-later
Summary: Qt based cross-platform screenshot tool
URL: https://github.com/%{name}/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch: kImageAnnotator-kColorPicker-Qt5.patch

# Workaround to Wayland issues: https://github.com/ksnip/ksnip/pull/457
Patch100: %{name}-wayland-workaround.patch

BuildRequires: cmake(kColorPicker-Qt5)
BuildRequires: cmake(kImageAnnotator-Qt5)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5PrintSupport)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5XmlPatterns)

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: ninja-build

Requires: hicolor-icon-theme

%description
Ksnip is a Qt based cross-platform screenshot tool that provides
many annotation features for your screenshots.

%prep
%autosetup -p1

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_TESTS:BOOL=OFF
%cmake_build

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%install
%cmake_install
%find_lang %{name} --with-qt

%files -f %{name}.lang
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_metainfodir}/*.appdata.xml

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 15 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 1.10.1-1
- Updated to version 1.10.1.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 23 2022 Vitaly Zaitsev <vitaly@easycoding.org> - 1.10.0-1
- Updated to version 1.10.0.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 23 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 1.9.2-1
- Updated to version 1.9.2.

* Tue Sep 14 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 1.9.1-1
- Updated to version 1.9.1.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May 25 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 1.9.0-1
- Updated to version 1.9.0.

* Tue Mar 23 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 1.8.2-1
- Updated to version 1.8.2.

* Mon Feb 15 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 1.8.1-1
- Updated to version 1.8.1.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 14 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.8.0-1
- Updated to version 1.8.0.

* Fri Nov 06 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.7.3-2
- Added patch with workaround to Wayland issues.

* Fri Jul 31 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.7.3-1
- Initial SPEC release.
