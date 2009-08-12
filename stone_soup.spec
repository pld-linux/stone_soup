Summary:	stone soup :: crawl clone
Name:		stone_soup
Version:	0.5.1
Release:	0.1
License:	Nethack Like
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/crawl-ref/%{name}-%{version}-src.tbz2
# Source0-md5:	e1feb17d161311825e5eb676c14be44a
Patch0:		%{name}-systemlua.patch
Patch1:		%{name}-makefile.patch
Patch2:		%{name}-systemsqlite3.patch
Patch3:		%{name}-cflags.patch
URL:		http://crawl-ref.sourceforge.net/
BuildRequires:	bison
BuildRequires:	byacc
BuildRequires:	flex
BuildRequires:	lua51-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dungeon Crawl Clone.

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__make} -C source \
	CXX="%{__cxx}" \
	OPTFLAGS="%{rpmcxxflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/stone_soup{,/db,/des}
install -d $RPM_BUILD_ROOT%{_localstatedir}/games/stone_soup

%{__make} -C source install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS.txt README.* docs
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
