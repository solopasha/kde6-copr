Name:    kquickimageeditor
Version: 0.7.0.1
Release: 2%{?dist}
Summary: QtQuick components providing basic image editing capabilities
License: BSD-2-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only
URL:     https://invent.kde.org/libraries/%{name}
%kde_meta
BuildSystem:    cmake_kf6

Patch:   fix.diff

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6ShaderTools)

BuildRequires: cmake(KF6Config)

BuildRequires: cmake(hwy)

%description
%{summary}

%package qt6
Summary: Qt6 QtQuick components providing basic image editing capabilities

%description qt6
%{summary}

%package qt6-devel
Summary: Development files for %{name}-qt6
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}

%description qt6-devel
The %{name}-qt6-devel package contains cmake and mkspecs for developing
applications that use %{name}-qt6.

%files qt6
%{_kf6_qmldir}/org/kde/kquickimageeditor/
%{_kf6_libdir}/libKQuickImageEditor.so.0.7.0
%{_kf6_libdir}/libKQuickImageEditor.so.1

%files qt6-devel
%{_kf6_libdir}/libKQuickImageEditor.so
%{_kf6_libdir}/cmake/KQuickImageEditor
%{_includedir}/KQuickImageEditor/
%{_kf6_archdatadir}/mkspecs/modules/qt_KQuickImageEditor.pri

%changelog
* Sat Oct 03 2026 Zakir Zamirov <268826384+solopashachas@users.noreply.github.com> - 0.7.0.1-1
- new version

* Tue Sep 01 2026 Zakir Zamirov <268826384+solopashachas@users.noreply.github.com> - 0.7.0-1
- new version

* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Thu May 14 2026 Jan Grulich <jgrulich@redhat.com> - 0.6.0-6
- Rebuild (qt6)

* Thu Apr 16 2026 Jan Grulich <jgrulich@redhat.com> - 0.6.0-5
- Rebuild (qt6)

* Thu Jan 29 2026 Nicolas Chauvet <kwizart@gmail.com> - 0.6.0-4
- Rebuilt for OpenCV 4.13

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Dec 11 2025 Nicolas Chauvet <kwizart@gmail.com> - 0.6.0-2
- Rebuilt for OpenCV-4.12

* Sun Nov 16 2025 Steve Cossette <farchord@gmail.com> - 0.6.0-1
- 0.6.0

* Wed Oct 01 2025 Jan Grulich <jgrulich@redhat.com> - 0.5.0-4
- Rebuild (qt6)

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Mar 27 2025 Jan Grulich <jgrulich@redhat.com> - 0.5.0-2
- Rebuild (qt6)

* Sat Jan 18 2025 Steve Cossette <farchord@gmail.com> - 0.5.0-1
- 0.5.0

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.0-5
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 27 2023 Yaakov Selkowitz <yselkowitz@fedoraproject.org> - 0.3.0-1
- 0.3.0
- Create parallel qt5 and qt6 builds

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

