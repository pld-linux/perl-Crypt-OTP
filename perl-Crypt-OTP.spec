%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	OTP
Summary:	Crypt::OTP Perl module - OTP encryption method implementation
Summary(pl):	Modu³ Perla Crypt::OTP - implementacja kodowania metod± OTP
Name:		perl-Crypt-OTP
Version:	1.03
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
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
prosta i niemo¿liwa do z³amania bez znajomo¶ci w³a¶ciwego pliku
tablicy, z któr± wiadomo¶æ jest xorowana. Kodowanie i dekodowanie
odbywa siê dok³adnie t± sam± metod±, a wiadomo¶æ mo¿e byæ odkowowana
poprawnie tylko przy u¿yciu tej samej tablicy, która by³a u¿ywana do
kodowania.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_sitelib}/Crypt/OTP.pm
%{perl_sitelib}/auto/Crypt/OTP
%{_mandir}/man3/*
