%global srcname ytmusicapi

Name:           python-%{srcname}
Version:        1.12.3
Release:        %autorelease
License:        MIT
Summary:        Unofficial API for YouTube Music
Url:            https://github.com/sigma67/%{srcname}
Source0:        %{pypi_source}
Source1:        ytmusicapi.1

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
ytmusicapi is a Python 3 library to send requests to the YouTube Music API. 
It emulates YouTube Music web client requests using the user's 
cookie data for authentication.}

%description %_description


%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires -r
 
%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%pyproject_save_files %{srcname}
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/ytmusicapi.1

%check
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst CONTRIBUTING.rst
%{_bindir}/ytmusicapi
%{_mandir}/man1/ytmusicapi.1*


%changelog
%autochangelog
