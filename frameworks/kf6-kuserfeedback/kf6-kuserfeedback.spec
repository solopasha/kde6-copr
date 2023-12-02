%global framework kuserfeedback

Name:    kf6-%{framework}
Summary: Framework for collecting user feedback for apps via telemetry and surveys
Version: 5.246.0
Release: 1%{?dist}

License: MIT AND CC0-1.0 AND BSD-3-Clause
URL:     https://invent.kde.org/frameworks/%{framework}
%frameworks_source

## upstream patches


BuildRequires: cmake
BuildRequires: gnupg2
BuildRequires: gcc-c++

BuildRequires: kf6-rpm-macros
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules

BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Charts)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6LinguistTools)

BuildRequires: bison
BuildRequires: flex

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Network)
Requires:       cmake(Qt6Widgets)

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        console
Summary:        Analytics and administration tool for UserFeedback servers
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  qt6-qtbase-private-devel
Requires:       qt6-qtcharts%{?_isa}
# Obsolete the qt5 version
Obsoletes:      kuserfeedback-console < %{version}-%{release}
Provides:       kuserfeedback-console = %{version}-%{release}
Provides:       kuserfeedback-console%{?_isa} = %{version}-%{release}

%description    console
Analytics and administration tool for UserFeedback servers.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n %{framework}-%{version}


%build
%cmake_kf6 \
   -DBUILD_WITH_QT6=ON \
   -DENABLE_DOCS:BOOL=OFF \
   -DENABLE_CLI:BOOL=OFF


%cmake_build


%install
%cmake_install

%find_lang userfeedbackconsole6 --with-qt
%find_lang userfeedbackprovider6 --with-qt


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.kuserfeedback-console.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.kuserfeedback-console.desktop


%files -f userfeedbackprovider6.lang
%doc README.md
%license LICENSES/*
%dnl %{_kf6_bindir}/userfeedbackctl
%{_kf6_datadir}/qlogging-categories6/org_kde_UserFeedback.categories
%{_kf6_libdir}/libKF6UserFeedbackCore.so.*
%{_kf6_libdir}/libKF6UserFeedbackWidgets.so.*
%{_kf6_qmldir}/org/kde/userfeedback/


%files devel
%{_kf6_archdatadir}/mkspecs/modules/qt_KF6UserFeedback*.pri
%{_kf6_includedir}/KUserFeedback
%{_kf6_includedir}/KUserFeedbackCore/
%{_kf6_includedir}/KUserFeedbackWidgets/
%{_kf6_libdir}/cmake/KF6UserFeedback/
%{_kf6_libdir}/libKF6UserFeedbackCore.so
%{_kf6_libdir}/libKF6UserFeedbackWidgets.so


%files console -f userfeedbackconsole6.lang
%{_kf6_bindir}/UserFeedbackConsole
%{_kf6_datadir}/applications/org.kde.kuserfeedback-console.desktop
%{_kf6_metainfodir}/org.kde.kuserfeedback-console.appdata.xml


%changelog
* Sun Nov 12 2023 Alessandro Astone <ales.astone@gmail.com> - 5.245.0-1
- 5.245.0
- This is now part of KF6

* Thu Nov 02 2023 Yaroslav Sidlovsky <zawertun@gmail.com> - 1.3.0-1
- version 1.3.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep 23 2022 Jan Grulich <jgrulich@redhat.com> - 1.2.0-7
- Bring back dependency on qt5-qtcharts

* Fri Sep 23 2022 Jan Grulich <jgrulich@redhat.com> - 1.2.0-6
- Drop hardcoded Qt version requirement

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Jan Grulich <jgrulich@redhat.com> - 1.2.0-4
- Rebuild (qt5)

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 1.2.0-3
- Rebuild (qt5)

* Tue Mar 08 2022 Jan Grulich <jgrulich@redhat.com> - 1.2.0-2
- Rebuild (qt5)

* Fri Feb 04 2022 Yaroslav Sidlovsky <zawertun@gmail.com> - 1.2.0-1
- update to 1.2.0

* Fri Feb 04 2022 Rex Dieter <rdieter@fedoraproject.org> - 1.0.0-11
- -console: uses qt5-qtcharts private api
- -devel: use cmake-style deps instead of hard-coding qt5-qtbase

* Thu Feb 03 2022 Rex Dieter <rdieter@fedoraproject.org> - 1.0.0-10
- backport crash fix recommended by upstream
- cleanup macros
- simplify %%files
- BR: bison flex (enables Survey targeting expressions support)
- drop BR: qt5-qtbase-private-devel (no private api use detected)
- drop non-autodetected runtime deps

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 21:50:41 MSK 2021 Yaroslav Sidlovsky <zawertun@gmail.com> - 1.0.0-6
- track Qt private api usage

* Tue Nov 24 13:19:14 MSK 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 1.0.0-5
- rebuild due to new Qt version

* Sun Sep 20 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 1.0.0-4
- one more rebuild

* Sat Sep 19 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 1.0.0-3
- rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 06 2020 Yaroslav Sidlovsky <zawertun@gmail.com> - 1.0.0-1
- first spec for version 1.0.0

