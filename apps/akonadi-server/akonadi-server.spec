%global commit0 7a182cbfdbd1f840b324da702874d783435b11d7
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

%global base_name akonadi
%global mysql mysql

%if 0%{?flatpak}
%global database_backend SQLITE
%endif

Name:    akonadi-server
Summary: PIM Storage Service
Version: 24.12.0
Release: 1%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LicenseRef-KDE-Accepted-GPL AND MIT
URL:     https://invent.kde.org/pim/akonadi
%apps_source

## mysql config
Source10:       akonadiserverrc.mysql
Source11:       akonadiserverrc.sqlite

%define mysql_conf_timestamp 20231125

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Designer)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  qt6-qtbase-private-devel

BuildRequires:  cmake(AccountsQt6)
BuildRequires:  cmake(KAccounts6)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  pkgconfig(sqlite3)

Requires(post): /usr/sbin/update-alternatives
Requires(postun): /usr/sbin/update-alternatives

%if ! 0%{?flatpak}
Recommends:     %{name}-mysql = %{version}-%{release}
%endif

Obsoletes:      kf5-akonadi-server < 23.08.5-9

Obsoletes:      akonadi < 24.01.85-2
Provides:       akonadi = %{version}-%{release}
Provides:       akonadi%{?_isa} = %{version}-%{release}

%description
%{summary}.

%package devel
Summary:        Developer files for %{name}
Conflicts:      kf5-akonadi-server-devel < 23.08.3-2
Obsoletes:      akonadi-devel < 24.01.85-2
Provides:       akonadi-devel = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6Config)
Requires:       cmake(KF6ConfigWidgets)
Requires:       cmake(KF6CoreAddons)
Requires:       cmake(KF6ItemModels)
Requires:       cmake(KF6XmlGui)
Requires:       cmake(KF6KIO)
Requires:       cmake(Qt6Core)
Requires:       cmake(Qt6DBus)
Requires:       cmake(Qt6Gui)
Requires:       cmake(Qt6Network)
Requires:       cmake(Qt6Widgets)
Requires:       cmake(Qt6Xml)
%description devel
%{summary}.

%package mysql
Summary:        Akonadi MySQL backend support
Obsoletes:      kf5-akonadi-server-mysql < 24.01.75
Provides:       kf5-akonadi-server-mysql = %{version}-%{release}
Obsoletes:      akonadi-mysql < 24.01.85-2
Provides:       akonadi-mysql = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%if %{fedora} >= 40
Requires:       mariadb-server
%else
Requires:       %{mysql}-server
%if "%{?mysql}" != "mariadb" && 0%{?fedora} > 20
Recommends:     mariadb-server
%endif
%endif
Requires:       qt6-qtbase-mysql%{?_isa}
Requires(post): /usr/sbin/update-alternatives
Requires(postun): /usr/sbin/update-alternatives
%description mysql
Configures akonadi to use mysql backend by default.

Requires an available instance of mysql server at runtime.
Akonadi can spawn a per-user one automatically if the mysql-server
package is installed on the machine.
See also: %{_sysconfdir}/akonadi/mysql-global.conf


%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1


%build
%cmake_kf6 \
  %{?database_backend:-DDATABASE_BACKEND=%{database_backend}} \
  -DINSTALL_APPARMOR:BOOL=OFF \
  -DMYSQLD_EXECUTABLE:FILEPATH=%{_libexecdir}/mysqld \
  -DMYSQLD_SCRIPTS_PATH:FILEPATH=%{_bindir}/mysql_install_db \
  -DPOSTGRES_PATH:FILEPATH=%{_bindir}/pg_ctl
%cmake_build


%install
%cmake_install

%find_lang libakonadi6
%find_lang akonadi_knut_resource
%find_lang akonadi-db-migrator
cat akonadi_knut_resource.lang >> libakonadi6.lang
cat akonadi-db-migrator.lang >> libakonadi6.lang

