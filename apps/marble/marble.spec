%global commit0 d9e23912775aa566b5e48c08cf85fc2f84f7e469
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

Name:    marble
Summary: Virtual globe and world atlas
Epoch:   1
Version: 24.08.2
Release: 1%{?dist}

License: Apache-2.0 AND BSD-3-Clause AND CC0-1.0 AND GPL-3.0-only AND GPL-3.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND MIT AND (LGPL-2.1-only WITH Qt-LGPL-exception-1.1)
URL:     https://apps.kde.org/marble/
%apps_source

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: extra-cmake-modules
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kcrash-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-knewstuff-devel
BuildRequires: kf5-kparts-devel
BuildRequires: kf5-krunner-devel
BuildRequires: kf5-kservice-devel
BuildRequires: kf5-kwallet-devel
BuildRequires: kf5-rpm-macros
%if 0%{?fedora} && ! 0%{?flatpak}
BuildRequires: pkgconfig(libgps)
%endif
BuildRequires: pkgconfig(phonon4qt5)
BuildRequires: pkgconfig(protobuf)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Script)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Quick)
%ifarch %{?qt5_qtwebengine_arches}
BuildRequires: cmake(Qt5WebEngine)
BuildRequires: cmake(Qt5WebEngineWidgets)
%endif
BuildRequires: pkgconfig(Qt5SerialPort)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5Sql)
BuildRequires: pkgconfig(Qt5Concurrent)
BuildRequires: pkgconfig(Qt5PrintSupport)
BuildRequires: pkgconfig(Qt5Location) pkgconfig(Qt5Positioning)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: pkgconfig(shapelib)
BuildRequires: pkgconfig(shared-mime-info)
BuildRequires: zlib-devel

# when split occurred
Obsoletes: kdeedu-marble < 4.7.0-10
Provides:  kdeedu-marble = %{version}-%{release}
Provides:  kdeedu-marble%{?_isa} = %{version}-%{release}

# fixme, insert last build this was included -- rex
Obsoletes: python-marble < %{epoch}:%{version}-%{release}

Requires: %{name}-widget-qt5%{?_isa} = %{epoch}:%{version}-%{release}

# filter plugin provides
%global __provides_exclude_from ^(%{_libdir}/marble/plugins/.*\\.so)$

%description
Marble is a Virtual Globe and World Atlas that you can use to learn more
about Earth: You can pan and zoom around and you can look up places and
roads. A mouse click on a place label will provide the respective Wikipedia
article.

Of course it's also possible to measure distances between locations or watch
the current cloud cover. Marble offers different thematic maps: A classroom-
style topographic map, a satellite view, street map, earth at night and
temperature and precipitation maps. All maps include a custom map key, so it
can also be used as an educational tool for use in class-rooms. For
educational purposes you can also change date and time and watch how the
starry sky and the twilight zone on the map change.

In opposite to other virtual globes Marble also features multiple
projections: Choose between a Flat Map ("Plate carré"), Mercator or the Globe.

%package qt
Summary: Marble qt-only interface
Requires: %{name}-widget-qt5%{?_isa} = %{epoch}:%{version}-%{release}
Requires: %{name}-common = %{epoch}:%{version}-%{release}
%description qt
%{summary}.

%package common
Summary:  Common files of %{name}
BuildArch: noarch
%if ! 0%{?mobile}
Obsoletes: marble-mobile < %{epoch}:%{version}-%{release}
%endif
%if ! 0%{?touch}
Obsoletes: marble-touch < %{epoch}:%{version}-%{release}
%endif
%description common
{summary}.

%package astro
Summary: Marble Astro Library
Requires: %{name}-common = %{epoch}:%{version}-%{release}
%description astro
%{summary}.

%package astro-devel
Summary: Development files for Marble Astro Library
Requires: %{name}-astro%{?_isa} = %{epoch}:%{version}-%{release}
%description astro-devel
%{summary}.

%package widget-data
Summary: Marble Widget data
Requires: %{name}-common = %{epoch}:%{version}-%{release}
BuildArch: noarch
%description widget-data
%{summary}.

%package widget-qt5
Summary: Marble Widget Library
Requires: %{name}-astro%{?_isa} = %{epoch}:%{version}-%{release}
Requires: %{name}-widget-data = %{epoch}:%{version}-%{release}
%description widget-qt5
%{summary}.

