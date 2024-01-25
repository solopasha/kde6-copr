Name:    mimetreeparser
Version: 24.01.95
Release: 1%{?dist}
Summary: Parser for MIME trees

License: LGPL-2.0-or-later AND GPL-3.0-only AND GPL-2.0-only AND GPL-2.0-or-later AND (LGPL-2.1-only OR LGPL-3.0-only OR LicenseRef-KDE-Accepted-LGPL)
URL:     https://invent.kde.org/pim/mimetreeparser
%apps_source

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6WidgetsAddons)

BuildRequires:  cmake(KPim6Libkleo)
BuildRequires:  cmake(KPim6Mbox)
BuildRequires:  cmake(KPim6Mime)

BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  qt6-qtbase-private-devel

BuildRequires:  cmake(Gpgmepp)

Requires:       kf6-kirigami2

%description
%{summary}.

%package   devel
Summary:   Development files for %{name}
Requires:  %{name}%{?_isa} = %{version}-%{release}
Requires:  cmake(KF6I18n)
Requires:  cmake(KPim6Mbox)
Requires:  cmake(KPim6Mime)
Requires:  cmake(Qt6Core5Compat)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name


%files -f %{name}.lang
%license LICENSES/*
%{_kf6_libdir}/libKPim6MimeTreeParserCore.so.5.*
%{_kf6_libdir}/libKPim6MimeTreeParserCore.so.6
%{_kf6_libdir}/libKPim6MimeTreeParserWidgets.so.5.*
%{_kf6_libdir}/libKPim6MimeTreeParserWidgets.so.6
%{_kf6_qmldir}/org/kde/pim/mimetreeparser/
%{_kf6_datadir}/qlogging-categories6/mimetreeparser2.categories

%files devel
%{_includedir}/KPim6/MimeTreeParserCore/
%{_includedir}/KPim6/MimeTreeParserWidgets/
%{_kf6_archdatadir}/mkspecs/modules/*.pri
%{_kf6_libdir}/cmake/KPim6MimeTreeParserCore/
%{_kf6_libdir}/cmake/KPim6MimeTreeParserWidgets/
%{_kf6_libdir}/libKPim6MimeTreeParserCore.so
%{_kf6_libdir}/libKPim6MimeTreeParserWidgets.so


%changelog
* Sun Nov 26 2023 Pavel Solovev <daron439@gmail.com> - 24.01.75-1
- Init

