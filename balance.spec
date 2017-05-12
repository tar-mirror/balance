Summary: TCP load-balancing proxy server
Name: balance
Version: 3.34
Release: 1
Group: Networking/Daemons
Source: http://www.inlab.de/%{name}-%{version}.tar.gz
Copyright: Proprietary
BuildRoot: %{_tmppath}/%{name}-buildroot

%define strip_binaries 1
%define gzip_man 1
%define  __prefix /usr

Prefix: %{__prefix}

%description
Balance is a simple but powerful generic tcp proxy with round robin
load balancing and failover mechanisms.  The program behaviour can
be controlled at runtime using a simple command line syntax. 

%prep
%setup 
%build

make CFLAGS="$RPM_OPT_FLAGS"
	
%install
[ "${RPM_BUILD_ROOT}" != "/" ] && /bin/rm -rf ${RPM_BUILD_ROOT}
mkdir -p $RPM_BUILD_ROOT/usr/sbin
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT/var/run/balance
chmod 1777 $RPM_BUILD_ROOT/var/run/balance
install -m 755 -s balance $RPM_BUILD_ROOT/usr/sbin/balance
install -m 644 balance.1 $RPM_BUILD_ROOT%{_mandir}/man1/balance.1

%if %{strip_binaries}
{ cd $RPM_BUILD_ROOT
  strip .%{__prefix}/sbin/balance || /bin/true
}
%if %{gzip_man}
{ cd $RPM_BUILD_ROOT
  gzip .%{_mandir}/man1/balance.1
}
%endif

%clean
[ "${RPM_BUILD_ROOT}" != "/" ] && /bin/rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc README COPYING
%{__prefix}/sbin/balance
%{_mandir}/man1/balance.1.gz
%dir /var/run/balance

%changelog
* Sat Mar 18 2006 T.Obermair > 3.34 
- update version

* Wed Oct 19 2005 T.Obermair > 3.28 
- update version

* Fri Oct 31 2003 Bojan Smojver <bojan at rexursive dot com> 3.11-1 
- update version

* Mon Sep  22 2003 Thomas Steudten <thomas at steudten dot com> 3.10-2 
- rebuild
- fix/expand specfile