install -p -m644 -D %{SOURCE10} %{buildroot}%{_sysconfdir}/xdg/akonadi/akonadiserverrc.mysql
install -p -m644 -D %{SOURCE11} %{buildroot}%{_sysconfdir}/xdg/akonadi/akonadiserverrc.sqlite

mkdir -p %{buildroot}%{_datadir}/akonadi/agents

touch -d %{mysql_conf_timestamp} \
  %{buildroot}%{_sysconfdir}/xdg/akonadi/mysql-global*.conf \
  %{buildroot}%{_sysconfdir}/xdg/akonadi/mysql-local.conf

# create/own these dirs
mkdir -p %{buildroot}%{_kf6_datadir}/akonadi/plugins
mkdir -p %{buildroot}%{_kf6_libdir}/akonadi

# %%ghost'd global akonadiserverrc
touch akonadiserverrc
install -p -m644 -D akonadiserverrc %{buildroot}%{_sysconfdir}/xdg/akonadi/akonadiserverrc

## unpackaged files
# omit mysql-global-mobile.conf
rm -fv %{buildroot}%{_sysconfdir}/xdg/akonadi/mysql-global-mobile.conf


%post
/usr/sbin/update-alternatives \
  --install %{_sysconfdir}/xdg/akonadi/akonadiserverrc \
  akonadiserverrc \
  %{_sysconfdir}/xdg/akonadi/akonadiserverrc.sqlite \
  8

%postun
if [ $1 -eq 0 ] ; then
/usr/sbin/update-alternatives \
  --remove akonadiserverrc \
  %{_sysconfdir}/xdg/akonadi/akonadiserverrc.sqlite
fi


%files -f libakonadi6.lang
%license LICENSES/*
%dir %{_sysconfdir}/xdg/akonadi/
%ghost %config(missingok,noreplace) %{_sysconfdir}/xdg/akonadi/akonadiserverrc
%config(noreplace) %{_sysconfdir}/xdg/akonadi/akonadiserverrc.sqlite
%{_kf6_bindir}/akonadi_agent_launcher
%{_kf6_bindir}/akonadi_agent_server
%{_kf6_bindir}/akonadi_control
%{_kf6_bindir}/akonadi_rds
%{_kf6_bindir}/akonadictl
%{_kf6_bindir}/akonadiserver
%{_kf6_bindir}/akonadi-db-migrator
%{_kf6_datadir}/akonadi/
%{_kf6_datadir}/config.kcfg/resourcebase.kcfg
%{_kf6_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.*.xml
%{_kf6_datadir}/dbus-1/services/org.freedesktop.Akonadi.*.service
%{_kf6_datadir}/icons/hicolor/*/apps/akonadi.*
%{_kf6_datadir}/kf6/akonadi/
%{_kf6_datadir}/mime/packages/akonadi-mime.xml
%{_kf6_datadir}/qlogging-categories6/akonadi.*
%{_kf6_libdir}/akonadi/
%{_kf6_libdir}/libKPim6AkonadiAgentBase.so.*
%{_kf6_libdir}/libKPim6AkonadiCore.so.*
%{_kf6_libdir}/libKPim6AkonadiPrivate.so.*
%{_kf6_libdir}/libKPim6AkonadiWidgets.so.*
%{_kf6_libdir}/libKPim6AkonadiXml.so.*
%{_kf6_qtplugindir}/designer/akonadi6widgets.so
# akonadi_knut_resource
%{_kf6_bindir}/akonadi_knut_resource
%{_kf6_datadir}/kf6/akonadi_knut_resource/

