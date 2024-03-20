%global framework kded

Name:    kf6-%{framework}
Version: 6.0.0
Release: 2%{?dist}
Summary: KDE Frameworks 6 Tier 3 addon with extensible daemon for system-level services

License: CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6Service)

BuildRequires:  qt6-qtbase-devel

BuildRequires:  systemd-rpm-macros

Requires:  kf6-filesystem

%description
KDED stands for KDE Daemon which isn't very descriptive. KDED runs
in the background and performs a number of small tasks. Some of these
tasks are built in, others are started on demand.

Custom KDED modules can be provided by 3rd party frameworks and
applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
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
%find_lang kded6 --with-man --without-mo
# create/own this
mkdir -p %{buildroot}%{_kf6_plugindir}/kded

%post
%systemd_user_post  plasma-kded6.service

%preun
%systemd_user_preun plasma-kded6.service

%files -f kded6.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_bindir}/kded6
%{_kf6_datadir}/applications/org.kde.kded6.desktop
%{_kf6_datadir}/dbus-1/services/*.service
%{_kf6_mandir}/man8/kded6.8*
%dir %{_kf6_plugindir}/kded/
%{_userunitdir}/plasma-kded6.service

%files devel
%{_kf6_libdir}/cmake/KF6KDED/
%{_kf6_datadir}/dbus-1/interfaces/*.xml


%changelog
* Wed Mar 20 2024 Pavel Solovev <daron439@gmail.com> - 6.0.0-2
- qmlcache rebuild

* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Mon Oct 09 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231005.021018.cbc5874-1
- Initial release
