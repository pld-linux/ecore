#
# Conditional build:
%bcond_without	static_libs	# don't build static library
%bcond_with	xcb		# XCB instead of Xlib
#
Summary:	Enlightened Core X interface library
Summary(pl.UTF-8):	Biblioteka interfejsu X Enlightened Core
Name:		ecore
Version:	0.9.9.038
Release:	1
License:	BSD
Group:		X11/Libraries
Source0:	http://enlightenment.freedesktop.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	a391c19e01c08b6591cc30f85c597ed2
Patch0:		%{name}-tslib.patch
Patch1:		%{name}-link.patch
URL:		http://enlightenment.org/Libraries/Ecore/
BuildRequires:	DirectFB-devel >= 0.9.16
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	eet-devel >= 0.9.10.038
BuildRequires:	evas-devel >= %{version}
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	tslib-devel
%if %{with xcb}
BuildRequires:	libxcb-devel
BuildRequires:	xcb-util-devel
%else
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXp-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXrender-devel
%endif
Requires:	evas >= %{version}
Obsoletes:	ecore-libs
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

%package con
Summary:	Ecore Connection Library
Summary(pl.UTF-8):	Biblioteka połączeń Ecore
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Conflicts:	ecore-libs

%description con
Ecore Connection Library.

%description con -l pl.UTF-8
Biblioteka połączeń Ecore.

%package config
Summary:	Ecore Enlightened Property Library
Summary(pl.UTF-8):	Biblioteka właściwości Ecore
Group:		Libraries
Requires:	%{name}-ipc = %{version}-%{release}
Requires:	evas-devel >= %{version}
Requires:	eet-devel >= 0.9.10.038
Conflicts:	ecore-libs

%description config
Ecore Enlightened Property Library.

%description config -l pl.UTF-8
Biblioteka właściwości Ecore.

%package dbus
Summary:	Ecore DBus Library
Summary(pl.UTF-8):	Biblioteka Ecore DBus
Group:		Libraries
Requires:	%{name}-con = %{version}-%{release}
Conflicts:	ecore-libs

%description dbus
Ecore DBus Library.

%description dbus -l pl.UTF-8
Biblioteka Ecore DBus.

%package desktop
Summary:	Ecore freedesktop.org .desktop, icon, menu parsing Library
Summary(pl.UTF-8):	Biblioteka przetwarzania plików .desktop, ikon i menu
Group:		X11/Libraries
Requires:	%{name}-file = %{version}-%{release}
Conflicts:	ecore-libs

%description desktop
Ecore freedesktop.org .desktop, icon, menu parsing Library.

%description desktop -l pl.UTF-8
Biblioteka przetwarzania plików .desktop, ikon i menu.

%package directfb
Summary:	Ecore frame buffer system functions
Summary(pl.UTF-8):	Funkcje systemowe framebuffera Ecore
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	DirectFB >= 0.9.16
Conflicts:	ecore-libs

%description directfb
Ecore frame buffer system functions.

%description directfb -l pl.UTF-8
Funkcje systemowe framebuffera Ecore.

%package evas
Summary:	Ecore Evas Wrapper Library
Summary(pl.UTF-8):	Biblioteka Ecore Evas Wrapper
Group:		Libraries
Requires:	%{name}-directfb = %{version}-%{release}
Requires:	%{name}-fb = %{version}-%{release}
Requires:	%{name}-x = %{version}-%{release}
Requires:	evas >= %{version}
Conflicts:	ecore-libs

%description evas
Ecore Evas Wrapper Library.

%description evas -l pl.UTF-8
Biblioteka Ecore Evas Wrapper.

%package fb
Summary:	Ecore frame buffer system functions
Summary(pl.UTF-8):	Funkcje systemowe framebuffera Ecore
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Conflicts:	ecore-libs

%description fb
Ecore frame buffer system functions.

%description fb -l pl.UTF-8
Funkcje systemowe framebuffera Ecore.

%package file
Summary:	Ecore File Library
Summary(pl.UTF-8):	Biblioteka Ecore File
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Conflicts:	ecore-libs

%description file
Ecore File Library.

%description file -l pl.UTF-8
Biblioteka Ecore File.

%package ipc
Summary:	Ecore inter-process communication functions
Summary(pl.UTF-8):	Funkcje komunikacji międzyprocesowej Ecore
Group:		Libraries
Requires:	%{name}-con = %{version}-%{release}
Conflicts:	ecore-libs

%description ipc
Ecore inter-process communication functions.

%description ipc -l pl.UTF-8
Funkcje komunikacji międzyprocesowej Ecore.

%package job
Summary:	Ecore job dealing functions
Summary(pl.UTF-8):	Funkcje obsługi zadań Ecore
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Conflicts:	ecore-libs

%description job
Ecore job dealing functions.

%description job -l pl.UTF-8
Funkcje obsługi zadań Ecore.

