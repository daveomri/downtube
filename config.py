#!/usr/bin/env python3
# Dave Omrai 16.6.2018
import os
def config():
    # This function is for downloading needed things for downtube program
    os.system("sudo add-apt-repository ppa:nilarimogard/webupd8")
    os.system("sudo apt-get update")
    os.system("sudo apt-get install youtube-dl")
    os.system("sudo apt-get install python-setuptools")
    os.system("sudo easy-install pip")
    os.system("sudo pip install --upgrade youtube-dl")
    os.system("sudo apt-get install python3-tk -y")
    os.system("chmod +x downtube.py")
    os.system("mkdir ~/.downtubebin")
    os.system("mv downtube.py ~/.downtubebin/downtube")
    os.system('export PATH=$PATH":$HOME/.downtubebin"')
config()