%package widget-qt5-devel
Summary: Development files for Qt5 Marble Widget
Requires: %{name}-widget-qt5%{?_isa} = %{epoch}:%{version}-%{release}
Requires: cmake(Qt5Xml)
Requires: cmake(Qt5Widgets)
%ifarch %{?qt5_qtwebengine_arches}
Requires: cmake(Qt5WebEngine)
Requires: cmake(Qt5WebEngineWidgets)
%endif
%description widget-qt5-devel
%{summary}.


%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1

rm -rf src/3rdparty/zlib


%build
%cmake_kf5 \
  -Wno-dev \
  -DBUILD_MARBLE_TESTS:BOOL=OFF \
  -DMARBLE_DATA_PATH:PATH="%{_datadir}/marble/data" \
  -DMARBLE_PRI_INSTALL_DIR:PATH="%{_qt5_archdatadir}/mkspecs/modules" \
  -DWITH_DESIGNER_PLUGIN:BOOL=OFF

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html
# hack around buggy --with-qt ^^
%find_lang_kf5 marble_qt
cat marble_qt.lang >> %{name}.lang


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.marble.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.plasma.worldclock.appdata.xml ||:
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.plasma.worldmap.appdata.xml ||:
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.marble.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.marble-qt.desktop


%files
%{_bindir}/marble
%{_datadir}/kxmlgui5/marble/
%{_kf5_metainfodir}/org.kde.marble.appdata.xml
%{_kf5_metainfodir}/org.kde.plasma.worldclock.appdata.xml
%{_kf5_metainfodir}/org.kde.plasma.worldmap.appdata.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.worldclock/
%{_datadir}/plasma/wallpapers/org.kde.plasma.worldmap/
%{_kf5_datadir}/kservices5/plasma-applet-org.kde.plasma.worldclock.desktop
%{_kf5_datadir}/kservices5/plasma-wallpaper-org.kde.plasma.worldmap.desktop
%{_datadir}/applications/org.kde.marble.desktop
%{_datadir}/applications/marble_geo.desktop
%{_datadir}/applications/marble_geojson.desktop
%{_datadir}/applications/marble_gpx.desktop
%{_datadir}/applications/marble_kml.desktop
%{_datadir}/applications/marble_kmz.desktop
%{_datadir}/applications/marble_shp.desktop
%{_datadir}/applications/marble_worldwind.desktop
%{_datadir}/config.kcfg/marble.kcfg
%{_datadir}/kservices5/marble_thumbnail_geojson.desktop
%{_datadir}/kservices5/marble_thumbnail_gpx.desktop
%{_datadir}/kservices5/marble_thumbnail_kml.desktop
%{_datadir}/kservices5/marble_thumbnail_kmz.desktop
%{_datadir}/kservices5/marble_thumbnail_osm.desktop
%{_datadir}/kservices5/marble_thumbnail_shp.desktop
%{_datadir}/qlogging-categories5/marble.categories

