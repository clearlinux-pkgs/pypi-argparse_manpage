#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-argparse_manpage
Version  : 4.4
Release  : 5
URL      : https://files.pythonhosted.org/packages/d4/1f/49e8ce0d72a53eab1a0a3ea86a1bb3a97b2f469398730f2578a1e288346e/argparse-manpage-4.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/d4/1f/49e8ce0d72a53eab1a0a3ea86a1bb3a97b2f469398730f2578a1e288346e/argparse-manpage-4.4.tar.gz
Summary  : Build manual page from python's ArgumentParser object.
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-argparse_manpage-bin = %{version}-%{release}
Requires: pypi-argparse_manpage-license = %{version}-%{release}
Requires: pypi-argparse_manpage-man = %{version}-%{release}
Requires: pypi-argparse_manpage-python = %{version}-%{release}
Requires: pypi-argparse_manpage-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(packaging)
BuildRequires : pypi(setuptools)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Hack to work-around missing stuff.

%package bin
Summary: bin components for the pypi-argparse_manpage package.
Group: Binaries
Requires: pypi-argparse_manpage-license = %{version}-%{release}

%description bin
bin components for the pypi-argparse_manpage package.


%package license
Summary: license components for the pypi-argparse_manpage package.
Group: Default

%description license
license components for the pypi-argparse_manpage package.


%package man
Summary: man components for the pypi-argparse_manpage package.
Group: Default

%description man
man components for the pypi-argparse_manpage package.


%package python
Summary: python components for the pypi-argparse_manpage package.
Group: Default
Requires: pypi-argparse_manpage-python3 = %{version}-%{release}

%description python
python components for the pypi-argparse_manpage package.


%package python3
Summary: python3 components for the pypi-argparse_manpage package.
Group: Default
Requires: python3-core
Provides: pypi(argparse_manpage)

%description python3
python3 components for the pypi-argparse_manpage package.


%prep
%setup -q -n argparse-manpage-4.4
cd %{_builddir}/argparse-manpage-4.4
pushd ..
cp -a argparse-manpage-4.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1693929633
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-argparse_manpage
cp %{_builddir}/argparse-manpage-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-argparse_manpage/92170cdc034b2ff819323ff670d3b7266c8bffcd || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/argparse-manpage

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-argparse_manpage/92170cdc034b2ff819323ff670d3b7266c8bffcd

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/argparse-manpage.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
