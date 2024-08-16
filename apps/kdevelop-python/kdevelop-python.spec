%global commit0 e80eae82c7ef72b94fe83cebb947421478fb5c17
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

%global base_name kdev-python

Name:           kdevelop-python
Summary:        KDevelop Python language support
Version:        24.08.0
Release:        1%{?dist}

License:        GPL-2.0-or-later
URL:            https://invent.kde.org/kdevelop/kdev-python
%apps_source

BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6TextEditor)
BuildRequires:  cmake(KF6ThreadWeaver)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  kdevelop-devel >= %{majmin_ver_kf6}
BuildRequires:  python3-devel

%{?kdevelop_requires}

%description
%{summary}.


%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

rm -r %{buildroot}%{_kf6_datadir}/kdevpythonsupport/documentation_files/{PyKDE4,PyQt4}

%find_lang %{name} --all-name

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_datadir}/kdevappwizard/
%{_kf6_datadir}/kdevpythonsupport/
%{_kf6_datadir}/qlogging-categories6/kdevpythonsupport.categories
%{_kf6_libdir}/libkdev*python*.so*
%{_kf6_metainfodir}/org.kde.kdev-python.metainfo.xml
%{_qt6_plugindir}/kdevplatform/


%changelog
* Fri Aug 16 2024 Pavel Solovev <daron439@gmail.com> - 24.08.0-1
- Update to 24.08.0

* Fri Aug 09 2024 Pavel Solovev <daron439@gmail.com> - 24.07.90-1
- Update to 24.07.90

* Thu Jul 25 2024 Pavel Solovev <daron439@gmail.com> - 24.07.80-1
- Update to 24.07.80

* Thu Jul 04 2024 Pavel Solovev <daron439@gmail.com> - 24.05.2-1
- Update to 24.05.2

* Thu Jun 13 2024 Pavel Solovev <daron439@gmail.com> - 24.05.1-1
- Update to 24.05.1

* Thu May 23 2024 Pavel Solovev <daron439@gmail.com> - 24.05.0-1
- Update to 24.05.0

* Fri Apr 26 2024 Pavel Solovev <daron439@gmail.com> - 24.04.80-1
- Update to 24.04.80

* Thu Apr 11 2024 Pavel Solovev <daron439@gmail.com> - 24.02.2-1
- Update to 24.02.2

* Thu Mar 21 2024 Pavel Solovev <daron439@gmail.com> - 24.02.1-1
- Update to 24.02.1
