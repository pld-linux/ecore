Summary:	Enlightened Core X interface library
Name:		ecore
Version:	1.0.0
#%define _pre	pre7
%define	_snap	20050106
Release:	0.%{_snap}.0.1
License:	BSD
Group:		X11/Libraries
#Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}_%{_pre}.tar.gz
Source0:	ftp://ftp.sparky.homelinux.org/pub/e17/%{name}-%{version}-%{_snap}.tar.gz
# Source0-md5:	97ca7567fcaeb72cae779d08f8c0e527
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	evas-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ecore is the event/X abstraction layer that makes doing selections,
Xdnd, general X stuff, event loops, timeouts and idle handlers fast,
optimized, and convenient. It's a separate library so anyone can make
use of the work put into Ecore to make this job easy for applications.

%package devel
Summary:	Ecore headers and development libraries
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	evas-devel
Requires:	openssl-devel

%description devel
Ecore development files.

%package static
Summary:	Static libraries
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libraries.

%prep
#%%setup -q -n %{name}-%{version}_%{_pre}
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING* README*
%attr(755,root,root) %{_libdir}/libecore*.so.*
%attr(755,root,root) %{_bindir}/ecore_*
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ecore-config
%attr(755,root,root) %{_libdir}/libecore*.so
%{_libdir}/libecore*.la
%attr(755,root,root) %{_libdir}/ecore_config_ipc_*.so
%{_libdir}/ecore_config_ipc_*.la
%{_pkgconfigdir}/ecore.pc
%{_aclocaldir}/ecore.m4
%{_includedir}/Ecore*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libecore*.a
%{_libdir}/ecore_config_ipc_*.a
