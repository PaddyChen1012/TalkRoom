import requests
from bs4 import BeautifulSoup

html = requests.get("https://sg.news.yahoo.com/sports/")
sp = BeautifulSoup(html.text,"html.parser")
v = sp.find_all("a","js-content-viewer wafer-caas Fw(b) Fz(20px) Lh(23px) Fz(17px)--sm1024 Lh(19px)--sm1024 mega-item-header-link Td(n) C(#0078ff):h C(#000) LineClamp(2,46px) LineClamp(2,38px)--sm1024 not-isInStreamVideoEnabled")

Jsondata=[]
for s in v:
    dataTitle=s.text.strip()
    dataUrl="https://sg.news.yahoo.com" + s.get("href")
    Jsondata = Jsondata + [{'title' : dataTitle,'url' : dataUrl}]
    print("標題 : " + dataTitle,"網址 : " + dataUrl)


import json
with open("data.json",mode="w",encoding="utf-8") as file:
    finalData = json.dump(Jsondata,file)

