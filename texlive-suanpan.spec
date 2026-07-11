%global tl_name suanpan
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	MetaPost macros for drawing Chinese and Japanese abaci
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/suanpan
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/suanpan.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/suanpan.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
These macros are described in Denis Roegel: MetaPost macros for drawing
Chinese and Japanese abaci, TUGboat (volume 30, number 1, 2009, pages
74-79)

