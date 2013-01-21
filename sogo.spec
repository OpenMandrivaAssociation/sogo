%define beta %nil
%define scmrev %nil
# Apparently we can't create debug packages for objective-c
%define debug_package %nil

Name: sogo
Version: 2.0.3a
%if "%scmrev" == ""
%if "%beta" != ""
Release: 0.%beta.1
%else
Release: 1
%endif
Source: http://www.sogo.nu/files/downloads/SOGo/Sources/SOGo-%version%beta.tar.gz
%else
Release: 0.%scmrev.1ark
Source: SOGo-%scmrev.tar.xz
%endif
Summary: The SOGo groupware server
URL: http://sogo.nu/
License: GPL/LGPL v2+
Group: System/Servers
BuildRequires: gnustep-make >= 2.6.2-3
BuildRequires: gnustep-base-devel gnustep-gui-devel
BuildRequires: gcc-objc sope-devel
BuildRequires: pkgconfig(libmemcached)

%description
SOGo is fully supported and trusted groupware server with a focus
on scalability and open standards.
SOGo is released under the GNU GPL/LGPL v2 and above.

SOGo provides a rich AJAX-based Web interface and supports multiple
native clients through the use of standard protocols such as CalDAV,
CardDAV and GroupDAV.

SOGo is the missing component of your infrastructure; it sits in the
middle of your servers to offer your users a uniform and complete
interface to access their information. It has been deployed in
production environments where thousands of users are involved.

%package devel
Summary: Development files for SOGo
Group: Development/C
Requires: %name = %version-%release

%description devel
Development files for SOGo -- needed if you wish to develop
or compile SOGo plugins.

%track
prog sogo = {
	version = %{version}
	url = http://www.sogo.nu/downloads/backend.html
	regex = SOGo-(__VER__)\.tar\.gz
}

%prep
%setup -q -n SOGo-%version
# Not autoconf, even though it looks similar
# Not actually %_prefix/System -- the bogus configure script translates
# that to "GNUstep System installation"
./configure --prefix=%_prefix/System

%build
make %?_smp_mflags

%install
rm -rf $RPM_BUILD_ROOT
make %?_smp_mflags install DESTDIR="$RPM_BUILD_ROOT" GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%files
%_sbindir/*
%_libdir/*.so*
%_libdir/GNUstep/WOxElemBuilders-4.9
%_libdir/GNUstep/SaxMappings
%_libdir/GNUstep/SaxDrivers-4.9
%_libdir/GNUstep/SOGo
%_libdir/GNUstep/OCSTypeModels
%_libdir/GNUstep/Libraries/Resources/NGCards
%_libdir/GNUstep/Frameworks/SOGo.framework
%exclude %_libdir/GNUstep/Frameworks/*/Versions/*/Headers

%files devel
%_includedir/NGCards
%_includedir/SOGo
%_includedir/SOGoUI
%_includedir/GDLContentStore
%_libdir/GNUstep/Frameworks/*/Versions/*/Headers