%files devel
%{_includedir}/KPim6/Akonadi/
%{_includedir}/KPim6/AkonadiAgentBase/
%{_includedir}/KPim6/AkonadiCore/
%{_includedir}/KPim6/AkonadiWidgets/
%{_includedir}/KPim6/AkonadiXml/
%{_kf6_bindir}/akonadi2xml
%{_kf6_bindir}/akonadiselftest
%{_kf6_bindir}/akonaditest
%{_kf6_bindir}/asapcat
%{_kf6_datadir}/kdevappwizard/templates/akonadiresource.tar.bz2
%{_kf6_datadir}/kdevappwizard/templates/akonadiserializer.tar.bz2
%{_kf6_libdir}/cmake/KPim6Akonadi/
%{_kf6_libdir}/libKPim6AkonadiAgentBase.so
%{_kf6_libdir}/libKPim6AkonadiCore.so
%{_kf6_libdir}/libKPim6AkonadiPrivate.so
%{_kf6_libdir}/libKPim6AkonadiWidgets.so
%{_kf6_libdir}/libKPim6AkonadiXml.so
%{_kf6_qtplugindir}/pim6/akonadi/akonadi_test_searchplugin.so

%post mysql
/usr/sbin/update-alternatives \
  --install %{_sysconfdir}/xdg/akonadi/akonadiserverrc \
  akonadiserverrc \
  %{_sysconfdir}/xdg/akonadi/akonadiserverrc.mysql \
  10

%postun mysql
if [ $1 -eq 0 ]; then
/usr/sbin/update-alternatives \
  --remove akonadiserverrc \
  %{_sysconfdir}/xdg/akonadi/akonadiserverrc.mysql
fi

%files mysql
%config(noreplace) %{_sysconfdir}/xdg/akonadi/akonadiserverrc.mysql
%config(noreplace) %{_sysconfdir}/xdg/akonadi/mysql-global.conf
%config(noreplace) %{_sysconfdir}/xdg/akonadi/mysql-local.conf


%changelog
* Fri Dec 06 2024 Pavel Solovev <daron439@gmail.com> - 24.12.0-1
- Update to 24.12.0

* Mon Dec 02 2024 Pavel Solovev <daron439@gmail.com> - 24.08.3-2
- Remove Qt6 version constraints

* Tue Nov 05 2024 Pavel Solovev <daron439@gmail.com> - 24.08.3-1
- Update to 24.08.3

* Thu Oct 31 2024 Pavel Solovev <daron439@gmail.com> - 24.08.2-2
- rebuilt

* Mon Oct 07 2024 Pavel Solovev <daron439@gmail.com> - 24.08.2-1
- Update to 24.08.2

* Tue Sep 10 2024 Pavel Solovev <daron439@gmail.com> - 24.08.1-1
- Update to 24.08.1

* Fri Aug 16 2024 Pavel Solovev <daron439@gmail.com> - 24.08.0-1
- Update to 24.08.0

* Fri Aug 09 2024 Pavel Solovev <daron439@gmail.com> - 24.07.90-1
- Update to 24.07.90

* Thu Jul 25 2024 Pavel Solovev <daron439@gmail.com> - 24.07.80-1
- Update to 24.07.80

* Thu Jul 04 2024 Pavel Solovev <daron439@gmail.com> - 24.05.2-1
- Update to 24.05.2

* Thu Jun 13 2024 Pavel Solovev <daron439@gmail.com> - 24.05.1-1
- Update to 24.05.1

* Sun Jun 02 2024 Pavel Solovev <daron439@gmail.com> - 24.05.0-2.1
- obsolete kf5-akonadi-server

* Sun Jun 02 2024 Pavel Solovev <daron439@gmail.com> - 24.05.0-2
- fix requires

* Thu May 23 2024 Pavel Solovev <daron439@gmail.com> - 24.05.0-1
- Update to 24.05.0

* Fri Apr 26 2024 Pavel Solovev <daron439@gmail.com> - 24.04.80-1
- Update to 24.04.80

* Thu Apr 11 2024 Pavel Solovev <daron439@gmail.com> - 24.02.2-1
- Update to 24.02.2

* Thu Mar 21 2024 Pavel Solovev <daron439@gmail.com> - 24.02.1-1
- Update to 24.02.1

