%global commit0 1001e9fcebe265564b8d61f7cfc16eb90585c454
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

%global		framework sonnet

Name:		kf6-%{framework}
Version:	6.0.0%{?bumpver:^%{bumpver}.git%{shortcommit0}}
Release:	1%{?dist}
Summary:	KDE Frameworks 6 Tier 1 solution for spell checking
License:	BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:		https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:	appstream
BuildRequires:	extra-cmake-modules
BuildRequires:	kf6-rpm-macros
BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	qt6-qtbase-devel
BuildRequires:	qt6-qtdeclarative-devel
BuildRequires:	qt6-qttools-devel
BuildRequires:	zlib-devel
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	pkgconfig(hunspell)
BuildRequires:	pkgconfig(aspell)
BuildRequires:	pkgconfig(libvoikko)
BuildRequires:	hspell-devel

Requires:	kf6-filesystem
Recommends:	hunspell

%description
KDE Frameworks 6 Tier 1 solution for spell checking.

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
%find_lang_kf6 sonnet6_qt

%files -f sonnet6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6SonnetCore.so.6
%{_kf6_libdir}/libKF6SonnetCore.so.%{lua: print((macros.version:gsub('[%^~].*', '')))}
%{_kf6_bindir}/parsetrigrams6
%{_kf6_qmldir}/org/kde/sonnet/
%dir %{_kf6_plugindir}/sonnet
%{_kf6_plugindir}/sonnet/sonnet_hunspell.so
%{_kf6_plugindir}/sonnet/sonnet_voikko.so
%{_kf6_plugindir}/sonnet/sonnet_hspell.so
%{_kf6_plugindir}/sonnet/sonnet_aspell.so
%{_kf6_libdir}/libKF6SonnetUi.so.6
%{_kf6_libdir}/libKF6SonnetUi.so.%{lua: print((macros.version:gsub('[%^~].*', '')))}
%{_kf6_qtplugindir}/designer/*6widgets.so

%files devel
%{_qt6_docdir}/*.tags
%doc README.md
%license LICENSES/*.txt
%{_kf6_includedir}/Sonnet/
%{_kf6_includedir}/SonnetCore/
%{_kf6_includedir}/SonnetUi/
%{_kf6_libdir}/cmake/KF6Sonnet/
%{_kf6_libdir}/libKF6SonnetCore.so
%{_kf6_libdir}/libKF6SonnetUi.so


%changelog
* Wed Mar 20 2024 Pavel Solovev <daron439@gmail.com> - 6.0.0-2
- qmlcache rebuild

* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Sun Sep 24 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230920.235103.01f7019-1
- Initial release
