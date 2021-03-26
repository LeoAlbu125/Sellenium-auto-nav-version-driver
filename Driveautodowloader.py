import wget #utilizar essa biblioteca para fazer dowload dos chrome drivers
from Mainfile import googlev
import shutil
import subprocess
import os
import pathlib
'''
try:
    os.remove(str(pathlib.Path().absolute())+r'\chromedriver_win32.zip')
    os.remove(str(pathlib.Path().absolute())+r'\Webdrivers\chromedriver_win32.zip')
except Exception as e:
    pass
    
listavg = []
listavd = []

with open("listaversaogoogle.txt", "r") as rfile1:
    for i in rfile1:
        listavg.append(i.rstrip().strip( ))
    i = 0

with open('listaversaodrivers.txt', 'r') as rfile2:
    for i in rfile2:
        listavd.append(i.rstrip().strip( ))
    i = 0

versiondict = dict(zip(listavg, listavd))

output = subprocess.check_output(
        r'wmic datafile where name="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" get Version /value',
        shell=True
    )

v = output.decode('utf-8').strip()[8:10]

'''

class autoget: 
    def getdriver():
        try:
            os.remove(str(pathlib.Path().absolute())+r'\Webdrivers\chromedriver_win32.zip')
            os.remove(str(pathlib.Path().absolute())+r'\chromedriver_win32.zip')
            
        except Exception as e:
            pass
            
        listavg = []
        listavd = []

        with open("listaversaogoogle.txt", "r") as rfile1:
            for i in rfile1:
                listavg.append(i.rstrip().strip( ))
            i = 0

        with open('listaversaodrivers.txt', 'r') as rfile2:
            for i in rfile2:
                listavd.append(i.rstrip().strip( ))
            i = 0

        versiondict = dict(zip(listavg, listavd))

        output = subprocess.check_output(
                r'wmic datafile where name="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" get Version /value',
                shell=True
            )

        v = output.decode('utf-8').strip()[8:10]


        wget.download(f'https://chromedriver.storage.googleapis.com/{versiondict[v]}/chromedriver_win32.zip')
        shutil.move(str(pathlib.Path().absolute())+r'\chromedriver_win32.zip',str(pathlib.Path().absolute())+r'\Webdrivers')
        
        
        
        


autoget.getdriver()