* Fri Oct 13 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.2-2
- Rebuild (Qt5)

* Thu Oct 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.2-1
- 23.08.2

* Mon Oct 09 2023 Jan Grulich <jgrulich@redhat.com> - 23.08.1-2
- Rebuild (qt5)

* Sat Sep 16 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.1-1
- 23.08.1

* Sat Aug 26 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.0-1
- 23.08.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.3-1
- 23.04.3

* Wed Jun 14 2023 Jan Grulich <jgrulich@redhat.com> - 23.04.2-2
- Rebuild (qt5)

* Tue Jun 06 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.2-1
- 23.04.2

* Sat May 13 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.1-1
- 23.04.1

* Fri Apr 14 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.0-1
- 23.04.0

* Wed Apr 12 2023 Jan Grulich <jgrulich@redhat.com> - 23.03.90-2
- Rebuild (qt5)

* Fri Mar 31 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.90-1
- 23.03.90

* Mon Mar 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.80-1
- 23.03.80

* Thu Mar 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 22.12.3-1
- 22.12.3

* Tue Jan 31 2023 Marc Deop <marcdeop@fedoraproject.org> - 22.12.2-1
- 22.12.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 06 2023 Jan Grulich <jgrulich@redhat.com> - 22.12.1-2
- Rebuild (qt5)

* Tue Jan 03 2023 Justin Zobel <justin@1707.io> - 22.12.1-1
- Update to 22.12.1

* Mon Dec 19 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.12.0-1
- 22.12.0

* Fri Nov 04 2022 Marc Deop i Argemí (Private) <marc@marcdeop.com> - 22.08.3-1
- 22.08.3

* Mon Oct 31 2022 Jan Grulich <jgrulich@redhat.com> - 22.08.2-2
- Rebuild (qt5)

* Fri Oct 14 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.2-1
- 22.08.2

* Mon Sep 26 2022 Than Ngo <than@redhat.com> - 22.08.1-2
- Fixed bz#2129725, konadi-server crash on startup, rebuild against qt-5.15.6

* Thu Sep 08 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.1-1
- 22.08.1

* Fri Aug 19 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.0-1
- 22.08.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.04.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Jan Grulich <jgrulich@redhat.com> - 22.04.3-2
- Rebuild (qt5)

* Thu Jul 07 2022 Than Ngo <than@redhat.com> - 22.04.3-1
- 22.04.3

* Thu Jun 23 2022 Than Ngo <than@redhat.com> - 22.04.2-1
- 22.04.2

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 22.04.1-2
- Rebuild (qt5)

* Thu May 12 2022 Justin Zobel <justin@1707.io> - 22.04.1-1
- Update to 22.04.1

* Mon May 09 2022 Justin Zobel <justin@1707.io> - 22.04.0-1
- Update to 22.04.0

* Tue Mar 08 2022 Jan Grulich <jgrulich@redhat.com> - 21.12.3-2
- Rebuild (qt5)

* Wed Mar 02 2022 Marc Deop <marcdeop@fedoraproject.org> - 21.12.3-1
- 21.12.3

* Fri Feb 04 2022 Rex Dieter <rdieter@fedoraproject.org> - 21.12.2-1
- 21.12.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 06 2022 Marc Deop <marcdeop@fedoraproject.org> - 21.12.1-1
- 21.12.1

* Mon Dec 20 2021 Marc Deop <marcdeop@fedoraproject.org> - 21.12.0-1
- 21.12.0

* Tue Nov 02 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.08.3-1
- 21.08.3

* Thu Oct 21 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.08.2-1
- 21.08.2

* Wed Jul 28 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.3-1
- 21.04.3

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 10 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.2-1
- 21.04.2

* Tue May 11 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.1-1
- 21.04.1

* Tue Apr 27 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.0-1
- 21.04.0

* Wed Mar 03 2021 Rex Dieter <rdieter@fedoraproject.org> - 20.12.3-1
- 20.12.3

