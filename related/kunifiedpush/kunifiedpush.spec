%global commit0 83064e6feea25a3b2422b8cfffdf631f0242430d
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

Name:           kunifiedpush
Version:        0^1.git%{shortcommit0}
Release:        1%{?dist}
Summary:        UnifiedPush client components

License:        LGPL-2.0-or-later
URL:            https://invent.kde.org/libraries/kunifiedpush
Source:         %{url}/-/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6Service)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6WebSockets)

Requires:       kf6-kirigami2

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core)
%description    devel
%{summary}.


%prep
%autosetup -n %{name}-%{commit0} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/kunifiedpush-distributor
%{_kf6_datadir}/applications/kcm_push_notifications.desktop
%{_kf6_datadir}/qlogging-categories6/org_kde_kunifiedpush.categories
%{_kf6_libdir}/libKUnifiedPush.so.1
%{_kf6_libdir}/libKUnifiedPush.so.22.04.00
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_push_notifications.so
%{_kf6_sysconfdir}/xdg/autostart/org.kde.kunifiedpush-distributor.desktop

%files devel
%{_includedir}/KUnifiedPush/
%{_kf6_libdir}/cmake/KUnifiedPush/
%{_kf6_libdir}/libKUnifiedPush.so


%changelog
%autochangelog
