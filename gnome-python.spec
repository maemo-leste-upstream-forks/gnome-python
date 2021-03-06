# -*- mode: rpm-spec -*-
%define python python2

%define buildgtkhtml %(pkg-config libgtkhtml-2.0 && echo 1 || echo 0)
%define haveorbit %(pkg-config orbit-python-2.0 && echo 1 || echo 0)

Summary: The sources for the PyGNOME Python extension module.
Name: gnome-python2
Version:   2.28.1
Release: 9
Source: ftp://ftp.gnome.org/pub/GNOME/stable/sources/gnome-python/gnome-python-%{version}.tar.gz
Copyright: LGPL
Group: Development/Languages
BuildRoot: %{_tmppath}/gnome-python-root
Packager: James Henstridge <james@daa.com.au>
BuildRequires: pygtk2-devel = 2.10.3
BuildRequires: %{python}-devel
BuildRequires: gtk2-devel >= 2.6.0
BuildRequires: libgnomecanvas-devel >= 2.8.0
BuildRequires: libgnome-devel >= 2.8.0
BuildRequires: GConf2-devel >= 2.11.1
%if %{haveorbit}
Requires: gnome-python2-bonobo
BuildRequires: orbit-python >= @ORBIT_PYTHON_VERSION@
BuildRequires: bonobo-activation-devel >= 2.8.0
BuildRequires: libbonobo-devel >= 2.8.0
BuildRequires: libbonoboui-devel >= 2.8.0
BuildRequires: nautilus-devel >= @NAUTILUS_VERSION@
BuildRequires: eel2-devel
BuildRequires: gnome-panel >= @LIBPANELAPPLET_VERSION@
%endif
%if %{buildgtkhtml}
BuildRequires: gtkhtml2-devel >= @GTKHTML2_VERSION@
%endif


%description
The gnome-python package contains the source packages for the Python
bindings for GNOME called PyGNOME.

PyGNOME is an extension module for Python that provides access to the
base GNOME libraries, so you have access to more widgets, a simple
configuration interface, and metadata support.

%package applet
Version: %{version}
Summary: Python bindings for GNOME Panel applets.
Group: Development/Languages

%description applet
This module contains a wrapper that allows GNOME Panel applets to be
written in Python.

%package capplet
Version: %{version}
Summary: Python bindings for GNOME Panel applets.
Group: Development/Languages

%description capplet
This module contains a wrapper that allows GNOME Control Center
capplets to be in Python.

%package canvas
Version: %{version}
Summary: Python bindings for the GNOME Canvas.
Group: Development/Languages
Requires: libgnomecanvas >= 2.8.0
Requires: gtk2 >= 2.6.0
Requires: pygtk2 >= 2.10.3

%description canvas
This module contains a wrapper that allows use of the GNOME Canvas
in Python.

%package nautilus
Version: %{version}
Summary: Python bindings for interacting with Nautilus.
Group: Development/Languages
Requires: orbit-python >= @ORBIT_PYTHON_VERSION@
Requires: nautilus >= @NAUTILUS_VERSION@

%description nautilus
This module contains a wrapper that allows access to Nautilus via Python.

%package bonobo
Version: %{version}
Summary: Python bindings for interacting with bonobo.
Group: Development/Languages
Requires: orbit-python >= @ORBIT_PYTHON_VERSION@
Requires: bonobo-activation >= 2.8.0
Requires: libbonobo >= 2.8.0
Requires: libbonoboui >= 2.8.0

%description bonobo
This module contains a wrapper that allows the creation of bonobo
components and the embedding of bonobo components in Python.

%package gconf
Version: %{version}
Summary: Python bindings for interacting with GConf
Group: Development/Languages
Requires: GConf2 >= 1.1.10

%description gconf
This module contains a wrapper that allows the use of GConf via Python.

%package gtkhtml2
Version: %{version}
Summary: Python bindings for interacting with gtkhtml2
Group: Development/Languages
Requires: gtkhtml2 >= 1.99.7

