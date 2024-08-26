%global app_id  org.kde.markdownpart

Name:           markdownpart-qt5
Summary:        Markdown KPart
Version:        23.08.5
Release:        %autorelease -b3
License:        LGPL-2.1-or-later
URL:            https://apps.kde.org/categories/utilities/

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source:         https://download.kde.org/%{stable}/release-service/%{version}/src/markdownpart-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libappstream-glib

Supplements:    krusader
%if %{fedora} < 40
Supplements:    kdevelop
%endif

%description
A Markdown viewer KParts plugin, which allows KParts-using applications to
display files in Markdown format in the target format.


%prep
%autosetup -n markdownpart-%{version} -p1


%build
%cmake_kf5
%cmake_build


%install
%cmake_install
rm %{buildroot}%{_kf5_metainfodir}/%{app_id}.metainfo.xml
rm -rf %{buildroot}%{_kf5_datadir}/locale


%files
%doc README.md
%license LICENSES/*
%{_kf5_plugindir}/parts/markdownpart.so


%changelog
%autochangelog
