%define upstream_name    MIME-Lite
%define upstream_version 3.027

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:    Low-calorie MIME generator 
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/MIME/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(Email::Date)
BuildRequires:  perl(MIME::Types)
BuildRequires:  perl(Mail::Address)
BuildRequires:  perl(Email::Date::Format)
BuildRequires:  sendmail-command

BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

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
