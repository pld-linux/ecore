Summary:	Enlightened Core X interface library
Summary(pl):	Biblioteka interfejsu X Enlightened Core
Name:		ecore
Version:	0.9.9.018
Release:	1
License:	BSD
Group:		X11/Libraries
Source0:	http://enlightenment.freedesktop.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	1b138060711920ff76808a8ff75d0017
Patch0:		%{name}-missing_m4.patch
URL:		http://enlightenment.org/Libraries/Ecore/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	evas-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
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
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
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
	--enable-ecore-dbus	\
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
%doc AUTHORS COPYING COPYING-PLAIN INSTALL README
%attr(755,root,root) %{_bindir}/ecore_*
%attr(755,root,root) %{_libdir}/libecore*.so.*.*.*
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ecore-config
%attr(755,root,root) %{_libdir}/libecore*.so
%{_libdir}/libecore*.la
%{_pkgconfigdir}/ecore.pc
%{_aclocaldir}/ecore.m4
%{_includedir}/Ecore*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libecore*.a
