Summary:	Enlightened Core X interface library
Summary(pl):	Biblioteka interfejsu X Enlightened Core
Name:		ecore
Version:	0.9.9
%define	_snap	20050329
Release:	0.%{_snap}.0.1
License:	BSD
Group:		X11/Libraries
#Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}_%{_pre}.tar.gz
Source0:	ftp://ftp.sparky.homelinux.org/pub/e17/%{name}-%{_snap}.tar.gz
# Source0-md5:	6d27d042591ab19c4877b6f1355756d1
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
Ecore to warstwa abstracji zdarzeñ/X, która powoduje, ¿e dokonywanie
zaznaczeñ, Xdnd, ogólne operacje X, pêtle zdarzeñ, obs³uga timeoutów i
bezczynno¶ci s± szybkie, zoptymalizowane i wygodne. Jest to wydzielona
biblioteka, wiêc ka¿dy mo¿e skorzystaæ z pracy w³o¿onej w Ecore do
u³atwienia swojej pracy przy aplikacjach.

%package devel
Summary:	Ecore header files
Summary(pl):	Pliki nag³ówkowe Ecore
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
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-ecore-txt	\
	--enable-ecore-x	\
	--enable-ecore-job	\
	--enable-ecore-fb	\
	--enable-ecore-evas	\
	--enable-ecore-evas-gl	\
	--enable-ecore-evas-fb	\
	--enable-ecore-evas-buffer \
	--enable-ecore-con	\
	--enable-openssl	\
	--enable-ecore-ipc	\
	--enable-ecore-config	\
	--enable-ecore-file	\
	--enable-pthreads

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
