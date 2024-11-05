%global commit0 cf1893cfaa3a0c1be3e07da29b33df8883a65e67
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

Name:           kgraphviewer
Version:        24.08.3
Release:        1%{?dist}
License:        GPL-2.0-only
Summary:        Graphviz DOT graph file viewer
URL:            https://invent.kde.org/graphics/kgraphviewer
%apps_source

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib

BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6WidgetsAddons)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  boost-devel
BuildRequires:  graphviz-devel

Requires:       graphviz
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%package        libs
Summary:        Graphviz dot graph file viewer library
%description    libs
KGraphViewer is a Graphviz dot graph file viewer for KDE.
This packages contains a library that can be shared by other tools.


%package        devel
Summary:        Graphviz dot graph file viewer development files
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    devel
KGraphViewer is a Graphviz dot graph file viewer for KDE
This package contains files useful for software development with
th KGraphViewer library.

%description
KGraphViewer is a Graphviz DOT graph file viewer, aimed to replace the
other outdated Graphviz tools. Graphs are commonly used in scientific
domains and particularly in computer science.

Features:

* Zooming
* Threaded loading of several graphs in tabs
* Saving of the recent files list
* Manual reload of files
* Display of a bird-eye view of the graph
* Moving of the graph by dragging
* Full featured printing
* Perfect drawing of all graphviz example graphs
* Automatically choose dot for directed graphs and neato for undirected
* Possibility to use an arbitrary layout algorithm as soon as it
  produces xdot format
* Automatic reloading with user confirmation of (externally) modified
  files (configurable)
* Open new instances as new tabs in the old one (configurable).

%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%find_lang %{name} --with-html

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/*.appdata.xml


%files -f %{name}.lang
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/config.kcfg/%{name}settings.kcfg
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}.png
%{_kf6_datadir}/qlogging-categories6/%{name}.categories
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml

%files libs
%doc AUTHORS
%license COPYING
%{_kf6_datadir}/config.kcfg/%{name}_partsettings.kcfg
%{_kf6_libdir}/lib%{name}.so.0
%{_kf6_libdir}/lib%{name}.so.2*
%{_kf6_plugindir}/parts/%{name}part.so

%files devel
%{_includedir}/%{name}/
%{_kf6_libdir}/cmake/KGraphViewerPart/
%{_kf6_libdir}/lib%{name}.so


%changelog
* Tue Nov 05 2024 Pavel Solovev <daron439@gmail.com> - 24.08.3-1
- Update to 24.08.3

* Mon Oct 07 2024 Pavel Solovev <daron439@gmail.com> - 24.08.2-1
- Update to 24.08.2

* Tue Sep 10 2024 Pavel Solovev <daron439@gmail.com> - 24.08.1-1
- Update to 24.08.1

* Fri Aug 16 2024 Pavel Solovev <daron439@gmail.com> - 24.08.0-1
- Update to 24.08.0

* Fri Aug 09 2024 Pavel Solovev <daron439@gmail.com> - 24.07.90-1
- Update to 24.07.90

* Thu Jul 25 2024 Pavel Solovev <daron439@gmail.com> - 24.07.80-1
- Initial build
