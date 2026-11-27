%global commit0 544397526e51028ccff290bf2e6ed5fafbcd4454
%global shortcommit0 %{sub %{commit0} 1 7}
%global bumpver 1

Name:           kemoji
Version:        0.2.0%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
Summary:        Emoji dictionary, models, and QML components for KDE applications
License:        LGPL-3.0-only AND Unicode-3.0 AND CC0-1.0
URL:            https://invent.kde.org/libraries/kemoji
%kde_meta
BuildSystem:    cmake_kf6

BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Kirigami)

BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Quick)

Requires:       kf6-kirigami%{?_isa}

%description
KEmoji provides a searchable Unicode emoji dictionary, models for organizing
emoji, and QML components for integrating emoji selection into applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa}
Requires:       cmake(KF6I18n)
Requires:       cmake(Qt6Gui)
%description    devel
Headers and CMake configuration files for developing applications that use
KEmoji.

%files
%license LICENSES/*.txt
%doc README.md
%{_kf6_datadir}/kemoji/
%{_kf6_datadir}/qlogging-categories6/kemoji.categories
%{_kf6_libdir}/libKEmoji.so.0
%{_kf6_libdir}/libKEmoji.so.0.*
%{_kf6_qmldir}/org/kde/kemoji/

%files devel
%{_includedir}/KEmoji/
%{_kf6_libdir}/cmake/KEmoji/
%{_kf6_libdir}/libKEmoji.so

%changelog
%{?kde_snapshot_changelog_entry}
