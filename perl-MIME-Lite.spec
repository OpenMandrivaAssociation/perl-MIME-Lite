%define upstream_name    MIME-Lite
%define upstream_version 3.027

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Low-calorie MIME generator 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MIME/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Email::Date)
BuildRequires:	perl(MIME::Types)
BuildRequires:	perl(Mail::Address)
BuildRequires:	perl(Email::Date::Format)
BuildRequires:	perl-devel
BuildRequires:	sendmail-command

BuildArch:	noarch

%description
MIME::Lite is intended as a simple, standalone module for generating
(not parsing!) MIME messages... specifically, it allows you to output a
simple, decent single- or multi-part message with text or binary
attachments. It does not require that you have the Mail:: or MIME::
modules installed. 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
chmod 644 README changes.pod lib/MIME/* examples/*
%__perl Makefile.PL INSTALLDIRS=vendor </dev/null
%make

%check
make test

%install
%makeinstall_std
rm -f %{buildroot}%{perl_vendorlib}/MIME/changes.pod

%files
%doc COPYING INSTALLING README changes.pod
%{perl_vendorlib}/MIME
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 3.27.0-4mdv2012.0
+ Revision: 765483
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 3.27.0-2
+ Revision: 667237
- mass rebuild

* Fri Nov 06 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 3.27.0-1mdv2010.1
+ Revision: 461326
- update to 3.027

* Fri Sep 18 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 3.26.0-1mdv2010.0
+ Revision: 444246
- update to 3.026

* Thu Aug 20 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 3.25.0-1mdv2010.0
+ Revision: 418410
- update to 3.025

* Sat Jan 17 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.024-1mdv2009.1
+ Revision: 330407
- update to new version 3.024

* Sat Nov 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.023-1mdv2009.1
+ Revision: 305749
- update to new version 3.023

* Mon Nov 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.022-1mdv2009.1
+ Revision: 299392
- update to new version 3.022

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 3.021-2mdv2009.0
+ Revision: 223820
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Dec 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.021-1mdv2008.1
+ Revision: 115163
- new version

* Thu Aug 30 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.020-1mdv2008.0
+ Revision: 75283
- update to new version 3.020

* Sun Aug 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.01-9mdv2008.0
+ Revision: 67063
- rebuild


* Tue Jul 11 2006 Guillaume Rousse <guillomovitch@mandriva.org> 3.01-8mdv2007.0
- %%mkrel
- spec cleanup
- better summary

* Wed Jun 29 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 3.01-7mdk
- Rebuild, cleanup, trim description

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 3.01-6mdk
- fix buildrequires in a backward compatible way

* Fri Jul 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 3.01-5mdk 
- rpmbuildupdate aware

* Wed Feb 25 2004 Guillaume Rousse <guillomovitch@mandrake.org> 3.01-4mdk
- fixed dir ownership (distlint)

* Fri Aug 15 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 3.01-3mdk
- rebuild for new perl
- use %%makeinstall_std macro

