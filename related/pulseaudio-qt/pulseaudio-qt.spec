Name:           pulseaudio-qt
Summary:        Qt bindings for PulseAudio
Version:        1.5.0
Release:        1%{?dist}

License:        CC0-1.0 AND LGPL-2.1-only AND LGPL-3.0-only
URL:            https://invent.kde.org/libraries/pulseaudio-qt
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        signing-key.pgp

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libpulse)

%description
Pulseaudio-Qt is a library providing Qt bindings to PulseAudio.

%package        qt6
Summary:        Qt6 bindings for PulseAudio
Obsoletes:      %{name} < 1.4.0-4
Provides:       %{name} = %{version}-%{release}
%description    qt6
%{summary}.

%package        qt6-devel
Summary:        Development files for %{name}
Obsoletes:      %{name}-devel < 1.4.0-4
Provides:       %{name}-devel = %{version}-%{release}
Requires:       %{name}-qt6%{?_isa} = %{version}-%{release}
%description    qt6-devel
%{summary}.

%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -p1

%build
%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build

%install
%cmake_install

%files qt6
%license LICENSES/*.txt
%doc README.md
%{_kf6_libdir}/libKF6PulseAudioQt.so.%{version}
%{_kf6_libdir}/libKF6PulseAudioQt.so.5

%files qt6-devel
%{_kf6_includedir}/KF6PulseAudioQt/
%{_kf6_includedir}/pulseaudioqt_version.h
%{_kf6_libdir}/cmake/KF6PulseAudioQt/
%{_kf6_libdir}/libKF6PulseAudioQt.so
%{_kf6_libdir}/pkgconfig/KF6PulseAudioQt.pc

%changelog
* Fri May 24 2024 Pavel Solovev <daron439@gmail.com> - 1.5.0-1
- new version

* Wed Mar 20 2024 Pavel Solovev <daron439@gmail.com> - 1.4.0-6
- qmlcache rebuild

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

