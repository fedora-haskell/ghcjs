# https://fedoraproject.org/wiki/Packaging:Haskell

%global ghc_without_dynamic 1
%global ghc_without_shared 1
%global without_prof 1
%global without_haddock 1

%global pkg_name ghcjs

# no useful debuginfo for Haskell packages without C sources
%global debug_package %{nil}

Name:           %{pkg_name}
Version:        0.2.0.20161021
Release:        1%{?dist}
Summary:        GHC JS compiler

License:        BSD
URL:            https://github.com/ghcjs/ghcjs
# generated with cabal sdist
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  ghc > 7.10.2
BuildRequires:  cabal-install
BuildRequires:  ghc-rpm-macros
Requires:       nodejs
Requires:       ghc-compiler = %{ghc_version}

%description
GHCJS is a Haskell to JavaScript compiler that uses the GHC API.
GHCJS supports many modern Haskell features, including:

- All type system extensions supported by GHC
- Lightweight preemptive threading with blackholes, MVar, STM, asynchronous exceptions
- Weak references, CAF deallocation, StableName, StablePtr
- Unboxed arrays, emulated pointers
- Integer support through JSBN, 32 and 64 bit signed and unsigned arithmetic (Word64, Int32 etc.)
- Cost-centres, stack traces
- Cabal support, GHCJS has its own package database

And some JavaScript-specific features:

- new JavaScriptFFI extension, with convenient import patterns, asynchronous FFI and a JSVal FFI type,
- synchronous and asynchronous threads.


%prep
%autosetup


%build
[ -d "$HOME/.cabal" ] || cabal update
%global cabal cabal
#%%cabal sandbox init
%cabal install --only-dependencies
%ghc_bin_build


%install
%ghc_bin_install

rm -r %{buildroot}%{ghclibdir}


%files
%license LICENSE
%doc README.markdown
%{_bindir}/*ghcjs*
%{_datadir}/%{name}-%{version}


%changelog
* Fri Oct 28 2016 Jens Petersen <petersen@redhat.com> - 0.2.0.20161021-1
- initial snapshot packaging
