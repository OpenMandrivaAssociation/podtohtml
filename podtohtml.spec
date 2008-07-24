%define name	podtohtml
%define Name	PodToHTML
%define version	0.07
%define release	%mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Convert POD documentation to HTML
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{Name}
Source:		http://search.cpan.org/CPAN/authors/id/B/BD/BDFOY/%{Name}-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
podtohtml converts POD documentation to HTML. It is based on the generic
Pod::Parser. It works by making two passes over the selected pods, the fisrt
pass uses Pod::Links to pre-scan for L<> links and =head1 NAME sections, and
then a second to build a tree of HTML::Elements for each POD and calling the
as_HTML method on the resulting tree.

The Generated HTML uses relative links.

%prep
%setup -q -n %{Name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%_bindir/*
%_mandir/*/*
%{perl_vendorlib}/Pod

