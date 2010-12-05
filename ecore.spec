#
# Conditional build:
%bcond_without	static_libs	# don't build static library
%bcond_with	xcb		# XCB instead of Xlib (highly experimental)
#
Summary:	Enlightened Core X interface library
Summary(pl.UTF-8):	Biblioteka interfejsu X Enlightened Core
Name:		ecore
%define	subver	beta3
Version:	1.0.0
Release:	0.%{subver}.1
License:	BSD
Group:		X11/Libraries
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.%{subver}.tar.bz2
# Source0-md5:	34c13b29f675eaaea4b51b7b3963d7a1
URL:		http://enlightenment.org/p.php?p=about/libs/ecore
BuildRequires:	DirectFB-devel >= 0.9.16
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6
BuildRequires:	c-ares-devel
BuildRequires:	curl-devel
BuildRequires:	eina-devel >= 1.0.0
# for disabled config library
#BuildRequires:	eet-devel >= 1.4.0
BuildRequires:	evas-devel >= %{version}
BuildRequires:	gettext-devel >= 0.12.1
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gnutls-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	tslib-devel
%if %{with xcb}
BuildRequires:	libxcb-devel
BuildRequires:	xcb-util-devel
%else
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXp-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-lib-libXtst-devel
%endif
Requires:	eina >= 1.0.0
Obsoletes:	ecore-desktop
Obsoletes:	ecore-job
Obsoletes:	ecore-libs
Obsoletes:	ecore-txt
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

%description
Ecore is the event/X abstraction layer that makes doing selections,
Xdnd, general X stuff, event loops, timeouts and idle handlers fast,
optimized, and convenient. It's a separate library so anyone can make
use of the work put into Ecore to make this job easy for applications.

%description -l pl.UTF-8
Ecore to warstwa abstrakcji zdarzeń/X, która powoduje, że dokonywanie
zaznaczeń, Xdnd, ogólne operacje X, pętle zdarzeń, obsługa timeoutów i
bezczynności są szybkie, zoptymalizowane i wygodne. Jest to wydzielona
biblioteka, więc każdy może skorzystać z pracy włożonej w Ecore do
ułatwienia swojej pracy przy aplikacjach.

%package devel
Summary:	Header files for Ecore library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Ecore
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	eina-devel >= 1.0.0
Requires:	glib2-devel >= 2.0

%description devel
Header files for Ecore library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Ecore.

%package static
Summary:	Static Ecore library
Summary(pl.UTF-8):	Statyczna biblioteka Ecore
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Ecore library.

%description static -l pl.UTF-8
Statyczna biblioteka Ecore.

%package con
Summary:	Ecore Con(nection) library
Summary(pl.UTF-8):	Biblioteka połączeń Ecore Con
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description con
Ecore Con(nection) Library.

%description con -l pl.UTF-8
Biblioteka połączeń Ecore Con.

%package con-devel
Summary:	Header file for Ecore Con library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki Ecore Con
Group:		Development/Libraries
Requires:	%{name}-con = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	c-ares-devel
Requires:	curl-devel
Requires:	gnutls-devel

%description con-devel
Header file for Ecore Con(nection) library.

%description con-devel -l pl.UTF-8
Plik nagłówkowy biblioteki połączeń Ecore Con.

%package con-static
Summary:	Static Ecore Con library
Summary(pl.UTF-8):	Statyczna biblioteka Ecore Con
Group:		Development/Libraries
Requires:	%{name}-con-devel = %{version}-%{release}

%description con-static
Static Ecore Con(nection) library.

%description con-static -l pl.UTF-8
Statyczna biblioteka połączeń Ecore Con.

%package config
Summary:	Ecore Config library
Summary(pl.UTF-8):	Biblioteka właściwości Ecore Config
Group:		Libraries
Requires:	%{name}-ipc = %{version}-%{release}
Requires:	eet >= 1.4.0
Requires:	evas >= 1.0.0

%description config
Ecore Config library.

%description config -l pl.UTF-8
Biblioteka właściwości Ecore Config.

%package config-devel
Summary:	Header file for Ecore Config library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki Ecore Config
Group:		Development/Libraries
Requires:	%{name}-config = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-ipc-devel = %{version}-%{release}
Requires:	eet-devel >= 1.4.0
Requires:	evas-devel >= 1.0.0

