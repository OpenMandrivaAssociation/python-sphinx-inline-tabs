Name:           python-sphinx-inline-tabs
Version:        2023.4.21
Release:        1
Summary:        Add inline tabbed content to your Sphinx documentation
License:        MIT
URL:            https://github.com/pradyunsg/sphinx-inline-tabs
Source0:        https://files.pythonhosted.org/packages/source/s/sphinx-inline-tabs/sphinx_inline_tabs-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:	python
BuildRequires:  python%{pyver}dist(sphinx)

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
%license LICENSE
%{python_sitelib}/sphinx_inline_tabs-%{version}.dist-info
%{python_sitelib}/sphinx_inline_tabs/
