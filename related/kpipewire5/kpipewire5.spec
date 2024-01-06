Name:    kpipewire5
Summary: Set of convenient classes to use PipeWire in Qt projects
Version: 5.27.10
Release: 2%{?dist}

License: LGPLv2+
URL:     https://invent.kde.org/plasma/kpipewire

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/plasma/%{version}/kpipewire-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Wayland)
BuildRequires:  plasma-wayland-protocols-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtwayland-devel

BuildRequires:  libavcodec-free-devel
BuildRequires:  libavutil-free-devel
BuildRequires:  libavformat-free-devel
BuildRequires:  libepoxy-devel
BuildRequires:  libdrm-devel
BuildRequires:  libswscale-free-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  pipewire-devel
BuildRequires:  wayland-devel

Requires:       kf5-filesystem

%description
It is developed in C++ and it's main use target is QML components.
As it's what's been useful, this framework focuses on graphical PipeWire
features. If it was necessary, these could be included.

At the moment we offer two main components:

- KPipeWire: offers the main components to connect to and render
PipeWire into your app.
- KPipeWireRecord: using FFmpeg, helps to record a PipeWire video stream
into a file.

%package        devel
Summary:        Development files for %{name}
# This requires pipewire headers to be installed
Requires:       pipewire-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
# This conflicts with kpipewire-devel
Conflicts:      kpipewire-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n kpipewire-%{version}

%build
%cmake_kf5

%cmake_build


%install
%cmake_install

%find_lang kpipewire --with-qt --all-name

%ldconfig_scriptlets

%files -f kpipewire.lang
%license LICENSES/*
%{_libdir}/libKPipeWire.so.*
%{_libdir}/libKPipeWireRecord.so.*
%{_libdir}/libKPipeWireDmaBuf.so.*
%{_qt5_qmldir}/org/kde/pipewire/*
%{_kf5_datadir}/qlogging-categories5/*.categories

%files devel
%{_libdir}/libKPipeWire.so
%{_libdir}/libKPipeWireRecord.so
%{_libdir}/libKPipeWireDmaBuf.so
%dir %{_includedir}/KPipeWire
%{_includedir}/KPipeWire/*
%dir %{_libdir}/cmake/KPipeWire
%{_libdir}/cmake/KPipeWire/*.cmake

%changelog
* Mon Jan 01 2024 Neal Gompa <ngompa@fedoraproject.org> - 5.27.10-2
- Rename to kpipewire5 to ship the Qt5/KF5 version

* Sat Dec 16 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.10-1
- 5.27.10

* Tue Oct 24 2023 Steve Cossette <farchord@gmail.com> - 5.27.9-1
- 5.27.9

* Tue Sep 12 2023 justin.zobel@gmail.com - 5.27.8-1
- 5.27.8

* Tue Aug 01 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.7-1
- 5.27.7

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.27.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jun 25 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.6-1
- 5.27.6

* Wed May 10 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.5-1
- 5.27.5

* Tue Apr 04 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.4-1
- 5.27.4

* Tue Mar 14 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.3-1
- 5.27.3

* Sun Mar 12 2023 Neal Gompa <ngompa@fedoraproject.org> - 5.27.2-2
- Rebuild for ffmpeg 6.0

* Tue Feb 28 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.2-1
- 5.27.2

* Tue Feb 21 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.27.1-1
- 5.27.1

* Thu Feb 09 2023 Marc Deop <marcdeop@fedoraproject.org> - 5.27.0-1
- 5.27.0

* Mon Jan 30 2023 Neal Gompa <ngompa@fedoraproject.org> - 5.26.90-3
- Add patch to use VP8 on WebM for screen recording by default

* Thu Jan 26 2023 Neal Gompa <ngompa@fedoraproject.org> - 5.26.90-2
- Add dependency on pipewire-devel for devel subpackage

* Thu Jan 19 2023 Marc Deop <marcdeop@fedoraproject.org> - 5.26.90-1
- 5.26.90

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.26.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 05 2023 Justin Zobel <justin@1707.io> - 5.26.5-1
- Update to 5.26.5

* Tue Nov 29 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.26.4-1
- 5.26.4

* Wed Nov 09 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.26.3-1
- 5.26.3

* Wed Oct 26 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.26.2-1
- 5.26.2

* Thu Oct 06 2022 Marc Deop <marcdeop@fedoraproject.org> - 5.26.0-1
- 5.26.0

* Mon Sep 19 2022 Jan Grulich <jgrulich@redhat.com> - 5.25.90-1
- Initial package