%description config-devel
Header file for Ecore Config library.

%description config-devel -l pl.UTF-8
Plik nagłówkowy biblioteki właściwości Ecore Config.

%package config-static
Summary:	Static Ecore Config library
Summary(pl.UTF-8):	Statyczna biblioteka Ecore Config
Group:		Development/Libraries
Requires:	%{name}-config-devel = %{version}-%{release}

%description config-static
Static Ecore Config library.

%description config-static -l pl.UTF-8
Statyczna biblioteka właściwości Ecore Config.

%package directfb
Summary:	Ecore DirectFB (frame buffer system functions) library
Summary(pl.UTF-8):	Biblioteka Ecore DirectFB (funkcji systemowych framebuffera)
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	DirectFB >= 0.9.16

%description directfb
Ecore DirectFB (frame buffer system functions) library.

%description directfb -l pl.UTF-8
Biblioteka Ecore DirectFB (funkcji systemowych framebuffera).

%package directfb-devel
Summary:	Header file for Ecore DirectFB library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki Ecore DirectFB
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-directfb = %{version}-%{release}
Requires:	DirectFB-devel >= 0.9.16

%description directfb-devel
Header file for Ecore DirectFB (frame buffer system functions)
library.

%description directfb-devel -l pl.UTF-8
Plik nagłówkowy biblioteki Ecore DirectFB (funkcji systemowych
framebuffera).

%package directfb-static
Summary:	Static Ecore DirectFB library
Summary(pl.UTF-8):	Statyczna biblioteka Ecore DirectFB
Group:		Development/Libraries
Requires:	%{name}-directfb-devel = %{version}-%{release}

%description directfb-static
Static Ecore DirectFB (frame buffer system functions) library.

%description directfb-static -l pl.UTF-8
Statyczna biblioteka Ecore DirectFB (funkcji systemowych
framebuffera).

%package evas
Summary:	Ecore Evas library
Summary(pl.UTF-8):	Biblioteka Ecore Evas
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-directfb = %{version}-%{release}
Requires:	%{name}-fb = %{version}-%{release}
Requires:	%{name}-input = %{version}-%{release}
Requires:	%{name}-input-evas = %{version}-%{release}
Requires:	%{name}-sdl = %{version}-%{release}
Requires:	%{name}-x = %{version}-%{release}
Requires:	evas >= 1.0.0

%description evas
Ecore Evas library.

%description evas -l pl.UTF-8
Biblioteka Ecore Evas.

%package evas-devel
Summary:	Header file for Ecore Evas library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki Ecore Evas
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-directfb-devel = %{version}-%{release}
Requires:	%{name}-fb-devel = %{version}-%{release}
Requires:	%{name}-input-devel = %{version}-%{release}
Requires:	%{name}-input-evas-devel = %{version}-%{release}
Requires:	%{name}-sdl-devel = %{version}-%{release}
Requires:	%{name}-x-devel = %{version}-%{release}
Requires:	evas-devel >= 1.0.0

%description evas-devel
Header file for Ecore Evas library.

%description evas-devel -l pl.UTF-8
Plik nagłówkowy biblioteki Ecore Evas.

%package evas-static
Summary:	Static Ecore Evas library
Summary(pl.UTF-8):	Biblioteka statyczna Ecore Evas
Group:		Development/Libraries
Requires:	%{name}-evas-devel = %{version}-%{release}

%description evas-static
Static Ecore Evas library.

%description evas-static -l pl.UTF-8
Biblioteka statyczna Ecore Evas.

%package fb
Summary:	Ecore FB (frame buffer system functions) library
Summary(pl.UTF-8):	Biblioteka Ecore FB (funkcji systemowych framebuffera)
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description fb
Ecore FB (frame buffer system functions) library.

%description fb -l pl.UTF-8
Biblioteka Ecore FB (funkcji systemowych framebuffera).

%package fb-devel
Summary:	Header file for Ecore FB library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki Ecore FB
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-fb = %{version}-%{release}
Requires:	tslib-devel

%description fb-devel
Header file for Ecore FB (frame buffer system functions) library.

%description fb -l pl.UTF-8
Plik nagłówkowy biblioteki Ecore FB (funkcji systemowych
framebuffera).

