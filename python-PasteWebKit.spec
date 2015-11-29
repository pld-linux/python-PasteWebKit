%define		module PasteWebKit
Summary:	A port/reimplementation of Webware WebKit in WSGI and Paste
Summary(pl.UTF-8):	Port/reimplementacja WebKitu Webware w WSGI i Paste
Name:		python-%{module}
Version:	1.0
Release:	5
Group:		Libraries/Python
License:	X11/MIT
Source0: 	http://cheeseshop.python.org/packages/source/P/PasteWebKit/%{module}-%{version}.tar.gz
# Source0-md5:	3f06815a43eebf4672143b4e29021a57
URL:		http://pythonpaste.org/webkit/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python-devel
BuildRequires:	python-setuptools >= 0.6-0.a9.1
%pyrequires_eq	python-modules
Requires:	python-Paste
Requires:	python-PasteDeploy
Requires:	python-PasteScript
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a reimplementation of the Webware API, using Paste for most of
the functionality, and just providing an API wrapper.

While the basic layout of applications is different from what
Webware's MakeAppWorkDir creates, this is intended to be backward
compatible for most typical Webware applications.

%description -l pl.UTF-8
To jest reimplementacja API Webware przy użyciu Paste dla większości
funkcjonalności, z udostępnieniem zwykłego obudowania API.

O ile podstawowy wygląd aplikacji jest różny od tworzonego przez
MakeAppWorkDir w Webware, powinien być wstecznie kompatybilny z
większością typowych aplikacji Webware.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install \
	--single-version-externally-managed \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/
%{py_sitescriptdir}/paste*
%{py_sitescriptdir}/Paste*
