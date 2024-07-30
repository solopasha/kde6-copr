Name:           mpvqt
Version:        1.0.1
Release:        1%{?dist}
Summary:        A libmpv wrapper for QtQuick2 and QML

License:        LGPL-2.1-only OR LGPL-3.0-only OR LicenseRef-KDE-Accepted-LGPL
URL:            https://invent.kde.org/libraries/mpvqt
Source:         https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
Source:         https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz.sig
Source:         signing-key.pgp

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
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
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
