%global framework kcontacts

Name:    kf6-%{framework}
Version: 6.3.0
Release: 1%{?dist}
Summary: The KContacts Library

# The following licenses are present in LICENSES but go unused: BSD-3-Clause, MIT, Unicode-DFS-2016
License: CC0-1.0 AND LGPL-2.0-or-later
URL:     https://projects.kde.org/%{framework}
%frameworks_meta

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)

BuildRequires:  cmake(Qt6Gui)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6CoreAddons)
Requires:       cmake(KF6Config)
Requires:       cmake(KF6I18n)
Requires:       cmake(KF6Codecs)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.



%qch_package

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{framework}-%{version} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*%{framework}.*
%{_kf6_libdir}/libKF6Contacts.so.%{version}
%{_kf6_libdir}/libKF6Contacts.so.6
%{_kf6_qmldir}/org/kde/contacts/

%files devel
%{_qt6_docdir}/*.tags
%{_kf6_includedir}/KContacts/
%{_kf6_libdir}/cmake/KF6Contacts/
%{_kf6_libdir}/libKF6Contacts.so

%changelog
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

* Tue Oct 03 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231003.053528.606920e-1
- Initial Release
