# TODO pl summary, eng,pl description
Summary:	Captures Postfix configuration for reporting errors
Summary(pl):	-
Name:		postfinger
Version:	1.30
Release:	0.1
Epoch:		0
License:	GPL v2
Group:		Applications
Source0:	http://ftp.wl0.org/postfinger/%{name}-%{version}
# Source0-md5:	7ae1d8089869e6b883c3b338939df27d
URL:		http://ftp.wl0.org/postfinger/
Requires:	postfix
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%setup -q

%build
cp ../SOURCES/%{name}-%{version} %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
install postfinger $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/postfinger
