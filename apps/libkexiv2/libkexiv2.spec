Name:    libkexiv2
Summary: A wrapper around Exiv2 library
Version: 24.01.90
Release: 1%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later
URL:     https://invent.kde.org/graphics/%{name}
%apps_source

BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Core5Compat)
BuildRequires: pkgconfig(exiv2)


%global _description %{expand:
Libkexiv2 is a wrapper around Exiv2 library to manipulate pictures metadata
as EXIF IPTC and XMP.}

%description %{_description}

%package qt5
Summary: Qt5 version of %{name}
Requires: kf5-filesystem
# Renamed from kf5-libkexiv2
Obsoletes: kf5-libkexiv2 < %{version}-%{release}
Provides:  kf5-libkexiv2 = %{version}-%{release}
%description qt5
%{_description}

%package qt5-devel
Summary:  Development files for %{name}-qt5
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
Requires: cmake(Qt5Gui)
Obsoletes: kf5-libkexiv2-devel < %{version}-%{release}
Provides:  kf5-libkexiv2-devel = %{version}-%{release}
%description qt5-devel
%{summary}.

%package qt6
Summary: Qt6 version of %{name}
%description qt6
%{_description}

%package qt6-devel
Summary:  Development files for %{name}-qt6
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}
Requires: cmake(Qt6Gui)
%description qt6-devel
%{summary}.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1


%build
%global _vpath_builddir %{_target_platform}-qt5
%cmake_kf5 -DBUILD_WITH_QT6=OFF
%cmake_build

%global _vpath_builddir %{_target_platform}-qt6
%cmake_kf6 -DBUILD_WITH_QT6=ON
%cmake_build

%install
%global _vpath_builddir %{_target_platform}-qt5
%cmake_install

%global _vpath_builddir %{_target_platform}-qt6
%cmake_install


%files qt6
%doc AUTHORS README
%license LICENSES/*
%{_datadir}/qlogging-categories6/*%{name}.*
%{_libdir}/libKExiv2Qt6.so.*

%files qt5
%{_kf5_datadir}/qlogging-categories5/*%{name}.*
%{_kf5_libdir}/libKF5KExiv2.so.*

%files qt6-devel
%{_libdir}/libKExiv2Qt6.so
%{_includedir}/KExiv2Qt6/
%{_libdir}/cmake/KExiv2Qt6/

%files qt5-devel
%{_kf5_libdir}/libKF5KExiv2.so
%{_kf5_includedir}/KExiv2/
%{_kf5_libdir}/cmake/KF5KExiv2/


%changelog
* Tue Nov 14 2023 Alessandro Astone <ales.astone@gmail.com> - 24.01.75-2
- Initial Release
