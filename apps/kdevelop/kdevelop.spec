%global commit0 4262d7e6363738cd0403260b068ed717c32ba61f
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

%global __requires_exclude ^/usr/bin/zsh$

Name:           kdevelop
Summary:        Integrated Development Environment for C++/C
Epoch:          9
Version:        24.12.0
Release:        2%{?dist}
License:        GPL-2.0-only
URL:            http://www.kdevelop.org/
%apps_source

Source10:       macros.kdevelop

BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  extra-cmake-modules
BuildRequires:  boost-devel
BuildRequires:  meson
BuildRequires:  desktop-file-utils
BuildRequires:  shared-mime-info
BuildRequires:  llvm-devel
BuildRequires:  clang-devel
BuildRequires:  okteta-devel
BuildRequires:  pcre-devel
BuildRequires:  subversion-devel
BuildRequires:  astyle-devel

BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6NotifyConfig)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Purpose)
BuildRequires:  cmake(KF6Runner)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6Sonnet)
BuildRequires:  cmake(KF6TextEditor)
BuildRequires:  cmake(KF6TextTemplate)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6ThreadWeaver)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)

BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Help)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake(KSysGuard)
BuildRequires:  cmake(Plasma)

BuildRequires:  cmake(KompareDiff2)

BuildRequires:  cmake(KDevelop-PG-Qt)

# some arches don't have valgrind so we need to disable its support on them
%ifarch %{ix86} x86_64 ppc ppc64 s390x
BuildRequires: valgrind-devel
%endif

# kdevelop-custom-buildsystem has been merged to kdevelop 4.5.0
Provides:  kdevelop-custom-buildsystem = 9:%{version}-%{release}
Obsoletes: kdevelop-custom-buildsystem < 1.2.1-5

Provides:  kdevplatform = %{version}-%{release}
Obsoletes: kdevplatform < 5.1.80-1

Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Recommends: astyle
Requires: cmake
Recommends: clang-tools-extra
Suggests: clazy
Recommends: cppcheck
Requires: git
Recommends: meson
Requires: konsole-part
Recommends: heaptrack

%description
The KDevelop Integrated Development Environment provides many features
that developers need as well as providing a unified interface to programs
like gdb, the C/C++ compiler, and make. KDevelop manages or provides:

All development tools needed for C++ programming like Compiler,
Linker, automake and autoconf; KAppWizard, which generates complete,
ready-to-go sample applications; Classgenerator, for creating new
classes and integrating them into the current project; File management
for sources, headers, documentation etc. to be included in the
project; The creation of User-Handbooks written with SGML and the
automatic generation of HTML-output with the KDE look and feel;
Automatic HTML-based API-documentation for your project's classes with
cross-references to the used libraries; Internationalization support
for your application, allowing translators to easily add their target
language to a project;

KDevelop also includes WYSIWYG (What you see is what you get)-creation
of user interfaces with a built-in dialog editor; Debugging your
application by integrating KDbg; Editing of project-specific pixmaps
with KIconEdit; The inclusion of any other program you need for
development by adding it to the "Tools"-menu according to your
individual needs.


%package devel
Summary: Development files for %{name}
Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Provides: kdevplatform-devel = %{version}-%{release}
Obsoletes: kdevplatform-devel < 5.1.80-1
%description devel
%{summary}.

%package libs
Summary: %{name} runtime libraries
Requires: %{name} = %{epoch}:%{version}-%{release}
Provides: kdevplatform-libs = %{version}-%{release}
Obsoletes: kdevplatform-libs < 5.1.80-1
%description libs
%{summary}.


%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1

%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name

# rpm macros
install -p -m644 -D %{SOURCE10} \
  %{buildroot}%{rpmmacrodir}/macros.kdevelop
sed -i \
  -e "s|@@NAME@@|%{name}|g" \
  -e "s|@@EPOCH@@|%{?epoch}%{!?epoch:0}|g" \
  -e "s|@@VERSION@@|%{version}|g" \
  -e "s|@@EVR@@|%{?epoch:%{epoch}:}%{version}-%{release}|g" \
  %{buildroot}%{rpmmacrodir}/macros.kdevelop


%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/*.desktop


%files -f %{name}.lang
%doc AUTHORS
%license COPYING.DOC
%{_docdir}/HTML/*/kdevelop/
%{_kf6_bindir}/kdev_dbus_socket_transformer
%{_kf6_bindir}/kdev_format_source
%{_kf6_bindir}/kdev_includepathsconverter
%{_kf6_bindir}/kdevelop
%{_kf6_bindir}/kdevelop!
%{_kf6_bindir}/kdevplatform_shell_environment.sh
%{_kf6_datadir}/applications/org.kde.kdevelo*.desktop
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_kf6_datadir}/kdev*/
%{_kf6_datadir}/kdevplatform/shellutils/.zshrc
%{_kf6_datadir}/knotifications6/kdevelop.notifyrc
%{_kf6_datadir}/knsrcfiles/kdev*.knsrc
%{_kf6_datadir}/metainfo/org.kde.kdevelop.appdata.xml
%{_kf6_datadir}/metainfo/org.kde.kdevelopsessions.appdata.xml
%{_kf6_datadir}/mime/packages/kdevclang.xml
%{_kf6_datadir}/mime/packages/kdevelop.xml
%{_kf6_datadir}/mime/packages/kdevgit.xml
%{_kf6_datadir}/plasma/plasmoids/org.kde.kdevelopsessions/
%{_kf6_datadir}/qlogging-categories6/kdevelop.categories
%{_kf6_datadir}/qlogging-categories6/kdevplatform.categories
%{_qt6_qmldir}/org/kde/plasma/private/kdevelopsessions/


%files libs
%{_kf6_libdir}/libKDev*.so.*
%{_kf6_libdir}/libKDevelopSessionsWatch.so
%{_kf6_plugindir}/krunner/kdevelopsessions.so
%{_kf6_plugindir}/ktexttemplate/kdev_filters.so
%{_kf6_qtplugindir}/kdevplatform/


%files devel
%{_includedir}/kdevelop/
%{_includedir}/kdevplatform/
%{_kf6_libdir}/cmake/KDevelop/
%{_kf6_libdir}/cmake/KDevPlatform/
%exclude %{_libdir}/libKDevelopSessionsWatch.so
%{_kf6_libdir}/libKDev*.so
%{rpmmacrodir}/macros.kdevelop

