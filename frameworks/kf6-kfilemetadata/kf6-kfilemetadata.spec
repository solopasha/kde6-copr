%global commit0 6b48af6ceab64b8c339cb8c7d42ffc4a453568d7
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 2

%global framework kfilemetadata

Name:           kf6-%{framework}
Summary:        A Tier 2 KDE Framework for extracting file metadata
Version:        6.9.0%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}

License:        BSD-3-Clause AND CC0-1.0 AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-LGPL
URL:            https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)

BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Xml)

BuildRequires:  catdoc
BuildRequires:  cmake(QMobipocket6)
BuildRequires:  ebook-tools-devel
BuildRequires:  ffmpeg-free-devel
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(libattr)
BuildRequires:  pkgconfig(poppler-qt6)
BuildRequires:  pkgconfig(taglib)

Recommends:     catdoc

%description
%{summary}.

%package        devel
Summary:        Developer files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core)
%description    devel
%{summary}.

%qch_package

%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name
mkdir -p %{buildroot}%{_kf6_plugindir}/kfilemetadata/writers/

%files -f %{name}.lang
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}*
%{_kf6_libdir}/libKF6FileMetaData.so.%{version_no_git}
%{_kf6_libdir}/libKF6FileMetaData.so.3
%dir %{_kf6_plugindir}/kfilemetadata
%{_kf6_plugindir}/kfilemetadata/kfilemetadata_*.so
%dir %{_kf6_plugindir}/kfilemetadata/writers
%{_kf6_plugindir}/kfilemetadata/writers/kfilemetadata_taglibwriter.so

%files devel
%{_kf6_includedir}/KFileMetaData/
%{_kf6_libdir}/cmake/KF6FileMetaData/
%{_kf6_libdir}/libKF6FileMetaData.so
%{_qt6_docdir}/*.tags

%changelog
%{?kde_snapshot_changelog_entry}
* Sat Oct 05 2024 Pavel Solovev <daron439@gmail.com> - 6.7.0-2
- rebuilt

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

* Tue Oct 03 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231001.112804.6fcc94b-1
- Initial Release
