# BAD, UGLY, works for me not sure if for anyone else
#
# Conditional build:
%bcond_with	tests		# build with tests
%bcond_without	tests		# build without tests
#
Summary:	stone soup :: crawl clone
Name:		stone_soup
Version:	0.5.1
Release:	0.1
License:	Nethack Like
Group:		Applications
Source0:	http://dl.sourceforge.net/crawl-ref/%{name}-%{version}-src.tbz2
# Source0-md5:	e1feb17d161311825e5eb676c14be44a
Patch0:		%{name}-systemlua.patch
Patch1:		%{name}-makefile.patch
#Source1:	-
# Source1-md5:	-
#Patch0:		%{name}-DESTDIR.patch
URL:		-
BuildRequires:	bison
BuildRequires:	byacc
BuildRequires:	flex
BuildRequires:	lusa51-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dungeon Crawl Clone


%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1 
%patch1 -p1 

# remove CVS control files
#find -name CVS -print0 | xargs -0 rm -rf

# you'll need this if you cp -a complete dir in source
# cleanup backups after patching
find . '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%build
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
#%%{__intltoolize}
#%%{__gettextize}
#%%{__libtoolize}
#%%{__aclocal}
#%%{__autoconf}
#%%{__autoheader}
#%%{__automake}
# if not running libtool or automake, but config.sub is too old:
#cp -f /usr/share/automake/config.sub .
#%%configure
%{__make} -C source 

#%{__make} \
#	CFLAGS="%{rpmcflags}" \
#	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} -C source install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_localstatedir}/games/stone_soup
install -d $RPM_BUILD_ROOT%{_datadir}/stone_soup{,/db,/des}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(2755,root,games) %{_bindir}/stone_soup
%attr(3777,root,games) %dir %{_datadir}/stone_soup
%attr(2775,root,games) %dir %{_datadir}/stone_soup/db
%attr(2775,root,games) %dir %{_datadir}/stone_soup/des
%attr(775,root,games) %dir %{_datadir}/stone_soup/dat
%attr(775,root,games) %dir %{_datadir}/stone_soup/dat/clua
%attr(775,root,games) %dir %{_datadir}/stone_soup/dat/lua
%attr(775,root,games) %dir %{_datadir}/stone_soup/dat/descript
%attr(775,root,games) %dir %{_datadir}/stone_soup/dat/database
%attr(775,root,games) %dir %{_datadir}/stone_soup/settings
%attr(3777,root,games) %dir %{_localstatedir}/games/stone_soup
%attr(644,root,games) %{_datadir}/stone_soup/dat/*des
%attr(644,root,games) %{_datadir}/stone_soup/dat/clua/*lua
%attr(644,root,games) %{_datadir}/stone_soup/dat/lua/*lua
%attr(644,root,games) %{_datadir}/stone_soup/dat/descript/*.txt
%attr(644,root,games) %{_datadir}/stone_soup/dat/database/*.txt
%attr(644,root,games) %{_datadir}/stone_soup/settings/*.txt
