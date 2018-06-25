# revision 15878
# category Package
# catalog-ctan /graphics/metapost/contrib/macros/suanpan
# catalog-date 2009-11-10 00:30:52 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-suanpan
Version:	20180303
Release:	1
Summary:	MetaPost macros for drawing Chinese and Japanese abaci
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/suanpan
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/suanpan.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/suanpan.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20091110-2
+ Revision: 756298
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20091110-1
+ Revision: 719599
- texlive-suanpan
- texlive-suanpan
- texlive-suanpan
- texlive-suanpan

