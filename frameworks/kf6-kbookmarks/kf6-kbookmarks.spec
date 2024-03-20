%global framework kbookmarks

Name:    kf6-%{framework}
Version: 6.0.0
Release: 2%{?dist}
Summary: KDE Frameworks 6 Tier 3 addon for bookmarks manipulation
License: CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-LGPL
URL:     https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6WidgetsAddons)

Requires:  kf6-filesystem

%description
KBookmarks lets you access and manipulate bookmarks stored using the
XBEL format.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6WidgetsAddons)
Requires:       cmake(Qt6Widgets)
Requires:       cmake(Qt6Xml)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%qch_package

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{framework}-%{version} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang_kf6 kbookmarks6_qt


%files -f kbookmarks6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_datadir}/qlogging-categories6/%{framework}widgets.categories
%{_kf6_libdir}/libKF6Bookmarks.so.6
%{_kf6_libdir}/libKF6Bookmarks.so.%{version}
%{_kf6_libdir}/libKF6BookmarksWidgets.so.%{version}
%{_kf6_libdir}/libKF6BookmarksWidgets.so.6

%files devel
%{_qt6_docdir}/*.tags
%{_kf6_includedir}/KBookmarks/
%{_kf6_includedir}/KBookmarksWidgets/
%{_kf6_libdir}/cmake/KF6Bookmarks/
%{_kf6_libdir}/libKF6Bookmarks.so
%{_kf6_libdir}/libKF6BookmarksWidgets.so


%changelog
* Wed Mar 20 2024 Pavel Solovev <daron439@gmail.com> - 6.0.0-2
- qmlcache rebuild

* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231009.021624.89d7de2-1
- Initial release
