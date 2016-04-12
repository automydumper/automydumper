Name: automydumper	
Version: 1.0.1
Release: 1
Summary: Mydumper-based MySQL backups	
BuildRoot: %{_tmppath}/%{name}-root
Group: Applications/System
License: GPL	
URL: http://automydumper.org
Packager: Bart Verwilst <bart@verwilst.be>
Source0: automydumper-%{version}.tar.gz

Requires: bash, mydumper >= 0.9	

%description
MySQL/Mariadb backup tool based on Mydumper.

%prep
%setup -q
%build


%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}/usr/bin
mkdir -p ${RPM_BUILD_ROOT}/etc/default
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man8
install -m 755 automydumper ${RPM_BUILD_ROOT}%{_bindir}
install -m 640 debian/defaults ${RPM_BUILD_ROOT}/etc/default/automydumper
install -m 644 debian/man/automydumper.8 ${RPM_BUILD_ROOT}%{_mandir}/man8

%files
%doc
%attr(755,root,root) %{_bindir}/automydumper
%config /etc/default/automydumper
%{_mandir}/man8/*

#%changelog
#* Mon Mar 21 2016 Bart Verwilst <bart@verwilst.be>
#- Initial release

