%global tl_name correctmathalign
%global tl_revision 44131

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Correct spacing of the alignment in expressions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/correctmathalign
License:	bsd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/correctmathalign.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/correctmathalign.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package realigns the horizontal spacing of the alignments in some
mathematical environments.