* Thu Feb 04 2021 Rex Dieter <rdieter@fedoraproject.org> - 20.12.2-1
- 20.12.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.08.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 07:52:37 CET 2020 Jan Grulich <jgrulich@redhat.com> - 20.08.3-2
- rebuild (qt5)

* Fri Nov  6 15:38:03 CST 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.3-1
- 20.08.3

* Fri Oct 02 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.1-2
- rebuild

* Tue Sep 15 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.1-1
- 20.08.1

* Fri Sep 11 2020 Jan Grulich <jgrulich@redhat.com> - 20.08.0-2
- rebuild (qt5)

* Tue Aug 18 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.0-1
- 20.08.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.3-3
- Rebuilt for https://fedoraprojprivate

* Sat Mar 07 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.3-1
- 19.12.3

* Tue Feb 04 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.2-1
- 19.12.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.1-1
- 19.12.1

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 19.08.3-2
- rebuild (qt5)

* Mon Nov 11 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.3-1
- 19.08.3

* Fri Oct 18 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.2-1
- 19.08.2

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 19.04.3-3
- rebuild (qt5)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.04.3-1
- 19.04.3

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 19.04.2-2
- rebuild (qt5)

* Wed Jun 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.04.2-1
- 19.04.2

* Tue Jun 04 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.3-3
- rebuild (qt5)

* Fri Apr 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.3-2
- pull in upstream fixes

* Fri Mar 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.3-1
- 18.12.3

* Sun Mar 03 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.2-2
- rebuild (qt5)

* Tue Feb 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.2-1
- 18.12.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.1-1
- 18.12.1

* Tue Dec 18 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.12.0-2
- rebuild

* Fri Dec 14 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.12.0-1
- 18.12.0

* Tue Dec 11 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.3-2
- rebuild (Qt5)

* Tue Nov 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.3-1
- 18.08.3

* Sun Oct 14 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.2-2
- move akonadi_knut_resource to main (from -devel)
- use %%make_build

* Wed Oct 10 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.2-1
- 18.08.2

* Mon Oct 01 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.1-1
- 18.08.1

* Fri Sep 21 2018 Jan Grulich <jgrulich@redhat.com> - 18.04.3-3
- rebuild (qt5)

* Wed Aug 22 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.3-2
- rebuild (qt5)

* Fri Jul 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.3-1
- 18.04.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.04.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.2-2
- rebuild (qt5)

* Wed Jun 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.2-1
- 18.04.2

* Sun May 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.1-3
- bootstrap off

* Sun May 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.1-2
- rebuild (qt5)
- bootstrap mode (avoids broken qtwebkit for now)
- drop Requires: kf5-filesystem (tier 1 frameworks handle that)
- devel: drop R: kf5-kdelibs4support

* Wed May 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.1-1
- 18.04.1

* Sat Apr 21 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.0-2
- own /usr/share/akonadi/plugins, update scriptlets, cleanup

* Fri Apr 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.0-1
- 18.04.0

* Tue Mar 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.3-1
- 17.12.3

* Wed Feb 14 2018 Jan Grulich <jgrulich@redhat.com> - 17.12.2-2
- rebuild (qt5)

* Tue Feb 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.2-1
- 17.12.2

* Thu Jan 25 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.1-2
- rebuild (qt5)

* Thu Jan 11 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.1-1
- 17.12.1

* Wed Dec 20 2017 Jan Grulich <jgrulich@redhat.com> - 17.12.0-2
- rebuild (qt5)

* Tue Dec 12 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.12.0-1
- 17.12.0

* Wed Dec 06 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.11.90-1
- 17.11.90

* Sun Nov 26 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.11.80-2
- rebuild (qt5)

* Wed Nov 22 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.11.80-1
- 17.11.80

* Wed Nov 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.3-1
- 17.08.3

* Mon Oct 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.1-3
- rebuild (qt5)

