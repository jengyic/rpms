# $Id$

# Authority: dag
# Upstream: 

%define real_version 20031202

Summary: Standard netcat enhanced with twofish encryption. 
Name: cryptcat
Version: 0.0.20031202
Release: 1
License: GPL
Group: Applications/Internet
URL: http://farm9.org/Cryptcat/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://farm9.org/Cryptcat/cryptcat_%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++

%description
Cryptcat is the standard netcat enhanced with twofish encryption.
netcat was origianally written by the l0pht (hobbit and weld pond).

%prep
%setup -n %{name}_%{real_version}

%build
%{__perl} -pi -e 's|STATIC=-static||g;' Makefile
%{__make} linux XLIBS=-lstdc++

%install
%{__rm} -rf %{buildroot}
%{__install} -m0755 -D cryptcat %{buildroot}%{_bindir}/cryptcat

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog README*
%{_bindir}/cryptcat

%changelog
* Sun Mar 28 2004 Dag Wieers <dag@wieers.com> - 0.0.20031202-1
- Initial package. (using DAR)
