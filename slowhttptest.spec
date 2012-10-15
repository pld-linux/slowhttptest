Summary:	Application Layer DoS attack simulator
Name:		slowhttptest
Version:	1.5
Release:	1
License:	Apache v2.0
Group:		Applications/Networking
Source0:	https://slowhttptest.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	1437fdac96e99305f765a7f0b075b006
URL:		https://code.google.com/p/slowhttptest/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SlowHTTPTest is a highly configurable tool that simulates some
Application Layer Denial of Service attacks.

It implements most common low-bandwidth Application Layer DoS attacks,
such as slowloris, Slow HTTP POST, Slow Read attack (based on TCP
persist timer exploit) by draining concurrent connections pool, as
well as Apache Range Header attack by causing very significant memory
and CPU usage on the server.

Slowloris and Slow HTTP POST DoS attacks rely on the fact that the
HTTP protocol, by design, requires requests to be completely received
by the server before they are processed. If an HTTP request is not
complete, or if the transfer rate is very low, the server keeps its
resources busy waiting for the rest of the data. If the server keeps
too many resources busy, this creates a denial of service. This tool
is sending partial HTTP requests, trying to get denial of service from
target HTTP server.

Slow Read DoS attack aims the same resources as slowloris and slow
POST, but instead of prolonging the request, it sends legitimate HTTP
request and reads the response slowly.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/slowhttptest
%{_mandir}/man1/slowhttptest.1*
