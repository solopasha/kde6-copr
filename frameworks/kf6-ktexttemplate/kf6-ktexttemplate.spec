%global		framework ktexttemplate

Name:		kf6-%{framework}
Version:	5.249.0
Release:	1%{?dist}
Summary:	Separates the structure of documents from their data
License:	CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:		https://invent.kde.org/frameworks/%{framework}

%frameworks_meta

BuildRequires:	cmake
BuildRequires:	extra-cmake-modules >= %{version}
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
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{framework}-%{version}

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
%{_kf6_libdir}/libKF6TextTemplate.so.%{version}

%files devel
%{_qt6_docdir}/*.tags
%{_kf6_includedir}/KTextTemplate/
%{_kf6_libdir}/cmake/KF6TextTemplate/
%{_kf6_libdir}/libKF6TextTemplate.so

%changelog
* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Thu Sep 28 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230902.184733.74c03a0-1
- Initial release
