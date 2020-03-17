#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Locale-Msgfmt
Version  : 0.15
Release  : 13
URL      : https://cpan.metacpan.org/authors/id/A/AZ/AZAWAWI/Locale-Msgfmt-0.15.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AZ/AZAWAWI/Locale-Msgfmt-0.15.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libl/liblocale-msgfmt-perl/liblocale-msgfmt-perl_0.15-2.debian.tar.xz
Summary  : 'Compile .po files to .mo files'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Locale-Msgfmt-license = %{version}-%{release}
Requires: perl-Locale-Msgfmt-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Install::DSL)

%description
Locale-Msgfmt
Locale::Msgfmt is a pure Perl reimplementation of msgfmt from GNU
gettext-tools.

%package dev
Summary: dev components for the perl-Locale-Msgfmt package.
Group: Development
Provides: perl-Locale-Msgfmt-devel = %{version}-%{release}
Requires: perl-Locale-Msgfmt = %{version}-%{release}

%description dev
dev components for the perl-Locale-Msgfmt package.


%package license
Summary: license components for the perl-Locale-Msgfmt package.
Group: Default

%description license
license components for the perl-Locale-Msgfmt package.


%package perl
Summary: perl components for the perl-Locale-Msgfmt package.
Group: Default
Requires: perl-Locale-Msgfmt = %{version}-%{release}

%description perl
perl components for the perl-Locale-Msgfmt package.


%prep
%setup -q -n Locale-Msgfmt-0.15
cd %{_builddir}
tar xf %{_sourcedir}/liblocale-msgfmt-perl_0.15-2.debian.tar.xz
cd %{_builddir}/Locale-Msgfmt-0.15
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Locale-Msgfmt-0.15/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Locale-Msgfmt
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Locale-Msgfmt/ffd6a5ea3cafbd9dbbd9ab11a831de183d860ac8
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Locale::Msgfmt.3
/usr/share/man/man3/Locale::Msgfmt::Utils.3
/usr/share/man/man3/Locale::Msgfmt::mo.3
/usr/share/man/man3/Locale::Msgfmt::po.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Locale-Msgfmt/ffd6a5ea3cafbd9dbbd9ab11a831de183d860ac8

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.2/Locale/Msgfmt.pm
/usr/lib/perl5/vendor_perl/5.30.2/Locale/Msgfmt/Utils.pm
/usr/lib/perl5/vendor_perl/5.30.2/Locale/Msgfmt/mo.pm
/usr/lib/perl5/vendor_perl/5.30.2/Locale/Msgfmt/po.pm
/usr/lib/perl5/vendor_perl/5.30.2/Module/Install/Msgfmt.pm
