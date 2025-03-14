%global commit0 5a0e64d55737d683689acbf9ea64094ec25d3f10
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 5

Name:           aurorae
Summary:        Aurorae decoration engine
Version:        6.3.80%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}

License:        GPL-2.0-or-later
URL:            https://invent.kde.org/plasma/aurorae
%plasma_source

BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6WindowSystem)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6UiTools)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake(KDecoration3)

Conflicts:      kwin-common < 6.3.80~48.gitd2276e5

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
Development files for %{name}.

%description
Aurorae is a themeable window decoration for KWin.
It supports theme files consisting of several SVG files for decoration and buttons.
Themes can be installed and selected directly in the configuration module of KWin
decorations.

%files -f %{name}.lang
%{_kf6_datadir}/knsrcfiles/aurorae.knsrc
%{_kf6_datadir}/kwin/aurorae/
%{_kf6_datadir}/kwin/decorations/kwin4_decoration_qml_plastik/
%{_libexecdir}/plasma-apply-aurorae
%{_qt6_plugindir}/org.kde.kdecoration3.kcm/kcm_auroraedecoration.so
%{_qt6_plugindir}/org.kde.kdecoration3/org.kde.kwin.aurorae.so
%{_qt6_qmldir}/org/kde/kwin/decoration/
%{_qt6_qmldir}/org/kde/kwin/decorations/plastik/

%files devel
%{_kf6_libdir}/cmake/Aurorae/

%changelog
%{?kde_snapshot_changelog_entry}
* Thu Feb 20 2025 Pavel Solovev <daron439@gmail.com> - 6.3.80-2
- Initial package
