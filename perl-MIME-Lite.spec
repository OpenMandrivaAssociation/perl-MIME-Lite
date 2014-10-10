%define modname	MIME-Lite
%define modver 3.030

Summary:	Low-calorie MIME generator 
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	4
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/MIME/MIME-Lite-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Email::Date)
BuildRequires:	perl(MIME::Types)
BuildRequires:	perl(Mail::Address)
BuildRequires:	perl(Email::Date::Format)
BuildRequires:	perl-devel
BuildRequires:	sendmail-command

%description
MIME::Lite is intended as a simple, standalone module for generating
(not parsing!) MIME messages... specifically, it allows you to output a
simple, decent single- or multi-part message with text or binary
attachments. It does not require that you have the Mail::	or MIME::
modules installed. 

%prep
%setup -qn %{modname}-%{modver}

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
%{_mandir}/man3/*



