%global commit0 05e79ebbbf3784a87f72b7be571070125c10dfe3
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    accounts-qml-module
Summary: QML bindings for libaccounts-qt + libsignon-qt
Version: 0.7^1.git%{shortcommit0}
Release: 2%{?dist}

License: LGPL-2.1-only
URL:     https://gitlab.com/accounts-sso/accounts-qml-module
Source:  %{url}/-/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

BuildRequires: qt6-doctools
BuildRequires: cmake(AccountsQt6)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(SignOnQt6)

BuildRequires: qt5-doctools
BuildRequires: cmake(AccountsQt5)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(SignOnQt5)

%description
This QML module provides an API to manage the user's online accounts and get
their authentication data. It's a tiny wrapper around the Qt-based APIs of
libaccounts-qt and libsignon-qt.

%package        qt5
Summary:        Qt5 support for %{name}
%description    qt5
%{summary}.

%package        qt6
Summary:        Qt6 build of %{name}
Obsoletes:      %{name} < 0.7^1.git05e79eb-2
Provides:       %{name} = %{version}-%{release}
Provides:       %{name}%{?_isa} = %{version}-%{release}
%description    qt6
%{summary}.

%package doc
Summary: Documentation for %{name}
BuildArch: noarch
%description doc
This package contains the developer documentation for accounts-qml-module.


%prep
%autosetup -n %{name}-%{commit0} -p1


%build
mkdir %{_target_platform}-qt6
pushd %{_target_platform}-qt6
%{qmake_qt6} \
  CONFIG+=release \
  PREFIX=%{_prefix} \
  LIBDIR=%{_libdir} \
  ..
popd

%make_build -C %{_target_platform}-qt6

mkdir %{_target_platform}-qt5
pushd %{_target_platform}-qt5
%{qmake_qt5} \
  CONFIG+=release \
  PREFIX=%{_prefix} \
  LIBDIR=%{_libdir} \
  ..
popd

%make_build -C %{_target_platform}-qt5

%install
make install INSTALL_ROOT=%{buildroot} -C %{_target_platform}-qt6
make install INSTALL_ROOT=%{buildroot} -C %{_target_platform}-qt5

## unpackaged files
# remove tests
rm %{buildroot}%{_bindir}/tst_plugin
# avoid rpmlint warning
rm -fv %{buildroot}/%{_datadir}/%{name}/doc/html/.gitignore


%files qt6
%license COPYING
%doc README.md
%{_qt6_archdatadir}/qml/SSO/

%files qt5
%license COPYING
%doc README.md
%{_qt5_archdatadir}/qml/SSO/

%files doc
%doc %{_datadir}/%{name}/


%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 Rex Dieter <rdieter@fedoraproject.org> - 0.7-5
- build without -Werror

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 11 2020 Rex Dieter <rdieter@fedoraproject.org> - 0.7-1
- first try, inspiration from opensuse packaging

