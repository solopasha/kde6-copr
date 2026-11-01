%global commit0 14c6506273e443991fcc52c01e1af107ec0ff0be
%global shortcommit0 %{sub %{commit0} 1 7}
%global bumpver 30

%global base_name union

Name:           plasma-union
Version:        6.8.80%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
Summary:        A Qt style supporting both QtQuick and QtWidgets

License:        BSD-2-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND MIT
URL:            https://invent.kde.org/plasma/union
%plasma_source

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6ShaderTools)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6KirigamiPlatform)
BuildRequires:  cmake(KF6WindowSystem)

BuildRequires:  cmake(cxx-rust-cssparser)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/union-styletool
%{_kf6_datadir}/kstyle/themes/union.themerc
%{_kf6_datadir}/qlogging-categories6/union.categories
%{_kf6_datadir}/union/
%{_kf6_libdir}/libUnion.so.6{,.*}
%{_kf6_libdir}/libUnionQuickImpl.so.6{,.*}
%{_kf6_libdir}/libUnionQuickStyle.so.6{,.*}
%{_kf6_qmldir}/org/kde/kirigami/styles/org.kde.union/
%{_kf6_qmldir}/org/kde/union/
%{_kf6_qtplugindir}/kf6/kirigami/platform/org.kde.union.so
%{_kf6_qtplugindir}/styles/UnionWidgetsStyle.so
%{_kf6_qtplugindir}/union/

%files devel
%{_includedir}/union/
%{_kf6_bindir}/union-ruleinspector
%{_kf6_libdir}/cmake/Union/
%{_kf6_libdir}/libUnion.so

%changelog
%{?kde_snapshot_changelog_entry}
