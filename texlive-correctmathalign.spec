Name:		texlive-correctmathalign
Version:	44131
Release:	2
Summary:	Correct spacing of the alignment in expressions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/correctmathalign
License:	bsd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/correctmathalign.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/correctmathalign.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package realigns the horizontal spacing of the alignments
in some mathematical environments.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/correctmathalign
%doc %{_texmfdistdir}/doc/latex/correctmathalign

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
