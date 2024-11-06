Name:           kunifiedpush
Version:        1.0.0
Release:        1%{?dist}
Summary:        UnifiedPush client components

License:        LGPL-2.0-or-later
URL:            https://invent.kde.org/libraries/kunifiedpush
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        signing-key.pgp

BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6Service)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6WebSockets)

Requires:       kf6-kirigami%{?_isa}

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core)
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
%find_lang kcm_push_notifications

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f kcm_push_notifications.lang
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/kunifiedpush-distributor
%{_kf6_datadir}/applications/kcm_push_notifications.desktop
%{_kf6_datadir}/qlogging-categories6/org_kde_kunifiedpush.categories
%{_kf6_libdir}/libKUnifiedPush.so.{1,%{version}}
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_push_notifications.so
%{_kf6_sysconfdir}/xdg/autostart/org.kde.kunifiedpush-distributor.desktop
%config(noreplace) %{_sysconfdir}/xdg/KDE/kunifiedpush-distributor.conf

%files devel
%{_includedir}/KUnifiedPush/
%{_kf6_libdir}/cmake/KUnifiedPush/
%{_kf6_libdir}/libKUnifiedPush.so

%changelog
%autochangelog
