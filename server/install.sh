#!/bin/bash

# Network Practicum Final Project: DDOS Attacking & Defending
# Environment Configuration and Installation
# Copyright (C) 2018 Yingchao.Ma, all rights reserved
# Contact Point: http://yingchao.ma/send i@yingchao.ma

SUPPORTED_PLATFORMS="ubuntu|debian"


#Check sudo status
if [[ $(id -u) -ne 0 ]]
then
  echo "Error: This script requires privileged access. Try sudo ./install.sh. "
  exit 1
fi

#Check platform compatibility
platform="$(lsb_release -d | cut -f2-)"
if [ -z "$(egrep -i "$SUPPORTED_PLATFORMS" <<< $platform)"  ]
then
  echo "Warning: Supported platforms are $SUPPORTED_PLATFORMS but not your $platform. " 1>&2
  read -p "Continue? (y/n)" continue
  if [ "$continue" != "y" ]
  then
    echo "Warning: User Aborted."
    exit 2
  fi
fi

#Update Package Cache & Install Apache & PHP
if [ -f /etc/apache2/apache2.conf ]
then
  read -p "Apache has been installed. All your previous websites will be erased. Continue (y/n)?" choice
  if [ "$choice" != "y" ]
  then
    echo "Warning: User Aborted."
    exit 3
  fi
  rm -rf /var/www/*
fi
apt update
apt install -y apache2 php7.0 libapache2-mod-php7.0

#Extract files to /var/www
rsync -av ./www/ /var/www/
rsync -av ./apache2/ /etc/apache2/
chmod 777 -R /etc/apache2/*
chmod 777 -R /var/www/*

#Enable the target site
a2dissite 000-default
a2ensite 001-ddos
service apache2 restart