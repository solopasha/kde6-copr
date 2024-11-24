%global commit0 e5958faa53dc05ded9b124a344e435c9b573704b
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 3

%global framework sonnet

Name:           kf6-%{framework}
Version:        6.9.0%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 1 solution for spell checking
License:        BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:	cmake
BuildRequires:	extra-cmake-modules
BuildRequires:	gcc-c++
BuildRequires:	kf6-rpm-macros

BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Widgets)

BuildRequires:	hspell-devel
BuildRequires:	pkgconfig(aspell)
BuildRequires:	pkgconfig(hunspell)
BuildRequires:	pkgconfig(libvoikko)
BuildRequires:	zlib-devel

Requires:	    kf6-filesystem
Recommends:	    %{name}-hunspell

%description
KDE Frameworks 6 Tier 1 solution for spell checking.

%package        aspell
Summary:        aspell plugin for %{name}
Requires:       %{name} = %{version}-%{release}
%description    aspell
The %{name}-aspell package contains the aspell spellchecking
plugin for %{name}.

%package        hunspell
Summary:        hunspell plugin for %{name}
Requires:       %{name} = %{version}-%{release}
%description    hunspell
The %{name}-hunspell package contains the hunspell spellchecking
plugin for %{name}.

%package        hspell
Summary:        hspell plugin for %{name}
Supplements:    (%{name} and langpacks-he)
Requires:       %{name} = %{version}-%{release}
Requires:       hunspell-he
%description    hspell
The %{name}-hspell package contains the Hebrew hspell spellchecking
plugin for %{name}.

%package        voikko
Summary:        voikko plugin for %{name}
Supplements:    (%{name} and langpacks-fi)
Requires:       %{name} = %{version}-%{release}
%description    voikko
The %{name}-voikko package contains the Finnish voikko spellchecking
plugin for %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core)
%description    devel
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
%{_kf6_bindir}/parsetrigrams6
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6SonnetCore.so.%{version_no_git}
%{_kf6_libdir}/libKF6SonnetCore.so.6
%{_kf6_libdir}/libKF6SonnetUi.so.%{version_no_git}
%{_kf6_libdir}/libKF6SonnetUi.so.6
%{_kf6_qmldir}/org/kde/sonnet/
%{_kf6_qtplugindir}/designer/*6widgets.so
%dir %{_kf6_plugindir}/sonnet

%files aspell
%{_kf6_plugindir}/sonnet/sonnet_aspell.so

%files hunspell
%{_kf6_plugindir}/sonnet/sonnet_hunspell.so

%files hspell
%{_kf6_plugindir}/sonnet/sonnet_hspell.so

%files voikko
%{_kf6_plugindir}/sonnet/sonnet_voikko.so

%files devel
%{_kf6_includedir}/Sonnet/
%{_kf6_includedir}/SonnetCore/
%{_kf6_includedir}/SonnetUi/
%{_kf6_libdir}/cmake/KF6Sonnet/
%{_kf6_libdir}/libKF6SonnetCore.so
%{_kf6_libdir}/libKF6SonnetUi.so
%{_qt6_docdir}/*.tags

%changelog
%{?kde_snapshot_changelog_entry}
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

* Sun Jun 02 2024 Pavel Solovev <daron439@gmail.com> - 6.2.0-1.1.1
- rebuild for f40

* Sun May 12 2024 Pavel Solovev <daron439@gmail.com> - 6.2.0-1
- Update to 6.2.0

* Fri Apr 12 2024 Pavel Solovev <daron439@gmail.com> - 6.1.0-1
- Update to 6.1.0

* Wed Mar 20 2024 Pavel Solovev <daron439@gmail.com> - 6.0.0-2
- qmlcache rebuild

* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Sun Sep 24 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230920.235103.01f7019-1
- Initial release