%package fb-static
Summary:	Static Ecore FB library
Summary(pl.UTF-8):	Statyczna biblioteka Ecore FB
Group:		Development/Libraries
Requires:	%{name}-fb-devel = %{version}-%{release}

%description fb-static
Static Ecore FB (frame buffer system functions) library.

%description fb-static -l pl.UTF-8
Statyczna biblioteka Ecore FB (funkcji systemowych framebuffera).

%package file
Summary:	Ecore File library
Summary(pl.UTF-8):	Biblioteka Ecore File
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-con = %{version}-%{release}

%description file
Ecore File library.

%description file -l pl.UTF-8
Biblioteka Ecore File.

%package file-devel
Summary:	Header file for Ecore File library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki Ecore File
Group:		Development/Libraries
Requires:	%{name}-con-devel = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-file = %{version}-%{release}

%description file-devel
Header file for Ecore File library.

%description file-devel -l pl.UTF-8
Plik nagłówkowy biblioteki Ecore File.

%package file-static
Summary:	Static Ecore File library
Summary(pl.UTF-8):	Statyczna biblioteka Ecore File
Group:		Development/Libraries
Requires:	%{name}-file-devel = %{version}-%{release}

%description file-static
Static Ecore File library.

%description file-static -l pl.UTF-8
Statyczna biblioteka Ecore File.

%package imf
Summary:	Ecore IMF library
Summary(pl.UTF-8):	Biblioteka Ecore IMF
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description imf
Ecore IMF library.

%description imf -l pl.UTF-8
Biblioteka Ecore IMF.

%package imf-devel
Summary:	Header file for Ecore IMF library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki Ecore IMF
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-imf = %{version}-%{release}

%description imf-devel
Header file for Ecore IMF library.

%description imf-devel -l pl.UTF-8
Plik nagłówkowy biblioteki Ecore IMF.

%package imf-static
Summary:	Static Ecore IMF library
Summary(pl.UTF-8):	Statyczna biblioteka Ecore IMF
Group:		Development/Libraries
Requires:	%{name}-imf-devel = %{version}-%{release}

%description imf-static
Static Ecore IMF library.

%description imf-static -l pl.UTF-8
Statyczna biblioteka Ecore IMF.

%package imf-evas
Summary:	Ecore IMF Evas library
Summary(pl.UTF-8):	Biblioteka Ecore IMF Evas
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-imf = %{version}-%{release}
Requires:	evas >= 1.0.0

%description imf-evas
Ecore IMF Evas library.

%description imf-evas -l pl.UTF-8
Biblioteka Ecore IMF Evas.

%package imf-evas-devel
Summary:	Header file for Ecore IMF Evas library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki Ecore IMF Evas
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-imf-devel = %{version}-%{release}
Requires:	%{name}-imf-evas = %{version}-%{release}
Requires:	evas-devel >= 1.0.0

%description imf-evas-devel
Header file for Ecore IMF Evas library.

%description imf-evas-devel -l pl.UTF-8
Plik nagłówkowy biblioteki Ecore IMF Evas.

%package imf-evas-static
Summary:	Static Ecore IMF Evas library
Summary(pl.UTF-8):	Statyczna biblioteka Ecore IMF Evas
Group:		Development/Libraries
Requires:	%{name}-imf-evas-devel = %{version}-%{release}

%description imf-evas-static
Static Ecore IMF Evas library.

%description imf-evas-static -l pl.UTF-8
Statyczna biblioteka Ecore IMF Evas.

%package input
Summary:	Ecore Input library
Summary(pl.UTF-8):	Biblioteka Ecore Input
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description input
Ecore Input library.

%description input -l pl.UTF-8
Biblioteka Ecore Input.

%package input-devel
Summary:	Header file for Ecore Input library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki Ecore Input
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-input = %{version}-%{release}

%description input-devel
Header file for Ecore Input library.

%description input-devel -l pl.UTF-8
Plik nagłówkowy biblioteki Ecore Input.

%package input-static
Summary:	Static Ecore Input library
Summary(pl.UTF-8):	Statyczna biblioteka Ecore Input
Group:		Development/Libraries
Requires:	%{name}-input-devel = %{version}-%{release}

