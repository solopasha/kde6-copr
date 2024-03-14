Name:    ksanecore
Summary: Library providing logic to interface scanners
Version: 24.02.1
Release: 1%{?dist}

License: LGPL-2.1-only OR LGPL-3.0-only
URL:     https://invent.kde.org/libraries/ksanecore
%apps_source

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++

BuildRequires: kf5-rpm-macros
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)

BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)

BuildRequires: pkgconfig(sane-backends)

%description
%{summary}.

%package qt5
Summary: Qt5 library providing logic to interface scanners
Requires: %{name}-common = %{version}-%{release}
%description qt5
%{summary}.

%package qt5-devel
Summary: Development files for %{name}-qt5
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
Requires: cmake(Qt5Gui)
%description qt5-devel
%{summary}.

%package qt6
Summary: Qt6 library providing logic to interface scanners
Obsoletes: %{name} < 24.01.85
Requires: %{name}-common = %{version}-%{release}
%description qt6
%{summary}.

%package qt6-devel
Summary:  Development files for %{name}-qt6
Obsoletes: %{name}-devel < 24.01.85
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}
Requires: cmake(Qt6Gui)
%description qt6-devel
%{summary}.

%package common
Summary: Files shared between the Qt5 and Qt6 versions of the library
Conflicts: %{name} < 24.01
%description common
%{summary}.
Provides internationalization files.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1


%build
%global _vpath_builddir %{_target_platform}-qt5
%cmake_kf5 -DBUILD_WITH_QT6=OFF
%cmake_build

%global _vpath_builddir %{_target_platform}-qt6
%cmake_kf6 -DBUILD_WITH_QT6=ON
%cmake_build

%install
%global _vpath_builddir %{_target_platform}-qt5
%cmake_install

%global _vpath_builddir %{_target_platform}-qt6
%cmake_install

%find_lang %{name} --all-name --with-html

%files common -f %{name}.lang
%doc README.md
%license LICENSES/*

%files qt5
%{_libdir}/libKSaneCore.so.{1,%{maj_ver_kf6}.*}

%files qt5-devel
%{_includedir}/KSaneCore/
%{_libdir}/cmake/KSaneCore/
%{_libdir}/libKSaneCore.so

%files qt6
%{_libdir}/libKSaneCore6.so.{1,%{maj_ver_kf6}.*}

%files qt6-devel
%{_includedir}/KSaneCore6/
%{_libdir}/cmake/KSaneCore6/
%{_libdir}/libKSaneCore6.so


%changelog
* Thu Mar 21 2024 Pavel Solovev <daron439@gmail.com> - 24.02.1-1
- Update to 24.02.1

* Thu Oct 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.2-1
- 23.08.2

* Sat Sep 16 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.1-1
- 23.08.1

* Sat Aug 26 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.0-1
- 23.08.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.3-1
- 23.04.3

* Tue Jun 06 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.2-1
- 23.04.2

* Sat May 13 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.1-1
- 23.04.1

* Fri Apr 14 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.0-1
- 23.04.0

* Fri Mar 31 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.90-1
- 23.03.90

* Mon Mar 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.80-1
- 23.03.80

* Thu Mar 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 22.12.3-1
- 22.12.3

* Tue Jan 31 2023 Marc Deop <marcdeop@fedoraproject.org> - 22.12.2-1
- 22.12.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 Justin Zobel <justin@1707.io> - 22.12.1-1
- Update to 22.12.1

* Wed Dec 21 2022 Justin Zobel <justin@1707.io> - 22.12.0-1
- Initial inclusion
