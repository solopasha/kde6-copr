Name:          kjournald
Version:       24.01.95
Release:       1%{?dist}
Summary:       Framework for interacting with systemd-journald

License:       BSD-3-Clause and CC0-1.0 and MIT and LGPL-2.1-or-later and MIT
URL:           https://invent.kde.org/system/%{name}
%apps_source


BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: libappstream-glib
BuildRequires: systemd-devel

BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Widgets)

# QML module dependencies
Requires:      kf6-kirigami%{?_isa}

%description
%{summary}.

%package       libs
Summary:       Library files for kjournald
Requires:      %{name} = %{version}
%description   libs

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-kde --with-man --all-name
# unpackaged (headers not installed, no stable API)
rm -f %{buildroot}%{_kf6_libdir}/libkjournald.so

%check
desktop-file-validate %{buildroot}/%{_kf6_datadir}/applications/org.kde.kjournaldbrowser.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kjournaldbrowser.appdata.xml

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/kjournaldbrowser
%{_kf6_datadir}/applications/org.kde.kjournaldbrowser.desktop
%{_kf6_datadir}/qlogging-categories6/kjournald.categories
%{_kf6_metainfodir}/org.kde.kjournaldbrowser.appdata.xml

%files libs
%{_kf6_libdir}/libkjournald.so.%{version}
%{_kf6_libdir}/libkjournald.so.0

%changelog
* Sun Dec 03 2023 Yaakov Selkowitz <yselkowitz@fedoraproject.org> - 24.01.80-1
- 24.01.80

* Mon Nov 27 2023 Yaakov Selkowitz <yselkowitz@fedoraproject.org> - 24.01.75-1
- 24.01.75

* Thu Oct 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.2-1
- 23.08.2

* Sat Sep 23 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.1-2
- Rebuild(extra-cmake-modules)

* Sat Sep 16 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.1-1
- 23.08.1

* Sat Aug 26 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.0-1
- 23.08.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 16 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.3-1
- 23.04.3

* Thu Jun 8 2023 Steve Cossette <farchord@gmail.com> - 23.04.2-1
- Initial release
