%global commit0 0d0a62b96b75f6baee7b16e0da8795f754836d90
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

Name:           mpvqt
Version:        0%{?bumpver:^%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
Summary:        A libmpv wrapper for QtQuick2 and QML

License:        LGPL-2.1-only OR LGPL-3.0-only OR LicenseRef-KDE-Accepted-LGPL
URL:            https://github.com/KDE/mpvqt
Source:         %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  pkgconfig(mpv)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(mpv)
%description    devel
%{summary}.


%prep
%autosetup -n %{name}-%{commit0} -p1


%build
%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build


%install
%cmake_install


%files
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libMpvQt.so.1{,.*}

%files devel
%{_includedir}/MpvQt
%{_kf6_libdir}/libMpvQt.so
%{_kf6_libdir}/cmake/MpvQt


%changelog
%autochangelog