%description input-static
Static Ecore Input library.

%description input-static -l pl.UTF-8
Statyczna biblioteka Ecore Input.

%package input-evas
Summary:	Ecore Input Evas extension library
Summary(pl.UTF-8):	Biblioteka rozszerzenia Ecore Input Evas
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-input = %{version}-%{release}
Requires:	evas >= 1.0.0

%description input-evas
Ecore Input Evas extension library.

%description input-evas -l pl.UTF-8
Biblioteka rozszerzenia Ecore Input Evas.

%package input-evas-devel
Summary:	Header file for Ecore Input Evas extension library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki rozszerzenia Ecore Input Evas
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-input-devel = %{version}-%{release}
Requires:	evas-devel >= 1.0.0

%description input-evas-devel
Header file for Ecore Input Evas extension library.

%description input-evas-devel -l pl.UTF-8
Plik nagłówkowy biblioteki rozszerzenia Ecore Input Evas.

%package input-evas-static
Summary:	Static Ecore Input Evas extension library
Summary(pl.UTF-8):	Statyczna biblioteka rozszerzenia Ecore Input Evas
Group:		Libraries
Requires:	%{name}-input-evas-devel = %{version}-%{release}

%description input-evas-static
Static Ecore Input Evas extension library.

%description input-evas-static -l pl.UTF-8
Statyczna biblioteka rozszerzenia Ecore Input Evas.

%package ipc
Summary:	Ecore IPC (inter-process communication functions) library
Summary(pl.UTF-8):	Biblioteka Ecore IPC (funkcji komunikacji międzyprocesowej)
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-con = %{version}-%{release}

%description ipc
Ecore IPC (inter-process communication functions) library.

%description ipc -l pl.UTF-8
Biblioteka Ecore IPC (funkcji komunikacji międzyprocesowej).

%package ipc-devel
Summary:	Header file for Ecore IPC library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki Ecore IPC
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-ipc = %{version}-%{release}

%description ipc-devel
Header file for Ecore IPC (inter-process communication functions)
library.

%description ipc-devel -l pl.UTF-8
Plik nagłówkowy biblioteki Ecore IPC (funkcji komunikacji
międzyprocesowej).

%package ipc-static
Summary:	Static Ecore IPC library
Summary(pl.UTF-8):	Statyczna biblioteka Ecore IPC
Group:		Development/Libraries
Requires:	%{name}-ipc-devel = %{version}-%{release}

%description ipc-static
Static Ecore IPC (inter-process communication functions) library.

%description ipc-static -l pl.UTF-8
Statyczna biblioteka Ecore IPC (funkcji komunikacji międzyprocesowej).

%package sdl
Summary:	Ecore SDL library
Summary(pl.UTF-8):	Biblioteka Ecore SDL
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-input = %{version}-%{release}

%description sdl
Ecore SDL library.

%description sdl -l pl.UTF-8
Biblioteka Ecore SDL.

%package sdl-devel
Summary:	Header file for Ecore SDL library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki Ecore SDL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-input-devel = %{version}-%{release}
Requires:	SDL-devel >= 1.2.0

%description sdl-devel
Header file for Ecore SDL library.

%description sdl-devel -l pl.UTF-8
Plik nagłówkowy biblioteki Ecore SDL.

%package sdl-static
Summary:	Static Ecore SDL library
Summary(pl.UTF-8):	Statyczna biblioteka Ecore SDL
Group:		Development/Libraries
Requires:	%{name}-sdl-devel = %{version}-%{release}

%description sdl-static
Static Ecore SDL library.

%description sdl-static -l pl.UTF-8
Statyczna biblioteka Ecore SDL.

%package x
Summary:	Ecore X (functions for dealing with the X Window System) library
Summary(pl.UTF-8):	Biblioteka Ecore X (funkcji do obsługi X Window System)
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-input = %{version}-%{release}

%description x
Ecore X (functions for dealing with the X Window System) library.

%description x -l pl.UTF-8
Biblioteka Ecore X (funkcji do obsługi X Window System).

