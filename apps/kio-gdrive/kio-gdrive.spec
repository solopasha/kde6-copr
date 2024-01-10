Name:           kio-gdrive
Version:        24.01.90
Release:        1%{?dist}
Summary:        An Google Drive KIO slave for KDE

License:        GPL-2.0-or-later
URL:            https://community.kde.org/KIO_GDrive
%apps_source

BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  intltool
BuildRequires:  kf6-rpm-macros
BuildRequires:  kf5-rpm-macros
BuildRequires:  libappstream-glib

BuildRequires:  cmake(KAccounts6)

BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Purpose)

BuildRequires:  cmake(KPim6GAPI)

BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake(KAccounts)

BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Purpose)

BuildRequires:  cmake(KPim5GAPI)

BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Widgets)

Recommends:     (kio-gdrive-qt5 if kf5-kio-core)

%description
Provides KIO Access to Google Drive using the gdrive:/// protocol.

%package        qt5
Summary:        Qt5 support for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    qt5
%{summary}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
sed -i 's/Ubuntu\.OnlineAccounts/SSO.OnlineAccounts/' purpose/purpose_gdrive_config.qml


%build
%global _vpath_builddir %{_target_platform}-qt5
%cmake_kf5 -DQT_MAJOR_VERSION=5
%cmake_build

%global _vpath_builddir %{_target_platform}-qt6
%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build


%install
%global _vpath_builddir %{_target_platform}-qt5
%cmake_install

%global _vpath_builddir %{_target_platform}-qt6
%cmake_install

%find_lang kio5_gdrive --all-name --with-html


%check
desktop-file-validate %{buildroot}%{_datadir}/remoteview/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.xml ||:


%files -f kio5_gdrive.lang
%license COPYING
%doc HACKING README.md
%{_kf6_datadir}/accounts/services/kde/google-drive.service
%{_kf6_datadir}/knotifications6/gdrive.notifyrc
%{_kf6_datadir}/metainfo/org.kde.kio_gdrive.metainfo.xml
%{_kf6_datadir}/purpose/purpose_gdrive_config.qml
%{_kf6_datadir}/remoteview/gdrive-network.desktop
%dir %{_kf6_plugindir}/kfileitemaction/
%{_kf6_plugindir}/kfileitemaction/gdrivecontextmenuaction.so
%{_kf6_plugindir}/kio/gdrive.so
%{_kf6_plugindir}/propertiesdialog/gdrivepropertiesplugin.so
%{_kf6_plugindir}/purpose/purpose_gdrive.so
%{_qt6_plugindir}/kaccounts/daemonplugins/gdrive.so

%files qt5
%dir %{_kf5_plugindir}/kfileitemaction/
%{_kf5_plugindir}/kfileitemaction/gdrivecontextmenuaction.so
%{_kf5_plugindir}/kio/gdrive.so
%{_kf5_plugindir}/propertiesdialog/gdrivepropertiesplugin.so
%{_kf5_plugindir}/purpose/purpose_gdrive.so
%{_kf5_datadir}/knotifications5/gdrive.notifyrc
%{_qt5_plugindir}/kaccounts/daemonplugins/gdrive.so


%changelog
* Thu Oct 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.2-1
- 23.08.2

* Sat Sep 16 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.1-1
- 23.08.1

* Sat Aug 26 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.0-1
- 23.08.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.3-1
- 23.04.3

* Tue Jun 06 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.2-1
- 23.04.2

* Sat May 13 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.1-1
- 23.04.1

* Wed Apr 26 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.0-3
- Rebuild

* Mon Apr 24 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 23.04.0-2
- Fix license

* Fri Apr 14 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.0-1
- 23.04.0

* Fri Mar 31 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.90-1
- 23.03.90

* Mon Mar 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.80-1
- 23.03.80

* Thu Mar 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 22.12.3-1
- 22.12.3

* Tue Jan 31 2023 Marc Deop <marcdeop@fedoraproject.org> - 22.12.2-1
- 22.12.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Justin Zobel <justin@1707.io> - 22.12.1-1
- Update to 22.12.1

* Mon Dec 19 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.12.0-1
- 22.12.0

