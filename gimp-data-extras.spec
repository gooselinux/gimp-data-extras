%define gimpdatadir %(%{_bindir}/gimptool --gimpdatadir || echo blah)

Summary: Extra files for GIMP
Name: gimp-data-extras
Version: 2.0.2
Release: 3.1%{?dist}
License: GPLv2+
Group: Applications/Multimedia
URL: http://www.gimp.org/
Source: ftp://ftp.gimp.org/pub/gimp/extras/gimp-data-extras-%{version}.tar.bz2
Source1: license-clarification.txt
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%__id_u -n)
BuildArch: noarch
BuildRequires: gimp-devel-tools
BuildRequires: gimp-devel >= 2:2.0
Requires: gimp >= 2:2.0

%description
Patterns, gradients, and other extra files for the GIMP.

%prep
%setup -q
cp %{SOURCE1} .

%build
%configure
make

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%defattr (-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README license-clarification.txt
%{gimpdatadir}/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.0.2-3.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Nils Philippsen <nils@redhat.com> - 2.0.2-1
- bump release for importing

* Fri Feb 13 2009 Nils Philippsen <nils@redhat.com> - 2.0.2-0.3
- merge review (#225797): include IRC log which clarifies the package license

* Mon Feb 09 2009 Nils Philippsen <nils@redhat.com> - 2.0.2-0.2
- don't require gimptool file, but gimp-devel-tools package for building
- merge review (#225797)
  - don't require /usr/share/gimp/2.0 directory, but specific minimum gimp
    version
  - work around problematic gimpdatadir macro definition if gimptool is not
    available 

* Wed Nov 14 2007 Nils Philippsen <nphilipp@redhat.com> - 2.0.2-0.1
- version 2.0.2
- use RPM macros where appropriate
- use "make DESTDIR=... install"
- merge review (#225797)
  - add dist tag
  - change license tag to GPLv2+
  - sanitize buildroot
  - set default mode 0755 for directories
  - add documentation files
  - separate BuildRequires, add epoch to BR: gimp-devel ...
  - sanitize summary
  - recode SPEC file to UTF-8
  - clean buildroot at beginning of %%install

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.0.1-1.1.1
- rebuild

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Mar 02 2005 Nils Philippsen <nphilipp@redhat.com> 2.0.1-1
- version 2.0.1

* Mon Oct 18 2004 Nils Philippsen <nphilipp@redhat.com> 2.0.0-1
- rather cosmetic version upgrade
- fix BuildRoot

* Tue Sep 21 2004 Than Ngo <than@redhat.com> 1.2.0-12 
- rebuilt

* Mon Apr 05 2004 Nils Philippsen <nphilipp@redhat.com>
- require gimp (#70753)

* Thu Feb 19 2004 Nils Philippsen <nphilipp@redhat.com>
- build with gimp-2.0
- run %%setup quietly
- use path macros
- fix source URL

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Dec 23 2002 Matt Wilson <msw@redhat.com> 1.2.0-7
- rebuild in new collection

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Feb 25 2002 Than Ngo <than@redhat.com> 1.2.0-4
- rebuild in new enviroment

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Aug 27 2001 Trond Eivind Glomsrød <teg@redhat.com> 1.2.0-2
- s/Copyright/License/
- Use %%{_tmppath}
- Add gimp-devel as a build dependency (#44744)

* Mon Dec 25 2000 Matt Wilson <msw@redhat.com>
- 1.2.0

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jun 19 2000 Matt Wilson <msw@redhat.com>
- defattr root

* Sun May 28 2000 Matt Wilson <msw@redhat.com>
- pass GIMP_DATA_DIR to make install target so we get in the buildroot

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 4)

* Mon Mar 15 1999 Matt Wilson <msw@redhat.com>
- packaged for rawhide

* Fri Sep 11 1998 Cristian Gafton <gafton@redhat.com>
- packaged for 5.2
