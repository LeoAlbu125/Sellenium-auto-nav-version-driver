import subprocess
import pathlib

def verdict():
    listavg = []
    listavd = []

    with open("listaversaogoogle.txt", "r") as rfile1:
        for i in rfile1:
            listavg.append(i.rstrip())
        i = 0

    with open('listaversaodrivers.txt', 'r') as rfile2:
        for i in rfile2:
            listavd.append(i.rstrip())
        i = 0

    versiondict = dict(zip(listavg, listavd))
    return versiondict

def googlev():
    output = subprocess.check_output(
        r'wmic datafile where name="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" get Version /value',
        shell=True
    )

    return output.decode('utf-8').strip()[8:10]

    # print(pathlib.Path().absolute())
