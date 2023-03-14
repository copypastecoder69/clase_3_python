#!/bin/sh

cd /home/stickm4n/devops || exit

sudo apt-get update
apt list --upgradable | grep -o '.*[/]' | grep -o '.*[^/]' > upgradable_pkgs.lst

PKGS=$(cat upgradable_pkgs.lst)
sudo apt-get install -y $PKGS
