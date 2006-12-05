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
BuildRequires:	DirectFB-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	evas-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXp-devel
BuildRequires:	xorg-lib-libXrandr-devel
Obsoletes:	ecore-libs
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

%package con
Summary:	Ecore Connection Library
Summary(pl):	Biblioteka po³±czeñ Ecore
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Conflicts:	ecore-libs

%description con
Ecore Connection Library.

%description con -l pl
Biblioteka po³±czeñ Ecore.

%package config
Summary:	Ecore Enlightened Property Library
Summary(pl):	Biblioteka w³a¶ciwo¶ci Ecore
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Conflicts:	ecore-libs

%description config
Ecore Enlightened Property Library.

%description config -l pl
Biblioteka w³a¶ciwo¶ci Ecore.

%package dbus
Summary:	Ecore DBus Library
Summary(pl):	Biblioteka Ecore DBus
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Conflicts:	ecore-libs

%description dbus
Ecore DBus Library.

%description dbus -l pl
Biblioteka Ecore DBus.

%package desktop
Summary:	Ecore freedesktop.org .desktop, icon, menu parsing Library
Summary(pl):	Biblioteka przetwarzania plików .desktop, ikon i menu
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Conflicts:	ecore-libs

%description desktop
Ecore freedesktop.org .desktop, icon, menu parsing Library.

%description desktop -l pl
Biblioteka przetwarzania plików .desktop, ikon i menu.

%package directfb
Summary:	Ecore frame buffer system functions
Summary(pl):	Funkcje systemowe framebuffera Ecore
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Conflicts:	ecore-libs

%description directfb
Ecore frame buffer system functions.

%description directfb -l pl
Funkcje systemowe framebuffera Ecore.

%package evas
Summary:	Ecore Evas Wrapper Library
Summary(pl):	Biblioteka Ecore Evas Wrapper
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Conflicts:	ecore-libs

%description evas
Ecore Evas Wrapper Library.

%description evas -l pl
Biblioteka Ecore Evas Wrapper.

%package fb
Summary:	Ecore frame buffer system functions
Summary(pl):	Funkcje systemowe framebuffera Ecore
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Conflicts:	ecore-libs

%description fb
Ecore frame buffer system functions.

%description fb -l pl
Funkcje systemowe framebuffera Ecore.

%package file
Summary:	Ecore File Library
Summary(pl):	Biblioteka Ecore File
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Conflicts:	ecore-libs

%description file
Ecore File Library.

%description file -l lp
Biblioteka Ecore File.

%package ipc
Summary:	Ecore inter-process communication functions
Summary(pl):	Funkcje komunikacji miêdzyprocesowej Ecore
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Conflicts:	ecore-libs

%description ipc
Ecore inter-process communication functions.

%description ipc -l pl
Funkcje komunikacji miêdzyprocesowej Ecore.

%package job
Summary:	Ecore job dealing functions
Summary(pl):	Funkcje obs³ugi zadañ Ecore
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Conflicts:	ecore-libs

%description job
Ecore job dealing functions.

%description job -l pl
Funkcje obs³ugi zadañ Ecore.

%package txt
Summary:	Ecore text encoding conversion functions
Summary(pl):	Funkcje konwersji kodowania tekstu Ecore
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Conflicts:	ecore-libs

%description txt
Ecore text encoding conversion functions.

%description txt -l pl
Funkcje konwersji kodowania tekstu Ecore.

%package x
Summary:	Ecore functions for dealing with the X Window System
Summary(pl):	Funkcje Ecore do obs³ugi X Window System
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Conflicts:	ecore-libs

%description x
Ecore functions for dealing with the X Window System.

%description x -l pl
Funkcje Ecore do obs³ugi X Window System.

%package devel
Summary:	Ecore header files
Summary(pl):	Pliki nag³ówkowe Ecore
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-con = %{version}-%{release}
Requires:	%{name}-config = %{version}-%{release}
Requires:	%{name}-dbus = %{version}-%{release}
Requires:	%{name}-desktop = %{version}-%{release}
Requires:	%{name}-directfb = %{version}-%{release}
Requires:	%{name}-evas = %{version}-%{release}
Requires:	%{name}-fb = %{version}-%{release}
Requires:	%{name}-file = %{version}-%{release}
Requires:	%{name}-ipc = %{version}-%{release}
Requires:	%{name}-job = %{version}-%{release}
Requires:	%{name}-txt = %{version}-%{release}
Requires:	%{name}-x = %{version}-%{release}
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
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
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
%doc AUTHORS COPYING COPYING-PLAIN INSTALL README
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
