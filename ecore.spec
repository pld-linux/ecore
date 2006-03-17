#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Enlightened Core X interface library
Summary(pl):	Biblioteka interfejsu X Enlightened Core
Name:		ecore
Version:	0.9.9.025
Release:	1
License:	BSD
Group:		X11/Libraries
Source0:	http://enlightenment.freedesktop.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	c3a6f4392896defa4a768a13817e38d8
URL:		http://enlightenment.org/Libraries/Ecore/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	evas-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	%{name}-libs = %{version}-%{release}
Requires:	fonts-TTF-bitstream-vera
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
sed -e 's/^@BUILD_ECORE_DIRECTFB_TRUE@/#/'	\
    -e 's/^@BUILD_ECORE_DIRECTFB_FALSE@//'	\
    -i src/lib/ecore_directfb/Makefile.in	\
       src/lib/ecore_evas/Makefile.in

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
	--disable-ecore-evas-dfb	\
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

cd $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts
VERA=$(ls Vera*.ttf)
for FONT in $VERA; do
	rm -f $FONT
	ln -s %{_fontsdir}/TTF/$FONT .
done

%clean
rm -rf $RPM_BUILD_ROOT

%post libs	-p /sbin/ldconfig
%postun libs	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING COPYING-PLAIN INSTALL README
%attr(755,root,root) %{_bindir}/ecore_*
%{_datadir}/%{name}

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore*.so.*.*.*

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
