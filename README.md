# Linux Packaging at Linux Foundation / ApacheCon NA 2014

This is a part of my tutorial at ApacheCon North America 2014 on building Linux packages for software projects. The tutorial covers Debian and RPM packages. This document is accompanied by example code to build packages for the Apache HTTP server, and explains how to set up a build environment, how to build the packages, and how to deploy packages in a repository.

## Build Environment

Although it is possible to cross-compile packages (i.e. build RPM packages in Ubuntu) it is highly recommend that packages always be built on the same distribution as the target environment to ensure a compatible version of the packaging tools, and also any shared libraries you may link against, etc.

To build this example you will need a Debian-based Linux environment (for \*.deb packages) and a Red Hat or SUSE-based Linux environment (for \*.rpm packages). If you have Oracle VirtualBox installed, I recommend Vagrant for quickly and simply creating a virtual Linux environment:

### Vagrant

If you have Oracle VirtualBox and Vagrant installed (http://www.vagrantup.com/), you can use the following instructions to easily create the environments you need to build the example packages. Once you are SSH'd into the machine, the contents of this project will be in ~/linux-packaging.

Both environments are 32-bit VMs for portability. Do not attempt to boot a Vagrant instance while another is still booting; wait until you can connect with SSH before starting additional instances.

#### openSUSE environment for RPM packaging

    $ vagrant box add rpm http://goo.gl/dZkk64
    $ vagrant up rpm
    $ vagrant ssh rpm

```
Unshortened URL: http://sourceforge.net/projects/opensusevagrant/files/12.3/opensuse-12.3-32.box/download
```

#### Ubuntu environment for Debian packaging

    $ vagrant box add deb http://goo.gl/CvmEcv
    $ vagrant up deb
    $ vagrant ssh deb

```
Unshortened URL: http://files.vagrantup.com/precise32.box
```

### Packaging Tools

Once you have a base Linux system, you will need some additional tools to be able to build packages and repositories for this system. Note that some of these commands will ask for your confirmation before proceeding with the installation.

On Red Hat-based distros:

    sudo yum install rpmbuild createrepo

On SUSE-based distros*:

    sudo zypper refresh
    sudo zypper install rpm-build createrepo

On Debian-based distros:

    sudo apt-get update
    sudo apt-get install build-essential dh-make debhelper devscripts reprepro

* If there's a conflict when installing createrepo in the openSUSE Vagrant box, select option 1

## Building RPM Packages

From the ~/linux-packaging/rpm/ directory, run the following commands to install build dependencies, extract the source where rpmbuild expects it, and invoke rpmbuild:

    sudo zypper install libapr-util1-devel pcre-devel
    cp ../httpd-2.4.7.tar.gz SOURCES/
    rpmbuild -ba --define "_topdir `pwd`" SPECS/apachecon.spec

## Building Debian Packages

From the ~/linux-packaging/deb/ directory, run the following commands to install build dependencies, extract the source where debuild expects it, and invoke debuild:

    sudo apt-get install libaprutil1-dev
    tar xzf ../httpd-2.4.7.tar.gz --strip-components=1
    cp ../httpd-2.4.7.tar.gz ../apachecon_2.4.7.orig.tar.gz
    debuild -i -us -uc

## Creating a Yum / Zypper Repository

To create a repository usable by the Yum or Zypper package managers (used in Red Hat and SUSE distributions, respectively), you use createrepo to generate an index of the packages in the current directory. All client machines need to have a corresponding .repo file installed:

    createrepo .
    cp apachecon.repo /etc/yum.repos.d/
    # OR
    cp apachecon.repo /etc/zypp/repos.d/

## Creating an Apt Repository

To create a repository usable by the apt-get or aptitude package managers (used in in Debian and Ubuntu distributions), you use dpkg-scanpackages to generate an index of the packages in the current directory. All client machines need to have a corresponding .list file installed:

    dpkg-scanpackages . /dev/null | gzip -9c > Packages.gz
    cp apachecon.list /etc/apt/sources.list.d/

## License

This project includes Apache HTTP Server 2.4.7, which includes its own licensing information.

All other code and documentation in this project is released under the Apache Software License, version 2.0.

    Copyright 2014 Sean Mackrory

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
