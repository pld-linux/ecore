#
# Conditional build:
%bcond_without	static_libs	# don't build static library
%bcond_with	xcb		# XCB instead of Xlib
#
%define		_snap	20080813
%define		eet_ver	1.0.1

Summary:	Enlightened Core X interface library
Summary(pl.UTF-8):	Biblioteka interfejsu X Enlightened Core
Name:		ecore
Version:	0.9.9.044
Release:	0.%{_snap}.1
License:	BSD
Group:		X11/Libraries
Source0:	%{name}-%{version}-%{_snap}.tar.bz2
# Source0-md5:	d04c6ca6acfd6b05b81ac4d65b2f229b
URL:		http://enlightenment.org/p.php?p=about/libs/ecore
BuildRequires:	DirectFB-devel >= 0.9.16
BuildRequires:	SDL-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6
BuildRequires:	curl-devel
BuildRequires:	eet-devel >= %{eet_ver}
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
Requires:	eet-devel >= %{eet_ver}
Conflicts:	ecore-libs

%description config
Ecore Enlightened Property Library.

%description config -l pl.UTF-8
Biblioteka właściwości Ecore.

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

%package imf
Summary:	Ecore library IMF module
Summary(pl.UTF-8):	Moduł IMF biblioteki Ecore
Group:		Libraries
Requires:	%{name}-con = %{version}-%{release}
Conflicts:	ecore-libs

%description imf
Ecore library IMF module.

%description imf -l pl.UTF-8
Moduł IMF biblioteki Ecore.

%package imf-evas
Summary:	Ecore library IMF Evas module
Summary(pl.UTF-8):	Moduł IMF Evas biblioteki Ecore
Group:		Libraries
Requires:	%{name}-evas = %{version}-%{release}
Requires:	%{name}-imf = %{version}-%{release}
Conflicts:	ecore-libs

%description imf-evas
Ecore library IMF Evas module.

%description imf-evas -l pl.UTF-8
Moduł IMF Evas biblioteki Ecore.

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

%package sdl
Summary:	Ecore library SDL module
Summary(pl.UTF-8):	Moduł SDL biblioteki Ecore
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Conflicts:	ecore-libs

%description sdl
Ecore library SDL module.

%description sdl -l pl.UTF-8
Moduł SDL biblioteki Ecore.

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
Requires:	%{name}-desktop = %{version}-%{release}
Requires:	%{name}-directfb = %{version}-%{release}
# + DirectFB-devel >= 0.9.16
Requires:	%{name}-fb = %{version}-%{release}
# + tslib-devel
Requires:	%{name}-file = %{version}-%{release}
# + curl-devel
Requires:	%{name}-imf = %{version}-%{release}
Requires:	%{name}-ipc = %{version}-%{release}
Requires:	%{name}-job = %{version}-%{release}
Requires:	%{name}-sdl = %{version}-%{release}
# + sdl-devel
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

%package evas
Summary:	Ecore Evas Wrapper Library
Summary(pl.UTF-8):	Biblioteka Ecore Evas Wrapper
Group:		Libraries
#Requires:	%{name}-directfb = %{version}-%{release}
Requires:	%{name}-fb = %{version}-%{release}
Requires:	%{name}-sdl = %{version}-%{release}
Requires:	%{name}-x = %{version}-%{release}
Requires:	evas >= %{version}
Conflicts:	ecore-libs

%description evas
Ecore Evas Wrapper Library.

%description evas -l pl.UTF-8
Biblioteka Ecore Evas Wrapper.

%package evas-devel
Summary:	Header files for Ecore Evas Wrapper Library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteka Ecore Evas Wrapper
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-imf-evas = %{version}-%{release}
#Requires:	DirectFB-devel >= 0.9.16
Requires:	SDL-devel
Requires:	evas-devel >= %{version}
Requires:	tslib-devel

%description evas-devel
Header files for Ecore Evas Wrapper Library.

%description evas-devel -l pl.UTF-8
Pliki nagłówkowe biblioteka Ecore Evas Wrapper.

%package evas-static
Summary:	Static Ecore Evas Wrapper Library
Summary(pl.UTF-8):	Biblioteka statyczna Ecore Evas Wrapper
Group:		Development/Libraries
Requires:	%{name}-evas-devel = %{version}-%{release}

%description evas-static
Static Ecore Evas Wrapper Library.

%description evas-static -l pl.UTF-8
Biblioteka statyczna Ecore Evas Wrapper.

%prep
%setup -q -n %{name}-%{version}-%{_snap}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static} \
	--enable-ecore-con	\
	--enable-ecore-config	\
	--enable-ecore-desktop	\
	--enable-ecore-directfb	\
	--enable-ecore-fb	\
	--enable-ecore-file	\
	--enable-ecore-ipc	\
	--enable-ecore-job	\
	--enable-ecore-sdl	\
	--enable-ecore-txt	\
	--enable-ecore-x	\
	%{?with_xcb:--enable-ecore-x-xcb}	\
	--enable-ecore-evas	\
	--enable-ecore-evas-buffer \
	--disable-ecore-evas-dfb \
	--enable-ecore-evas-fb	\
	--enable-ecore-evas-sdl	\
	--enable-ecore-evas-xrender \
	--enable-curl		\
	--enable-inotify	\
	--enable-openssl	\
	--enable-poll

