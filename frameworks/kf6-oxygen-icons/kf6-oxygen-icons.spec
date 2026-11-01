%global commit0 681c1b9c7a5004583d722d00af7fdd3a1657e8a1
%global shortcommit0 %{sub %{commit0} 1 7}
%global bumpver 17

%global framework oxygen-icons

Name:           kf6-oxygen-icons
Version:        6.32.0%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
Summary:        Oxygen icon theme

License:        CC0-1.0 AND LGPL-3.0-or-later
URL:            https://invent.kde.org/frameworks/oxygen-icons
%kde_meta -n
BuildOption:    -DBUILD_WITH_QT6=ON

BuildArch:      noarch

BuildRequires:  libappstream-glib
BuildRequires:  cmake(Qt6Core)

%description
Oxygen Icons is a freedesktop.org compatible icon theme originally
developed for the KDE Plasma desktop environment in combination with
the Oxygen Style. It features smooth gradients, soft shadows, and a
slightly glossy look.

%package -n oxygen-icon-theme
Epoch:       1
Summary:     Oxygen icon theme
License:     CC0-1.0 AND LGPL-3.0-or-later
BuildArch:   noarch
Requires:    hicolor-icon-theme
# Needed for proper Fedora logo
Requires:    system-logos
# Renamed from oxygen-icon-theme
Obsoletes:   oxygen-icon-theme < 1:6.27.0-1
Conflicts:   oxygen-icon-theme < 1:6.27.0-1

%description -n oxygen-icon-theme
Oxygen Icons is a freedesktop.org compatible icon theme originally
developed for the KDE Plasma desktop environment in combination with
the Oxygen Style. It features smooth gradients, soft shadows, and a
slightly glossy look.

%install -a
## icon optimizations
du -s .
hardlink -c -v %{buildroot}%{_datadir}/icons/
du -s .

# %%ghost icon.cache
touch %{buildroot}%{_kf6_datadir}/icons/oxygen/icon-theme.cache

## trigger-based scriptlets
%transfiletriggerin -n oxygen-icon-theme -- %{_datadir}/icons/oxygen
gtk-update-icon-cache --force %{_datadir}/icons/oxygen &>/dev/null || :

%transfiletriggerpostun -n oxygen-icon-theme -- %{_datadir}/icons/oxygen
gtk-update-icon-cache --force %{_datadir}/icons/oxygen &>/dev/null || :

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.oxygenicon.metainfo.xml

%files -n oxygen-icon-theme
%license LICENSES/*
%doc README.md AUTHORS
%ghost %{_datadir}/icons/oxygen/icon-theme.cache
%{_datadir}/icons/oxygen/index.theme
%{_datadir}/icons/oxygen/*/
%{_datadir}/icons/oxygen/icon-settings.json
%{_metainfodir}/org.kde.oxygenicon.metainfo.xml

%changelog
%{?kde_snapshot_changelog_entry}
