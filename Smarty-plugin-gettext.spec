%define		subver	b1
%define		rel		11
%include	/usr/lib/rpm/macros.php
%define		php_min_version 5.2.1
Summary:	Gettext support for Smarty
Summary(pl.UTF-8):	Obsługa gettexta dla systemu Smarty
Name:		Smarty-plugin-gettext
Version:	1.0
Release:	0.%{subver}.%{rel}
License:	LGPL v2+
Group:		Development/Languages/PHP
Source0:	http://downloads.sourceforge.net/smarty-gettext/smarty-gettext-%{version}%{subver}.tgz
# Source0-md5:	3795d4ce1a391e8eace9bd2adb5b1abb
Source1:	http://bazaar.launchpad.net/~eventum-developers/eventum/trunk/download/head%3A/tsmarty2c-20091105141507-sh36mrwjgo63hzxk-1/tsmarty2c
# Source1-md5:	589fd057a8dec5ee9796849885bb93c4
URL:		http://smarty.incutio.com/?page=SmartyGettext
BuildRequires:	rpm-php-pearprov
BuildRequires:	sed >= 4.0
Requires:	Smarty >= 2.6.10-4
Requires:	php(core) >= %{php_min_version}
Requires:	php(gettext)
Provides:	smarty-gettext = %{version}-%{release}
Obsoletes:	smarty-gettext
Obsoletes:	smarty-gettext-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_smartyplugindir	%{_datadir}/php/Smarty/plugins

%description
smarty-gettext provides gettext support for Smarty, the popular PHP
templating engine <http://smarty.php.net/>.

%description -l pl.UTF-8
smarty-gettext dodaje obsługę gettexta do systemu Smarty - popularnego
silnika szablonów dla PHP - <http://smarty.php.net/>.

%prep
%setup -q -n smarty-gettext-%{version}%{subver}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_smartyplugindir},%{_bindir}}
cp -a block.t.php $RPM_BUILD_ROOT%{_smartyplugindir}
install -p %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/tsmarty2c

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/tsmarty2c
%{_smartyplugindir}/*.php
