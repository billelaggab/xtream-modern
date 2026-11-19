#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Xtream Codes Modern - Installation Script
Modern Python 3 version of the original install.py
"""

import subprocess
import os
import random
import string
import sys

# =============================================
# الإعدادات الأساسية
# =============================================

class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    YELLOW = '\033[33m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def generate(length=32): return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(length))

def getIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def getVersion():
    try:
        return subprocess.check_output("lsb_release -d".split()).decode().split(":")[-1].strip()
    except:
        return ""

def printc(rText, rColour=Color.OKBLUE, rPadding=0):
    print(f"{rColour}┌──────────────────────────────────────────┐{Color.ENDC}")
    for i in range(rPadding):
        print(f"{rColour}│                                          │{Color.ENDC}")
    print(f"{rColour}│ {rText}{Color.ENDC} │")
    for i in range(rPadding):
        print(f"{rColour}│                                          │{Color.ENDC}")
    print(f"{rColour}└──────────────────────────────────────────┘ {Color.ENDC}")
    print(" ")

def prepare(rType="MAIN"):
    global rPackages
    if rType != "MAIN": rPackages = rPackages[:-3]
    printc("Preparing Installation", Color.OKBLUE)
    for rFile in ["/var/lib/dpkg/lock-frontend", "/var/cache/apt/archives/lock", "/var/lib/dpkg/lock"]:
        try:
            os.remove(rFile)
        except:
            pass
    
    os.system("apt-get update > /dev/null")
    printc("Removing libcurl4 if installed", Color.WARNING)
    os.system("apt-get remove --auto-remove libcurl4 -y > /dev/null")
    
    rPackages = [
        "libcurl4", "libxslt1-dev", "libgeoip-dev", "e2fsprogs", 
        "wget", "mcrypt", "nscd", "htop", "zip", "unzip", 
        "mc", "libjemalloc1", "python3", "python3-pip", "python3-setuptools"
    ]
    
    for rPackage in rPackages:
        printc(f"Installing {rPackage}", Color.WARNING)
        os.system(f"apt-get install {rPackage} -y > /dev/null")
    
    printc("Installing libpng", Color.WARNING)
    os.system("wget -q -O /tmp/libpng12.deb http://mirrors.kernel.org/ubuntu/pool/main/libp/libpng/libpng12-0_1.2.54-1ubuntu1_amd64.deb")
    os.system("dpkg -i /tmp/libpng12.deb > /dev/null")
    os.system("apt-get install -y > /dev/null")  # Clean up
    
    try:
        os.remove("/tmp/libpng12.deb")
    except:
        pass
    
    # Create user
    if not os.path.exists("/home/xtreamcodes"):
        os.makedirs("/home/xtreamcodes")
    os.system("adduser --system --shell /bin/false --group --disabled-login xtreamcodes > /dev/null")
    
    return True

def install(rType="MAIN"):
    global rInstall, rDownloadURL
    printc("Downloading Software", Color.WARNING)
    
    rInstall = {"MAIN": "main", "LB": "sub"}
    rDownloadURL = {
        "main": "https://github.com/emre1393/xtreamui_mirror/releases/latest/download/main.tar.gz",
        "sub": "https://github.com/emre1393/xtreamui_mirror/releases/latest/download/LB.tar.gz"
    }
    
    try:
        rURL = rDownloadURL[rInstall[rType]]
    except:
        printc("Invalid download URL!", Color.FAIL)
        return False
    
    os.system(f'wget -q -O "/tmp/xtreamcodes.tar.gz" "{rURL}"')
    
    if os.path.exists("/tmp/xtreamcodes.tar.gz"):
        printc("Installing Software", Color.WARNING)
        os.system('chattr -f -i /home/xtreamcodes/iptv_xtream_codes/GeoLite2.mmdb > /dev/null')
        os.system(f'tar -zxvf "/tmp/xtreamcodes.tar.gz" -C "/home/xtreamcodes/" > /dev/null')
        try:
            os.remove("/tmp/xtreamcodes.tar.gz")
        except:
            pass
        return True
    
    printc("Failed to download installation file!", Color.FAIL)
    return False

def installadminpanel():
    printc("Downloading Admin Panel", Color.WARNING)
    os.system('wget -q -O "/tmp/update.zip" "https://github.com/emre1393/xtreamui_mirror/releases/latest/download/release_22f.zip"')
    
    if os.path.exists("/tmp/update.zip"):
        try:
            os.system('unzip -o /tmp/update.zip -d /tmp/update/ > /dev/null && cp -rf /tmp/update/XtreamUI-master/* /home/xtreamcodes/iptv_xtream_codes/ > /dev/null && rm -rf /tmp/update/XtreamUI-master > /dev/null && rm -rf /tmp/update > /dev/null && chown -R xtreamcodes:xtreamcodes /home/xtreamcodes > /dev/null')
            os.remove("/tmp/update.zip")
            printc("Admin Panel installed successfully", Color.GREEN)
            return True
        except:
            printc("Invalid link or zip file is corrupted!", Color.FAIL)
            os.remove("/tmp/update.zip")
            return False
    
    printc("Failed to download installation file!", Color.FAIL)
    return False

def mysql(rUsername, rPassword):
    global rMySQLCnf
    printc("Configuring MySQL", Color.WARNING)
    rCreate = True
    if os.path.exists("/etc/mysql/my.cnf"):
        if open("/etc/mysql/my.cnf", "r").read(14) == "# Xtream Codes":
            rCreate = False
    
    if rCreate:
        rFile = open("/etc/mysql/my.cnf", "w")
        rFile.write(rMySQLCnf)
        rFile.close()
        os.system("service mysql restart > /dev/null")
    
    printc("Enter MySQL Root Password:", Color.WARNING)
    for i in range(5):
        rMySQLRoot = input("  ")
        print(" ")
        if len(rMySQLRoot) > 0:
            rExtra = " -p%s" % rMySQLRoot
        else:
            rExtra = ""
        
        printc("Drop existing & create database? Y/N", Color.WARNING)
        if input("  ").upper() == "Y":
            rDrop = True
        else:
            rDrop = False
        
        try:
            if rDrop:
                # Use a safer mysql command to drop users
                os.system('mysql -u root%s -e "DROP USER IF EXISTS \'%s\'@\'%%\';" > /dev/null' % (rExtra, rUsername))
                os.system('mysql -u root%s -e "DROP USER IF EXISTS \'%s\'@\'localhost\';" > /dev/null' % (rExtra, rUsername))
                os.system('mysql -u root%s -e "CREATE USER IF NOT EXISTS \'%s\'@\'%%\' IDENTIFIED BY \'%s\';" > /dev/null' % (rExtra, rUsername, rPassword))
                os.system('mysql -u root%s -e "GRANT ALL PRIVILEGES ON *.* TO \'%s\'@\'%%\';" > /dev/null' % (rExtra, rUsername))
                printc("Database configured", Color.GREEN)
            else:
                printc("Skipping database configuration", Color.YELLOW)
        except:
            printc("Error configuring MySQL", Color.FAIL)

def main():
    printc("Starting Xtream Codes Modern Installation", Color.HEADER)
    if not prepare():
        return False
    
    printc("Starting main installation", Color.HEADER)
    if not install("MAIN"):
        return False
    
    printc("Starting admin panel installation", Color.HEADER)
    if not installadminpanel():
        return False
    
    printc("Starting MySQL configuration", Color.HEADER)
    mysql("xtreamcodes", "xtream123")
    
    printc("Installation completed successfully!", Color.GREEN)
    return True

if __name__ == "__main__":
    main()