%package txt
Summary:	Ecore text encoding conversion functions
Summary(pl.UTF-8):	Funkcje konwersji kodowania tekstu Ecore
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Conflicts:	ecore-libs

%description txt
Ecore text encoding conversion functions.

%description txt -l pl.UTF-8
Funkcje konwersji kodowania tekstu Ecore.

%package x
Summary:	Ecore functions for dealing with the X Window System
Summary(pl.UTF-8):	Funkcje Ecore do obsługi X Window System
Group:		X11/Libraries
Requires:	%{name}-txt = %{version}-%{release}
Conflicts:	ecore-libs

%description x
Ecore functions for dealing with the X Window System.

%description x -l pl.UTF-8
Funkcje Ecore do obsługi X Window System.

%package devel
Summary:	Ecore header files
Summary(pl.UTF-8):	Pliki nagłówkowe Ecore
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-con = %{version}-%{release}
# + openssl-devel curl-devel
Requires:	%{name}-config = %{version}-%{release}
# + eet-devel >= 0.9.10.038
Requires:	%{name}-dbus = %{version}-%{release}
Requires:	%{name}-desktop = %{version}-%{release}
Requires:	%{name}-directfb = %{version}-%{release}
# + DirectFB-devel >= 0.9.16
Requires:	%{name}-evas = %{version}-%{release}
# + evas-devel >= %{version}
Requires:	%{name}-fb = %{version}-%{release}
# + tslib-devel
Requires:	%{name}-file = %{version}-%{release}
# + curl-devel
Requires:	%{name}-ipc = %{version}-%{release}
Requires:	%{name}-job = %{version}-%{release}
Requires:	%{name}-txt = %{version}-%{release}
Requires:	%{name}-x = %{version}-%{release}
%if %{with xcb}
# + libxcb-devel xcb-util-devel
%else
# + xorg-lib-libXScrnSaver-devel xorg-lib-libXcursor-devel xorg-lib-libXdamage-devel xorg-lib-libXext-devel xorg-lib-libXfixes-devel xorg-lib-libXinerama-devel xorg-lib-libXp-devel xorg-lib-libXrandr-devel xorg-lib-libXrender-devel
%endif

%description devel
Ecore development files.

%description devel -l pl.UTF-8
Pliki programistyczne Ecore.

%package static
Summary:	Static Ecore libraries
Summary(pl.UTF-8):	Statyczne biblioteki Ecore
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Ecore libraries.

%description static -l pl.UTF-8
Statyczne biblioteki Ecore.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static} \
	--enable-ecore-txt	\
	--enable-ecore-x	\
	%{?with_xcb:--enable-ecore-x-xcb}	\
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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%post	con	-p /sbin/ldconfig
%postun	con	-p /sbin/ldconfig
%post	config	-p /sbin/ldconfig
%postun	config	-p /sbin/ldconfig
%post	dbus	-p /sbin/ldconfig
%postun	dbus	-p /sbin/ldconfig
%post	directfb -p /sbin/ldconfig
%postun	directfb -p /sbin/ldconfig
%post	desktop	-p /sbin/ldconfig
%postun	desktop	-p /sbin/ldconfig
%post	evas	-p /sbin/ldconfig
%postun	evas	-p /sbin/ldconfig
%post	fb	-p /sbin/ldconfig
%postun	fb	-p /sbin/ldconfig
%post	file	-p /sbin/ldconfig
%postun	file	-p /sbin/ldconfig
%post	ipc	-p /sbin/ldconfig
%postun	ipc	-p /sbin/ldconfig
%post	job	-p /sbin/ldconfig
%postun	job	-p /sbin/ldconfig
%post	txt	-p /sbin/ldconfig
%postun	txt	-p /sbin/ldconfig
%post	x	-p /sbin/ldconfig
%postun	x	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING COPYING-PLAIN README
%attr(755,root,root) %{_libdir}/libecore.so.*.*.*

%files con
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_con.so.*.*.*

%files config
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ecore_config
%attr(755,root,root) %{_libdir}/libecore_config.so.*.*.*

%files dbus
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_dbus.so.*.*.*

%files directfb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_directfb.so.*.*.*

%files desktop
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_desktop.so.*.*.*

%files evas
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_evas.so.*.*.*

%files fb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_fb.so.*.*.*

%files file
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_file.so.*.*.*

%files ipc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_ipc.so.*.*.*

%files job
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_job.so.*.*.*

%files txt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_txt.so.*.*.*

%files x
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_x.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ecore-config
%attr(755,root,root) %{_libdir}/libecore.so
%{_libdir}/libecore.la
%{_includedir}/Ecore.h
%{_pkgconfigdir}/ecore.pc
# modules
%attr(755,root,root) %{_libdir}/libecore_*.so
%{_libdir}/libecore_*.la
%{_includedir}/Ecore_*.h
%{_pkgconfigdir}/ecore-*.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libecore.a
# modules
%{_libdir}/libecore_*.a
%endif