* Tue Sep 26 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.1-2
- backport mariadb workaround (#1491316)

* Mon Sep 25 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.1-1
- 17.08.1

* Fri Jul 28 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.3-1
- 17.04.3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17.04.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.2-3
- rebuild (qt5)

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 17.04.2-2
- Rebuilt for Boost 1.64

* Thu Jun 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.2-1
- 17.04.2

* Mon May 22 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.1-3
- rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 17.04.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Thu May 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.1-1
- 17.04.1

* Thu May 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.3-3
- rebuild (qt5)

* Thu Mar 30 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.3-2
- rebuild, update URL

* Thu Mar 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.3-1
- 16.12.3

* Thu Feb 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.2-1
- 16.12.2

* Mon Jan 16 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.1-1
- 16.12.1

* Thu Dec 15 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.3-2
- rebuild (qt5)

* Mon Dec 05 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.3-1
- 16.08.3

* Thu Nov 17 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.2-2
- release++

* Thu Nov 17 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.2-1.2
- branch rebuild (qt5)

* Thu Oct 13 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.2-1
- 16.08.2

* Thu Oct 13 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.1-3
- Obsoletes: kf5-akonadi-socialutils(-devel) (#1384477)

* Sun Sep 25 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.1-2
- drop hack to workaround issue(s) with case-insensitive filesystems (#1379080)

* Thu Sep 08 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.1-1
- 16.08.1

* Sat Sep 03 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.0-1
- 16.08.0

* Sat Sep 03 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.3-4
- rebuild (gcc)

* Sun Jul 17 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.3-3
- backport FTBFS fix
- make build use mysql backend as default (so tests use that)
- add alternatives support for sqlite backend to main pkg

* Wed Jul 13 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.3-2
- BR: qt5-qtbase-private-devel (sqlite3 driver plugin)

* Sun Jul 10 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.3-1
- 16.04.3

* Tue Jun 28 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.2-1
- 16.04.2

* Tue May 24 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.1-2
- backport Fix-MySQL-5.7-support.patch

* Sun May 08 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.1-1
- 16.04.1

* Sun May 01 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.0-2
- -devel: Obsoletes: kf5-akonadi-devel, add Requires: inherited from kf5-aknoadi-devel

* Sat Apr 30 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.0-1
- 16.04.0, update URL, support bootstrap, add %%check

* Mon Mar 21 2016 Rex Dieter <rdieter@fedoraproject.org> - 15.12.3-3
- -mysql: Provides: akonadi-mysql

* Thu Mar 17 2016 Rex Dieter <rdieter@fedoraproject.org> - 15.12.3-2
- Recommends: kf5-akonadi-mysql

* Tue Mar 15 2016 Rex Dieter <rdieter@fedoraproject.org> - 15.12.3-1
- 15.12.3

* Sun Feb 14 2016 Rex Dieter <rdieter@fedoraproject.org> - 15.12.2-1
- 15.12.2

* Sat Feb 06 2016 Rex Dieter <rdieter@fedoraproject.org> 15.12.1-1
- 15.12.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 15.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 17 2015 Rex Dieter <rdieter@fedoraproject.org> 15.12.0-2
- move dbus-1/interfaces to -devel, (unversioned) Conflicts: akonadi-devel

* Tue Dec 15 2015 Jan Grulich <jgrulich@redhat.com> - 15.12-0-1
- Update to 15.12.0

* Fri Dec 11 2015 Rex Dieter <rdieter@fedoraproject.org> 15.11.90-2
- Conflicts: akonadi < 1.13.0-100 (#1289646)

* Mon Dec 07 2015 Jan Grulich <jgrulich@redhat.com> - 15.11.90-1
- Update to 15.11.90

* Thu Dec 03 2015 Jan Grulich <jgrulich@redhat.com> - 15.11.80-1
- Update to 15.11.80

* Mon Aug 24 2015 Daniel Vrátil <dvratil@redhat.com> - 15.08.0-1
- Initial version, based on akonadi.spec
