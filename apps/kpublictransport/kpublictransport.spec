Name:           kpublictransport
Version:        24.01.85
Release:        1%{?dist}
License:        BSD and CC0-1.0 and LGPLv2+ and MIT and ODbL-1.0
Summary:        Library to assist with accessing public transport timetables and other data
URL:            https://invent.kde.org/libraries/kpublictransport
%apps_source

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: zlib-devel
BuildRequires: protobuf-devel

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Quick)

BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6NetworkManagerQt)
BuildRequires: qt6-qtbase-private-devel

%description
%{summary}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build

%install
%cmake_install

%files
%{_kf6_datadir}/qlogging-categories6/org_kde_kpublictransport_onboard.categories
%{_kf6_datadir}/qlogging-categories6/org_kde_kpublictransport.categories
%{_kf6_libdir}/libKPublicTransport.so.%{version}
%{_kf6_libdir}/libKPublicTransport.so.1
%{_kf6_libdir}/libKPublicTransportOnboard.so.%{version}
%{_kf6_libdir}/libKPublicTransportOnboard.so.1
%{_kf6_qmldir}/org/kde/kpublictransport/

%package devel
Summary: Development files for %{name}
License: BSD and CC0-1.0 and LGPLv2+ and MIT and ODbL-1.0
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.

%files devel
%{_includedir}/KPublicTransport/
%{_kf6_libdir}/cmake/KPublicTransport/
%{_kf6_libdir}/*.so

%changelog
* Sat Nov 25 2023 Steve Cossette <farchord@gmail.com> - 24.01.75-1
- 24.01.75

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

* Sun Jan 08 2023 Marc Deop <marcdeop@fedoraproject.org> - 22.12.1-1
- 22.12.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Than Ngo <than@redhat.com> - 22.04.3-1
- 22.04.3

* Mon May 16 2022 Justin Zobel <justin@1707.io> - 22.04.1-1
- Update to 22.04.1

* Thu Apr 21 2022 Justin Zobel <justin@1707.io> - 21.12.3-1
- Update to 21.12.3

* Wed Feb 09 2022 Justin Zobel <justin@1707.io> - 21.12.2-1
- Update to 21.12.2

* Wed Dec 22 2021 Justin Zobel <justin@1707.io> - 21.12-1
- Initial version of package
