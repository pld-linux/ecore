Summary:	Enlightened Core X interface library
Summary(pl):	Biblioteka interfejsu X Enlightened Core
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

%description -l pl
Ecore to warstwa abstracji zdarze�/X, kt�ra powoduje, �e dokonywanie
zaznacze�, Xdnd, og�lne operacje X, p�tle zdarze�, obs�uga timeout�w i
bezczynno�ci s� szybkie, zoptymalizowane i wygodne. Jest to wydzielona
biblioteka, wi�c ka�dy mo�e skorzysta� z pracy w�o�onej w Ecore do
u�atwienia swojej pracy przy aplikacjach.

%package devel
Summary:	Ecore header files
Summary(pl):	Pliki nag��wkowe Ecore
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	evas-devel
Requires:	openssl-devel

%description devel
Ecore development files.

%description devel -l pl
Pliki programistyczne Ecore.

%package static
Summary:	Static Ecore libraries
Summary(pl):	Statyczne biblioteki Ecore
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Ecore libraries.

%description static -l pl
Statyczne biblioteki Ecore.

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
%attr(755,root,root) %{_bindir}/ecore_*
%attr(755,root,root) %{_libdir}/libecore*.so.*.*.*
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
