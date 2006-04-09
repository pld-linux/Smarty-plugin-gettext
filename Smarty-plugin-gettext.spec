%define		_beta b1
%define		_rel 1
Summary:	Gettext support for Smarty
Name:		smarty-gettext
Version:	1.0
Release:	0.%{_beta}.%{_rel}
License:	LGPL v2+
Group:		Development/Languages/PHP
Source0:	http://dl.sourceforge.net/smarty-gettext/%{name}-%{version}%{_beta}.tgz
# Source0-md5:	3795d4ce1a391e8eace9bd2adb5b1abb
URL:		http://smarty.incutio.com/?page=SmartyGettext
BuildRequires:	sed >= 4.0
Requires:	Smarty >= 2.6.10-4
Requires:	php-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_smartyplugindir	%{_datadir}/php/Smarty/plugins

%description
smarty-gettext provides gettext support for Smarty, the popular PHP
templating engine <http://smarty.php.net/>.

%prep
%setup -q -n %{name}-%{version}%{_beta}
%{__sed} -i -e '1s,#!.*php,#!%{_bindir}/php,' tsmarty2c.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_smartyplugindir},%{_bindir}}

install block.t.php $RPM_BUILD_ROOT%{_smartyplugindir}
install tsmarty2c.php $RPM_BUILD_ROOT%{_bindir}/tsmarty2c

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{_smartyplugindir}/*.php
%attr(755,root,root) %{_bindir}/tsmarty2c
