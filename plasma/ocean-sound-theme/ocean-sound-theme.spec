Name:           ocean-sound-theme
Summary:        Ocean Sound Theme for Plasma
Version:        5.90.0
Release:        1%{?dist}
BuildArch:      noarch
License:        CC0-1.0 AND BSD-2-Clause AND CC-BY-SA-4.0
URL:            https://invent.kde.org/plasma/%{name}
%plasma_source

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake

Requires:       kf6-filesystem

%description
%{summary}.

%prep
%autosetup


%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSES/*.txt
%{_datadir}/sounds/ocean/

%changelog
* Sun Dec 03 2023 Justin Zobel <justin.zobel@gmail.com> - 5.90.0-1
- Update to 5.90.0

* Fri Nov 10 2023 Alessandro Astone <ales.astone@gmail.com> - 5.27.80-1
- 5.27.80

* Fri Sep 22 2023 Steve Cossette <farchord@gmail.com> - 5.27.80^20230706.180800.683acbb-1
- Initial build
