# Copyright 2014 Sean Mackrory
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

Name:           apachecon
Version:        2.4.7
Release:        1
License:        ASL 2.0
Summary:        A robust, commercial-grade, featureful, and freely-available open-source HTTP (Web) server.
Url:            http://httpd.apache.org
Group:          System Environment/Daemons
Source:         httpd-%{version}.tar.gz
#Patch:
BuildRequires:  libapr-util1-devel, pcre-devel
Requires:       libapr-util1, pcre
Provides:       httpd
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Apache HTTP Server Project is an effort to develop and maintain an
open-source HTTP server for modern operating systems including UNIX and
Windows NT. The goal of this project is to provide a secure, efficient and
extensible server that provides HTTP services in sync with the current HTTP
standards.

%package devel
Requires: %{name}
Summary: Development headers for Apache

%description devel
Development headers for Apache

%prep
%setup -q -n httpd-%{version}

%build
%{configure}
make -j4

%install
%{make_install}

%post
# Add alternatives

%postun
# Delete alternatives

%files
%defattr(-,root,root)
%doc README
%config(noreplace) /etc/*
%attr(0755,root,root) /usr/bin/*
%attr(0755,root,root) /usr/sbin/*
/usr/lib/*
/usr/share/build/
/usr/share/cgi-bin/
/usr/share/error/
/usr/share/htdocs/
/usr/share/icons/
/usr/share/man/man1/
/usr/share/man/man8/
/usr/share/manual/

%files devel
%defattr(-,root,root)
/usr/include/*

%changelog

