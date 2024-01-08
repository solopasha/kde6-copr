# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    kdiagram2
Summary: Powerful libraries (KChart, KGantt) for creating business diagrams
Version: 2.8.0
Release: 8%{?dist}

License: GPLv2+
Url:     https://invent.kde.org/graphics/kdiagram
Source0: http://download.kde.org/stable/kdiagram/%{version}/kdiagram-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Help)
BuildRequires: cmake(Qt5PrintSupport)
BuildRequires: cmake(Qt5Sql)
BuildRequires: cmake(Qt5Svg)

%if 0%{?tests}
BuildRequires: cmake(Qt5Test)
BuildRequires: xorg-x11-server-Xvfb
%endif

# For AutoReq cmake-filesystem
BuildRequires: cmake

%description
Powerful libraries (KChart, KGantt) for creating business diagrams.

%package devel
Summary: Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(Qt5Svg)
Requires: cmake(Qt5Widgets)
Requires: cmake(Qt5PrintSupport)
%description devel
%{summary}.


%prep
%autosetup -n kdiagram-%{version} -p1

%build
%cmake_kf5 \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{?!tests:OFF}

%cmake_build


%install
%cmake_install

%find_lang_kf5 kchart_qt
%find_lang_kf5 kgantt_qt
cat kchart_qt.lang kgantt_qt.lang > %{name}.lang


%check
%if 0%{?tests}
# FIXME/TODO: make macros better to not have to do this when using xvfb-run
echo "%ctest" > ./rpm-check.sh
chmod +x ./rpm-check.sh
xvfb-run -a ./rpm-check.sh
%endif


%ldconfig_scriptlets

%files -f %{name}.lang
%license LICENSE.GPL.txt
%{_kf5_libdir}/libKChart.so.2*
%{_kf5_libdir}/libKGantt.so.2*

%files devel
%{_includedir}/KChart/
%{_includedir}/KGantt/
%{_includedir}/kchart_version.h
%{_includedir}/kgantt_version.h
%{_kf5_libdir}/libKChart.so
%{_kf5_libdir}/libKGantt.so
%{_kf5_libdir}/cmake/KChart/
%{_kf5_libdir}/cmake/KGantt/
%{_kf5_archdatadir}/mkspecs/modules/qt_KChart.pri
%{_kf5_archdatadir}/mkspecs/modules/qt_KGantt.pri


%changelog
* Mon Dec 18 2023 Neal Gompa <ngompa@fedoraproject.org> - 2.8.0-8
- Rename to kdiagram2

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 2021 Rex Dieter <rdieter@fedoraproject.org> - 2.8.0-1
- 2.8.0
- %%check: use %%ctest (with some hackery)
- update URL
- drop 'BR: make', cmake pulls it in

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Apr 21 2020 Rex Dieter <rdieter@fedoraproject.org> - 2.7.0-1
- 2.7.0

* Mon Apr 13 2020 Rex Dieter <rdieter@fedoraproject.org> - 2.6.3-1
- 2.6.3

* Sun Mar 29 2020 Rex Dieter <rdieter@fedoraproject.org> - 2.6.2-1
- 2.6.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 19 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.6.1-1
- 2.6.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 07 2017 Björn Esser <besser82@fedoraproject.org> - 2.6.0-7
- Rebuilt for AutoReq cmake-filesystem

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Daniel Vrátil <dvratil@fedoraproject.org> - 2.6.0-4
- Add -devel dependencies

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 17 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.6.0-2
- add library scriptlets, reduce test time to 20 sec

* Sat Dec 31 2016 Rex Dieter <rdieter@math.unl.edu> - 2.6.0-1
- kdiagram-2.6.0

