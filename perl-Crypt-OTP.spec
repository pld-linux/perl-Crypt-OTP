#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	OTP
Summary:	Crypt::OTP Perl module - OTP encryption method implementation
Summary(pl):	Modu� Perla Crypt::OTP - implementacja kodowania metod� OTP
Name:		perl-Crypt-OTP
Version:	2.00
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The One Time Pad encryption method is very simple, and impossible to
crack without the actual pad file against which the to-be-encrypted
message is XOR'ed. Encryption and decryption are performed using
exactly the same method, and the message will decrypt correctly only
if the same pad is used in decryption as was use in encryption.

%description -l pl
Metoda kodowania OTP (One Time Pad - jednorazowa tablica) jest bardzo
prosta i niemo�liwa do z�amania bez znajomo�ci w�a�ciwego pliku
tablicy, z kt�r� wiadomo�� jest xorowana. Kodowanie i dekodowanie
odbywa si� dok�adnie t� sam� metod�, a wiadomo�� mo�e by� odkowowana
poprawnie tylko przy u�yciu tej samej tablicy, kt�ra by�a u�ywana do
kodowania.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

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