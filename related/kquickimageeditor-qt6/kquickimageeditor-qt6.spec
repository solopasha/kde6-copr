Name:    kquickimageeditor-qt6
Version: 0.3.0
Release: 1.1%{?dist}
Summary: QtQuick components providing basic image editing capabilities
License: GPLv2+
URL:     https://invent.kde.org/libraries/kquickimageeditor
Source:  https://invent.kde.org/libraries/kquickimageeditor/-/archive/v%{version}/kquickimageeditor-v%{version}.tar.gz
Patch:   https://invent.kde.org/libraries/kquickimageeditor/-/commit/dc9dbee60a0ec827c58670666d14f7d233e03755.patch

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Quick)

%description
%{summary}

%package        devel
Summary:        Development files for %{name}
Conflicts:      kquickimageeditor-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
%{summary}.


%prep
%autosetup -n kquickimageeditor-v%{version} -p1


%build
%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build


%install
%cmake_install


%files
%{_kf6_qmldir}/org/kde/kquickimageeditor/

%files devel
%{_kf6_libdir}/cmake/KQuickImageEditor/
%{_kf6_libdir}/qt6/mkspecs/modules/qt_KQuickImageEditor.pri


%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 18 2021 Marc Deop <marcdeop@fedoraproject.org> - 0.2.0-1
- Upgrade to version 0.2.0.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 23 2020 Marc Deop <marcdeop@fedoraproject.org> - 0.1.2-1
- Initial package.

