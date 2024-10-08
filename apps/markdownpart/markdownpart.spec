%global commit0 7c8090a9df078476f61695f2faa999038a66938d
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

%global app_id  org.kde.markdownpart

Name:           markdownpart
Summary:        Markdown KPart
Version:        24.08.2
Release:        1%{?dist}
License:        LGPL-2.1-or-later
URL:            https://apps.kde.org/categories/utilities/
%apps_source

Patch:          qt6.6.patch

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
* Mon Oct 07 2024 Pavel Solovev <daron439@gmail.com> - 24.08.2-1
- Update to 24.08.2

* Tue Sep 10 2024 Pavel Solovev <daron439@gmail.com> - 24.08.1-1
- Update to 24.08.1

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

* Sun Jun 02 2024 Pavel Solovev <daron439@gmail.com> - 24.05.0-2
- remove recommends

* Thu May 23 2024 Pavel Solovev <daron439@gmail.com> - 24.05.0-1
- Update to 24.05.0

* Fri Apr 26 2024 Pavel Solovev <daron439@gmail.com> - 24.04.80-1
- Update to 24.04.80

* Thu Apr 11 2024 Pavel Solovev <daron439@gmail.com> - 24.02.2-1
- Update to 24.02.2

* Thu Mar 21 2024 Pavel Solovev <daron439@gmail.com> - 24.02.1-1
- Update to 24.02.1
