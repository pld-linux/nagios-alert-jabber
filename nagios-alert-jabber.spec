Summary:	Program to send (Nagios) alerts via jabber
Name:		nagios-alert-jabber
Version:	1.0
Release:	0.1
License:	GPL
Group:		Networking
Source0:	nagios-jabber.alert
# Source0-md5:	bee229fc60f7536f854d8f10f7f553f4
Requires:	python-pyxmpp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nagios-jabber.alert is a program to send Nagios (or other)
notifications over jabber protocol.

%prep
%setup -q -c -T
install %{SOURCE0} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install nagios-jabber.alert $RPM_BUILD_ROOT%{_bindir}/nagios-jabber.alert

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
