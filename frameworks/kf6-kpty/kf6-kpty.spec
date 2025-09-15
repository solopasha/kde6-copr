%global commit0 dd8d23a3c06c7310ec637f60dac2fc437cf98848
%global shortcommit0 %{sub %{commit0} 1 7}
%global bumpver 1

%global framework kpty

Name:           kf6-%{framework}
Version:        6.18.0
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 2 module providing Pty abstraction

License:        BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://invent.kde.org/frameworks/%{framework}
%frameworks_meta
BuildOption: -DUTEMPTER_EXECUTABLE:PATH=/usr/libexec/utempter/utempter

BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)

BuildRequires:  cmake(Qt6Core)

BuildRequires:  libutempter-devel

# runtime calls %%_libexexdir/utempter/utempter
Requires:       libutempter

%description
KDE Frameworks 6 tier 2 module providing Pty abstraction.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6CoreAddons)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Pty.so.%{version_no_git}
%{_kf6_libdir}/libKF6Pty.so.6

%files devel
%{_kf6_includedir}/KPty/
%{_kf6_libdir}/cmake/KF6Pty/
%{_kf6_libdir}/libKF6Pty.so

%changelog
* Mon Sep 15 2025 Pavel Solovev <daron439@gmail.com> - 6.18.0-1
- Update to 6.18.0

* Fri Jan 03 2025 Pavel Solovev <daron439@gmail.com> - 6.10.0-1
- Update to 6.10.0

* Fri Dec 06 2024 Pavel Solovev <daron439@gmail.com> - 6.9.0-1
- Update to 6.9.0

* Sat Nov 02 2024 Pavel Solovev <daron439@gmail.com> - 6.8.0-1
- Update to 6.8.0

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

* Fri Oct 06 2023 Steve Cossette <farchord@gmail.com> - 5.27.80^20231001.123821.2d5f7cb-1
- Initial build
