%global framework kimageformats

Name:           kf6-%{framework}
Version:        6.3.0
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 1 addon with additional image plugins for QtGui
License:        LGPLv2+
URL:            https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig(libavif)
BuildRequires:  cmake(OpenEXR)
BuildRequires:  cmake(Imath)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  pkgconfig(libheif)
BuildRequires:	pkgconfig(libjxl) >= 0.7.0
BuildRequires:	pkgconfig(libjxl_threads) >= 0.7.0
BuildRequires:	pkgconfig(libraw)
BuildRequires:	pkgconfig(libraw_r)

Requires:       kf6-filesystem

%description
This framework provides additional image format plugins for QtGui.  As
such it is not required for the compilation of any other software, but
may be a runtime requirement for Qt-based software to support certain
image formats.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6 -DKIMAGEFORMATS_HEIF=ON
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_qtplugindir}/imageformats/*.so

%changelog
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
