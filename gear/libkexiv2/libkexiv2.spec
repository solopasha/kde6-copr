%global commit0 7e3a08807b3089822b2a2c618a5a07b35bbef154
%global shortcommit0 %{sub %{commit0} 1 7}
%global bumpver 5

Name:    libkexiv2
Summary: A wrapper around Exiv2 library
Version: 26.11.70%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release: 1%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later
URL:     https://invent.kde.org/graphics/%{name}
%apps_source

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Core5Compat)
BuildRequires: pkgconfig(exiv2)


%global _description %{expand:
Libkexiv2 is a wrapper around Exiv2 library to manipulate pictures metadata
as EXIF IPTC and XMP.}

%description %{_description}

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
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%files qt6
%doc AUTHORS README
%license LICENSES/*
%{_datadir}/qlogging-categories6/*%{name}.*
%{_libdir}/libKExiv2Qt6.so.*

%files qt6-devel
%{_libdir}/libKExiv2Qt6.so
%{_includedir}/KExiv2Qt6/
%{_libdir}/cmake/KExiv2Qt6/


%changelog
%{?kde_snapshot_changelog_entry}
* Fri Dec 06 2024 Pavel Solovev <daron439@gmail.com> - 24.12.0-1
- Update to 24.12.0

* Tue Nov 05 2024 Pavel Solovev <daron439@gmail.com> - 24.08.3-1
- Update to 24.08.3

* Mon Oct 07 2024 Pavel Solovev <daron439@gmail.com> - 24.08.2-1
- Update to 24.08.2

* Tue Sep 10 2024 Pavel Solovev <daron439@gmail.com> - 24.08.1-1
- Update to 24.08.1

* Fri Aug 16 2024 Pavel Solovev <daron439@gmail.com> - 24.08.0-1
- Update to 24.08.0

* Fri Aug 09 2024 Pavel Solovev <daron439@gmail.com> - 24.07.90-1
- Update to 24.07.90

* Thu Jul 25 2024 Pavel Solovev <daron439@gmail.com> - 24.07.80-1
- Update to 24.07.80

* Thu Jul 04 2024 Pavel Solovev <daron439@gmail.com> - 24.05.2-1
- Update to 24.05.2

* Thu Jun 13 2024 Pavel Solovev <daron439@gmail.com> - 24.05.1-1
- Update to 24.05.1

* Thu May 23 2024 Pavel Solovev <daron439@gmail.com> - 24.05.0-1
- Update to 24.05.0

* Fri Apr 26 2024 Pavel Solovev <daron439@gmail.com> - 24.04.80-1
- Update to 24.04.80

* Thu Apr 11 2024 Pavel Solovev <daron439@gmail.com> - 24.02.2-1
- Update to 24.02.2

* Thu Mar 21 2024 Pavel Solovev <daron439@gmail.com> - 24.02.1-1
- Update to 24.02.1

* Tue Nov 14 2023 Alessandro Astone <ales.astone@gmail.com> - 24.01.75-2
- Initial Release
