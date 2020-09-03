from bs4 import BeautifulSoup as bs
import requests as req
import locale
from datetime import datetime as dt
import json


res = req.get('https://www.uvv.br/noticias-e-eventos/')
res.encoding = "utf-8"

soup = bs(res.text,'html.parser')

all_posts = soup.find_all(class_="holder-noticia-unica")

noticias = []

# separando cada noticia
for post in all_posts:
    title = post.find("h4").text

    data_raw = post.find(class_="data").text
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    data = dt.strptime(data_raw,'%d, %B de %Y').strftime('%Y-%m-%d')
    # extrai um datetime do texto no post e converte no formato apropriado

    link = post.a.get("href")
    noticias.append({'title': title,'date': data,'link': link})

# salvando no arquivo json
with open('noticias.json','w',encoding='utf-8') as json_file:
    json.dump(noticias,json_file,indent=3, ensure_ascii=False)

