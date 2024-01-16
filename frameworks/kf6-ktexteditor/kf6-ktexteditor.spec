%global framework ktexteditor

Name:    kf6-%{framework}
Version: 5.248.0
Release: 1%{?dist}
Summary: KDE Frameworks 6 Tier 3 with advanced embeddable text editor

License: BSD-2-Clause AND CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND MIT
URL:     https://invent.kde.org/frameworks/%{framework}

%frameworks_meta

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules >= %{version}
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
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{framework}-%{version} -p1

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
%{_kf6_datadir}/dbus-1/system-services/org.kde.ktexteditor6.katetextbuffer.service
%{_kf6_datadir}/dbus-1/system.d/org.kde.ktexteditor6.katetextbuffer.conf
%{_kf6_datadir}/polkit-1/actions/org.kde.ktexteditor6.katetextbuffer.policy
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6TextEditor.so.6
%{_kf6_libdir}/libKF6TextEditor.so.%{version}
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
* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231012.021300.814f396-1
- Initial release
