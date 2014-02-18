# Linux Packaging at ApacheCon NA 2014

## Build Environment

Although it is possible to cross-compile packages (i.e. build RPM packages in Ubuntu) it is highly recommend that packages always be built on the same distribution as the target environment to ensure a compatible version of the packaging tools, and also any shared libraries you may link against, etc.

To build this example you will need a Debian-based Linux environment (for \*.deb packages) and a Red Hat or SUSE-based Linux environment (for \*.rpm packages). If you have Oracle VirtualBox installed, I recommend Vagrant for quickly and simply creating a virtual Linux environment:

### Vagrant

If you have VirtualBox installed, you can use the following instructions for Vagrant (http://www.vagrantup.com/) to easily create lightweight Linux environments.

For portability, the following environments are all 32-bit, and use the smallest available image of the target operating system.

#### RPM

    $ vagrant box add linux-packaging-rpm http://goo.gl/kvL47z
    $ vagrant up linux-packaging-rpm
    $ vagrant ssh

```
Unshortened URL: https://dl.dropbox.com/sh/yim9oyqajopoiqs/kXejEiEBAO/oracle59-32.box
```

#### DEB

    $ vagrant box add linux-packaging-deb http://goo.gl/CvmEcv
    $ vagrant up linux-packaging-deb
    $ vagrant ssh

```
Unshortened URL: http://files.vagrantup.com/precise32.box
```

### Install required tools

Once you have a base Linux system, you will need some additional tools to be able to build packages for this system:

On RPM-based distros:

    yum install rpm-build createrepo

or

    zypper install rpm-build creatrepo

On Debian-based distros:

    apt-get install build-essential dh-make debhelper devscripts reprepro

## License

This project includes Apache Avro 1.7.6, which includes its own licensing information.

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
