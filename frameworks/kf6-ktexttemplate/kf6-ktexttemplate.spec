%global commit0 0f66a469aa12ec88a0aa6b9fcdc3b1c12fd0f814
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 2

%global		framework ktexttemplate

Name:		kf6-%{framework}
Version:	6.9.0%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:	1%{?dist}
Summary:	Separates the structure of documents from their data
License:	CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:		https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:	cmake
BuildRequires:	extra-cmake-modules
BuildRequires:	gcc-c++
BuildRequires:	kf6-rpm-macros
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Qml)

%description
The goal of KTextTemplate is to make it easier for application developers to
separate the structure of documents from the data they contain, opening the door
for theming and advanced generation of other text such as code.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	cmake(Qt6Core)
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%qch_package

%prep
%{!?bumpver:%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}
%autosetup -n %{sourcerootdir} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%files
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/ktexttemplate.categories
%{_kf6_plugindir}/ktexttemplate/
%{_kf6_libdir}/libKF6TextTemplate.so.6
%{_kf6_libdir}/libKF6TextTemplate.so.%{version_no_git}

%files devel
%{_qt6_docdir}/*.tags
%{_kf6_includedir}/KTextTemplate/
%{_kf6_libdir}/cmake/KF6TextTemplate/
%{_kf6_libdir}/libKF6TextTemplate.so

%changelog
%{?kde_snapshot_changelog_entry}
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

* Thu Sep 28 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230902.184733.74c03a0-1
- Initial release