%changelog
* Thu Jan 02 2025 Pavel Solovev <daron439@gmail.com> - 9:24.12.0-2
- rebuilt

* Fri Dec 06 2024 Pavel Solovev <daron439@gmail.com> - 9:24.12.0-1
- Update to 24.12.0

* Tue Nov 05 2024 Pavel Solovev <daron439@gmail.com> - 9:24.08.3-1
- Update to 24.08.3

* Mon Oct 07 2024 Pavel Solovev <daron439@gmail.com> - 9:24.08.2-1
- Update to 24.08.2

* Sat Sep 14 2024 Pavel Solovev <daron439@gmail.com> - 9:24.08.1-3
- filter out zsh

* Sat Sep 14 2024 Pavel Solovev <daron439@gmail.com> - 9:24.08.1-2
- fix file list

* Tue Sep 10 2024 Pavel Solovev <daron439@gmail.com> - 9:24.08.1-1
- Update to 24.08.1

* Fri Aug 16 2024 Pavel Solovev <daron439@gmail.com> - 9:24.08.0-1
- Update to 24.08.0

* Fri Aug 09 2024 Pavel Solovev <daron439@gmail.com> - 9:24.07.90-1
- Update to 24.07.90

* Thu Jul 25 2024 Pavel Solovev <daron439@gmail.com> - 9:24.07.80-1
- Update to 24.07.80

* Thu Jul 04 2024 Pavel Solovev <daron439@gmail.com> - 9:24.05.2-1
- Update to 24.05.2

* Thu Jun 13 2024 Pavel Solovev <daron439@gmail.com> - 9:24.05.1-1
- Update to 24.05.1

* Thu May 23 2024 Pavel Solovev <daron439@gmail.com> - 9:24.05.0-1
- Update to 24.05.0

* Fri Apr 26 2024 Pavel Solovev <daron439@gmail.com> - 9:24.04.80-1
- Update to 24.04.80

* Thu Apr 11 2024 Pavel Solovev <daron439@gmail.com> - 9:24.02.2-1
- Update to 24.02.2

* Thu Mar 21 2024 Pavel Solovev <daron439@gmail.com> - 9:24.02.1-1
- Update to 24.02.1

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 9:24.02.0-1
- 24.02.0

* Wed Jan 31 2024 Than Ngo <than@redhat.com> - 24.01.95-1
- 24.01.95

* Tue Jan 23 2024 Nicolas Fella <nicolas.fella@gmx.de> - 9:24.01.90-3
- Add missing konsolepart dependency

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9:24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 9:24.01.90-1
- 24.01.90

* Thu Dec 28 2023 Marie Loise Nolden <loise@kde.org> - 24.01.85-1
- update to 24.01.85 (still using qt5/kf5)
- fix qtwebkit -> qtwebengine
- add kf5-purpose
- add meson for meson plugin

* Tue Dec 19 2023 Than Ngo <than@redhat.com> - 23.08.4-1
- update to 23.08.4

* Wed Dec 06 2023 Than Ngo <than@redhat.com> - 23.08.2-2
- Fix bz#2252983, rebuilt against new libksysguard

* Thu Oct 12 2023 Than Ngo <than@redhat.com> - 23.08.2-1
- update to 23.08.2

* Sat Sep 16 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 9:23.08.1-1
- 23.08.1

* Sat Sep 16 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 9:23.08.0-3
- Add upstream patch to fix build against llvm 17

* Tue Sep 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 9:23.08.0-2
- Add astyle-devel dependency

* Sat Aug 26 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 9:23.08.0-1
- 23.08.0

* Fri Aug 11 2023 Than Ngo <than@redhat.com> - 23.07.90-1
- Fix bz#2220926, update to 23.07.90

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9:23.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 9:23.04.3-1
- 23.04.3

* Tue Jun 06 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 9:23.04.2-1
- 23.04.2

* Thu May 11 2023 Than Ngo <than@redhat.com> - 23.04.1-1
- update to 23.04.1

* Fri Apr 14 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 9:23.04.0-1
- 23.04.0

* Fri Mar 31 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 9:23.03.90-1
- 23.03.90


* Wed Mar 22 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 9:23.03.80-1
- 23.03.80

* Wed Mar 22 2023 Jan Grulich <jgrulich@redhat.com> - 9:22.12.3-2
- Rebuild (grantlee-qt5)

* Thu Mar 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 9:22.12.3-1
- 22.12.3

* Wed Feb 15 2023 Than Ngo <than@redhat.com> - 9:22.12.2-2
- migrated to SPDX license

* Tue Jan 31 2023 Marc Deop <marcdeop@fedoraproject.org> - 9:22.12.2-1
- 22.12.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9:22.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jan 07 2023 Marc Deop <marcdeop@fedoraproject.org> - 9:22.12.1-1
- 22.12.1

* Fri Dec 09 2022 Than Ngo <than@redhat.com> - 22.12.0-1
- 22.12.0

* Thu Nov 03 2022 Than Ngo <than@redhat.com> - 22.08.3-1
- 22.08.3

* Fri Oct 14 2022 Than Ngo <than@redhat.com> - 22.08.2-1
- 22.08.2

* Mon Sep 19 2022 Pete Walter <pwalter@fedoraproject.org> - 9:22.08.1-2
- Rebuild for clang 15

* Thu Sep 08 2022 Marc Deop <marcdeop@fedoraproject.org> - 9:22.08.1-1
- 22.08.1

* Fri Aug 19 2022 Marc Deop <marcdeop@fedoraproject.org> - 9:22.08.0-1
- 22.08.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9:22.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 07 2022 Than Ngo <than@redhat.com> - 22.04.3-1
- 22.04.3

* Thu Jun 09 2022 Than Ngo <than@redhat.com> - 22.04.2-1
- 22.04.2

* Thu May 12 2022 Than Ngo <than@redhat.com> - 22.04.1-1
- 22.04.1

* Thu Apr 21 2022 Than Ngo <than@redhat.com> - 22.04.0-1
- 22.04.0

* Wed Mar 02 2022 Marc Deop <marcdeop@fedoraproject.org> - 9:21.12.3-1
- 21.12.3

