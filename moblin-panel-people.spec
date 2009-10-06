Name: moblin-panel-people
Summary: People panel for Moblin
Group: Graphical desktop/Other 
Version: 0.0.3
License: LGPL 2.1
URL: http://www.moblin.org
Release: %mkrel 1
Source0: http://git.moblin.org/cgit.cgi/%{name}/snapshot/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: anerley-devel
BuildRequires: gtk2-devel
BuildRequires: nbtk-devel
BuildRequires: moblin-panel-devel
BuildRequires: intltool
BuildRequires: gettext
BuildRequires: gnome-common

%description
Moblin people panel for Moblin

%prep
%setup -q 

%build
NOCONFIGURE=nil ./autogen.sh
%configure2_5x

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root,-)
%doc COPYING NEWS README AUTHORS ChangeLog
%{_libexecdir}/*
%{_datadir}/*