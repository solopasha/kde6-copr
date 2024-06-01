%global commit0 cb0d0f1e37f51d58933dd1a7eeac8ac97ffc73ea
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global bumpver 6

Name:           alpaka
Version:        0.1.1%{?bumpver:^%{bumpver}.git%{shortcommit0}}
Release:        1%{?dist}
Summary:        Kirigami client for Ollama

License:        CC0-1.0 AND GPL-2.0-only OR GPL-3.0-only OR LicenseRef-KDE-Accepted-GPL
URL:            https://invent.kde.org/utilities/alpaka
Source:         %{url}/-/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Widgets)

Requires:       kf6-kirigami
Requires:       kf6-kirigami-addons

Recommends:     ollama

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{commit0} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.alpaka.desktop
%{_kf6_datadir}/qlogging-categories6/kllm.categories
%{_kf6_libdir}/libkllmcore.so.0{,.*}
%{_kf6_libdir}/libkllmwidgets.so.0{,.*}

%files devel
%{_includedir}/KLLMCore/
%{_includedir}/KLLMWidgets/
%{_kf6_libdir}/cmake/KLLMCore/
%{_kf6_libdir}/cmake/KLLMWidgets/
%{_kf6_libdir}/libkllmcore.so
%{_kf6_libdir}/libkllmwidgets.so

%changelog
%autochangelog
