%define name	podtohtml
%define Name	PodToHTML
%define version	0.07
%define release	5

Name:		%{name}
Version:		%{version}
Release:		%{release}
Summary:		Convert POD documentation to HTML
License:		GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{Name}
Source:		http://search.cpan.org/CPAN/authors/id/B/BD/BDFOY/%{Name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-HTML-Format
BuildRequires:	perl-devel


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
%makeinstall_std

%files
%doc README
%_bindir/*
%_mandir/*/*
%{perl_vendorlib}/Pod



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.07-5mdv2010.0
+ Revision: 430752
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.07-4mdv2009.0
+ Revision: 259135
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.07-3mdv2009.0
+ Revision: 247072
- rebuild

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdv2008.1
+ Revision: 136849
- new version

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-3mdv2008.1
+ Revision: 136773
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - import podtohtml


* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-2mdv2007.0
- Rebuild

* Sun Apr 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-1mdk
- first mdk release
