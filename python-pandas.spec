%global pypi_name pandas
%bcond_with test

Name:           python-%{pypi_name}
Version:        0.25.3
Release:        1
Summary:        Data structures and data analysis tools for Python
License:        BSD
URL:            https://pandas.pydata.org/
Source0:        https://github.com/pandas-dev/pandas/releases/download/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  gcc gcc-c++ gdb-headless
BuildRequires:  python3-devel python3-setuptools python3-numpy
%if %{with test}
BuildRequires:  python3-pytest >= 4.0.2
%endif

%global _description \
pandas is an open source, BSD-licensed library \
providing high-performance, easy-to-use data structures \
and data analysis tools for the Python programming language.

%description %{_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires: python3-numpy python3-dateutil python3-pytz


%description -n python3-%{pypi_name} %{_description}

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%if %{with test}
%check
py.test-%{python3_version}
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md RELEASE.md
%{python3_sitearch}/%{pypi_name}/
%{python3_sitearch}/%{pypi_name}-*.egg-info/

%changelog
* Wed Nov 6 2019 shanshishi <shanshishi@huawei.com> - 0.25.3-1
- Init package
