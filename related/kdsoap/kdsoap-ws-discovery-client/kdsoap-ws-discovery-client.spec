Name:           kdsoap-ws-discovery-client
Version:        0.3.0
Release:        1%{?dist}
Summary:        Library for finding WS-Discovery devices in the network using Qt6 and KDSoap

License:        GPL-3.0-or-later AND LicenseRef-OASIS AND LicenseRef-WS-Addressing AND LicenseRef-Discovery AND W3C
URL:            https://invent.kde.org/libraries/kdsoap-ws-discovery-client/
Source0:        https://download.kde.org/unstable/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  gcc-c++

BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KDSoap-qt6)
BuildRequires:  cmake(Qt6)

%description
%{summary}.


%package        devel
Summary:        Development libraries and header files for Qt6 %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KDSoap-qt6)
%description    devel
%{summary}.

%prep
%autosetup -p1

%build
%cmake -DBUILD_WITH_QT6=ON
%cmake_build

%install
%cmake_install

%check
# Tests fail without internet
%ctest || :

%files
%doc README.md
%license LICENSES/*
%{_libdir}/libKDSoapWSDiscoveryClient.so.0*

%files devel
%{_includedir}/KDSoapWSDiscoveryClient/
%{_libdir}/cmake/KDSoapWSDiscoveryClient/
%{_libdir}/libKDSoapWSDiscoveryClient.so

%changelog
* Tue Nov 14 2023 Alessandro Astone <ales.astone@gmail.com> - 0.3.0-1
- Initial Release
