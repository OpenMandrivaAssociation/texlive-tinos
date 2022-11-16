Name:		texlive-tinos
Version:	64504
Release:	1
Summary:	Tinos fonts with LaTeX support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tinos
License:	apache2 lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tinos.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tinos.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Tinos, designed by Steve Matteson, is an innovative, refreshing
serif design that is metrically compatible with Times New
Roman.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tinos
%{_texmfdistdir}/fonts/vf/google/tinos
%{_texmfdistdir}/fonts/type1/google/tinos
%{_texmfdistdir}/fonts/truetype/google/tinos
%{_texmfdistdir}/fonts/tfm/google/tinos
%{_texmfdistdir}/fonts/map/dvips/tinos
%{_texmfdistdir}/fonts/enc/dvips/tinos
%doc %{_texmfdistdir}/doc/fonts/tinos

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
