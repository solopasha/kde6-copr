%global commit0 fdc17bf805631b30fb032bc0fb73afcab93f86d7
%global shortcommit0 %{sub %{commit0} 1 7}
%global bumpver 1

%global framework kdoctools

Name:           kf6-%{framework}
Version:        6.20.0%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 2 addon for generating documentation

License:        BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-LGPL
URL:            https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Any::URI::Escape)

Requires:       docbook-dtds
Requires:       docbook-style-xsl

%description
Provides tools to generate documentation in various format from DocBook files.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       kf6-kdoctools-static = %{version}-%{release}
Requires:       qt6-qtbase-devel
Requires:       perl(Any::URI::Escape)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_bindir}/checkXML6
%{_kf6_bindir}/meinproc6
%{_kf6_datadir}/kf6/kdoctools/
%{_kf6_libdir}/libKF6DocTools.so.%{version_no_git}
%{_kf6_libdir}/libKF6DocTools.so.6
%{_kf6_mandir}/man1/*.1*
%{_kf6_mandir}/man7/*.7*

%files devel
%{_kf6_includedir}/KDocTools/
%{_kf6_libdir}/cmake/KF6DocTools/
%{_kf6_libdir}/libKF6DocTools.so

%changelog
%{?kde_snapshot_changelog_entry}
* Fri Jan 03 2025 Pavel Solovev <daron439@gmail.com> - 6.10.0-1
- Update to 6.10.0

* Fri Dec 06 2024 Pavel Solovev <daron439@gmail.com> - 6.9.0-1
- Update to 6.9.0

* Sat Nov 02 2024 Pavel Solovev <daron439@gmail.com> - 6.8.0-1
- Update to 6.8.0

* Fri Oct 04 2024 Pavel Solovev <daron439@gmail.com> - 6.7.0-1
- Update to 6.7.0

* Fri Sep 06 2024 Pavel Solovev <daron439@gmail.com> - 6.6.0-1
- Update to 6.6.0

* Fri Aug 09 2024 Pavel Solovev <daron439@gmail.com> - 6.5.0-1
- Update to 6.5.0

* Fri Jul 12 2024 Pavel Solovev <daron439@gmail.com> - 6.4.0-1
- Update to 6.4.0

* Fri Jun 07 2024 Pavel Solovev <daron439@gmail.com> - 6.3.0-1
- Update to 6.3.0

* Sun Jun 02 2024 Pavel Solovev <daron439@gmail.com> - 6.2.0-1.1
- rebuild for f40

* Sun May 12 2024 Pavel Solovev <daron439@gmail.com> - 6.2.0-1
- Update to 6.2.0

* Fri Apr 12 2024 Pavel Solovev <daron439@gmail.com> - 6.1.0-1
- Update to 6.1.0

* Wed Mar 20 2024 Pavel Solovev <daron439@gmail.com> - 6.0.0-2
- qmlcache rebuild

* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Tue Oct 03 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231005.103639.d33466d-1
- Initial Release
