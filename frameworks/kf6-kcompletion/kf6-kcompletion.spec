%global commit0 6ddafe1e44a08b121ef4466f7b15f49da43581bd
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

%global framework kcompletion

Name:           kf6-%{framework}
Version:        6.3.0%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 2 addon with auto completion widgets and classes
# BSD-3-Clause is in the LICENSES folder but goes unused.
License:        CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  pkgconfig(Qt6Widgets)

%description
KCompletion provides widgets with advanced completion support as well as a
lower-level completion class which can be used with your own widgets.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(Qt6Widgets)
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
%find_lang_kf6 kcompletion6_qt

%files -f kcompletion6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Completion.so.6
%{_kf6_libdir}/libKF6Completion.so.%{lua: print((macros.version:gsub('[%^~].*', '')))}
%{_kf6_qtplugindir}/designer/*6widgets.so

%files devel
%{_qt6_docdir}/*.tags
%{_kf6_includedir}/KCompletion/
%{_kf6_libdir}/libKF6Completion.so
%{_kf6_libdir}/cmake/KF6Completion/


%changelog
%{?kde_snapshot_changelog_entry}
* Wed Mar 20 2024 Pavel Solovev <daron439@gmail.com> - 6.0.0-2
- qmlcache rebuild

* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Tue Oct 03 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231001.120552.4fc632b-1
- Initial Release
