%global framework kcontacts

Name:    kf6-%{framework}
Version: 5.246.0
Release: 1%{?dist}
Summary: The KContacts Library

# The following licenses are present in LICENSES but go unused: BSD-3-Clause, MIT, Unicode-DFS-2016
License: CC0-1.0 AND LGPL-2.0-or-later
URL:     https://projects.kde.org/%{framework}

%frameworks_source

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake
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
%{_kf6_libdir}/libKF6Contacts.so.*

%files devel
%{_kf6_includedir}/KContacts/
%{_kf6_libdir}/libKF6Contacts.so
%{_kf6_libdir}/cmake/KF6Contacts/

%changelog
* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Tue Oct 03 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231003.053528.606920e-1
- Initial Release
