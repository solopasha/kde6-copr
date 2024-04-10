%global commit0 afb984df1e42467e25c5f46316e45a5ea2545f54
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

%global		framework kcodecs

Name:		kf6-%{framework}
Version:	6.3.0%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:	1%{?dist}
Summary:	KDE Frameworks 6 Tier 1 addon with string manipulation methods
License:	BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND MIT AND MPL-1.1
URL:		https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:	fdupes
BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	gperf
BuildRequires:	extra-cmake-modules
BuildRequires:	kf6-rpm-macros
BuildRequires:	qt6-qtbase-devel
BuildRequires:	qt6-qttools-devel

Requires:	kf6-filesystem

%description
KDE Frameworks 6 Tier 1 addon with string manipulation methods.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	qt6-qtbase-devel
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%qch_package

%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang_kf6 kcodecs6_qt
%fdupes LICENSES

%files -f kcodecs6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6Codecs.so.6
%{_kf6_libdir}/libKF6Codecs.so.%{lua: print((macros.version:gsub('[%^~].*', '')))}

%files devel
%{_qt6_docdir}/*.tags
%{_kf6_includedir}/KCodecs/
%{_kf6_libdir}/cmake/KF6Codecs/
%{_kf6_libdir}/libKF6Codecs.so

%changelog
%{?kde_snapshot_changelog_entry}
* Wed Mar 20 2024 Pavel Solovev <daron439@gmail.com> - 6.0.0-2
- qmlcache rebuild

* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Mon Sep 25 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230829.232811.ea56b58-1
- Initial release
