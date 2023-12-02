
%global commit0 d759439066f0a34e5ad352ebab0b3bb2790d429e
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           signon-plugin-oauth2
Version:        0.25^1.git%{shortcommit0}
Release:        1%{?dist}
Summary:        OAuth2 plugin for the Accounts framework

License:        LGPLv2
URL:            https://gitlab.com/accounts-sso/signon-plugin-oauth2

Source0:        %{url}/-/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
Patch:          https://gitlab.com/accounts-sso/signon-plugin-oauth2/-/merge_requests/28.patch
# drop -Werror -fno-rtti
Patch100: signon-plugin-oauth2-cxxflags.patch

BuildRequires:  make
BuildRequires:  qt6-qtbase-devel
BuildRequires:  signon-devel
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  libproxy-devel

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.


%prep
%autosetup -n %{name}-%{commit0} -p1


%build
%qmake_qt6 \
    QMF_INSTALL_ROOT=%{_prefix} \
    CONFIG+=release \
    LIBDIR=%{?_libdir} \
    signon-oauth2.pro
%make_build


%install
%make_install INSTALL_ROOT=%{buildroot}

# Delete tests
rm -fv %{buildroot}/%{_bindir}/signon-oauth2plugin-tests
rm -rfv %{buildroot}/%{_datadir}/signon-oauth2plugin-tests

# Delete examples
rm -fv %{buildroot}/%{_bindir}/oauthclient
rm -rvf %{buildroot}/%{_sysconfdir}


%files
%{_libdir}/signon/liboauth2plugin.so

%files devel
%{_includedir}/signon-plugins/*.h
%{_libdir}/pkgconfig/signon-oauth2plugin.pc


%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 08 2020 Rex Dieter <rdieter@fedoraproject.org> - 0.24-1
- 0.24 (#1267568)

* Sun Nov 08 2020 Rex Dieter <rdieter@fedoraproject.org> - 0.22-14
- patch out -Werror move -no-rtti for tests/ only (#1891251)
- use %%autosetup, %%make_build, %%make_install
- add %check

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 18 2020 Than Ngo <than@redhat.com> - 0.22-12
- Fixed FTBFS

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 01 2015 Daniel Vrátil <dvratil@redhat.com> - 0.22-1
- Update to 0.22
- fix upstream URL (moved to gitlab)

* Wed Apr 29 2015 Daniel Vrátil <dvratil@redhat.com> - 0.21-2
- Manually specify libdir for installation

* Tue Mar 17 2015 Daniel Vrátil <dvratil@redhat.com> - 0.21-1
- Initial version