* Thu Feb 03 2022 Than Ngo <than@redhat.com> - 21.12.2-1
- update to 21.12.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9:21.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 19 2022 Than Ngo <than@redhat.com> - 21.12.1-1
- update to 21.12.1

* Tue Dec 14 2021 Than Ngo <than@redhat.com> - 21.12.0-2
- enable 390x build

* Fri Dec 10 2021 Than Ngo <than@redhat.com> - 21.12.0-1
- v21.12.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9:5.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Feb 02 2021 Jan Grulich <jgrulich@redhat.com> - 9:5.6.2-1
- 5.6.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9:5.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Tom Stellard <tstellar@redhat.com> - 9:5.6.1-2
- Rebuild for clang-11.1.0

* Wed Dec  9 10:37:30 CET 2020 Jan Grulich <jgrulich@redhat.com> - 9:5.6.1-1
- 5.6.1

* Tue Sep 08 2020 Jan Grulich <jgrulich@redhat.com> - 9:5.6.0-1
- 5.6.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9:5.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jan Grulich <jgrulich@redhat.com> - 9:5.5.2-2
- Rebuild (Plasma 5.19)

* Tue Jun 02 2020 Jan Grulich <jgrulich@redhat.com> - 9:5.5.2-1
- 5.5.2

* Wed May 27 2020 Jan Grulich <jgrulich@redhat.com> - 9:5.5.1-2
- Rebuild (libksysguard)

* Tue May 05 2020 Jan Grulich <jgrulich@redhat.com> - 9:5.5.1-1
- 5.5.1

* Wed Feb 19 2020 Jan Grulich <jgrulich@redhat.com> - 9:5.5.0-3
- Rebuild for grantlee

* Mon Feb 17 2020 Jan Grulich <jgrulich@redhat.com> - 9:5.5.0-2
- Do not crash when showing tooltip

* Mon Feb 03 2020 Jan Grulich <jgrulich@redhat.com> - 9:5.5.0-1
- 5.5.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9:5.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Jan Grulich <jgrulich@redhat.com> - 9:5.4.6-1
- 5.4.6

* Tue Dec 03 2019 Jan Grulich <jgrulich@redhat.com> - 9:5.4.5-1
- 5.4.5

* Tue Nov 05 2019 Jan Grulich <jgrulich@redhat.com> - 9:5.4.4-1
- 5.4.4

* Tue Oct 22 2019 Jan Grulich <jgrulich@redhat.com> - 9:5.4.3-1
- 5.4.3

* Tue Sep 03 2019 Jan Grulich <jgrulich@redhat.com> - 5.4.2-1
- 5.4.2

* Tue Aug 13 2019 Jan Grulich <jgrulich@redhat.com> - 5.4.1-1
- 5.4.1

* Tue Aug 06 2019 Jan Grulich <jgrulich@redhat.com> - 5.4.0-1
- 5.4.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9:5.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Jan Grulich <jgrulich@redhat.com> - 5.3.3-1
- 5.3.3

* Fri Mar 15 2019 Jan Grulich <jgrulich@redhat.com> - 5.3.2-1
- 5.3.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9:5.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Jan Grulich <jgrulich@redhat.com> - 5.3.1-2
- Rebuild (clang)

* Tue Dec 11 2018 Jan Grulich <jgrulich@redhat.com> - 5.3.1-1
- 5.3.1

* Wed Nov 14 2018 Jan Grulich <jgrulich@redhat.com> - 5.3.0-1
- 5.3.0

* Tue Oct 02 2018 Jan Grulich <jgrulich@redhat.com> - 5.2.80-1
- 5.2.80 (beta)

* Mon Aug 27 2018 Jan Grulich <jgrulich@redhat.com> - 5.2.4-1
- 5.2.4

* Thu Aug 16 2018 Than Ngo <than@redhat.com> - 5.2.3-4
- fixed #1405880, prefer qmake-qt5
- fixed #1518465, prefer bash and drop zsh dependency

* Mon Jul 23 2018 Than Ngo <than@redhat.com> - 5.2.3-3
- fixed FTBFS

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9:5.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 21 2018 Jan Grulich <jgrulich@redhat.com> - 9:5.2.3-1
- Update to 5.2.3

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9:5.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 24 2017 Jan Grulich <jgrulich@redhat.com> - 5.2.1-1
- Update to 5.2.1

* Tue Nov 14 2017 Jan Grulich <jgrulich@redhat.com> - 5.2.0-1
- Update to 5.2.0

* Tue Oct 24 2017 Jan Grulich <jgrulich@redhat.com> - 5.1.80-2
- rebuild (llvm-5.0)

* Fri Oct 06 2017 Jan Grulich <jgrulich@redhat.com> - 5.1.80-1
- Update to 5.1.80 (beta)
- KDevplatform merged to KDevelop

* Tue Aug 29 2017 Jan Grulich <jgrulich@redhat.com> - 5.1.2-1
- Update to 5.1.2

* Mon Aug 07 2017 Björn Esser <besser82@fedoraproject.org> - 9:5.1.1-6
- Rebuilt for AutoReq cmake-filesystem

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9:5.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9:5.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 9:5.1.1-3
- Rebuilt for Boost 1.64

* Tue May 30 2017 Björn Esser <besser82@fedoraproject.org> - 9:5.1.1-2
- Rebuilt for clang/llvm-4

* Mon May 29 2017 Jan Grulich <jgrulich@redhat.com> 9:5.1.1-1
- Update to 5.1.1

* Thu May 25 2017 Peter Robinson <pbrobinson@fedoraproject.org> 9:5.1.0-4
- Rebuild clang/llvm-4

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9:5.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Mar 24 2017 Igor Gnatenko <ignatenko@redhat.com> - 9:5.1.0-2
- Rebuild for LLVM4

* Mon Mar 20 2017 Jan Grulich <jgrulich@redhat.com> - 9:5.1.0-1
- Update to 5.1.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9:5.0.80-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 9:5.0.80-2
- Rebuilt for Boost 1.63

* Tue Jan 17 2017 Jan Grulich <jgrulich@redhat.com> - 5.0.80-1
- Update to 5.0.80 (beta)

* Thu Dec 01 2016 Jan Grulich <jgrulich@redhat.com> - 5.0.3-1
- Update to 5.0.3

