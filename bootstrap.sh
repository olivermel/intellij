#!/usr/bin/env bash

sudo yum -y groupinstall 'Development Tools'
sudo yum -y groupinstall "X Window System"
sudo yum -y groupinstall "GNOME Desktop"
sudo yum -y install vim tree xclock
sudo yum -y install vim xterm
sudo yum -y install java-1.8.0-openjdk*

SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")

if [ "$SCRIPTPATH" = "/tmp" ] ; then
	SCRIPTPATH=/vagrant
fi

mkdir -p $HOME/rpmbuild/{BUILD,RPMS,SOURCES,SRPMS}
ln -sf $SCRIPTPATH/SPECS $HOME/rpmbuild/SPECS
echo '%_topdir '$HOME'/rpmbuild' > $HOME/.rpmmacros
cd $HOME/rpmbuild/SOURCES

wget https://download.jetbrains.com/idea/ideaIC-2016.1.3.tar.gz


