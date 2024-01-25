%global		framework kcoreaddons

Name:		kf6-%{framework}
Version:	5.249.0
Release:	1%{?dist}
Summary:	KDE Frameworks 6 Tier 1 addon with various classes on top of QtCore
License:	BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND MPL-1.1 AND LGPL-2.0-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND LGPL-2.1-only WITH Qt-LGPL-exception-1.1
URL:		https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	extra-cmake-modules >= %{version}
BuildRequires:	kf6-rpm-macros
BuildRequires:	qt6-qtbase-devel
BuildRequires:	qt6-qttools-devel
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	systemd-devel

Requires:	kf6-filesystem

%description
KCoreAddons provides classes built on top of QtCore to perform various tasks
such as manipulating mime types, autosaving files, creating backup files,
generating random sequences, performing text manipulations such as macro
replacement, accessing user information and many more.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	qt6-qtbase-devel
%description	devel
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

%find_lang_kf6 kcoreaddons6_qt
%find_lang_kf6 kde6_xml_mimetypes
cat *.lang > all.lang

%files -f all.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/kf6/jsonschema/kpluginmetadata.schema.json
%{_kf6_datadir}/kf6/licenses/
%{_kf6_datadir}/mime/packages/kde6.xml
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6CoreAddons.so.6
%{_kf6_libdir}/libKF6CoreAddons.so.%{version}
%{_kf6_qmldir}/org/kde/coreaddons/

%files devel
%{_qt6_docdir}/*.tags
%{_kf6_includedir}/KCoreAddons/
%{_kf6_libdir}/cmake/KF6CoreAddons/
%{_kf6_libdir}/libKF6CoreAddons.so

%changelog
* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Tue Oct 03 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230915.190519.c53eeac-2
- Fixed a spec issue with some files and missing macros

* Wed Sep 27 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230915.130519.c53eeac-1
- Initial release