* Wed Nov 09 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.0.2-2
- rebuild (clang)

* Mon Oct 17 2016 Jan Grulich <jgrulich@redhat.com> - 5.0.2-1
- Update to 5.0.2

* Mon Sep 19 2016 Jan Grulich <jgrulich@redhat.com> - 5.0.1-1
- Update to 5.0.1

* Wed Sep 07 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.0.0-2
- +macros.kdevelop: make addon packages easier to manage

* Wed Aug 24 2016 Helio Chissini de Castro <helio@kde.org> - 5.0.0-1
- New upstream version

* Mon Aug 08 2016 Jan Grulich <jgrulich@redhat.com> - 5.0.0-0.3.20160808git
- Update to latest git snapshot

* Thu Jul 07 2016 Jan Grulich <jgrulich@redhat.com> - 5.0.0-0.2.20160608git
- Add BR: libksysguard-devel
  Resolves: bz#1352964

* Wed Jun 08 2016 Jan Grulich <jgrulich@redhat.com> - 5.0.0-0.1.20160608git
- Package latest git snapshot to address GCC 6 related crashes
  Resolves: bz#1343439

* Fri Apr 08 2016 Rex Dieter <rdieter@fedoraproject.org> - 9:4.90.91-5
- Conflicts: kapptemplate < 16.03.80
- .spec cosmetics, use %%license

* Fri Mar 04 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 9:4.90.91-4
- Rebuld against new clang

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 9:4.90.91-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Adam Jackson <ajax@redhat.com> 4.90.91-2
- Rebuild for llvm 3.7.1 library split

* Tue Jan 26 2016 Jan Grulich <jgrulich@redhat.com> - 9:4.90.91-1
- Update to 4.90.91 (beta 2)

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 9:4.90.90-2
- Rebuilt for Boost 1.60

* Thu Oct 29 2015 Jan Grulich <jgrulich@redhat.com> - 4.90.90-1
- Update to 4.90.90 (beta 1)

