Name:    pulseaudio-qt
Summary: Qt bindings for PulseAudio
Version: 1.9.0
Release: 1%{?dist}

License: CC0-1.0 AND LGPL-2.1-only AND LGPL-3.0-only
URL:     https://invent.kde.org/libraries/pulseaudio-qt
Source:  https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6DBus)

%description
Pulseaudio-Qt is a library providing Qt bindings to PulseAudio.

%package qt6
Summary: Qt6 bindings for PulseAudio
%description qt6
%{summary}.

%package qt6-devel
Summary: Development files for %{name} (Qt6)
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}
%description qt6-devel
%{summary}.


%prep
%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%files qt6
%license LICENSES/*.txt
%doc README.md
%{_kf6_libdir}/libKF6PulseAudioQt.so.5
%{_kf6_libdir}/libKF6PulseAudioQt.so.%{version}

%files qt6-devel
%{_kf6_includedir}/KF6PulseAudioQt/
%{_kf6_includedir}/pulseaudioqt_version.h
%{_kf6_libdir}/cmake/KF6PulseAudioQt/
%{_kf6_libdir}/libKF6PulseAudioQt.so
%{_kf6_libdir}/pkgconfig/KF6PulseAudioQt.pc
%{_qt6_metatypesdir}/qt6kf6pulseaudioqt_metatypes.json

%changelog
* Fri Sep 18 2026 Zakir Zamirov <268826384+solopashachas@users.noreply.github.com> - 1.9.0-1
- new version

* Thu Jul 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_45_Mass_Rebuild

* Wed Mar 25 2026 Steve Cossette <farchord@gmail.com> - 1.8.1-1
- 1.8.1

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 09 2025 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1.7.0-1
- 1.7.0
- Drop qt5 subpackages as upstream dropped support for it

* Mon Nov 18 2024 Alessandro Astone <ales.astone@gmail.com> - 1.6.1-1
- new version

* Fri Sep 13 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1.6.0-1
- 1.6.0

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri May 24 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1.5.0-1
- 1.5.0

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Alessandro Astone <ales.astone@gmail.com> - 1.4.0-2
- 1.4.0
- Add qt6-doc package for Qt6 API
- Release number 2 because we should always be ahead of f39 for the obsoletion path

* Tue Nov 21 2023 Steve Cossette <farchord@gmail.com> - 1.3^20231120.081305.36f5625-2
- Fixing bad requirements

* Tue Nov 21 2023 Steve Cossette <farchord@gmail.com> - 1.3^20231120.081305.36f5625-1
- Qt6 Build

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 05 2021 Onuralp Sezer <thunderbirdtr@fedoraproject.org> - 1.3-1
- update to new version 1.3

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 10 2020 Rex Dieter <rdieter@fedoraproject.org> - 1.2-4
- use new %%cmake macros

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 30 2020 Rex Dieter <rdieter@fedoraproject.org> - 1.2-1
- first try

