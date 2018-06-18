#!/usr/bin/env python3
# Dave Omrai 16.6.2018
import os, glob, shutil
def config():
    # This function is for downloading needed things for downtube program
    home = os.getenv('HOME')
    os.system("sudo add-apt-repository ppa:nilarimogard/webupd8")
    os.system("sudo apt-get update")
    os.system("sudo apt-get install youtube-dl")
    os.system("sudo apt-get install python-setuptools")
    os.system("sudo easy_install pip")
    os.system("sudo pip install --upgrade youtube-dl")
    os.system("sudo apt-get install python3-tk -y")
    os.system("chmod +x downtube.py")
    os.mkdir(home+"/.downtubebin")
    shutil.move("downtube.py", home+"/.downtubebin/downtube")
    file = open(home+".bashrc", "a")
    file.write("#Downtube alias\nalias downtube='~/.downtubebin/downtube'")
    file.close()
    os.sys("source ~/.bashrc")
config()
