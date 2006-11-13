Summary:	Program to send (Nagios) alerts via jabber
Summary(pl):	Program do wysy�ania alarm�w (Nagiosa) przez jabbera
Name:		nagios-alert-jabber
Version:	1.1
Release:	1
License:	GPL
Group:		Networking
Source0:	nagios-jabber.alert
Requires:	cyrus-sasl-plain
Requires:	python-M2Crypto
Requires:	python-pyxmpp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/nagios

%description
nagios-jabber.alert is a program to send Nagios (or other)
notifications over jabber protocol.

%description -l pl
nagios-jabber.alert to program do wysy�ania powiadomie� Nagiosa (lub
innych) po protokole jabber.

%prep
%setup -q -c -T
install %{SOURCE0} .
cat <<'EOF' > jabber-notify.ini
; jabber id and password for jabber-notify script
[jabber_id@example.org]
jid = jid@example.org
password = PASSWORD
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_sysconfdir}}
install nagios-jabber.alert $RPM_BUILD_ROOT%{_sbindir}/nagios-notify-jabber
cp -a jabber-notify.ini $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/jabber-notify.ini
%attr(755,root,root) %{_sbindir}/nagios-notify-jabber