%description gtkhtml2
This module contains a wrapper that allows the use of gtkhtml2 via
Python

%prep
%setup -q -n gnome-python-%{version}
export PYTHON=/usr/bin/python2.2
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{_prefix}

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README NEWS
%defattr(755,root,root,755)
%dir %{_prefix}/lib/python?.?/site-packages/gtk-2.0/gnome/
%{_prefix}/lib/python?.?/site-packages/gtk-2.0/gnome/__init__.*
%{_prefix}/lib/python?.?/site-packages/gtk-2.0/gnome/_gnomemodule.so
%if %{haveorbit}
%{_prefix}/lib/python?.?/site-packages/gtk-2.0/gnome/uimodule.so
%endif

%files applet
%defattr(755,root,root,755)
%dir %{_prefix}/lib/python?.?/site-packages/gtk-2.0/gnome/
%{_prefix}/lib/python?.?/site-packages/gtk-2.0/gnome/__init__.*
%{_prefix}/lib/python?.?/site-packages/gtk-2.0/gnome/appletmodule.so

%if %{haveorbit}
%files nautilus
%defattr(755,root,root,755)
%dir %{_prefix}/lib/python?.?/site-packages/gtk-2.0/gnome/
%{_prefix}/lib/python?.?/site-packages/gtk-2.0/gnome/__init__.*
%{_prefix}/lib/python?.?/site-packages/gtk-2.0/gnome/nautilusmodule.so
%defattr(644,root,root,755)
%doc examples/nautilus
%endif

%files canvas
%defattr(755,root,root,755)
%dir %{_prefix}/lib/python?.?/site-packages/gtk-2.0/gnome/
%{_prefix}/lib/python?.?/site-packages/gtk-2.0/gnome/__init__.*
%{_prefix}/lib/python?.?/site-packages/gtk-2.0/gnome/canvasmodule.so
%defattr(644,root,root,755)
%doc examples/canvas

%if %{haveorbit}
%files bonobo
%defattr(755,root,root,755)
%dir %{_prefix}/lib/python?.?/site-packages/gtk-2.0/bonobo/
%{_prefix}/lib/python?.?/site-packages/gtk-2.0/bonobo/__init__.*
%{_prefix}/lib/python?.?/site-packages/gtk-2.0/bonobo/*.so
%defattr(644,root,root,755)
%doc examples/bonobo
%endif

%files gconf
%defattr(755,root,root,755)
%{_prefix}/lib/python?.?/site-packages/gtk-2.0/gconf*
%defattr(644,root,root,755)
%doc examples/gconf

%if %{buildgtkhtml}
%files gtkhtml2
%defattr(755,root,root,755)
%{_prefix}/lib/python?.?/site-packages/gtk-2.0/gtkhtml*
%defattr(644,root,root,755)
%doc examples/gtkhtml2
%endif

%changelog
* Thu May 30 2002 Matt Wilson <msw@redhat.com>
- s/Gconf/GConf/

* Thu May 30 2002 Jeremy Katz <katzj@redhat.com>
- add gtkhtml2 and gconf subpackages

* Wed May 29 2002 Bill Nottingham <notting@redhat.com>
- add some defattrs

* Fri May 24 2002 Matt Wilson <msw@redhat.com>
- added bonobo, nautilus subpackages.  re-enabled applet subpackage

* Mon Nov 26 2001 Matt Wilson <msw@redhat.com>
- subpackages will need __init__ included in them

* Thu Oct 18 2001 Matt Wilson <msw@redhat.com>
- doesn't obsolete pygnome - it can be installed side-by-side
- added _gnomemodule.so to base package filelist

* Mon Oct 15 2001 Matt Wilson <msw@redhat.com>
- added __init__ files to gnome-python main package

* Mon Oct  8 2001 Matt Wilson <msw@redhat.com>
- new gnome-python package based on old pygtk package.
