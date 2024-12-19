%global commit0 b649cca3040feb76bb7116451c2d374068ee00c1
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 4

%global framework kimageformats

Name:           kf6-%{framework}
Version:        6.10.0%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 1 addon with additional image plugins for QtGui
License:        LGPLv2+
URL:            https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(KF6Archive)

BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6PrintSupport)

BuildRequires:  pkgconfig(libjxl_threads)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libraw_r)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  cmake(Imath)
BuildRequires:  cmake(OpenEXR)
BuildRequires:  pkgconfig(libavif)
BuildRequires:  pkgconfig(libheif)
BuildRequires:  pkgconfig(zlib)

Requires:       kf6-filesystem

%description
This framework provides additional image format plugins for QtGui.  As
such it is not required for the compilation of any other software, but
may be a runtime requirement for Qt-based software to support certain
image formats.

%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1

%build
%cmake_kf6 -DKIMAGEFORMATS_HEIF=ON
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_qtplugindir}/imageformats/kimg_ani.so
%{_kf6_qtplugindir}/imageformats/kimg_avif.so
%{_kf6_qtplugindir}/imageformats/kimg_eps.so
%{_kf6_qtplugindir}/imageformats/kimg_exr.so
%{_kf6_qtplugindir}/imageformats/kimg_hdr.so
%{_kf6_qtplugindir}/imageformats/kimg_heif.so
%{_kf6_qtplugindir}/imageformats/kimg_jxl.so
%{_kf6_qtplugindir}/imageformats/kimg_kra.so
%{_kf6_qtplugindir}/imageformats/kimg_ora.so
%{_kf6_qtplugindir}/imageformats/kimg_pcx.so
%{_kf6_qtplugindir}/imageformats/kimg_pfm.so
%{_kf6_qtplugindir}/imageformats/kimg_pic.so
%{_kf6_qtplugindir}/imageformats/kimg_psd.so
%{_kf6_qtplugindir}/imageformats/kimg_pxr.so
%{_kf6_qtplugindir}/imageformats/kimg_qoi.so
%{_kf6_qtplugindir}/imageformats/kimg_ras.so
%{_kf6_qtplugindir}/imageformats/kimg_raw.so
%{_kf6_qtplugindir}/imageformats/kimg_rgb.so
%{_kf6_qtplugindir}/imageformats/kimg_sct.so
%{_kf6_qtplugindir}/imageformats/kimg_tga.so
%{_kf6_qtplugindir}/imageformats/kimg_xcf.so

%changelog
%{?kde_snapshot_changelog_entry}
* Fri Dec 06 2024 Pavel Solovev <daron439@gmail.com> - 6.9.0-1
- Update to 6.9.0

* Sat Nov 02 2024 Pavel Solovev <daron439@gmail.com> - 6.8.0-1
- Update to 6.8.0

* Fri Oct 04 2024 Pavel Solovev <daron439@gmail.com> - 6.7.0-1
- Update to 6.7.0

* Fri Sep 06 2024 Pavel Solovev <daron439@gmail.com> - 6.6.0-1
- Update to 6.6.0

* Fri Aug 09 2024 Pavel Solovev <daron439@gmail.com> - 6.5.0-1
- Update to 6.5.0

* Fri Jul 12 2024 Pavel Solovev <daron439@gmail.com> - 6.4.0-1
- Update to 6.4.0

* Fri Jun 07 2024 Pavel Solovev <daron439@gmail.com> - 6.3.0-1
- Update to 6.3.0

* Sun Jun 02 2024 Pavel Solovev <daron439@gmail.com> - 6.2.0-1.1
- rebuild for f40

* Sun May 12 2024 Pavel Solovev <daron439@gmail.com> - 6.2.0-1
- Update to 6.2.0

* Fri Apr 12 2024 Pavel Solovev <daron439@gmail.com> - 6.1.0-1
- Update to 6.1.0

* Wed Mar 20 2024 Pavel Solovev <daron439@gmail.com> - 6.0.0-2
- qmlcache rebuild

* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Tue Oct 03 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230925.210237.d932e0d-1
- Initial Release
