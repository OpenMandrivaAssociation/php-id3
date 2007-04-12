%define modname id3
%define dirname %{modname}
%define soname %{modname}.so
%define inifile A14_%{modname}.ini

Summary:	Functions to read and write ID3 tags in MP3 files
Name:		php-%{modname}
Version:	0.2
Release:	%mkrel 9
Group:		Development/PHP
URL:		http://pecl.php.net/package/id3
License:	PHP License
Source0:	id3-%{version}.tar.bz2
BuildRequires:	php-devel >= 3:5.2.0
Provides:	php5-id3
Obsoletes:	php5-id3
Epoch:		1
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
id3 enables to to retrieve and update information from ID3 tags in MP3 files.
It supports version 1.0 and version 1.1.

%prep

%setup -q -n id3-%{version}
[ "../package.xml" != "/" ] && mv ../package.xml .

%build

phpize
%configure2_5x --with-libdir=%{_lib} \
    --with-%{modname}=shared,%{_prefix}

%make
mv modules/*.so .

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot} 

install -d %{buildroot}%{_libdir}/php/extensions
install -d %{buildroot}%{_sysconfdir}/php.d

install -m755 %{soname} %{buildroot}%{_libdir}/php/extensions/

cat > %{buildroot}%{_sysconfdir}/php.d/%{inifile} << EOF
extension = %{soname}
EOF

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc examples CREDITS EXPERIMENTAL TODO package.xml
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/php.d/%{inifile}
%attr(0755,root,root) %{_libdir}/php/extensions/%{soname}


