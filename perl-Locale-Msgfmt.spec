#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Locale-Msgfmt
Version  : 0.15
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/A/AZ/AZAWAWI/Locale-Msgfmt-0.15.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AZ/AZAWAWI/Locale-Msgfmt-0.15.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libl/liblocale-msgfmt-perl/liblocale-msgfmt-perl_0.15-2.debian.tar.xz
Summary  : 'Compile .po files to .mo files'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Locale-Msgfmt-man
Requires: perl(Module::Install::DSL)
BuildRequires : perl(Module::Install::DSL)

%description
Locale-Msgfmt
Locale::Msgfmt is a pure Perl reimplementation of msgfmt from GNU
gettext-tools.

%package man
Summary: man components for the perl-Locale-Msgfmt package.
Group: Default

%description man
man components for the perl-Locale-Msgfmt package.


%prep
tar -xf %{SOURCE1}
cd ..
%setup -q -n Locale-Msgfmt-0.15
mkdir -p %{_topdir}/BUILD/Locale-Msgfmt-0.15/deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Locale-Msgfmt-0.15/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/Locale/Msgfmt.pm
/usr/lib/perl5/site_perl/5.26.1/Locale/Msgfmt/Utils.pm
/usr/lib/perl5/site_perl/5.26.1/Locale/Msgfmt/mo.pm
/usr/lib/perl5/site_perl/5.26.1/Locale/Msgfmt/po.pm
/usr/lib/perl5/site_perl/5.26.1/Module/Install/Msgfmt.pm

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/Locale::Msgfmt.3
/usr/share/man/man3/Locale::Msgfmt::Utils.3
/usr/share/man/man3/Locale::Msgfmt::mo.3
/usr/share/man/man3/Locale::Msgfmt::po.3
