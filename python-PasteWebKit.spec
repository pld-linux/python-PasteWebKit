%define		module PasteWebKit
Summary:	A port/reimplementation of Webware WebKit in WSGI and Paste
Name:		python-%{module}
Version:	0.9
Release:	1
Group:		Development/Languages/Python
License:	X11/MIT
Source0: 	http://cheeseshop.python.org/packages/source/P/PasteWebKit/%{module}-%{version}.tar.gz
# Source0-md5:	73381dab3b895f8d3f1bcd1ccc7f09dc
URL:		http://pythonpaste.org/webkit/
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

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
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
