#module: pak_fileOps.fileUtility.py
#version: 0.1
#author: andrew christ
#email: andrew.christ@gmail.com
#last update:
#notes:

import sys
import os

def appendFile(filename,contents):
    originalContents=returnListFromFile(file)
    for line in contents:
        originalContents.append(line)
    writeFile(filename,originalContents)

def deleteFile(filename):
    os.remove(filename)

def writeFile(filename,contents):
    fileObj=open(filename,'w') #the 'w' (write) tells the interpreter to create the file and then open it
    for line in contents:
        fileObj.write(line+'\n') # writes in the line and then adds a new line / drops the cursor
    fileObj.close

def returnListFromFile(filename):
    list1=[]
    try:
        for line in open(filename):
            line=line.rstrip() #removes whitespace characters
            list1.append(line)
    except FileNotFoundError:
        sys.exit(0)
    return list1
