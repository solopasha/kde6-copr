Name:           mpvqt
Version:        1.0.0
Release:        1%{?dist}
Summary:        A libmpv wrapper for QtQuick2 and QML

License:        LGPL-2.1-only OR LGPL-3.0-only OR LicenseRef-KDE-Accepted-LGPL
URL:            https://invent.kde.org/libraries/mpvqt
Source:         http://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  pkgconfig(mpv)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Quick)
Requires:       pkgconfig(mpv)
%description    devel
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install


%files
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libMpvQt.so.1{,.*}

%files devel
%{_includedir}/MpvQt/
%{_kf6_libdir}/cmake/MpvQt/
%{_kf6_libdir}/libMpvQt.so


%changelog
%autochangelog
