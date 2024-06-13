Name:		    merkuro
Version:	    24.05.1
Release:	    1%{?dist}
Summary:	    A calendar application using Akonadi to sync with external services (Nextcloud, GMail, ...)

License:	    GPL-3.0-or-later
URL:		    https://invent.kde.org/pim/%{name}
%apps_source

BuildRequires:	desktop-file-utils
BuildRequires:	extra-cmake-modules
BuildRequires:	gcc-c++
BuildRequires:	kf6-rpm-macros
BuildRequires:	libappstream-glib

BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(KF6QQC2DesktopStyle)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)

BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6AkonadiCalendar)
BuildRequires:  cmake(KPim6AkonadiContactCore)
BuildRequires:  cmake(KPim6AkonadiMime)
BuildRequires:  cmake(KPim6CalendarUtils)
BuildRequires:  cmake(KPim6IdentityManagementQuick)
BuildRequires:  cmake(KPim6MailCommon)
BuildRequires:  cmake(KPim6MailTransport)
BuildRequires:  cmake(KPim6Mbox)
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(KPim6MimeTreeParserCore)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6QuickTest)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)

BuildRequires:  cmake(QGpgmeQt6)


# QML module dependencies
Requires:	kf6-kirigami2%{?_isa}
Requires:   kf6-kirigami-addons%{?_isa}
Requires:	kf6-kitemmodels%{?_isa}

# kalendar has been renamed to merkuro
Obsoletes:	kalendar < 23.08
Provides:	kalendar = %{version}-%{release}
Provides:	kalendar%{?_isa} = %{version}-%{release}

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
# Package doesn't build on arches that qtwebengine is not built on.
ExclusiveArch:	%{qt6_qtwebengine_arches}

%description
Merkuro is a application suite designed to make handling your emails, \
calendars, contacts, and tasks simple. Merkuro handles local and \
remote accounts of your choice, keeping changes synchronised across \
your Plasma desktop or phone.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --with-kde --with-man --all-name


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/*.xml ||:


%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/merkuro-calendar
%{_kf6_bindir}/merkuro-contact
%{_kf6_bindir}/merkuro-mail
%{_kf6_datadir}/applications/org.kde.merkuro.calendar.desktop
%{_kf6_datadir}/applications/org.kde.merkuro.contact.desktop
%{_kf6_datadir}/applications/org.kde.merkuro.mail.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/org.kde.merkuro*.png
%{_kf6_datadir}/plasma/plasmoids/org.kde.merkuro.contact/
%{_kf6_datadir}/qlogging-categories6/akonadi.quick.categories
%{_kf6_datadir}/qlogging-categories6/merkuro.categories
%{_kf6_datadir}/qlogging-categories6/merkuro.contact.categories
%{_kf6_metainfodir}/org.kde.merkuro.*.xml
%{_kf6_qmldir}/org/kde/akonadi/*
%{_kf6_qmldir}/org/kde/merkuro/


%changelog
* Thu Jun 13 2024 Pavel Solovev <daron439@gmail.com> - 24.05.1-1
- Update to 24.05.1

* Thu May 23 2024 Pavel Solovev <daron439@gmail.com> - 24.05.0-1
- Update to 24.05.0

* Fri Apr 26 2024 Pavel Solovev <daron439@gmail.com> - 24.04.80-1
- Update to 24.04.80

* Thu Apr 11 2024 Pavel Solovev <daron439@gmail.com> - 24.02.2-1
- Update to 24.02.2

* Thu Mar 21 2024 Pavel Solovev <daron439@gmail.com> - 24.02.1-1
- Update to 24.02.1

* Wed Mar 20 2024 Pavel Solovev <daron439@gmail.com> - 24.02.0-2
- qmlcache rebuild

* Thu Oct 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.2-1
- 23.08.2

* Sat Sep 16 2023 Steve Cossette <farchord@gmail.com> - 23.08.1-1
- Initial Release
