Name:           accessibility-inspector
Version:        24.05.0
Release:        1%{?dist}
License:        (LGPL-2.1-only OR LGPL-3.0-only) AND CC0-1.0
Summary:        Inspect your application accessibility tree
URL:            https://invent.kde.org/accessibility/accessibility-inspector
%apps_source

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6XmlGui)

BuildRequires:  cmake(QAccessibilityClient6)

%description
%{summary}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/*.desktop

%find_lang accessibilityinspector

%files -f accessibilityinspector.lang
%license LICENSES/*.txt
%{_kf6_bindir}/accessibilityinspector
%{_kf6_datadir}/applications/org.kde.accessibilityinspector.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.accessibilityinspector.svg
%{_kf6_datadir}/qlogging-categories6/accessibilityinspector.categories
%{_kf6_libdir}/libaccessibilityinspector.so.1{,.*}
%{_kf6_metainfodir}/org.kde.accessibilityinspector.metainfo.xml

%changelog
* Thu May 23 2024 Pavel Solovev <daron439@gmail.com> - 24.05.0-1
- Update to 24.05.0

* Fri Apr 26 2024 Pavel Solovev <daron439@gmail.com> - 24.04.80-1
- Initial build
