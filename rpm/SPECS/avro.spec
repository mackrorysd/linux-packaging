#
# spec file for package 
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           avro
Version:        1.7.6
Release:        1
License:        ASL 2.0
Summary:        Apache Avro is a data serialization system
Url:            http://avro.apache.org
Group:          Development/Libraries
Source:         apache-avro-%{version}.tar.gz
#Patch:
BuildRequires:  python, cmake, make
#PreReq:
Provides:       avro-tools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Avro provides rich data structures, a compact, fast, binary data format, a
container file to store persistent data, remote procedure calls (RPC), and
simple integration with dynamic languages. Code generation is not required
to read or write data files nor to use or implement RPC protocols. Code
generation is an optional optimization, only worth implementing for
statically typed languages.

%prep
%setup -q

%build
# ./configure
# make

for dir in c c++; do (cd lang/$dir; cmake .; make); done
mvn package -X -DskipTests -Dmaven.test.skip=true $@
(cd lang/py && ./setup.py build)

%install
# %make_install

%post

%postun

%files
%defattr(-,root,root)
%doc ChangeLog README COPYING

%changelog

