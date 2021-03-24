import re
import requests

try:
    cfile = open("listaversaodrivers.txt","x")
    cfile.close()

except:
    pass

try:
    cfile2 = open('listaversaogoogle.txt','x')
    cfile2.close()
    
except Exception as e:

    r = requests.get('https://chromedriver.chromium.org/downloads')

    Vdrive1 = re.findall(r'(?<=ChromeDriver) \d{2}.\d{1}.\d{4}.\d{2}',r.text)

    Vdrive2 = re.findall(r'(?<=ChromeDriver) \d.\d{2}',r.text)

    Vgoogle1 = re.findall(r"(?<=Supports Chrome version) \d{2}",r.text)

    Vgoogle2 = re.findall(r"(?<=Supports Chrome) v\d{2}-\d{2}",r.text)

    with open('listaversaodrivers.txt','w') as  wfile:

        for i in range(len(Vdrive1)):
            wfile.write(Vdrive1[i]+'\n')
        i = 0

        for k in range(len(Vdrive2)):
            wfile.write(Vdrive2[k]+'\n')
        k = 0

    with open("listaversaogoogle.txt","w") as wfile2:

        for i in range(len(Vgoogle1)):
            wfile2.write(Vgoogle1[i]+'\n')
        i = 0

        for k in range(len(Vgoogle2)):
            wfile2.write(Vgoogle2[k]+'\n')
        k=0