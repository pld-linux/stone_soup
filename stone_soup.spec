Summary:	stone soup :: crawl clone
Summary(pl.UTF-8):	stone soup :: klon crawla
Name:		stone_soup
Version:	0.5.1
Release:	1
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
BuildRequires:	sqlite3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dungeon Crawl Stone Soup is a fun, free rogue-like game of exploration
and treasure-hunting in dungeons filled with dangerous and unfriendly
monsters in a quest for the mystifyingly fabulous Orb of Zot.

Dungeon Crawl Stone Soup is a variant of Linley's Dungeon Crawl that's
openly developed and invites participation from the Crawl community.

%description -l pl.UTF-8
Dungeon Crawl Stone Soup jest zabawną darmową grą typu roguelike, w
której gracz zwiedza świat poszukując skarbów w lochach pełnyh
niebezpiecznych i nieprzyjaznych potworów w celu odnalezienia
tajemniczej baśniowej Kuli Zota.

Dungeon Crawl Stone Soup jest wariantem gry Dungeon Crawl stworzonej
przez Linleya. Jest on otwarcie rozwijany również przez
społeczeństwo Crawla.

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
%{_datadir}/stone_soup
%attr(775,root,games) %dir /var/games/stone_soup
