%global framework kdbusaddons

Name:			kf6-%{framework}
Version:		5.248.0
Release:		1%{?dist}
Summary:		KDE Frameworks 6 Tier 1 addon with various classes on top of QtDBus
License:		CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only
URL:			https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:		cmake
BuildRequires:		extra-cmake-modules >= %{version}
BuildRequires:		gcc-c++
BuildRequires:		kf6-rpm-macros
BuildRequires:		cmake(Qt6DBus)
BuildRequires:		cmake(Qt6Gui)
BuildRequires:      qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}

Requires:		kf6-filesystem

%description
KDBusAddons provides convenience classes on top of QtDBus, as well as an API to
create KDED modules.

%package		devel
Summary:		Development files for %{name}
Requires:		%{name} = %{version}-%{release}
Requires:		qt6-qtbase-devel
%description		devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang_kf6 kdbusaddons6_qt

%files -f kdbusaddons6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_bindir}/kquitapp6
%{_kf6_datadir}/qlogging-categories6/%{framework}*
%{_kf6_libdir}/libKF6DBusAddons.so.6
%{_kf6_libdir}/libKF6DBusAddons.so.%{version}

%files devel
%{_kf6_includedir}/KDBusAddons/
%{_kf6_libdir}/cmake/KF6DBusAddons/
%{_kf6_libdir}/libKF6DBusAddons.so


%changelog
* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com>
- 5.245.0

* Tue Oct 17 2023 Jan Grulich <jgrulich@redhat.com> - 5.240.0^20230829.232927.fbb8558-3
- Rebuild (qt6)

* Thu Oct 05 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230829.232927.fbb8558-2
- Rebuild for Qt Private API

* Sun Sep 24 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230829.232927.fbb8558-1
- Initial Release
