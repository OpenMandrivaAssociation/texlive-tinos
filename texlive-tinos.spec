%global tl_name tinos
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Tinos fonts with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/tinos
License:	apache2 lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tinos.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tinos.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Tinos, designed by Steve Matteson, is an innovative, refreshing serif
design that is metrically compatible with Times New Roman.

