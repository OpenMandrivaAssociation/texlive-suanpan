Name:		texlive-suanpan
Version:	15878
Release:	2
Summary:	MetaPost macros for drawing Chinese and Japanese abaci
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/suanpan
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/suanpan.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/suanpan.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
These macros are described in Denis Roegel: MetaPost macros for
drawing Chinese and Japanese abaci, TUGboat (volume 30, number
1, 2009, pages 74-79).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/metapost/suanpan/abacus.mp
%{_texmfdistdir}/metapost/suanpan/suanpan.mp
%doc %{_texmfdistdir}/doc/metapost/suanpan/README
%doc %{_texmfdistdir}/doc/metapost/suanpan/article.txt

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}
