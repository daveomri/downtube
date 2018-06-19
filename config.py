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
    file = open(home+"/.bashrc", "a")
    file.write("#Downtube alias\nalias downtube='~/.downtubebin/downtube'\n")
    file.close()
    os.system("echo '\nWe are almost done, there is just one thing to do.\nThis program created alias \033[0;32mdowntube\033[0m in file ~/.bashrc and now you have to install it.\nChoose one of these options\n\033[0;32msource ~/.bashrc\033[0m - type this command to install new .bashrc\nor\n\033[0;32mreboot\033[0m - reboot system to automatically install new .bashrc'")
config()
