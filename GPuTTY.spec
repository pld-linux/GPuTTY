Summary:	Remembers telnet and SSH sessions
Summary(pl.UTF-8):	Zapamiętywanie sesji telnet i SSH
Name:		GPuTTY
Version:	0.9.4
Release:	1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	ftp://ftp.defora.org/pub/projects/gputty/%{name}-%{version}.tar.gz
# Source0-md5:	70674349468d0bdcdba1de32934ea912
Source1:	%{name}.desktop
Source2:	%{name}-pl.po
Patch0:		%{name}-am_fix.patch
Patch1:		%{name}-pl.patch
URL:		http://www.defora.org/projects/gputty/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gnome-libs-devel
BuildRequires:	libgtkpp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPuTTY is a PuTTY clone using the GNOME environment. It can store and
launch telnet and SSH sessions. It's not a terminal emulator.

%description -l pl.UTF-8
GPuTTY jest klonem PuTTY używającym środowiska GNOME. Potrafi
zapamiętać o odpalić sesje telnet oraz SSH. Nie jest to emulator
terminala.

%prep
%setup -q
install %{SOURCE2} po/pl.po
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__gettextize}
%{__aclocal} -I %{_aclocaldir}/gnome
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications/%{name}.desktop

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gputty
%{_applnkdir}/Network/Communications/*
