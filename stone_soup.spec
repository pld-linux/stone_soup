#
# Conditional build:
%bcond_without	tiles		# build tiles version
#
Summary:	stone soup :: crawl clone
Summary(pl.UTF-8):	stone soup :: klon crawla
Name:		stone_soup
Version:	0.6.0
Release:	1
License:	Nethack Like
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/crawl-ref/%{name}-%{version}.tar.bz2
# Source0-md5:	f4ff3e148344fda6410933d35deb4ead
Patch0:		%{name}-systemlua.patch
Patch1:		%{name}-makefile.patch
Patch2:		%{name}-tiles.patch
URL:		http://crawl.develz.org/
%if %{with tiles}
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
%endif
%{?with_tiles:BuildRequires:	SDL_image-devel}
BuildRequires:	bison
BuildRequires:	flex
%{?with_tiles:BuildRequires:	freetype-devel}
%{?with_tiles:BuildRequires:	libpng-devel}
BuildRequires:	lua51-devel
BuildRequires:	ncurses-devel
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel
BuildRequires:	which
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dungeon Crawl Stone Soup is a fun, free rogue-like game of exploration
and treasure-hunting in dungeons filled with dangerous and unfriendly
monsters in a quest for the mystifyingly fabulous Orb of Zot.

Dungeon Crawl Stone Soup is a variant of Linley's Dungeon Crawl that's
openly developed and invites participation from the Crawl community.

%description -l pl.UTF-8
Dungeon Crawl Stone Soup jest zabawną darmową grą typu roguelike, w
której gracz zwiedza świat poszukując skarbów w lochach pełnych
niebezpiecznych i nieprzyjaznych potworów w celu odnalezienia
tajemniczej baśniowej Kuli Zota.

Dungeon Crawl Stone Soup jest wariantem gry Dungeon Crawl stworzonej
przez Linleya. Jest on otwarcie rozwijany również przez społeczeństwo
Crawla.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%if %{with tiles}
%patch2 -p1
%endif

%build
%{__make} -C source \
	prefix="%{_prefix}" \
	SAVEDIR="/var/games/stone_soup/" \
	DATADIR="%{_datadir}/stone_soup/" \
	%{?with_tiles:TILES="y"} \
	V="y" \
	CXX="%{__cxx}" \
	OPTFLAGS="%{rpmcxxflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C source install \
	prefix="%{_prefix}" \
	bin_prefix="bin" \
	SAVEDIR="/var/games/stone_soup/" \
	DATADIR="%{_datadir}/stone_soup/" \
	%{?with_tiles:TILES="y"} \
	V="y" \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS.txt README.* docs
%attr(2755,root,games) %{_bindir}/stone_soup
%{_datadir}/stone_soup
%attr(775,root,games) %dir /var/games/stone_soup
