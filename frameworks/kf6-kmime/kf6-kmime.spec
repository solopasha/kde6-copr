%global commit0 e3eb1c7c3ab219b118d7439b727b7f75fbcc9345
%global shortcommit0 %{sub %{commit0} 1 7}
%global bumpver 1

%global framework kmime

Name:           kf6-%{framework}
Version:        6.33.0%{?bumpver:~%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
Summary:        Library to assist handling MIME data
License:        BSD-2-Clause AND BSD-3-Clause AND CC-BY-SA-4.0 AND CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later
URL:            https://invent.kde.org/frameworks/%{framework}
%frameworks_meta

BuildRequires:  cmake(KF6Codecs)

BuildRequires:  cmake(Qt6Core)

%description
%{summary.}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core)
Requires:       cmake(KF6Codecs)
%description    devel
%{summary}.

%install -a
%find_lang_kf6 libkmime6_qt

%files -f libkmime6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Mime.so.%{version_no_git}
%{_kf6_libdir}/libKF6Mime.so.6

%files devel
%{_kf6_includedir}/KMime/
%{_kf6_libdir}/cmake/KF6Mime/
%{_kf6_libdir}/libKF6Mime.so

%changelog
%{?kde_snapshot_changelog_entry}