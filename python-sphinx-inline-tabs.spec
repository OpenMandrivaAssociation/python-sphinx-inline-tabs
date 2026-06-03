%define module sphinx-inline-tabs
%define oname sphinx_inline_tabs

Name:		python-sphinx-inline-tabs
Version:	2025.12.21.14
Release:	1
Summary:	Add inline tabbed content to your Sphinx documentation
License:	MIT
Group:		Development/Python
URL:		https://github.com/pradyunsg/sphinx-inline-tabs
Source0:	https://files.pythonhosted.org/packages/source/s/%{module}/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildOption(prep):	-p1
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(wheel)

%description
Add inline tabbed content to your Sphinx documentation.

Features:

- Elegant design: Small footprint in the markup and generated website,
  while looking good.
- Configurable: All the colors can be configured using CSS variables.
- Synchronization: Tabs with the same label all switch with a single click.
- Works without JavaScript: JavaScript is not required for the basics, only for
  synchronization.}

%files
%doc README.md
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}.dist-info
