%global commit0 d572d1865c54fd1af02a1758415ac5df11a7d698
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

%global app_id  org.kde.markdownpart

Name:           markdownpart
Summary:        Markdown KPart
Version:        24.05.0%{?bumpver:^%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
License:        LGPL-2.1-or-later
URL:            https://apps.kde.org/categories/utilities/
%apps_source

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libappstream-glib


%description
A Markdown viewer KParts plugin, which allows KParts-using applications to
display files in Markdown format in the target format.


%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/%{app_id}.metainfo.xml


%files -f %{name}.lang
%doc README.md
%license LICENSES/*
%{_kf6_plugindir}/parts/markdownpart.so
%{_kf6_metainfodir}/%{app_id}.metainfo.xml


%changelog
%{?kde_snapshot_changelog_entry}
%autochangelog
