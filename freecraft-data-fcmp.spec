Summary:	Freecraft Media Project - free data for Freecraft game
Summary(pl):	Freecraft Media Project - wolnodostêpne dane dla gry Freecraft
Name:		freecraft-data-fcmp
%define	snap	030311
Version:	1.18
#Release:	0.pre1.%{snap}.1
Release:	1
Epoch:		1
License:	BSD-like or GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/freecraft/fcmp-%{snap}.tar.gz
# Source0-md5:	df77bb91f5e6bcfa113d66064156002e
URL:		http://freecraft.sourceforge.net/
Requires:	freecraft >= 1:1.18-0.pre1
Provides:	freecraft-data = %{epoch}:%{version}-%{release}
Obsoletes:	freecraft-data-wc2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the distribution of the Freecraft Media Project - free data
package for Freecraft game.

%description -l pl
To jest dystrybucja Freecraft Media Project - wolnodostêpnych danych
dla gry Freecraft.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/games/freecraft

mv -f data/{doc,ChangeLog.html} .
cp -rf data $RPM_BUILD_ROOT%{_datadir}/games/freecraft

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/README.txt ChangeLog.html
%{_datadir}/games/freecraft/data
