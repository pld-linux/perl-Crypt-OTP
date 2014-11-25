#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"

%define		pdir	Crypt
%define		pnam	OTP
%include	/usr/lib/rpm/macros.perl
Summary:	Crypt::OTP Perl module - OTP encryption method implementation
Summary(pl.UTF-8):	Moduł Perla Crypt::OTP - implementacja kodowania metodą OTP
Name:		perl-Crypt-OTP
Version:	2.00
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	af841dbb3641f73ee4048b15e6b56197
URL:		http://search.cpan.org/dist/Crypt-OTP/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The One Time Pad encryption method is very simple, and impossible to
crack without the actual pad file against which the to-be-encrypted
message is XOR'ed. Encryption and decryption are performed using
exactly the same method, and the message will decrypt correctly only
if the same pad is used in decryption as was use in encryption.

%description -l pl.UTF-8
Metoda kodowania OTP (One Time Pad - jednorazowa tablica) jest bardzo
prosta i niemożliwa do złamania bez znajomości właściwego pliku
tablicy, z którą wiadomość jest xorowana. Kodowanie i dekodowanie
odbywa się dokładnie tą samą metodą, a wiadomość może być odkodowana
poprawnie tylko przy użyciu tej samej tablicy, która była używana do
kodowania.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Crypt/OTP.pm
%{_mandir}/man3/*