%package x-devel
Summary:	Header files for Ecore X library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Ecore X
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-input-devel = %{version}-%{release}
Requires:	%{name}-x = %{version}-%{release}
%if %{with xcb}
Requires:	libxcb-devel
Requires:	xcb-util-devel
%else
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXScrnSaver-devel
Requires:	xorg-lib-libXcomposite-devel
Requires:	xorg-lib-libXcursor-devel
Requires:	xorg-lib-libXdamage-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXfixes-devel
Requires:	xorg-lib-libXi-devel
Requires:	xorg-lib-libXinerama-devel
Requires:	xorg-lib-libXp-devel
Requires:	xorg-lib-libXrandr-devel
Requires:	xorg-lib-libXrender-devel
Requires:	xorg-lib-libXtst-devel
%endif

%description x-devel
Header files for Ecore X (functions for dealing with the X Window
System) library.

%description x-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Ecore X (funkcji do obsługi X Window
System).

%package x-static
Summary:	Static Ecore X library
Summary(pl.UTF-8):	Statyczna biblioteka Ecore X
Group:		Development/Libraries
Requires:	%{name}-x-devel = %{version}-%{release}

%description x-static
Static Ecore X (functions for dealing with the X Window System)
library.

%description x-static -l pl.UTF-8
Statyczna biblioteka Ecore X (funkcji do obsługi X Window System).

%prep
%setup -q -n %{name}-%{version}.%{subver}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static} \
	--enable-ecore-con	\
	--enable-ecore-directfb	\
	--enable-ecore-fb	\
	--enable-ecore-file	\
	--enable-ecore-ipc	\
	--enable-ecore-sdl	\
	--enable-ecore-x	\
	%{?with_xcb:--enable-ecore-x-xcb}	\
	--enable-ecore-evas	\
	--enable-ecore-evas-fb	\
	--enable-cares		\
	--enable-curl		\
	--enable-inotify	\
	--enable-openssl	\
	--enable-poll

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%post	con	-p /sbin/ldconfig
%postun	con	-p /sbin/ldconfig
%post	config	-p /sbin/ldconfig
%postun	config	-p /sbin/ldconfig
%post	directfb -p /sbin/ldconfig
%postun	directfb -p /sbin/ldconfig
%post	evas	-p /sbin/ldconfig
%postun	evas	-p /sbin/ldconfig
%post	fb	-p /sbin/ldconfig
%postun	fb	-p /sbin/ldconfig
%post	file	-p /sbin/ldconfig
%postun	file	-p /sbin/ldconfig
%post	imf	-p /sbin/ldconfig
%postun	imf	-p /sbin/ldconfig
%post	imf-evas -p /sbin/ldconfig
%postun	imf-evas -p /sbin/ldconfig
%post	input	-p /sbin/ldconfig
%postun	input	-p /sbin/ldconfig
%post	input-evas -p /sbin/ldconfig
%postun	input-evas -p /sbin/ldconfig
%post	ipc	-p /sbin/ldconfig
%postun	ipc	-p /sbin/ldconfig
%post	sdl	-p /sbin/ldconfig
%postun	sdl	-p /sbin/ldconfig
%post	x	-p /sbin/ldconfig
%postun	x	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libecore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore.so
%{_libdir}/libecore.la
%dir %{_includedir}/ecore-1
%{_includedir}/ecore-1/Ecore.h
%{_includedir}/ecore-1/Ecore_Getopt.h
%{_pkgconfigdir}/ecore.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libecore.a
%endif

%files con
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_con.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_con.so.1

%files con-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_con.so
%{_libdir}/libecore_con.la
%{_includedir}/ecore-1/Ecore_Con.h
%{_pkgconfigdir}/ecore-con.pc

%if %{with static_libs}
%files con-static
%defattr(644,root,root,755)
%{_libdir}/libecore_con.a
%endif

%if 0
%files config
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ecore_config
%attr(755,root,root) %{_libdir}/libecore_config.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_config.so.1

%files config-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_config.so
%{_libdir}/libecore_config.la
%{_includedir}/ecore-1/Ecore_Config.h
%{_pkgconfigdir}/ecore-config.pc

%if %{with static_libs}
%files config-static
%defattr(644,root,root,755)
%{_libdir}/libecore_config.a
%endif
%endif

%files directfb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_directfb.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_directfb.so.1

