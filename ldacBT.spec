Summary:	AOSP libldac dispatcher
Summary(pl.UTF-8):	Biblioteka libldac ekspediująca AOSP
Name:		ldacBT
Version:	2.0.2.3
Release:	1
License:	Apache v2.0
Group:		Libraries
#Source0Download: https://github.com/EHfive/ldacBT/releases
Source0:	https://github.com/EHfive/ldacBT/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	697e40bba3e4bdca93157b13f6d8451e
URL:		https://github.com/EHfive/ldacBT
BuildRequires:	cmake >= 3.0
BuildRequires:	gcc >= 5:3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AOSP libldac dispatcher.

%description -l pl.UTF-8
Biblioteka libldac ekspediująca AOSP.

%package devel
Summary:	Header files for ldacBT libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek ldacBT
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for ldacBT libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek ldacBT.

%prep
%setup -q -n %{name}

%build
install -d build
cd build
%cmake .. \
	-DINSTALL_LIBDIR=%{_libdir} \
	-DLDAC_SOFT_FLOAT=OFF

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md libldac/NOTICE
%attr(755,root,root) %{_libdir}/libldacBT_abr.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libldacBT_abr.so.2
%attr(755,root,root) %{_libdir}/libldacBT_enc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libldacBT_enc.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libldacBT_abr.so
%attr(755,root,root) %{_libdir}/libldacBT_enc.so
%{_includedir}/ldac
%{_pkgconfigdir}/ldacBT-abr.pc
%{_pkgconfigdir}/ldacBT-enc.pc