* Thu Jul 30 2015 Kevin Kofler <Kevin@tigcc.ticalc.org> - 9:4.7.1-7
- Readd missing BuildRequires: kde-workspace-devel (#1248073)

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9:4.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 9:4.7.1-5
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9:4.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 9:4.7.1-3
- Rebuilt for GCC 5 C++11 ABI change

* Tue Mar 31 2015 Rex Dieter <rdieter@fedoraproject.org> 9:4.7.1-2
- BR: okteta4-devel, -libs: drop Requires: okteta

* Tue Feb 03 2015 Jan Grulich <jgrulich@redhat.com> - 9:4.7.1-1
- Update to 4.7.1

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 9:4.7.0-2
- Rebuild for boost 1.57.0

* Wed Aug 27 2014 Jan Grulich <jgrulich@redhat.com> - 9:4.7.0-1
- Update to 4.7.0

* Fri Jul 11 2014 Jan Grulich <jgrulich@redhat.com> 9:4.6.90-1
- Update to 4.6.90 (beta1)

* Thu Jul 03 2014 Rex Dieter <rdieter@fedoraproject.org> 9:4.6.0-5
- optimize mimeinfo scriptlet, .spec cleanup
- BR: qtwebkit ...

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9:4.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 9:4.6.0-3
- Rebuild for boost 1.55.0

* Thu Dec 12 2013 Jan Grulich <jgrulich@redhat.com> - 9:4.6.0-2
- Fix ninja builder (bz#1040801)

* Sun Dec 08 2013 Jan Grulich <jgrulich@redhat.com> - 9:4.6.0-1
- Update to 4.6.0

* Wed Nov 27 2013 Jan Grulich <jgrulich@redhat.com> - 9:4.5.90-1
- Update to 4.5.90

* Mon Nov 18 2013 Jan Grulich <jgrulich@redhat.com> - 9:4.5.80-1
- Update to 4.5.80

* Thu Oct 31 2013 Jan Grulich <jgrulich@redhat.com> - 9:4.5.2-1
- Update to 4.5.2

* Wed Aug 07 2013 Jan Grulich <jgrulich@redhat.com> - 9:4.5.1-4
- Not necessary to require the latest version of okteta

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9:4.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 9:4.5.1-2
- Rebuild for boost 1.54.0

* Thu May 30 2013 Jan Grulich <jgrulich@redhat.com> - 9:4.5.1-1
- Update to 4.5.1

* Mon Apr 29 2013 Radek Novacek <rnovacek@redhat.com> - 9:4.5.0-2
- Obsoletes and provides kdevelop-custom-buildsystem

* Fri Apr 26 2013 Jan Grulich <jgrulich@redhat.com> - 9:4.5.0-1
- Update to 4.5.0

* Fri Apr 26 2013 Jan Grulich <jgrulich@redhat.com> - 9:4.4.90-2
- Add previusly removed rpath patch

* Thu Apr 25 2013 Jan Grulich <jgrulich@redhat.com> - 9:4.4.90-1
- Update to 4.4.90 (RC1)

* Mon Apr 01 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 9:4.4.1-4
- Requires: cmake (as per discussion of kde#274246)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9:4.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 22 2012 Jan Grulich <jgrulich@redhat.com> 9:4.4.1-2
- Don't execute cmake every time when you use ninja

* Mon Nov 05 2012 Jan Grulich <jgrulich@redhat.com> 9:4.4.1-1
- Update to 4.4.1
- Remove unnecessary fix for splash

* Wed Oct 24 2012 Jan Grulich <jgrulich@redhat.com> 9:4.4.0-2
- Fixed version in splash

* Tue Oct 23 2012 Jan Grulich <jgrulich@redhat.com> 9:4.4.0-1
- Update to 4.4.0
- Rebase no-rpath patch

* Fri Sep 07 2012 Radek Novacek <rnovacek@redhat.com> 9:4.3.90-1
- Update to 4.3.90 (RC 1)

* Thu Aug 09 2012 Radek Novacek <rnovacek@redhat.com> 9:4.3.80-1
- Update to 4.3.80 (beta 1)
- Rebase no-rpath patch
- Drop okteta09 patch (upstreamed)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9:4.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> 9:4.3.1-3
- reenable Okteta plugin, fix its build with Okteta 0.9 (upstream patch)

* Wed Jun 13 2012 Radek Novacek <rnovacek@redhat.com> 9:4.3.1-2
- Rebuild (kasten)

* Mon Apr 16 2012 Radek Novacek <rnovacek@redhat.com> 9:4.3.1-1
- Update to 4.3.1

* Wed Apr 04 2012 Than Ngo <than@redhat.com> - 9:4.3.0-2
- fix build failure on plattform wirh bigendian

* Mon Mar 12 2012 Jaroslav Reznik <jreznik@redhat.com> 9:4.3.0-1
- Update to 4.3.0

* Sun Feb 26 2012 Radek Novacek <rnovacek@redhat.com> 9:4.2.90-2
- Fix kdevplatform version

* Sun Feb 26 2012 Radek Novacek <rnovacek@redhat.com> 9:4.2.90-1
- Update to 4.2.90 (RC 1)

* Tue Feb 14 2012 Jaroslav Reznik <jreznik@redhat.com> 9:4.2.82-1
- Update to 4.2.82 (beta 2)
- Rebase include unistd.h patch

* Mon Jan 23 2012 Radek Novacek <rnovacek@redhat.com> 9:4.2.81-1
- Update to 4.2.81 (1.3 beta)
- Drop upstreamed patch
- Rebase rpath patch
- Fix with g++ 4.7 (missing include unistd.h)
- Fix unpackaged files

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9:4.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 24 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> 9:4.2.3-7
- remove set(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE) line

* Sat Dec 24 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> 9:4.2.3-6
- upstream patch to make Okteta plugin compile against libs from Okteta 0.8

* Mon Dec 05 2011 Rex Dieter <rdieter@fedoraproject.org> 9:4.2.3-5
- add explicit BR: boost-devel

* Sun Jul 31 2011 Rex Dieter <rdieter@fedoraproject.org> 9:4.2.3-4
- drop < f14 conditionals
- BR: okteta-devel

* Fri Jul 22 2011 Rex Dieter <rdieter@fedoraproject.org> 9:4.2.3-3
- fix dep(s) on kdesdk/okteta

* Tue Jun 28 2011 Radek Novacek <rnovacek@redhat.com> - 9:4.2.3-2
- Rebuild with kdevplatform-1.2.3

* Mon Jun 27 2011 Than Ngo <than@redhat.com> - 9:4.2.3-1
- 4.2.3

* Tue Apr 26 2011 Dan Horák <dan[at]danny.cz> - 9:4.2.2-2
- valgrind exists only on selected architectures

* Thu Apr 07 2011 Radek Novacek <rnovacek@redhat.com> 9:4.2.2-1
- Update to 4.2.2

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9:4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 25 2011 Rex Dieter <rdieter@fedoraproject.org> 4.2.0-1
- 4.2.0

* Fri Jan 21 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 9:4.1.90-1
- Update to 4.1.90 (4.2 RC1, uses kdevplatform 1.1.90)

* Tue Dec 28 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 9:4.1.81-1
- Update to 4.1.81 (4.2 Beta 2, uses kdevplatform 1.1.81)

* Thu Dec 16 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 9:4.1.80-1
- Update to 4.1.80 (4.2 Beta 1, required for kdelibs 4.6, #660345, #661077)

* Mon Dec 06 2010 Rex Dieter <rdieter@fedoraproject.org> - 9:4.1.1-1
- kdevelop-4.1.1

* Mon Dec 06 2010 Rex Dieter <rdieter@fedoraproject.org> - 9:4.1.0-4
- -libs: (versioned) Requires: kdeutils-libs (#656847)
- -libs: move kdevplatform dep here, make arch'd

* Tue Nov 23 2010 Rex Dieter <rdieter@fedoraproject.org> - 9:4.1.0-3
- rebuild
- BR: kdesdk-devel (f15+, kde46)

* Thu Nov 18 2010 Thomas Janssen <thomasj@fedoraproject.org> - 9:4.1.0-2
- added Requires git

* Fri Oct 22 2010 Thomas Janssen <thomasj@fedoraproject.org> - 9:4.1.0-1
- update to 4.1.0
- added BR kdeutils-devel

* Wed Sep 29 2010 jkeating - 9:4.0.82-2
- Rebuilt for gcc bug 634757

* Sun Sep 26 2010 Thomas Janssen <thomasj@fedoraproject.org> - 9:4.0.82-1
- update to 4.0.82

* Wed Aug 11 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 9:4.0.1-1
- update to 4.0.1 (uses kdevplatform 1.0.1)
- remove Source1, upstream doesn't ship a .md5sum anymore
- drop qmake_qt4 patch, fixed upstream

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 9:4.0.0-3
- recompiling .py files against Python 2.7 (rhbz#623326)

* Wed May 05 2010 Rex Dieter <rdieter@fedoraproject.org> 9:4.0.0-2
- Qt documentation not available on Fedora  (kde#236315)

* Thu Apr 29 2010 Rex Dieter <rdieter@fedoraproject.org> 9:4.0.0-1
- kdevelop-4.0.0

* Sat Apr 17 2010 Rex Dieter <rdieter@fedoraproject.org> 9:3.10.2-1
- kdevelop-3.10.2

* Thu Apr 08 2010 Rex Dieter <rdieter@fedoraproject.org> 9:3.10.0-1
- kdevelop-3.10.0

* Mon Mar 08 2010 Rex Dieter <rdieter@fedoraproject.org> 9:3.9.99-1
- kdevelop-3.9.99

* Mon Feb 22 2010 Rex Dieter <rdieter@fedoraproject.org> 9:3.9.98-1
- kdevelop-3.9.98

* Thu Jan 28 2010 Rex Dieter <rdieter@fedoraproject.org> 9:3.9.97-3
- -libs: fix Requires: kdelibs4 ...

* Sat Jan 16 2010 Rex Dieter <rdieter@fedoraproject.org> 9:3.9.97-2
- rebuild (boost)

* Thu Jan 07 2010 Rex Dieter <rdieter@fedoraproject.org> 9:3.9.97-1
- kdevelop-3.9.97

* Sun Nov 22 2009 Rex Dieter <rdieter@fedoraproject.org> 9:3.9.95-0.3.beta5
- rebuild (fc13+, qt-4.6.0-rc1)

* Tue Sep 29 2009 Ben Boeckel <MathStuf@gmail.com> - 9:3.9.95-0.1.beta5
- Upgrade to 3.9.95

* Sat Sep 12 2009 Rex Dieter <rdieter@fedoraproject.org> 9:3.5.4-6
- make -libs unconditional
- Requires: kdebase3 (#507653)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9:3.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 18 2009 Rex Dieter <rdieter@fedoraproject.org> - 9:3.5.4-4
- FTBFS kdevelop-3.5.4-3.fc11 (#511768)

* Mon Mar 02 2009 Than Ngo <than@redhat.com> - 3.5.4-3
- fix build problem with gcc-4.4

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9:3.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 18 2008 Than Ngo <than@redhat.com> - 3.5.4-1
- 3.5.4

* Sat Aug 30 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 9:3.5.3-1
- update to 3.5.3
- drop svn patch (fixed upstream)

* Mon Jul 07 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 9:3.5.2-3
- fix FTBFS (add BR openldap-devel to work around missing dep in apr-devel)

* Fri Jun 06 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 9:3.5.2-2
- improve integration of the KDE 4 app template

* Mon May 19 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 9:3.5.2-1
- update to 3.5.2
- F9+: BR qt3-devel-docs instead of qt-devel-docs
- F9+: Require qt3-designer instead of qt-designer
- drop backported fix_missing_output_kdev3.5.1 patch

* Tue Mar 04 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 9:3.5.1-4
- BR kdelibs3-apidocs instead of kdelibs-apidocs
- hardcode qt_ver again because 3.3.8b reports itself as 3.3.8

* Thu Feb 28 2008 Than Ngo <than@redhat.com> 9:3.5.1-3
- apply upstream patch to fix outputview

* Fri Feb 15 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 9:3.5.1-1
- update to 3.5.1 (KDE 3.5.9)
- drop backported autosave patch (fixed upstream)

* Sat Feb 09 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 9:3.5.0-7
- disable parallel make because of a race condition

* Sat Feb 09 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 9:3.5.0-6
- rebuild for GCC 4.3

* Thu Dec 06 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 9:3.5.0-5
- drop CVS integration in F9+ for now because it requires kdesdk3

* Wed Oct 31 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 9:3.5.0-4
- %%post/%%postun libs -p /sbin/ldconfig
- -libs conditional (f8+)

* Tue Oct 30 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 9:3.5.0-3
- -devel, -libs subpkgs, multiarch conflicts (#341791)

* Thu Oct 25 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 9:3.5.0-2
- autosave patch

* Sat Oct 13 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 9:3.5.0-1
- kdevelop-3.5.0 (kde-3.5.8)

* Mon Sep 03 2007 Than Ngo <than@redhat.com> - 9:3.4.1-5
- rebuilt against apr

* Wed Aug 29 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 9:3.4.1-4
- License: GPLv2
- (Build)Requires: kdelibs3-devel kdesdk3-devel
- svn patch (#265481)

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 9:3.4.1-3
- Rebuild for selinux ppc32 issue.

* Sun Jun 17 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 9:3.4.1-2
- merge missed changes from F-7 branch
- make qt-devel-doc/qt_ver detection more robust

* Sun Jun 17 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 9:3.4.1-1
- cleanup

* Thu Jun 14 2007 Than Ngo <than@redhat.com> - 9:3.4.1-1.fc7
- 3.4.1

* Thu Feb 08 2007 Than Ngo <than@redhat.com> 9:3.3.6-1.fc7
- 3.3.6

* Thu Aug 10 2006 Than Ngo <than@redhat.com> 9:3.3.4-1
- rebuild

* Mon Jul 24 2006 Than Ngo <than@redhat.com> 9:3.3.4-0.pre1
- prerelease of 3.3.4 (from the first-cut tag)

* Mon Jul 17 2006 Than Ngo <than@redhat.com> 9:3.3.3-3
- rebuild

* Fri Jul 14 2006 Than Ngo <than@redhat.com> 9:3.3.3-2
- cleanup specfile

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 9:3.3.3-1.1
- rebuild

* Mon Jun 05 2006 Than Ngo <than@redhat.com> 9:3.3.3-1
- update to 3.3.3

* Wed Apr 05 2006 Than Ngo <than@redhat.com> 9:3.3.2-1
- update to 3.3.2

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 9:3.3.1-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 9:3.3.1-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Sun Feb 05 2006 Than Ngo <than@redhat.com> 9:3.3.1-1
- 3.3.1

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Sun Dec 04 2005 Than Ngo <than@redhat.com> 3.3.0-1
- 3.3.0

* Tue Oct 25 2005 Than Ngo <than@redhat.com> 9:3.2.92-1
- update to KDE 3.5 beta2

* Thu Oct 06 2005 Than Ngo <than@redhat.com> 9:3.2.91-1
- update to KDE 3.5 beta 1

* Thu Sep 22 2005 Than Ngo <than@redhat.com> 9:3.2.2-2
- fix uic build problem

* Thu Aug 11 2005 Than Ngo <than@redhat.com> 9:3.2.2-1
- update to 3.2.2

* Thu Jul 07 2005 Than Ngo <than@redhat.com> 8:3.2.1-3
- fix uninitialized variable warning #162367

* Thu Jun 30 2005 Than Ngo <than@redhat.com> 9:3.2.1-2
- apply patch to fix undefined symbol issue #162146

* Wed Jun 29 2005 Than Ngo <than@redhat.com> 9:3.2.1-1
- 3.2.1
- fix gcc4 build problem

* Wed Apr 13 2005 Than Ngo <than@redhat.com> 9:3.2.0-2
- fix wrong qtdoc path

* Fri Mar 18 2005 Than Ngo <than@redhat.com> 9:3.2.0-1
- 3.2.0

* Fri Mar 04 2005 Than Ngo <than@redhat.com> 9:3.2.0-0.rc1.2
- rebuilt against gcc-4.0.0-0.31

* Tue Mar 01 2005 Than Ngo <than@redhat.com> 9:3.2.0-0.rc1.1
- KDE 3.4.0 rc1

* Mon Feb 21 2005 Than Ngo <than@redhat.com> 9:3.1.92-0.1
- KDE-3.4 beta2

* Sun Dec 05 2004 Than Ngo <than@redhat.com> 9:3.1.2-0.1
- update to 3.1.2

* Sun Oct 24 2004 Warren Togami <wtogami@redhat.com>
- req libtool used by kdevelop

* Sat Oct 16 2004 Than Ngo <than@redhat.com> 9:3.1.1-2
- rhel rebuilt

* Wed Oct 13 2004 Than Ngo <than@redhat.com> 9:3.1.1-1
- update to 3.1.1

* Thu Sep 02 2004 Than Ngo <than@redhat.com> 3.1.0-2
- remove kdevelop-gdb_shared_library.patch, it's include in new upstream
- cleanup specfile

* Wed Sep 01 2004 Than Ngo <than@redhat.com> 3.1.0-1
- update to 3.1.0

* Tue Aug 10 2004 Than Ngo <than@redhat.com> 3.1.0-0.1.rc2
- update to 3.1.0 rc2

* Sat Jun 19 2004 Than Ngo <than@redhat.com> 3.0.4-1
- update to 3.0.4

* Thu Apr 15 2004 Than Ngo <than@redhat.com> 3.0.3-2
- fixed multiple duplicate names, bug #117940

* Wed Apr 14 2004 Than Ngo <than@redhat.com> 9:3.0.3-1
- update to 3.0.3

* Tue Apr 06 2004 Than Ngo <than@redhat.com> 9:3.0.2-2
- fix a bug in creating of new PHP project that causes kdevelop to crash, bug #117113

* Tue Mar 09 2004 Than Ngo <than@redhat.com> 9:3.0.2-1
- rebuild

* Fri Mar 05 2004 Than Ngo <than@redhat.com> 9:3.0.2-0.1
- 3.0.2 release

* Sun Feb 08 2004 Than Ngo <than@redhat.com> 9:3.0.0-0.2
- rebuilt against qt-3.3.0

* Mon Feb 02 2004 Than Ngo <than@redhat.com> 9:3.0.0-0.1
- 3.0.0 release

* Thu Jan 22 2004 Than Ngo <than@redhat.com> 8:3.0.0r1-0.1
- 3.0.0 RC1

* Wed Dec 10 2003 Than Ngo <than@redhat.com> 8:3.0.0b2-0.3
- included BuildRequires: db4-devel

* Tue Dec 02 2003 Than Ngo <than@redhat.com> 8:3.0.0b2-0.2
- 3.0.0 Beta 2 respin

* Mon Dec 01 2003 Than Ngo <than@redhat.com> 8:3.0.0b2-0.1
- 3.0.0 Beta 2
- remove unneeded files: kdevelop-htdig.conf, admin-1.0.tar.gz

* Thu Nov 27 2003 Than Ngo <than@redhat.com> 8:3.0.0b1-0.2
- get rid of rpath

* Thu Nov 13 2003 Than Ngo <than@redhat.com> 8:3.0.0b1-0.1
- 3.0.0 Beta1
- po files moved in kde-i18n
- cleanup

* Tue Oct 21 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- add a %%clean specfile target

* Mon Oct 13 2003 Than Ngo <than@redhat.com> 8:2.1.5-13
- fix documention localtion

* Wed Aug 20 2003 Than Ngo <than@redhat.com> 8:2.1.5-12
- fix build problem with gcc 3.3

* Wed Jun 25 2003 <than@redhat.com> 2.1.5-11
- rebuilt

* Tue Jun 10 2003 <than@redhat.com> 2.1.5-10
- fix templates bug (bug #88718)

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun  3 2003 Jeff Johnson <jbj@redhat.com>
- add explicit epoch's where needed.

* Tue May 27 2003 <than@redhat.com> 2.1.5-7
- rebuild

* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 21 2003 <than@redhat.com> 2.1.5-2
- get rid of gcc path from dependency_libs

* Fri Jan 24 2003 <than@redhat.com> 2.1.5-1
- 2.1.5 release
- update c_cpp_reference
- cleanup sepcfile
- remove templates, which is now in new upstream
- remove unneeded c_cpp_reference-2.0.1-config.patch
- add missing mo files
- fixed #75084, #73128, #70656, #77767, #74425

* Wed Jan 22 2003 Tim Powers <timp@redhat.com> 2.1.4-6
- rebuilt

* Wed Jan  8 2003 Jeff Johnson <jbj@redhat.com> 2.1.4-5
- don't include -debuginfo files in package.

* Tue Dec 31 2002 Than Ngo <than@redhat.com> 2.1.4-4
- fix templates (bug #80745)

* Tue Dec 17 2002 Than Ngo <than@redhat.com> 2.1.4-3
- enable kdoc

* Mon Dec  9 2002 Than Ngo <than@redhat.com> 2.1.4-2
- fix build problem on s390/s390x
- fix bug #78866

* Sun Nov 10 2002 Than Ngo <than@redhat.com> 2.1.4-1
- update to 2.1.4

* Mon Oct 07 2002 Phil Knirsch <pknirsch@redhat.com> 2.1.3-3.2
- Fixed build for s390x.

* Thu Sep 12 2002 Than Ngo <than@redhat.com> 2.1.3-3.1
- clean up specfile for x86_64/ppc (bug #73862)

* Sun Sep  1 2002 Than Ngo <than@redhat.com> 2.1.3-3
- Add fix to show/hide KaboutKDE and Report Bug menu item over
  KDE Action Restrictions in kdeglobals

* Tue Aug 27 2002 Than Ngo <than@redhat.com> 2.1.3-2
- move kdevelop in X-Red-Hat-Base

* Mon Aug 12 2002 Than Ngo <than@redhat.com> 2.1.3-1
- 2.1.3
- Adapted a patch file to 2.1.3

* Mon Aug  5 2002 Than Ngo <than@redhat.com> 2.1.2-3
- fixed desktop file issue

* Tue Jul 23 2002 Tim Powers <timp@redhat.com>
- build using gcc-3.2-0.1

* Tue Jul 09 2002 Than Ngo <than@redhat.com> 2.1.2-1
- 2.1.2 for kde 3.0.2
- use desktop-file-install

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jun 19 2002 Than Ngo <than@redhat.com> 2.1.1-2
- don't forcibly strip binaries

* Sun Jun  2 2002 Than Ngo <than@redhat.com> 2.1.1-1
- 2.1.1

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Bernhard Rosenkraenzer <bero@redhat.com> 2.1-3
- Use automake15

* Tue Apr 16 2002 Bernhard Rosenkraenzer <bero@redhat.com> 2.1-2
- Change sonames

* Wed Mar 27 2002 Than Ngo <than@redhat.com> 2.1-1
- final

* Wed Mar 27 2002 Than Ngo <than@redhat.com> 2.1-0.cvs20020326.1
- update

* Wed Mar 20 2002 Than Ngo <than@redhat.com> 2.1rc3-1
- update to 2.1rc3

* Sun Mar 17 2002 Than Ngo <than@redhat.com> 2.1rc2-1
- update to 2.1rc2

* Sun Mar 10 2002 Than Ngo <than@redhat.com> 2.1beta2-3
- rebuild against new kdelibs

* Sun Mar 10 2002 Than Ngo <than@redhat.com> 2.1beta2-2
- fixed Strange characters appear in the output window (bug #59217)
- fixed return-line feed sign in Kdevelop setup tool (bug #55032)

* Fri Mar  8 2002 Than Ngo <than@redhat.com> 2.1beta2-1
- update to 2.1beta2

* Wed Jan 16 2002 Than Ngo <than@redhat.com> 2.1beta1-2
- rebuild against new kdelibs

* Wed Jan  9 2002 Than Ngo <than@redhat.com> 2.1beta1-1
- update to 2.1 beta1
- fix build against gcc 3
- fix some typo bugs
- get rid of libkfile
- update c_cpp_reference to 2.0.1

* Mon Oct 22 2001 Than Ngo <than@redhat.com> 2.0-1
- add patch to show non lattin1 font in build-in editor correct (bug #54457)

* Sat Sep 22 2001 Than Ngo <than@redhat.com> 2.0-2
- fix a bug in creating documentation index when running KDevelop Setup (bug #52760)
- backport some major bugfixes from 2.0.1

* Mon Jul 30 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.0-0.cvs20010730.1
- Don't crash on startup

* Tue Jul 24 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.0-0.cvs20010724.1
- Fix file list

* Mon Jul 23 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.0-0.cvs20010723.1
- Update

* Mon Feb 26 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Yet another respin - printing was broken.

* Sat Feb 24 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Update the C/C++ reference guide docs. The older version had a
  couple of examples that won't work with gcc 2.96-*

* Thu Feb 22 2001 Than Ngo <than@redhat.com>
- fix version number

* Wed Feb 21 2001 Than Ngo <than@redhat.com>
- 1.4-respin

* Tue Feb 20 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 1.4

* Wed Feb 14 2001 Than Ngo <than@redhat.com>
- update (only bugfixes)
- fix up kdelibs documentation path
- fix a dependency problem with kde-i18n package (Bug #27675)
- add qt-designer into requires

* Sun Feb 11 2001 Than Ngo <than@redhat.com>
- fixed to build on s390

* Tue Feb 06 2001 Than Ngo <than@redhat.com>
- update, only bugfixes

* Wed Jan 24 2001 Than Ngo <than@redhat.com>
- hacked for building of KDE references

* Tue Jan 23 2001 Than Ngo <than@redhat.com>
- work-around to build on alpha

* Mon Jan 22 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Update

* Wed Jan 10 2001 Than Ngo <than@redhat.com>
- update new snapshot, only require KDE2/Qt2

* Fri Dec 22 2000 Than Ngo <than@redhat.com>
- fixed dependency problem with kde-i18n

* Thu Dec 21 2000 Than Ngo <than@redhat.com>
- updated to 1.4beta1 with KDE2 support
- fixed to build on s390
- fixed some broken codes

* Fri Dec 8 2000 Than Ngo <than@redhat.com>
- fixed for building on ia64

* Wed Nov 15 2000 Than Ngo <than@redhat.com>
- build snapshot 20001112, it works now with KDE2 and kde1-compat
- fix libtool to build on sparc and alpha
- don't use make -j

* Sun Aug 13 2000 Than Ngo <than@redhat.com>
- fix kdelibsdoc-dir to show kdelibs-1.1.2 html docu correct

* Tue Aug 01 2000 Than Ngo <than@redhat.de>
- add missing ldconfig in post and postun section (Bug #14924)
- add missing C references stuff to kdevelop

* Sun Jul 30 2000 Than Ngo <than@redhat.de>
- rebuilt against compat-egcs-c++, put KDE1 under /usr
- cleanup specfile

* Tue Jul 25 2000 Than Ngo <than@redhat.de>
- fix dependency problem

* Wed Jul 19 2000 Than Ngo <than@redhat.de>
- rebuilt against compat-libstdc++

* Mon Jul 17 2000 Than Ngo <than@redhat.de>
- install under /usr/share instead /usr/lib/kde1-compat/share,
  fix dependency problem

* Sat Jul 15 2000 Than Ngo <than@redhat.de>
- rebuilt with egcs-c++-1.1.2

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jul 03 2000 Than Ngo <than@redhat.de>
- fix docdir
- add requires kdebase

* Sun Jul 02 2000 Than Ngo <than@redhat.de>
- rebuilt with  kde1-compat

* Sun Jun 18 2000 Than Ngo <than@redhat.de>
- rebuilt in the new build environment, fix docdir
- FHS packaging

* Thu Jun 08 2000 Than Ngo <than@redhat.de>
- update to 1.2
- move from powertools to main CD
- use %%configure

* Mon Apr 3 2000 Ngo Than <than@redhat.de>
- fix up reference (Bug #10368)

* Tue Feb 15 2000 Bernhard Rosenkränzer <bero@redhat.com>
- Fix up documentation path (Bug #7291)
- Update to current stable branch - this should fix up the debugger problem
- clean up spec file

* Thu Jan  6 2000 Bernhard Rosenkränzer <bero@redhat.com>
- Update to current stable branch
- Adapt to 6.2 Qt libraries
- Use BuildPrereq

* Wed Jan 05 2000 Ngo Than <than@redhat.de>
- added patch for alpha

* Tue Dec 21 1999 Ngo Than <than@redhat.de>
- updated kdevelop-1.0 release

* Tue Nov 16 1999 Preston Brown <pbrown@redhat.com>
- kdevelop 1.0beta4.1, docdir added, using DESTDIR env. variable.

* Thu Sep 09 1999 Preston Brown <pbrown@redhat.com>
- initial packaging for 6.1.
