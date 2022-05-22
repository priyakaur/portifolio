import re
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

base = "https://www.dictionary.com/browse/"

csv = pd.read_csv("words.csv")
meaning = []
pronounce = []
password = []
words = csv["Word"]

for word in words:
    url = base + word
    try:
        read = requests.get(url,allow_redirects=True)
        LK = read.url
        print(LK)
        Link = requests.get(LK)
        link = bs(Link.content,'html.parser')
    except:
        pro=""
        final = ""
    try:
        WO = link.find("h1",attrs={"data-first-headword":"true"})
        wo = WO.text
    except:
        wo=""
    try:
        PRO = link.find("span",attrs={"class":"pron-spell-content css-7iphl0 evh0tcl1"})
        pro = PRO.text
    except:
        pro = ""
    try:
        M1 = link.find("div",attrs={"value":"1"})
        m1 = M1.text + ", "
    except:
        m1 = ""
    try:
        M2 = link.find("div",attrs={"value":"2"})
        m2 = M2.text + ", "
    except:
        m2 = ""
    try:
        M3 = link.find("div",attrs={"value":"3"})
        m3 = M3.text + ", "
    except:
        m3 = ""
    try:
        M4 = link.find("div",attrs={"value":"4"})
        m4 = M4.text
    except:
        m4=""
    final = m1+ m2 +m3 + m4
    print(final)
    print(wo)
    print(pro)
    pronounce.append(pro)
    meaning.append(final)
    password.append(wo)
    print("Done")

csv["Meaning"] = meaning
csv["Pronunciation"] = pronounce
csv["password"] = password

csv.to_csv("meaning.csv")
print("CSV created!!")
