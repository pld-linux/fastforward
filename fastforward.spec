Summary:	Fast Forward (TCP and UDP) Proxy for Linux
Summary(pl.UTF-8):	Fast Forward - proxy TCP i UDP dla Linuksa
Name:		fastforward
Version:	1.01
Release:	0.1
License:	LGPL
Group:		Networking/Daemons
Source0:	http://open.nit.ca/download/%{name}-%{version}.tar.gz
# Source0-md5:	ba8f9614b99f57b7914d32c01ea34dd3
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

%description -l pl.UTF-8
Fast Forward należy do grupy programów znanych jako serwery proxy.
Jego zadanie to przyjmowanie połączeń TCP lub UDP na jednym adresie i
porcie oraz przekazywanie ich na inny adres i port. Jest wiele
programów realizujących to samo zadanie, ale Fast Forward ma
uproszczoną konfigurację, używa mało pamięci i jest szybszy. Nie
forkuje się, aby zminimalizować zużycie zasobów.

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
