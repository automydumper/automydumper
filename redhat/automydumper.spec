Name: automydumper	
Version: 1.3.1
Release: 1
Summary: Mydumper-based MySQL backups
BuildRoot: %{_tmppath}/%{name}-root
Group: Applications/System
License: GPL
BuildArch: noarch
URL: https://github.com/automydumper/automydumper
Packager: Bart Verwilst <bart@verwilst.be>
Source0: automydumper-%{version}.tar.gz

Requires: bash, mydumper

%description
MySQL/Percona/Mariadb backup tool based on Mydumper.

%prep
%setup -q
%build

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}/usr/bin
mkdir -p ${RPM_BUILD_ROOT}/etc
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man8
mkdir -p ${RPM_BUILD_ROOT}/usr/share/doc/automydumper/examples
mkdir -p ${RPM_BUILD_ROOT}/usr/share/doc/automydumper/examples/post.d
mkdir -p ${RPM_BUILD_ROOT}/var/backups/automydumper
mkdir -p ${RPM_BUILD_ROOT}/usr/share/automydumper/pre.d
mkdir -p ${RPM_BUILD_ROOT}/usr/share/automydumper/post.d
install -m 755 automydumper ${RPM_BUILD_ROOT}%{_bindir}
install -m 640 automydumper.cfg ${RPM_BUILD_ROOT}/etc/automydumper.cfg
install -m 644 debian/man/automydumper.8 ${RPM_BUILD_ROOT}%{_mandir}/man8
install -m 755 examples/post.d/* ${RPM_BUILD_ROOT}/usr/share/doc/automydumper/examples/post.d

%files
%doc
%attr(755,root,root) %{_bindir}/automydumper
%config(noreplace) /etc/automydumper.cfg
%{_mandir}/man8/*
%{_docdir}/automydumper/*
/var/backups/automydumper
/usr/share/automydumper/pre.d
/usr/share/automydumper/post.d

%changelog
* Mon Mar 22 2021 Bart Verwilst <bart@verwilst.be>
- New URL
- Increment version
* Mon Mar 21 2016 Bart Verwilst <bart@verwilst.be>
- Initial release

