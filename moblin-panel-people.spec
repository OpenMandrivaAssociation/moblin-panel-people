Name: moblin-panel-people
Summary: People panel for Moblin
Group: Graphical desktop/Other 
Version: 0.0.10
License: LGPL 2.1
URL: https://www.moblin.org
Release: %mkrel 2
Source0: http://git.moblin.org/cgit.cgi/%{name}/snapshot/%{name}-0.0.8.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

# this patch is necessary because developers didn't create a proper
# version tag for this moblin-2.1 release, they've also updated some
# .po files after 0.0.10 (remove this patch when the next tag is ok)
Patch0: moblin-panel-people-0.0.8-to-0.0.10.patch

BuildRequires: anerley-devel
BuildRequires: gtk2-devel
BuildRequires: nbtk-devel
BuildRequires: moblin-panel-devel
BuildRequires: intltool
BuildRequires: gettext
BuildRequires: gnome-common
#gw it is in a libtool archive:
BuildRequires: libbonobo2_x-devel

%description
Moblin people panel for Moblin

%prep
%setup -q -n %{name}-0.0.8
%patch0 -p1

%build
NOCONFIGURE=nil ./autogen.sh
%configure2_5x

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING NEWS README AUTHORS ChangeLog
%{_libexecdir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/dbus-1/services/*service
