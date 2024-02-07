Name:           kweathercore
Version:        0.8.0
Release:        1%{?dist}
License:        LGPLv2+
Summary:        Library to facilitate retrieval of weather information
URL:            https://invent.kde.org/libraries/kweathercore
Source0:        https://download.kde.org/stable/kweathercore/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/stable/kweathercore/%{version}/%{name}-%{version}.tar.xz.sig
Source2:        kde-frameworks-signing-keys.pgp

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Positioning)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Holidays)

%description
Get weather forecast and alerts anywhere on the earth easy. KWeatherCore
provides you a highly abstracted library for things related to weather:
Get local weather forecast, get weather of a location by name or coordinate,
get sunrise/set moonrise/set and many more informations about a location.

%package devel
Summary:        Development headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%find_lang %{name}6 --all-name

%files -f %{name}6.lang
%license LICENSES/*.txt
%{_kf6_libdir}/libKWeatherCore.so.%{version}
%{_kf6_libdir}/libKWeatherCore.so.6

%files devel
%{_includedir}/kweathercore_version.h
%{_includedir}/KWeatherCore/
%{_kf6_archdatadir}/mkspecs/modules/qt_KWeatherCore.pri
%{_kf6_libdir}/cmake/KWeatherCore/
%{_kf6_libdir}/libKWeatherCore.so


%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Sep 28 2022 Justin Zobel <justin@1707.io> - 0.7-1
- Update to 0.7

* Tue Sep 20 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 0.6-1
- version bump 0.6

* Tue Sep 20 2022 Justin Zobel <justin@1707.io> - 0.5-4
- Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 16 2022 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 0.5-1
- version bump 0.5

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 17 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.05-3
-  Clean up un needed command from build process

* Sat Jul 17 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.05-2
-  KF5_VERSION changed to 0.3.0 for kweather

* Wed May 5 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 21.05-1
- initial version of package