%files common -f %{name}.lang
%license LICENSE.txt
%doc CREDITS MANIFESTO.txt USECASES
%{_datadir}/icons/hicolor/*/apps/marble.*
%{_datadir}/mime/packages/geo.xml
%dir %{_datadir}/marble/

%files qt
%{_bindir}/marble-qt
%{_datadir}/applications/org.kde.marble-qt.desktop

%files astro
%{_libdir}/libastro.so.*

%files astro-devel
%{_includedir}/astro/
%{_kf5_libdir}/libastro.so
%{_libdir}/cmake/Astro/

%files widget-data
%{_datadir}/marble/data/

%files widget-qt5
%{_libdir}/libmarblewidget-qt5.so.*
%{_libdir}/marble/plugins/
%{_qt5_plugindir}/marblethumbnail.so
%{_kf5_plugindir}/krunner/plasma_runner_marble.so
# include part here too
%{_datadir}/kservices5/marble_part.desktop
%{_qt5_plugindir}/libmarble_part.so
%{_libdir}/libmarbledeclarative.so
%{_kf5_qmldir}/org/kde/marble/

%files widget-qt5-devel
%{_includedir}/marble/
%{_libdir}/libmarblewidget-qt5.so
%{_libdir}/cmake/Marble/
%{_qt5_archdatadir}/mkspecs/modules/qt_Marble.pri


%changelog
* Mon Oct 07 2024 Pavel Solovev <daron439@gmail.com> - 1:24.08.2-1
- Update to 24.08.2

* Tue Sep 10 2024 Pavel Solovev <daron439@gmail.com> - 1:24.08.1-1
- Update to 24.08.1

* Fri Aug 16 2024 Pavel Solovev <daron439@gmail.com> - 1:24.08.0-1
- Update to 24.08.0

* Fri Aug 09 2024 Pavel Solovev <daron439@gmail.com> - 1:24.07.90-1
- Update to 24.07.90

* Thu Jul 25 2024 Pavel Solovev <daron439@gmail.com> - 1:24.07.80-1
- Update to 24.07.80

* Thu Jul 04 2024 Pavel Solovev <daron439@gmail.com> - 1:24.05.2-1
- Update to 24.05.2

* Thu Jun 13 2024 Pavel Solovev <daron439@gmail.com> - 1:24.05.1-1
- Update to 24.05.1

* Thu May 23 2024 Pavel Solovev <daron439@gmail.com> - 1:24.05.0-1
- Update to 24.05.0

* Fri Apr 26 2024 Pavel Solovev <daron439@gmail.com> - 1:24.04.80-1
- Update to 24.04.80

* Thu Apr 11 2024 Pavel Solovev <daron439@gmail.com> - 1:24.02.2-1
- Update to 24.02.2

* Thu Mar 21 2024 Pavel Solovev <daron439@gmail.com> - 1:24.02.1-1
- Update to 24.02.1

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:24.02.0-1
- 24.02.0

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:24.01.95-1
- 24.01.95

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:24.01.90-1
- 24.01.90

* Mon Jan 08 2024 Steve Cossette <farchord@gmail.com> - 1:24.01.85-1
- 24.01.85 (Qt5)

* Sun Dec 24 2023 Sandro Mani <manisandro@gmail.com> - 1:23.08.2-2
- Rebuild (shapelib)

* Thu Oct 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:23.08.2-1
- 23.08.2

* Sat Sep 16 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:23.08.1-1
- 23.08.1

* Sat Aug 26 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:23.08.0-1
- 23.08.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:23.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:23.04.3-1
- 23.04.3

* Tue Jun 06 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:23.04.2-1
- 23.04.2

* Sat May 13 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:23.04.1-1
- 23.04.1

* Fri Apr 14 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:23.04.0-1
- 23.04.0

* Fri Mar 31 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:23.03.90-1
- 23.03.90

* Mon Mar 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:23.03.80-1
- 23.03.80

* Thu Mar 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1:22.12.3-1
- 22.12.3

* Tue Jan 31 2023 Marc Deop <marcdeop@fedoraproject.org> - 1:22.12.2-1
- 22.12.2

* Tue Jan 24 2023 Adam Williamson <awilliam@redhat.com> - 1:22.12.1-3
- rebuild for new libgps

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:22.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 Justin Zobel <justin@1707.io> - 22.12.1-1
- Update to 22.12.1

* Mon Dec 19 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:22.12.0-1
- 22.12.0

* Fri Nov 04 2022 Marc Deop i Argemí (Private) <marc@marcdeop.com> - 1:22.08.3-1
- 22.08.3

* Fri Oct 14 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:22.08.2-1
- 22.08.2

* Thu Sep 08 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:22.08.1-1
- 22.08.1

* Fri Aug 19 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:22.08.0-1
- 22.08.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:22.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Than Ngo <than@redhat.com> - 22.04.3-1
- 22.04.3

* Thu May 12 2022 Justin Zobel <justin@1707.io> - 22.04.1-1
- Update to 22.04.1

* Mon May 09 2022 Justin Zobel <justin@1707.io> - 22.04.0-1
- Update to 22.04.0

* Fri May 06 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:21.12.3-2
- Rebuild for new gpsd

* Wed Mar 02 2022 Marc Deop <marcdeop@fedoraproject.org> - 1:21.12.3-1
- 21.12.3

* Fri Feb 04 2022 Rex Dieter <rdieter@fedoraproject.org> - 1:21.12.2-1
- 21.12.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:21.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 06 2022 Rex Dieter <rdieter@fedoraproject.org> - 1:21.12.1-1
- 21.12.1

* Mon Dec 27 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:21.12.0-1
- 21.12.0

* Sat Nov 06 2021 Adrian Reber <adrian@lisas.de> - 1:21.08.3-2
- Rebuilt for protobuf 3.19.0

* Tue Nov 02 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:21.08.3-1
- 21.08.3

* Tue Oct 26 2021 Adrian Reber <adrian@lisas.de> - 1:21.08.2-2
- Rebuilt for protobuf 3.18.1

* Fri Oct 15 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:21.08.2-1
- 21.08.2

* Wed Aug 11 2021 Björn Esser <besser82@fedoraproject.org> - 1:21.04.3-2
- Rebuild (gpsd)

* Wed Jul 28 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:21.04.3-1
- 21.04.3

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:21.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 10 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:21.04.2-1
- 21.04.2

* Tue May 11 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:21.04.1-1
- 21.04.1

* Sat Apr 17 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:21.04.0-1
- 21.04.0

* Fri Feb 19 2021 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1:20.12.2-5
- fix GeoNames web service URL, is now api.geonames.org (kde#432598)

* Wed Feb 17 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:20.12.2-4
- -widget-qt5-devel: update Requires (esp. Qt5WebEngine )

* Sun Feb 07 2021 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1:20.12.2-3
- add missing BuildRequires: pkgconfig(protobuf) (new optional dep in 20.12)

* Sun Feb 07 2021 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1:20.12.2-2
- add missing BuildRequires on QtWebEngine (where supported) (kde#431152)
- drop obsolete BuildRequires on QtWebKit, upstream dropped support years ago

* Tue Feb 02 2021 Rex Dieter <rdieter@fedoraproject.org> - 1:20.12.2-1
- 20.12.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:20.08.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Marek Kasik <mkasik@redhat.com> - 1:20.08.3-2
- Rebuild for the new gpsd

* Fri Nov  6 13:22:57 CST 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:20.08.3-1
- 20.08.3

* Tue Sep 15 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:20.08.1-1
- 20.08.1

* Tue Aug 18 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:20.08.0-1
- 20.08.0

* Mon Aug 10 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:20.04.3-4
- use new cmake macros

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:20.04.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:20.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:20.04.3-1
- 20.04.3

* Thu Jun 18 2020 Björn Esser <besser82@fedoraproject.org> - 1:20.04.2-2
- Rebuild (gpsd)

* Fri Jun 12 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:20.04.2-1
- 20.04.2

* Tue May 26 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:20.04.1-1
- 20.04.1

* Fri Apr 24 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:20.04.0-1
- 20.04.0

* Fri Mar 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:19.12.3-1
- 19.12.3

* Tue Feb 04 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:19.12.2-1
- 19.12.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:19.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Rex Dieter <rdieter@fedoraproject.org> - 1:19.12.1-1
- 19.12.1

* Tue Nov 12 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:19.08.3-1
- 19.08.3

* Thu Oct 17 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:19.08.2-1
- 19.08.2

* Sun Sep 29 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:19.08.1-1
- 19.08.1

* Mon Aug 19 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:19.08.0-1
- 19.08.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:19.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:19.04.3-1
- 19.04.3

* Wed Jul 03 2019 Björn Esser <besser82@fedoraproject.org> - 1:19.04.2-2
- Rebuild (gpsd)

* Tue Jun 04 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:19.04.2-1
- 19.04.2

* Fri May 10 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:19.04.1-1
- 19.04.1

* Fri Mar 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:18.12.3-1
- 18.12.3

* Tue Feb 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:18.12.2-1
- 18.12.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:18.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 1:18.12.1-1
- 18.12.1

* Sat Dec 15 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.12.0-1
- 18.12.0

* Tue Nov 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:18.08.3-1
- 18.08.3

* Tue Oct 16 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:18.08.2-3
- rebuild (gpsd)

* Wed Oct 10 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:18.08.2-2
- rebuild (gpsd)

* Wed Oct 10 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:18.08.2-1
- 18.08.2

* Sun Sep 16 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:18.08.1-1
- 18.08.1

* Thu Jul 12 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:18.04.3-1
- 18.04.3

* Wed Jun 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:18.04.2-1
- 18.04.2

* Tue May 08 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:18.04.1-1
- 18.04.1

* Fri Apr 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:18.04.0-1
- 18.04.0

* Mon Apr 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:18.03.90-1
- 18.03.90

* Tue Mar 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:17.12.3-1
- 17.12.3

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:17.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Feb 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:17.12.2-1
- 17.12.2

* Thu Jan 11 2018 Rex Dieter <rdieter@fedoraproject.org> - 1:17.12.1-1
- 17.12.1

* Thu Dec 28 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:17.12.0-1
- 17.12.0

* Wed Nov 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:17.08.3-1
- 17.08.3

* Wed Oct 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:17.08.2-1
- 17.08.2

* Mon Sep 25 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:17.08.1-2
- rebuild (gpsd)

* Tue Sep 05 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:17.08.1-1
- 17.08.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:16.12.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:16.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:16.12.3-1
- 16.12.3

* Thu Feb 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:16.12.2-1
- 16.12.2

* Wed Jan 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:16.12.1-2
- do not omit libmarbledeclarative

* Wed Jan 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 1:16.12.1-1
- 16.12.1

* Sun Dec 11 2016 Igor Gnatenko <ignatenko@redhat.com> - 1:16.08.3-2
- Rebuild for shapelib SONAME bump

* Mon Dec 05 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:16.08.3-1
- 16.08.3

* Thu Oct 13 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:16.08.2-1
- 16.08.2

* Wed Sep 07 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:16.08.1-1
- 16.08.1

* Sun Aug 14 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:16.08.0-2
- BR: Qt5SerialPort

* Fri Aug 12 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:16.08.0-1
- 16.08.0

* Sat Aug 06 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:16.07.90-1
- 16.07.90

* Sat Jul 30 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:16.07.80-1
- 16.07.80

* Sat Jul 09 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:16.04.3-1
- 16.04.3

* Sun Jun 12 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:16.04.2-1
- 16.04.2

* Sun May 08 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:16.04.1-1
- 16.04.1

* Fri Apr 22 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:16.04.0-1
- 16.04.0

* Thu Apr 14 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:16.03.80-1
- 16.03.80

* Tue Mar 22 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:15.12.3-2
- filter plugin provides

* Tue Mar 15 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:15.12.3-1
- 15.12.3

* Sun Feb 14 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:15.12.2-1
- 15.12.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:15.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:15.12.1-1
- 15.12.1

* Wed Dec 23 2015 Rex Dieter <rdieter@fedoraproject.org> - 1:15.12.0-1
- 15.12.0, qt5/kf5 only

* Mon Nov 30 2015 Rex Dieter <rdieter@fedoraproject.org> - 1:15.08.3-1
- 15.08.3

* Sun Sep 20 2015 Rex Dieter <rdieter@fedoraproject.org> - 1:15.08.1-1
- 15.08.1


* Sun Aug 30 2015 Rex Dieter <rdieter@fedoraproject.org> 1:15.08.0-3
- explitly set CMAKE_MODULES_INSTALL_PATH, MARBLE_DATA_PATH, MARBLE_PLUGIN_PATH

* Sun Aug 30 2015 Rex Dieter <rdieter@fedoraproject.org> 1:15.08.0-2
- -widget-devel: include FindMarble.cmake

* Thu Aug 20 2015 Than Ngo <than@redhat.com> - 1:15.08.0-1
- 15.08.0
- drop -libs, -devel metapackages

* Mon Aug 17 2015 Rex Dieter <rdieter@fedoraproject.org> 1:15.04.3-1
- 15.04.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:15.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Rex Dieter <rdieter@fedoraproject.org> - 1:15.04.2-1
- 15.04.2

* Tue May 26 2015 Rex Dieter <rdieter@fedoraproject.org> - 1:15.04.1-1
- 15.04.1

* Tue Apr 21 2015 Rex Dieter <rdieter@fedoraproject.org> 1:15.04.0-2
- enable quazip-qt5 support

* Tue Apr 14 2015 Rex Dieter <rdieter@fedoraproject.org> - 1:15.04.0-1
- 15.04.0

* Thu Mar 12 2015 Rex Dieter <rdieter@fedoraproject.org> - 1:14.12.3-4
- widget-qt5: don't try to use qt4 versions of qextserialport quazip
- wigget-qt5: omit libRoutingPlugin.so for now, it links qt4 libphonon

* Wed Mar 11 2015 Rex Dieter <rdieter@fedoraproject.org> - 1:14.12.3-3
- install complete cityplacemarks.cache (#1093552)
- disable -mobile (doesn't work very well)

* Sun Mar 08 2015 Rex Dieter <rdieter@fedoraproject.org> 1:14.12.3-2
- rebuild (libgps)

* Sun Mar 01 2015 Rex Dieter <rdieter@fedoraproject.org> - 1:14.12.3-1
- 14.12.3

* Tue Feb 24 2015 Than Ngo <than@redhat.com> - 14.12.2-1
- 14.12.2

* Mon Feb 23 2015 Rex Dieter <rdieter@fedoraproject.org> - 1:14.12.1-2
- new -astro(-devel), -widget(-data,-devel), -widget-qt5(-devel) subpkgs

* Fri Jan 16 2015 Rex Dieter <rdieter@fedoraproject.org> - 1:14.12.1-1
- 14.12.1

* Tue Dec 09 2014 Rex Dieter <rdieter@fedoraproject.org> - 1:14.11.97-1
- 14.11.97

* Sat Nov 08 2014 Rex Dieter <rdieter@fedoraproject.org> - 1:4.14.3-1
- 4.14.3

* Sat Oct 11 2014 Rex Dieter <rdieter@fedoraproject.org> - 1:4.14.2-1
- 4.14.2

* Wed Sep 24 2014 Rex Dieter <rdieter@fedoraproject.org> 1:4.14.1-3
- fix -common deps (it's noarch, don't want %%_isa here)

* Tue Sep 23 2014 Richard Hughes <richard@hughsie.com> - 1:4.14.1-2
- Add a hard requires on marble-common (which contains the icon) on the main
  applications. The AppStream generator only can cope with one layer of dep-
  resolution and the app->libs->common chain means the icons don't get included.

* Mon Sep 15 2014 Rex Dieter <rdieter@fedoraproject.org> - 1:4.14.1-1
- 4.14.1

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Aug 14 2014 Rex Dieter <rdieter@fedoraproject.org> - 1:4.14.0-1
- 4.14.0

* Wed Aug 06 2014 Rex Dieter <rdieter@fedoraproject.org> 1:4.13.97-2
- marble-common scriptlet generates "touch: command not found" (#1127350)

* Tue Aug 05 2014 Rex Dieter <rdieter@fedoraproject.org> - 1:4.13.97-1
- 4.13.97

* Mon Jul 14 2014 Rex Dieter <rdieter@fedoraproject.org> - 1:4.13.3-1
- 4.13.3

* Thu Jul 03 2014 Rex Dieter <rdieter@fedoraproject.org> 1:4.13.2-3
- optimize mimeinfo scriptlet, move mime bits to -common

* Thu Jun 26 2014 Rex Dieter <rdieter@fedoraproject.org> 1:4.13.2-2
- BR: qtwebkit ...

* Mon Jun 09 2014 Rex Dieter <rdieter@fedoraproject.org> - 1:4.13.2-1
- 4.13.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 11 2014 Rex Dieter <rdieter@fedoraproject.org> - 1:4.13.1-1
- 4.13.1

* Sat Apr 12 2014 Rex Dieter <rdieter@fedoraproject.org> - 1:4.13.0-1
- 4.13.0

* Thu Apr 03 2014 Rex Dieter <rdieter@fedoraproject.org> - 1:4.12.97-1
- 4.12.97

* Sat Mar 22 2014 Rex Dieter <rdieter@fedoraproject.org> - 1:4.12.95-1
- 4.12.95

* Wed Mar 19 2014 Rex Dieter <rdieter@fedoraproject.org> - 1:4.12.90-1
- 4.12.90
- disable broken python bindings

* Sun Mar 16 2014 Rex Dieter <rdieter@fedoraproject.org> 4.12.3-2
- rebuild (sip)

* Sat Mar 01 2014 Rex Dieter <rdieter@fedoraproject.org> - 1:4.12.3-1
- 4.12.3

* Thu Feb 27 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1:4.12.2-3
- apply upstream fix for geonames.org API change (kde#331004)
- fix the hardcoded libmarblewidget version to actually match what is shipped

* Thu Feb 06 2014 Rex Dieter <rdieter@fedoraproject.org> - 1:4.12.2-2
- -libs: track libmarblewidget soname

* Fri Jan 31 2014 Rex Dieter <rdieter@fedoraproject.org> - 1:4.12.2-1
- 4.12.2

* Fri Jan 10 2014 Rex Dieter <rdieter@fedoraproject.org> - 1:4.12.1-1
- 4.12.1

* Tue Dec 24 2013 Rex Dieter <rdieter@fedoraproject.org> 1:4.12.0-2
- -common,-mobile,-qt subpkgs (#1045919)

* Thu Dec 19 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:4.12.0-1
- 4.12.0

* Sun Dec 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:4.11.97-1
- 4.11.97

* Sun Dec 01 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1:4.11.95-3
- backport more Python bindings updates from 4.11.97, reenable Python bindings

* Tue Nov 26 2013 Rex Dieter <rdieter@fedoraproject.org> 1:4.11.95-2
- rebuild (gpsd)

* Thu Nov 21 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:4.11.95-1
- 4.11.95 (disable still-not-building python bindings)

* Sun Nov 17 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1:4.11.90-3
- forward-port Python bindings updates from 4.11, reenable Python bindings

* Sun Nov 17 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1:4.11.90-2
- fix designer plugin path (kde#327690), reenable designer plugin

* Sat Nov 16 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:4.11.90-1
- 4.11.90, disable broken python bindings, designer plugin

* Sat Nov 02 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:4.11.3-1
- 4.11.3

* Sat Sep 28 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:4.11.2-1
- 4.11.2

* Wed Sep 04 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:4.11.1-1
- 4.11.1

* Mon Aug 12 2013 Rex Dieter <rdieter@fedoraproject.org> 1:4.11.0-3
- respin

* Sun Aug 11 2013 Rex Dieter <rdieter@fedoraproject.org> 1:4.11.0-2
- (re)enable python bindings

* Thu Aug 08 2013 Than Ngo <than@redhat.com> - 1:4.11.0-1
- 4.11.0

* Thu Jul 25 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:4.10.97-1
- 4.10.97

* Tue Jul 23 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:4.10.95-1
- 4.10.95

* Tue Jul 02 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1:4.10.90-2
- BuildRequires: qextserialport-devel quazip-devel
- find libqextserialport-1.2.so
- update the file list to list the files for kmz support (based on quazip)

* Thu Jun 27 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:4.10.90-1
- 4.10.90
- disable python bindings (for now, broken)

* Mon Jun 17 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.4-2
- rebuild (sip)

* Sat Jun 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:4.10.4-1
- 4.10.4

* Mon May 06 2013 Than Ngo <than@redhat.com> - 4.10.3-1
- 4.10.3

* Sun Mar 31 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:4.10.2-1
- 4.10.2

* Sat Mar 02 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.1-1
- 4.10.1

* Fri Feb 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:4.10.0-1
- 4.10.0

* Mon Jan 21 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:4.9.98-1
- 4.9.98

* Fri Jan 04 2013 Rex Dieter <rdieter@fedoraproject.org> - 1:4.9.97-1
- 4.9.97

* Sun Dec 23 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1:4.9.95-2
- apply upstream patch to fix the build of the Python bindings

* Thu Dec 20 2012 Rex Dieter <rdieter@fedoraproject.org> - 1:4.9.95-1
- 4.9.95
- disable python bindings

* Mon Dec 03 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.90-1
- 4.9.90 (4.10 beta2)

* Mon Dec 03 2012 Than Ngo <than@redhat.com> - 4.9.4-1
- 4.9.4

* Sat Nov 03 2012 Rex Dieter <rdieter@fedoraproject.org> - 1:4.9.3-1
- 4.9.3

* Thu Nov 01 2012 Rex Dieter <rdieter@fedoraproject.org> 1:4.9.2-4
- BR: shapelib-devel

* Wed Oct 03 2012 Rex Dieter <rdieter@fedoraproject.org> 1:4.9.2-3
- rebuild (sip)

* Sat Sep 29 2012 Rex Dieter <rdieter@fedoraproject.org> 1:4.9.2-2
- re-enable python bindings

* Sat Sep 29 2012 Rex Dieter <rdieter@fedoraproject.org> - 1:4.9.2-1
- 4.9.2

* Mon Sep 03 2012 Than Ngo <than@redhat.com> - 1:4.9.1-1
- 4.9.1

* Fri Jul 27 2012 Rex Dieter <rdieter@fedoraproject.org> - 1:4.9.0-1
- 4.9.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.8.97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Rex Dieter <rdieter@fedoraproject.org> - 1:4.8.97-1
- 4.8.97

* Wed Jun 27 2012 Rex Dieter <rdieter@fedoraproject.org> - 1:4.8.95-1
- 4.8.95

* Sat Jun 09 2012 Rex Dieter <rdieter@fedoraproject.org> - 1:4.8.90-1
- 4.8.90

* Tue May 29 2012 Rex Dieter <rdieter@fedoraproject.org> 1:4.8.80-1
- 4.8.80

* Mon Apr 30 2012 Jaroslav Reznik <jreznik@redhat.com> - 1:4.8.3-1
- 4.8.3

* Fri Mar 30 2012 Rex Dieter <rdieter@fedoraproject.org> - 1:4.8.2-1
- 4.8.2

* Tue Mar 27 2012 Rex Dieter <rdieter@fedoraproject.org> 1:4.8.1-2
- enable designer plugin (#807128)

* Mon Mar 05 2012 Jaroslav Reznik <jreznik@redhat.com> - 1:4.8.1-1
- 4.8.1

* Thu Feb 09 2012 Jaroslav Reznik <jreznik@redhat.com> 1:4.8.0-6
- more qt 4.8 fixes (show proper icons for MarbleLegendBrowser)

* Tue Feb 07 2012 Rex Dieter <rdieter@fedoraproject.org> 1:4.8.0-5
- upstream qt48_transparency patch (fix display of water/ocenas in atlas view)

* Mon Feb 06 2012 Rex Dieter <rdieter@fedoraproject.org> 1:4.8.0-4
- drop hard-coded -O3 optimization

* Fri Feb 03 2012 Rex Dieter <rdieter@fedoraproject.org> 1:4.8.0-3
- python-marble: fix versioned dependency

* Fri Feb 03 2012 Rex Dieter <rdieter@fedoraproject.org> 1:4.8.0-2
- enable (experimental) python bindings
- s/kdebase-runtime/kde-runtime/

* Sun Jan 22 2012 Rex Dieter <rdieter@fedoraproject.org> - 1:4.8.0-1
- 4.8.0

* Wed Jan 04 2012 Radek Novacek <rnovacek@redhat.com> - 1:4.7.97-1
- 4.7.97

* Wed Dec 21 2011 Radek Novacek <rnovacek@redhat.com> - 1:4.7.95-1
- 4.7.95

* Mon Dec 05 2011 Rex Dieter <rdieter@fedoraproject.org> 1:4.7.90-2
- set IGNORE_CMAKE_INSTALL_PREFIX_FOR_DECLARATIVE_PLUGINS

* Sun Dec 04 2011 Rex Dieter <rdieter@fedoraproject.org> - 1:4.7.90-1
- 4.7.90

* Fri Nov 25 2011 Rex Dieter <rdieter@fedoraproject.org> 1:4.7.80-1
- 4.7.80

* Sat Oct 29 2011 Rex Dieter <rdieter@fedoraproject.org> 1:4.7.3-1
- 4.7.3
- pkgconfig-style deps

* Tue Oct 04 2011 Rex Dieter <rdieter@fedoraproject.org> 1:4.7.2-1
- 4.7.2

* Sat Sep 17 2011 Rex Dieter <rdieter@fedoraproject.org> 1:4.7.1-2
- Provides: kdeedu-marble%%{?_isa}

* Fri Sep 16 2011 Rex Dieter <rdieter@fedoraproject.org> 1:4.7.1-1
- 4.7.1

* Wed Sep 14 2011 Rex Dieter <rdieter@fedoraproject.org> 1:4.7.0-11
- update URL

* Tue Aug 30 2011 Rex Dieter <rdieter@fedoraproject.org> 1:4.7.0-10
- first try

