%global commit0 7020017321c46d88ab13dd8ba74c57307fe66ac3
%global shortcommit0 %{sub %{commit0} 1 7}
%global bumpver 9

Name:           dragon-media-backend
Version:        0.83.0%{?bumpver:^%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
Summary:        Qt audio playback library for desktop music players
License:        (LGPL-2.1-only OR LGPL-3.0-only) AND MIT
URL:            https://invent.kde.org/libraries/dragon-media-backend
%kde_meta

BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(QCoro6Core)
BuildRequires:  cmake(QCoro6Network)
BuildRequires:  cmake(SDL3)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlIntegration)

BuildRequires:  pkgconfig(kissfft-float)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libswresample)

%description
Dragon Media Backend is a Qt audio playback library for desktop music players.
It provides FFmpeg decoding, PipeWire, PulseAudio and SDL audio output, spectrum
analysis, KIO access, audio CD playback and ICY metadata for radio streams.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core)
Requires:       cmake(Qt6QmlIntegration)

%description    devel
Headers and CMake configuration files for developing applications that use
Dragon Media Backend.

%prep
%autosetup -n %{sourcerootdir} -p1

%build
%cmake_kf6 \
    -DBUILD_EXAMPLES=OFF \
    -DCMAKE_SKIP_INSTALL_RPATH=ON \
    -DFETCHCONTENT_FULLY_DISCONNECTED=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSES/*.txt
%doc README.md
%{_kf6_datadir}/qlogging-categories6/dragonmediabackend.categories
%{_kf6_libdir}/libDragonMediaBackend.so.0
%{_kf6_libdir}/libDragonMediaBackend.so.0.*
%{_kf6_metainfodir}/org.kde.dragonmediabackend.metainfo.xml
%{_kf6_qmldir}/org/kde/dragonmediabackend/
%{_qt6_plugindir}/DragonMediaBackend/

%files devel
%{_includedir}/DragonMediaBackend/
%{_kf6_libdir}/cmake/DragonMediaBackend/
%{_kf6_libdir}/libDragonMediaBackend.so

%changelog
%{?kde_snapshot_changelog_entry}
