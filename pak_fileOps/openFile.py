
#module: pak_fileOps.openFile.py
#version: 0.1
#author: andrew christ
#email: andrew.christ@gmail.com
#last update: 7-18-2015
#notes:

import os, sys, subprocess

def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener ="open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])
