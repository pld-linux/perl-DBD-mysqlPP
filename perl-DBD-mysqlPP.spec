#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	DBD
%define		pnam	mysqlPP
Summary:	DBD::mysqlPP - pure Perl MySQL driver for the DBI
Summary(pl.UTF-8):	DBD::mysqlPP - czysto perlowy sterownik do MySQL-a dla DBI
Name:		perl-DBD-mysqlPP
Version:	0.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a259806d4c82e486fb474d8b5c15e6dd
%if %{with tests}
BuildRequires:	perl-DBI >= 1.0
BuildRequires:	perl-Net-MySQL >= 0.08
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Net-MySQL >= 0.08
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBD::mysqlPP is a Pure Perl MySQL driver for the Perl5 Database
Interface (DBI). This module implements network protool between
server and client of MySQL, thus you don't need external MySQL
client library like libmysqlclient for this module to work.
It means this module enables you to connect to MySQL server from
some operation systems which MySQL is not ported.

%description -l pl.UTF-8
DBD::mysqlPP to czysto perlowy sterownik do MySQL-a dla DBI (perlowego
interfejsu do baz danych). Ten moduł jest implementacją protokołu
sieciowego między serwerem a klientem MySQL-a, przez co nie wymaga do
działania zewnętrznej biblioteki klienckiej MySQL-a, takiej jak
libmysqlclient. Oznacza to, że moduł ten umożliwia połączenie z
serwerem MySQL nawet z systemu operacyjnego, na który MySQL nie został
sportowany.

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
%doc Changes README
%{perl_vendorlib}/DBD/mysqlPP.pm
%{_mandir}/man3/*
