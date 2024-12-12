%global commit0 dd2430b1a9237831140af8b7158e5eeae212d22b
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

Name:           khealthcertificate
Version:        24.12.0
Release:        1%{?dist}
License:        Apache2.0 and BSD and CC-BY-4.0 and CC0-1.0 and EUPL-1.2 and LGPL-2.0 and MIT and W3C-20120513
Summary:        Handling of digital vaccination, test and recovery certificates.
URL:            https://invent.kde.org/pim/khealthcertificate
%apps_source

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: gcc-c++
BuildRequires: openssl-devel
BuildRequires: zlib-devel

BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Codecs)
BuildRequires: cmake(KF6I18n)

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)

%description
%{summary}.

%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1

%build
%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build

%install
%cmake_install

%files
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/org_kde_khealthcertificate.categories
%{_kf6_libdir}/libKHealthCertificate.so.%{version_no_git}
%{_kf6_libdir}/libKHealthCertificate.so.1
%{_kf6_qmldir}/org/kde/khealthcertificate/


%package devel
Summary: Development files for khealthcertificate
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(Qt6Core)
%description devel
%{summary}.

%files devel
%{_includedir}/KHealthCertificate/
%{_kf6_libdir}/cmake/KHealthCertificate/
%{_kf6_libdir}/libKHealthCertificate.so

%changelog
* Fri Dec 06 2024 Pavel Solovev <daron439@gmail.com> - 24.12.0-1
- Update to 24.12.0

* Tue Nov 05 2024 Pavel Solovev <daron439@gmail.com> - 24.08.3-1
- Update to 24.08.3

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

* Mon Dec 18 2023 Steve cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.01.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jan 30 2023 Justin Zobel <justin@1707.io> - 23.01.0-1
- Update to 23.01.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 01 2022 Justin Zobel <justin@1707.io> - 22.11-1
- Update to 22.11

* Wed Sep 28 2022 Justin Zobel <justin@1707.io> - 22.09-1
- Update to 22.09

* Thu Aug 25 2022 Justin Zobel <justin@1707.io> - 22.06-1
- Update to 22.06

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.02-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Feb 09 2022 Justin Zobel <justin@1707.io> - 22.02-1
- Update to 22.02

* Wed Dec 22 2021 Justin Zobel <justin@1707.io> - 21.12-1
- Initial version of package
