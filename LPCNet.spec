#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : LPCNet
Version  : 0dc5935bbf49ff3ba3c9654cc2f802838ebbaead
Release  : 3
URL      : https://github.com/drowe67/LPCNet/archive/0dc5935bbf49ff3ba3c9654cc2f802838ebbaead.tar.gz
Source0  : https://github.com/drowe67/LPCNet/archive/0dc5935bbf49ff3ba3c9654cc2f802838ebbaead.tar.gz
Source1  : http://rowetel.com/downloads/deep/lpcnet_191005_v1.0.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: LPCNet-bin = %{version}-%{release}
Requires: LPCNet-lib = %{version}-%{release}
Requires: LPCNet-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : codec2-dev
BuildRequires : git
BuildRequires : pkgconfig(codec2)
Patch1: 0001-Build-fixes.patch
Patch2: 0002-Change-cmake-search-subtly-for-Codec2-1.0.patch

%description
# LPCNet for FreeDV
Experimental version of LPCNet that has been used to develop FreeDV 2020 - a HF radio Digial Voice mode for over the air experimentation with Neural Net speech coding.  Possibly the first use of Neural Net speech coding in real world operation.

%package bin
Summary: bin components for the LPCNet package.
Group: Binaries
Requires: LPCNet-license = %{version}-%{release}

%description bin
bin components for the LPCNet package.


%package dev
Summary: dev components for the LPCNet package.
Group: Development
Requires: LPCNet-lib = %{version}-%{release}
Requires: LPCNet-bin = %{version}-%{release}
Provides: LPCNet-devel = %{version}-%{release}
Requires: LPCNet = %{version}-%{release}

%description dev
dev components for the LPCNet package.


%package lib
Summary: lib components for the LPCNet package.
Group: Libraries
Requires: LPCNet-license = %{version}-%{release}

%description lib
lib components for the LPCNet package.


%package license
Summary: license components for the LPCNet package.
Group: Default

%description license
license components for the LPCNet package.


%prep
%setup -q -n LPCNet-0dc5935bbf49ff3ba3c9654cc2f802838ebbaead
cd %{_builddir}
mkdir -p lpcnet_191005_v1.0
cd lpcnet_191005_v1.0
tar xf %{_sourcedir}/lpcnet_191005_v1.0.tgz
cd %{_builddir}/LPCNet-0dc5935bbf49ff3ba3c9654cc2f802838ebbaead
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1631663947
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test || :

%install
export SOURCE_DATE_EPOCH=1631663947
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/LPCNet
cp %{_builddir}/LPCNet-0dc5935bbf49ff3ba3c9654cc2f802838ebbaead/COPYING %{buildroot}/usr/share/package-licenses/LPCNet/b3209e40e62e1f6c8e67b6fd25b88693419baa4d
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lpcnet_dec
/usr/bin/lpcnet_enc

%files dev
%defattr(-,root,root,-)
/usr/include/lpcnet/lpcnet_freedv.h
/usr/lib64/cmake/lpcnetfreedv/lpcnetfreedv-config-relwithdebinfo.cmake
/usr/lib64/cmake/lpcnetfreedv/lpcnetfreedv-config.cmake
/usr/lib64/liblpcnetfreedv.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/liblpcnetfreedv.so.0.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/LPCNet/b3209e40e62e1f6c8e67b6fd25b88693419baa4d
