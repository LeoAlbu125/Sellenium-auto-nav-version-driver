import re
import requests

try:
    cfile = open("listaversaodrivers.txt","x")
    cfile.close
except Exception as e:
    r = requests.get('https://chromedriver.chromium.org/downloads')
    values = re.findall(r'(?<=ChromeDriver) \d{2}.\d{1}.\d{4}.\d{2}',r.text)
    with open('listaversaodrivers.txt','w') as  wfile:
        for i in range(len(values)):
            wfile.write(values[i]+'\n')


