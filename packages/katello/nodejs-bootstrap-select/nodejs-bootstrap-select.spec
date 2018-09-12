%global npm_name bootstrap-select
%global enable_tests 1

Name: nodejs-%{npm_name}
Version: 1.12.4
Release: 1%{?dist}
Summary: Bootstrap-select is a jQuery plugin that utilizes Bootstrap's dropdown
License: MIT
Group: Development/Libraries
URL: http://silviomoreto.github.io/bootstrap-select
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
Requires: npm(jquery) >= 1.8
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr dist %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr less %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr nuget %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr sass %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr test.html %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
%endif

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE
%doc CHANGELOG.md
%doc CONTRIBUTING.md
%doc README.md
%doc docs

%changelog
* Thu Jun 07 2018 Eric D. Helms <ericdhelms@gmail.com> 1.12.4-1
- Update to 1.12.4

* Thu Apr 19 2018 Eric D. Helms <ericdhelms@gmail.com> 1.12.2-1
- Add nodejs-bootstrap-select generated by npm2rpm using the single strategy