# --enable-ecore-evas-dfb needs evas-directfb (currently disabled)

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
%post	imf	-p /sbin/ldconfig
%postun	imf	-p /sbin/ldconfig
%post	imf-evas -p /sbin/ldconfig
%postun	imf-evas -p /sbin/ldconfig
%post	ipc	-p /sbin/ldconfig
%postun	ipc	-p /sbin/ldconfig
%post	job	-p /sbin/ldconfig
%postun	job	-p /sbin/ldconfig
%post	sdl	-p /sbin/ldconfig
%postun	sdl	-p /sbin/ldconfig
%post	txt	-p /sbin/ldconfig
%postun	txt	-p /sbin/ldconfig
%post	x	-p /sbin/ldconfig
%postun	x	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING COPYING-PLAIN README
%attr(755,root,root) %{_libdir}/libecore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore.so.0

%files con
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_con.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_con.so.0

%files config
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ecore_config
%attr(755,root,root) %{_libdir}/libecore_config.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_config.so.0

%files directfb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_directfb.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_directfb.so.0

%files desktop
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_desktop.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_desktop.so.0

%files fb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_fb.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_fb.so.0

%files file
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_file.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_file.so.0

%files imf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_imf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_imf.so.0

%files imf-evas
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_imf_evas.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_imf_evas.so.0

%files ipc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_ipc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_ipc.so.0

%files job
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_job.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_job.so.0

%files sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_sdl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_sdl.so.0

%files txt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_txt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_txt.so.0

%files x
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_x.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_x.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore.so
%{_libdir}/libecore.la
%{_includedir}/Ecore.h
%{_includedir}/Ecore_Data.h
%{_includedir}/Ecore_Str.h
%{_pkgconfigdir}/ecore.pc
# modules
%attr(755,root,root) %{_libdir}/libecore_con.so
%attr(755,root,root) %{_libdir}/libecore_config.so
%attr(755,root,root) %{_libdir}/libecore_directfb.so
%attr(755,root,root) %{_libdir}/libecore_desktop.so
%attr(755,root,root) %{_libdir}/libecore_fb.so
%attr(755,root,root) %{_libdir}/libecore_file.so
%attr(755,root,root) %{_libdir}/libecore_imf.so
%attr(755,root,root) %{_libdir}/libecore_ipc.so
%attr(755,root,root) %{_libdir}/libecore_job.so
%attr(755,root,root) %{_libdir}/libecore_sdl.so
%attr(755,root,root) %{_libdir}/libecore_txt.so
%attr(755,root,root) %{_libdir}/libecore_x.so
%{_libdir}/libecore_con.la
%{_libdir}/libecore_config.la
%{_libdir}/libecore_directfb.la
%{_libdir}/libecore_desktop.la
%{_libdir}/libecore_fb.la
%{_libdir}/libecore_file.la
%{_libdir}/libecore_imf.la
%{_libdir}/libecore_ipc.la
%{_libdir}/libecore_job.la
%{_libdir}/libecore_sdl.la
%{_libdir}/libecore_txt.la
%{_libdir}/libecore_x.la
%{_includedir}/Ecore_Con.h
%{_includedir}/Ecore_Config.h
%{_includedir}/Ecore_Desktop.h
%{_includedir}/Ecore_DirectFB.h
%{_includedir}/Ecore_Fb.h
%{_includedir}/Ecore_File.h
%{_includedir}/Ecore_IMF.h
%{_includedir}/Ecore_Ipc.h
%{_includedir}/Ecore_Job.h
%{_includedir}/Ecore_Sdl.h
%{_includedir}/Ecore_Txt.h
%{_includedir}/Ecore_X.h
%{_includedir}/Ecore_X_Atoms.h
%{_includedir}/Ecore_X_Cursor.h
%{_pkgconfigdir}/ecore-con.pc
%{_pkgconfigdir}/ecore-config.pc
%{_pkgconfigdir}/ecore-directfb.pc
%{_pkgconfigdir}/ecore-desktop.pc
%{_pkgconfigdir}/ecore-fb.pc
%{_pkgconfigdir}/ecore-file.pc
%{_pkgconfigdir}/ecore-imf.pc
%{_pkgconfigdir}/ecore-ipc.pc
%{_pkgconfigdir}/ecore-job.pc
%{_pkgconfigdir}/ecore-sdl.pc
%{_pkgconfigdir}/ecore-txt.pc
%{_pkgconfigdir}/ecore-x.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libecore.a
# modules
%{_libdir}/libecore_con.a
%{_libdir}/libecore_config.a
%{_libdir}/libecore_directfb.a
%{_libdir}/libecore_desktop.a
%{_libdir}/libecore_fb.a
%{_libdir}/libecore_file.a
%{_libdir}/libecore_imf.a
%{_libdir}/libecore_ipc.a
%{_libdir}/libecore_job.a
%{_libdir}/libecore_sdl.a
%{_libdir}/libecore_txt.a
%{_libdir}/libecore_x.a
%endif

%files evas
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_evas.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_evas.so.0

%files evas-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_evas.so
%{_libdir}/libecore_evas.la
%{_includedir}/Ecore_Evas.h
%{_pkgconfigdir}/ecore-evas.pc
# evas modules
%attr(755,root,root) %{_libdir}/libecore_imf_evas.so
%{_libdir}/libecore_imf_evas.la
%{_includedir}/Ecore_IMF_Evas.h
%{_pkgconfigdir}/ecore-imf-evas.pc

%files evas-static
%defattr(644,root,root,755)
%{_libdir}/libecore_evas.a
# evas modules
%{_libdir}/libecore_imf_evas.a
