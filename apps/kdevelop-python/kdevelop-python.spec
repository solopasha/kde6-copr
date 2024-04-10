%global commit0 abbbf6acde81f332cc8c2d278e2129fc2d60914d
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

%global base_name kdev-python

Name:           kdevelop-python
Summary:        KDevelop Python language support
Version:        24.05.0%{?bumpver:^%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}

License:        GPL-2.0-or-later
URL:            https://invent.kde.org/kdevelop/kdev-python
%apps_source

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules

BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5ThreadWeaver)

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)

BuildRequires:  kdevelop-devel >= %{version}
BuildRequires:  python3-devel

%{?kdevelop_requires}

%description
%{summary}.


%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1
sed 's|<3.12|<3.13|' -i CMakeLists.txt


%build
%cmake_kf5
%cmake_build


%install
%cmake_install

rm -r %{buildroot}%{_kf5_datadir}/kdevpythonsupport/documentation_files/{PyKDE4,PyQt4}

%find_lang %{name} --all-name

%files -f %{name}.lang
%license LICENSES/*
%{_kf5_datadir}/kdevappwizard/
%{_kf5_datadir}/kdevpythonsupport/
%{_kf5_datadir}/qlogging-categories5/kdevpythonsupport.categories
%{_kf5_libdir}/libkdev*python*.so*
%{_kf5_metainfodir}/org.kde.kdev-python.metainfo.xml
%{_qt5_plugindir}/kdevplatform/


%changelog
%{?kde_snapshot_changelog_entry}
* Thu Mar 21 2024 Pavel Solovev <daron439@gmail.com> - 24.02.1-1
- Update to 24.02.1
