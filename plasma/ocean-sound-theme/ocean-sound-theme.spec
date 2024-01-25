%global commit0 517cc4d86be6c02f52f3eb140a3fa40d982510c3
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

Name:           ocean-sound-theme
Summary:        Ocean Sound Theme for Plasma
Version:        6.0.2%{?bumpver:^%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
BuildArch:      noarch
License:        CC0-1.0 AND BSD-2-Clause AND CC-BY-SA-4.0
URL:            https://invent.kde.org/plasma/%{name}
%plasma_source

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake

BuildRequires:  cmake(Qt6Core)

Requires:       kf6-filesystem

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

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/sounds/ocean/

%changelog
%{?kde_snapshot_changelog_entry}
* Wed Mar 20 2024 Pavel Solovev <daron439@gmail.com> - 6.0.2-2
- qmlcache rebuild

* Sun Dec 03 2023 Justin Zobel <justin.zobel@gmail.com> - 5.90.0-1
- Update to 5.90.0

* Fri Nov 10 2023 Alessandro Astone <ales.astone@gmail.com> - 5.27.80-1
- 5.27.80

* Fri Sep 22 2023 Steve Cossette <farchord@gmail.com> - 5.27.80^20230706.180800.683acbb-1
- Initial build
