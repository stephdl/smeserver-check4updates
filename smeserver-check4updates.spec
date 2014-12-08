
Summary: smeserver - check updates of external repositories
%define name smeserver-check4updates
Name: %{name}
%define version 0.0.2
%define release 1 
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
Requires: e-smith-base
Requires: smeserver-release >= 8
BuildRequires: e-smith-devtools
BuildArchitectures: noarch

%description
A rpm to check updates of external repositories

%changelog
* Tue Dec 9 2014 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.2-1.sme
- Added an exclude list of rpm

* Mon Dec 8 2014 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.1-1.sme
- Initial release to sme8

%prep
%setup

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
  /sbin/e-smith/genfilelist \
    --file /sbin/e-smith/check4repositoriesupdates 'attr(0750,root,root)' \
  $RPM_BUILD_ROOT > %{name}-%{version}-%{release}-filelist
echo "%doc COPYING" >> %{name}-%{version}-%{release}-filelist

%postun

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)

