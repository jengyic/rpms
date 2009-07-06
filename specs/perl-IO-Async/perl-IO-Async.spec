# $Id$
# Authority: cmr
# Upstream: Paul Evans E<lt>leonerd$leonerd,org,ukE<gt>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-Async

Summary: a collection of modules that implement asynchronous filehandle IO
Name: perl-IO-Async
Version: 0.21
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-Async/

Source: http://www.cpan.org/modules/by-module/IO/IO-Async-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(File::Temp)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Refcount)

%description
a collection of modules that implement asynchronous filehandle
IO.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml examples/
%doc %{_mandir}/man3/IO::Async*.3pm*
%dir %{perl_vendorlib}/IO/
%{perl_vendorlib}/IO/Async/
%{perl_vendorlib}/IO/Async.pm

%changelog
* Mon Jul 06 2009 Christoph Maser <cmr@financial.com> - 0.21-1
- Initial package. (using DAR)