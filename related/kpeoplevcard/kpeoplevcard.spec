%global commit0 2d8ed9929bacca2a748af1f028f87c9c88bace11
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

Name:           kpeoplevcard
Version:        0.1%{?bumpver:^%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
Summary:        Expose VCard contacts to KPeople
License:        LGPL-2.1-or-later
URL:            https://invent.kde.org/pim/kpeoplevcard
Source:         %{url}/-/archive/%{commit0}/pulseaudio-qt-%{commit0}.tar.gz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6People)

BuildRequires:  cmake(Qt6Widgets)

%description
Kpeoplevcard provides a datasource plugin for KPeople that reads vCard files
from the local filesystem.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep
%autosetup -n %{name}-%{commit0} -p1

%build
%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name

%files -f %{name}.lang
%license LICENSES/LGPL-2.1-or-later.txt
%{_qt6_plugindir}/kpeople/datasource/KPeopleVCard.so

%files devel
%{_kf6_libdir}/cmake/KF6PeopleVCard/

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jan 16 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 0.1-1
- Initial package
