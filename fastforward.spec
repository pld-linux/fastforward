Summary:	Fast Forward (TCP and UDP) Proxy for Linux
Summary(pl):	Fast Forward - proxy TCP i UDP dla Linuksa
Name:		fastforward
Version:	1.00
Release:	5
License:	LGPL
Group:		Networking/Daemons
Source0:	http://open.nit.ca/download/%{name}-%{version}.tar.gz
# Source0-md5:	62dc7241eee4c3538d4a242be2aea435
Patch0:		%{name}-opt.patch
Patch1:		%{name}-includes.patch
Patch2:		%{name}-types.patch
Patch3:		%{name}-gcc3.patch
URL:		http://open.nit.ca/fastforward/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fast Forward belongs to a class of programs known as proxy servers.
Its job is to accept TCP or UDP connections on one address and port,
and forward them off to some other address and port. There are lots of
programs around that do this, but Fast Forward provides simplified
configuration, uses less memory, and is generally faster than any
other solution we know of. It uses zero-forking technology to keep its
resource usage to a minimum while still running faster than most other
proxies.

%description -l pl
Fast Forward nale¿y do grupy programów znanych jako serwery proxy.
Jego zadanie to przyjmowanie po³±czeñ TCP lub UDP na jednym adresie i
porcie oraz przekazywanie ich na inny adres i port. Jest wiele
programów realizuj±cych to samo zadanie, ale Fast Forward ma
uproszczon± konfiguracjê, u¿ywa ma³o pamiêci i jest szybszy. Nie
forkuje siê, aby zminimalizowaæ zu¿ycie zasobów.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	COPTS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install fastforward/fastforward $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/*
