%define module  MIME-Lite
%define name    perl-%{module}
%define version 3.020
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Low-calorie MIME generator 
License:        GPL or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/MIME/%{module}-%{version}.tar.bz2
BuildRequires:  perl(Email::Date)
BuildRequires:  perl(MIME::Types)
BuildRequires:  perl(Mail::Address)
BuildRequires:  sendmail-command
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
MIME::Lite is intended as a simple, standalone module for generating
(not parsing!) MIME messages... specifically, it allows you to output a
simple, decent single- or multi-part message with text or binary
attachments. It does not require that you have the Mail:: or MIME::
modules installed. 

%prep
%setup -q -n %{module}-%{version}

%build
chmod 644 README changes.pod lib/MIME/* examples/*
%{__perl} Makefile.PL INSTALLDIRS=vendor </dev/null
%make

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%{perl_vendorlib}/MIME/changes.pod

%files
%defattr(-,root,root)
%doc COPYING INSTALLING README changes.pod
%{perl_vendorlib}/MIME
%{_mandir}/*/*

