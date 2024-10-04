%global commit0 1d2d8946041965175a9df7bdfbf3d0c8f4316d7a
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 1

%global framework ktexteditor

Name:    kf6-%{framework}
Version: 6.7.0
Release: 1%{?dist}
Summary: KDE Frameworks 6 Tier 3 with advanced embeddable text editor

License: BSD-2-Clause AND CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND MIT
URL:     https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Auth)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Sonnet)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  cmake(KF6TextWidgets)

BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6TextToSpeech)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)

BuildRequires:  pkgconfig(editorconfig)

Requires: kf6-filesystem

%description
KTextEditor provides a powerful text editor component that you can embed in your
application, either as a KPart or using the KF6::TextEditor library (if you need
more control).

The text editor component contains many useful features, from syntax
highlighting and automatic indentation to advanced scripting support, making it
suitable for everything from a simple embedded text-file editor to an advanced
IDE.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       cmake(KF6Parts)
Requires:       cmake(KF6SyntaxHighlighting)
%description    devel
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
%find_lang %{name} --all-name
# create/own dirs
mkdir -p %{buildroot}%{_kf6_qtplugindir}/ktexteditor
# Removing empty file
rm -f %{buildroot}%{_kf6_datadir}/katepart5/script/README.md

%files -f %{name}.lang
%dir %{_kf6_plugindir}/parts/
%doc README.md
%license LICENSES/*.txt
%{_kf6_bindir}/ktexteditor-script-tester6
%{_kf6_datadir}/dbus-1/system-services/org.kde.ktexteditor6.katetextbuffer.service
%{_kf6_datadir}/dbus-1/system.d/org.kde.ktexteditor6.katetextbuffer.conf
%{_kf6_datadir}/polkit-1/actions/org.kde.ktexteditor6.katetextbuffer.policy
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6TextEditor.so.6
%{_kf6_libdir}/libKF6TextEditor.so.%{version_no_git}
%{_kf6_libexecdir}/kauth/kauth_ktexteditor_helper
%{_kf6_plugindir}/parts/katepart.so
%{_kf6_qtplugindir}/ktexteditor/

%files devel
%{_qt6_docdir}/*.tags
%{_kf6_datadir}/kdevappwizard/templates/ktexteditor6-plugin.tar.bz2
%{_kf6_includedir}/KTextEditor/
%{_kf6_libdir}/cmake/KF6TextEditor/
%{_kf6_libdir}/libKF6TextEditor.so

%changelog
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

* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231012.021300.814f396-1
- Initial release
