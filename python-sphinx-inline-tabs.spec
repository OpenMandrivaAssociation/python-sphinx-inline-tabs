Name:           python-sphinx-inline-tabs
# There are 2 different versions here:
# https://github.com/pradyunsg/sphinx-inline-tabs/issues/7
Version:        2021.4.11b9
%global tag     2021.04.11.beta9
Release:        1
Summary:        Add inline tabbed content to your Sphinx documentation
License:        MIT
URL:            https://github.com/pradyunsg/sphinx-inline-tabs
Source0:         https://files.pythonhosted.org/packages/source/s/sphinx-inline-tabs/sphinx-inline-tabs-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  pkgconfig(python)

%description
Add inline tabbed content to your Sphinx documentation.

Features:

- Elegant design: Small footprint in the markup and generated website,
  while looking good.
- Configurable: All the colors can be configured using CSS variables.
- Synchronization: Tabs with the same label all switch with a single click.
- Works without JavaScript: JavaScript is not required for the basics, only for
  synchronization.}

%prep
%autosetup -p1 -n sphinx-inline-tabs-%{version}

%build
%py_build

%install
%py_install

%files
%doc README.md
%doc CODE_OF_CONDUCT.md
%license LICENSE