%files directfb-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_directfb.so
%{_libdir}/libecore_directfb.la
%{_includedir}/ecore-1/Ecore_DirectFB.h
%{_pkgconfigdir}/ecore-directfb.pc

%if %{with static_libs}
%files directfb-static
%defattr(644,root,root,755)
%{_libdir}/libecore_directfb.a
%endif

%files evas
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_evas.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_evas.so.1

%files evas-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_evas.so
%{_libdir}/libecore_evas.la
%{_includedir}/ecore-1/Ecore_Evas.h
%{_pkgconfigdir}/ecore-evas.pc

%if %{with static_libs}
%files evas-static
%defattr(644,root,root,755)
%{_libdir}/libecore_evas.a
%endif

%files fb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_fb.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_fb.so.1

%files fb-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_fb.so
%{_libdir}/libecore_fb.la
%{_includedir}/ecore-1/Ecore_Fb.h
%{_pkgconfigdir}/ecore-fb.pc

%if %{with static_libs}
%files fb-static
%defattr(644,root,root,755)
%{_libdir}/libecore_fb.a
%endif

%files file
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_file.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_file.so.1

%files file-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_file.so
%{_libdir}/libecore_file.la
%{_includedir}/ecore-1/Ecore_File.h
%{_pkgconfigdir}/ecore-file.pc

%if %{with static_libs}
%files file-static
%defattr(644,root,root,755)
%{_libdir}/libecore_file.a
%endif

%files imf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_imf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_imf.so.1

%files imf-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_imf.so
%{_libdir}/libecore_imf.la
%{_includedir}/ecore-1/Ecore_IMF.h
%{_pkgconfigdir}/ecore-imf.pc

%if %{with static_libs}
%files imf-static
%defattr(644,root,root,755)
%{_libdir}/libecore_imf.a
%endif

%files imf-evas
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_imf_evas.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_imf_evas.so.1

%files imf-evas-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_imf_evas.so
%{_libdir}/libecore_imf_evas.la
%{_includedir}/ecore-1/Ecore_IMF_Evas.h
%{_pkgconfigdir}/ecore-imf-evas.pc

%if %{with static_libs}
%files imf-evas-static
%defattr(644,root,root,755)
%{_libdir}/libecore_imf_evas.a
%endif

%files input
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_input.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_input.so.1

%files input-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_input.so
%{_libdir}/libecore_input.la
%{_includedir}/ecore-1/Ecore_Input.h
%{_pkgconfigdir}/ecore-input.pc

%if %{with static_libs}
%files input-static
%defattr(644,root,root,755)
%{_libdir}/libecore_input.a
%endif

%files input-evas
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_input_evas.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_input_evas.so.1

%files input-evas-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_input_evas.so
%{_libdir}/libecore_input_evas.la
%{_includedir}/ecore-1/Ecore_Input_Evas.h
%{_pkgconfigdir}/ecore-input-evas.pc

%if %{with static_libs}
%files input-evas-static
%defattr(644,root,root,755)
%{_libdir}/libecore_input_evas.a
%endif

%files ipc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_ipc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_ipc.so.1

%files ipc-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_ipc.so
%{_libdir}/libecore_ipc.la
%{_includedir}/ecore-1/Ecore_Ipc.h
%{_pkgconfigdir}/ecore-ipc.pc

%if %{with static_libs}
%files ipc-static
%defattr(644,root,root,755)
%{_libdir}/libecore_ipc.a
%endif

%files sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_sdl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_sdl.so.1

%files sdl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_sdl.so
%{_libdir}/libecore_sdl.la
%{_includedir}/ecore-1/Ecore_Sdl.h
%{_pkgconfigdir}/ecore-sdl.pc

%if %{with static_libs}
%files sdl-static
%defattr(644,root,root,755)
%{_libdir}/libecore_sdl.a
%endif

%files x
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_x.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_x.so.1

%files x-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_x.so
%{_libdir}/libecore_x.la
%{_includedir}/ecore-1/Ecore_X.h
%{_includedir}/ecore-1/Ecore_X_Atoms.h
%{_includedir}/ecore-1/Ecore_X_Cursor.h
%{_pkgconfigdir}/ecore-x.pc

%if %{with static_libs}
%files x-static
%defattr(644,root,root,755)
%{_libdir}/libecore_x.a
%endif
