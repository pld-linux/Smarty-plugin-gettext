%include	/usr/lib/rpm/macros.php
%define		php_min_version 5.2.1
Summary:	Gettext support for Smarty
Summary(pl.UTF-8):	Obsługa gettexta dla systemu Smarty
Name:		Smarty-plugin-gettext
Version:	1.0.1
Release:	1
License:	LGPL v2+
Group:		Development/Languages/PHP
Source0:	https://github.com/glensc/smarty-gettext/archive/%{version}/smarty-gettext-%{version}.tar.gz
# Source0-md5:	3b44479b461a066d705807dd4d3ecae7
URL:		https://github.com/glensc/smarty-gettext
BuildRequires:	rpm-php-pearprov
BuildRequires:	sed >= 4.0
Requires:	Smarty >= 2.6.10-4
Requires:	php(core) >= %{php_min_version}
Requires:	php(gettext)
Requires:	sed >= 4.0
Provides:	smarty-gettext = %{version}-%{release}
Obsoletes:	smarty-gettext
Obsoletes:	smarty-gettext-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_smartyplugindir	%{php_data_dir}/Smarty/plugins
%define		_smarty3plugindir	%{php_data_dir}/Smarty3/plugins

# tsmarty2c is deliberately packaged to both packages with same name
%define		_duplicate_files_terminate_build   0

%description
smarty-gettext provides gettext support for Smarty, the popular PHP
templating engine <http://smarty.php.net/>.

%description -l pl.UTF-8
smarty-gettext dodaje obsługę gettexta do systemu Smarty - popularnego
silnika szablonów dla PHP - <http://smarty.php.net/>.

%package -n php-Smarty-plugin-gettext
Summary:	Gettext support for Smarty
Summary(pl.UTF-8):	Obsługa gettexta dla systemu Smarty
Group:		Development/Languages/PHP
Requires:	php(core) >= %{php_min_version}
Requires:	php(gettext)
Requires:	php-Smarty >= 3.1.8-4

%description -n php-Smarty-plugin-gettext
smarty-gettext provides gettext support for Smarty, the popular PHP
templating engine <http://smarty.php.net/>.

%description -n php-Smarty-plugin-gettext -l pl.UTF-8
smarty-gettext dodaje obsługę gettexta do systemu Smarty - popularnego
silnika szablonów dla PHP - <http://smarty.php.net/>.

%prep
%setup -q -n smarty-gettext-%{version}

%{__sed} -i -e '1s,^#!.*php,#!/usr/bin/php,' tsmarty2c.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_smartyplugindir},%{_smarty3plugindir},%{_bindir}}
cp -p block.t.php $RPM_BUILD_ROOT%{_smartyplugindir}
cp -p block.t.php $RPM_BUILD_ROOT%{_smarty3plugindir}
cp -p tsmarty2c.php $RPM_BUILD_ROOT%{_bindir}/tsmarty2c

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md ChangeLog.md
%attr(755,root,root) %{_bindir}/tsmarty2c
%{_smartyplugindir}/*.php

%files -n php-Smarty-plugin-gettext
%defattr(644,root,root,755)
%doc README.md ChangeLog.md
%attr(755,root,root) %{_bindir}/tsmarty2c
%{_smarty3plugindir}/*.php