* Fri Nov 04 2022 Marc Deop i Argemí (Private) <marc@marcdeop.com> - 22.08.3-1
- 22.08.3

* Fri Oct 14 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.2-1
- 22.08.2

* Thu Sep 08 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.1-1
- 22.08.1

* Sun Aug 21 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 22.08.0-1
- Update to 22.08.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Than Ngo <than@redhat.com> - 22.04.3-1
- 22.04.3

* Tue May 24 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 22.04.1-1
- Update to 22.04.1

* Tue Apr 26 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 22.04.0-1
- Update to 22.04.0

* Thu Mar 03 2022 Marc Deop <marcdeop@fedoraproject.org> - 21.12.3-1
- 21.12.3

* Fri Feb 04 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 21.12.2-1
- Update to 21.12.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 11 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 21.12.1-1
- Update to 21.12.1

* Mon Dec 13 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 21.12.0-1
- Update to 21.12.0

* Fri Sep 24 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 21.08.1-1
- Update to 21.08.1

* Mon Aug 23 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 21.08.0-1
- Update to 21.08.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 15 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 21.04.3-1
- Update to 21.04.3

* Fri Jun 11 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 21.04.2-1
- Update to 21.04.2

* Wed May 19 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 21.04.1-1
- Update to 21.04.1

* Thu Apr 22 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 21.04.0-1
- Update to 21.04.0

* Mon Mar 15 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 20.12.3-1
- Update to 20.12.3

* Mon Feb 22 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 20.12.2-1
- Update to 20.12.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 20.12.1-2
- Add kaccounts-providers to requires

* Sun Jan 10 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 20.12.1-1
- Update to 20.12.1

* Fri Dec 11 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.12.0-1
- Update to 20.12.0

* Sat Nov 07 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.08.3-1
- Update to 20.08.3

* Wed Oct 21 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.08.2-1
- Update to 20.08.2

* Wed Sep 23 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.08.1-1
- Update to 20.08.1

* Thu Aug 20 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.08.0-1
- Update to 20.08.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 12 2020 Rex Dieter <rdieter@fedoraproject.org> - 1.3.0-2
- rebuild (kaccounts)

* Mon May 25 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 1.3.0-1
- Update to 1.3.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 08 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 1.2.7-2
- Enable LTO

* Fri Sep 06 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 1.2.7-1
- Update to 1.2.7

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 24 2019 Vasiliy N. Glazov <vascom2@gmail.com> 1.2.6-2
- Rebuild

* Mon May 20 2019 Vasiliy N. Glazov <vascom2@gmail.com> 1.2.6-1
- Update to 1.2.6

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 24 2018 Vasiliy N. Glazov <vascom2@gmail.com> 1.2.5-1
- Update to 1.2.5

* Mon Jul 16 2018 Vasiliy N. Glazov <vascom2@gmail.com> 1.2.4-1
- Update to 1.2.4
- Clean spec and BRs

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 1 2017 Wolnei Tomazelli Junior <wolnei@fedoraproject.org> -  1.2.1-2
- Fix bogus date

* Sun Oct 1 2017 Wolnei Tomazelli Junior <wolnei@fedoraproject.org> -  1.2.1-1
- Build fixes
- Updated translations

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 22 2017 Wolnei Tomazelli Junior <wolnei@fedoraproject.org> -  1.2.0-1
- Integration with KAccounts
- Google Drive free space is now reported

* Wed May 17 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.1.2-2
- rebuild (libkgapi), use %%find_lang for HTML docs too
- ExclusiveArch: %%{?qt6_qtwebengine_arches}

* Mon May 15 2017 Wolnei Tomazelli Junior <wolnei@fedoraproject.org> -  1.1.2-1
- Updated translations - v1.1.2
* Fri Feb 17 2017 Wolnei Tomazelli Junior <wolnei@fedoraproject.org> -  1.1.1-1
- Fixed wrong write permissions in the top-level accounts folder - v1.1.1
* Sun Jan 29 2017 Wolnei Tomazelli Junior <wolnei@fedoraproject.org> -  1.1.0-1
- update version 1.1
* Sat Jan 28 2017 Wolnei Tomazelli Junior <wolnei@fedoraproject.org> -  1.0.5-2
- Initial version of the package
