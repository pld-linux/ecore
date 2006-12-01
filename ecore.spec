#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Enlightened Core X interface library
Summary(pl):	Biblioteka interfejsu X Enlightened Core
Name:		ecore
Version:	0.9.9.036
Release:	1
License:	BSD
Group:		X11/Libraries
Source0:	http://enlightenment.freedesktop.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	b2f3ba94aa47a885c77c3ad7a686ee42
URL:		http://enlightenment.org/Libraries/Ecore/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	evas-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

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

%package libs
Summary:	Ecore library
Summary(pl):	Biblioteka ecore
Group:		X11/Libraries

%description libs
Ecore library.

%description libs -l pl
Biblioteka ecore.

%package devel
Summary:	Ecore header files
Summary(pl):	Pliki nag³ówkowe Ecore
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	curl-devel
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

%build
%configure \
	%{!?with_static_libs:--disable-static} \
	--enable-ecore-txt	\
	--enable-ecore-x	\
	--enable-ecore-job	\
	--enable-ecore-fb	\
	--enable-ecore-evas	\
	--enable-ecore-evas-gl	\
	--enable-ecore-evas-xrender \
	--enable-ecore-evas-dfb	\
	--enable-ecore-evas-fb	\
	--enable-ecore-evas-buffer \
	--enable-ecore-con	\
	--enable-openssl	\
	--enable-ecore-ipc	\
	--enable-ecore-dbus	\
	--enable-ecore-config	\
	--enable-ecore-file	\
	--enable-inotify	\
	--enable-poll		\
	--enable-curl		\
	--enable-pthreads

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post libs	-p /sbin/ldconfig
%postun libs	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING COPYING-PLAIN INSTALL README
%attr(755,root,root) %{_bindir}/ecore_config

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore.so.*.*.*
%attr(755,root,root) %{_libdir}/libecore_con.so.*.*.*
%attr(755,root,root) %{_libdir}/libecore_config.so.*.*.*
%attr(755,root,root) %{_libdir}/libecore_dbus.so.*.*.*
%attr(755,root,root) %{_libdir}/libecore_directfb.so.*.*.*
%attr(755,root,root) %{_libdir}/libecore_desktop.so.*.*.*
%attr(755,root,root) %{_libdir}/libecore_evas.so.*.*.*
%attr(755,root,root) %{_libdir}/libecore_fb.so.*.*.*
%attr(755,root,root) %{_libdir}/libecore_file.so.*.*.*
%attr(755,root,root) %{_libdir}/libecore_ipc.so.*.*.*
%attr(755,root,root) %{_libdir}/libecore_job.so.*.*.*
%attr(755,root,root) %{_libdir}/libecore_txt.so.*.*.*
%attr(755,root,root) %{_libdir}/libecore_x.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ecore-config
%attr(755,root,root) %{_libdir}/libecore*.so
%{_libdir}/libecore*.la
%{_pkgconfigdir}/ecore.pc
%{_aclocaldir}/ecore.m4
%{_includedir}/Ecore*.h

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libecore*.a
%endif
