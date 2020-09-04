from bs4 import BeautifulSoup as bs
import requests as req
import locale
from datetime import datetime as dt
import json


link_base = 'https://www.uvv.br/noticias-e-eventos/'

def retorna_links_paginacao(l_base,l_acesso):
    # l_base: link no qual sera feita a criacção do link completo
    # l_acesso: pagina que a função ira acessar
    _res = req.get(l_acesso)
    _res.encoding = "utf-8"

    _soup = bs(_res.text,'html.parser')

    paginacao = _soup.find(class_="paginacao")
    links_pgs_bruto = paginacao.find_all(class_="page-link")
    links = []
    for link in links_pgs_bruto:
        link_completo = l_base+link.get("href")
        if link_completo not in links:
            links.append(link_completo)     
    return links

# adicionando os links da primeira página acessada
links_paginas = retorna_links_paginacao(link_base,link_base)
continuar = True

while continuar: 
    # acessando o último link da lista inicial de links para coletar as próximas páginas
    novos_links = retorna_links_paginacao(link_base,links_paginas[len(links_paginas)-1])
    

    # checando se os links retornados já foram adicionados
    for link_novo in novos_links:
        if link_novo in links_paginas:
            continuar = False
            # se ao passar pelo último dos novos links, o mesmo já tiver sido adicionado, o ciclo encerra
        else:
            links_paginas.append(link_novo)
            continuar = True
    print(f"Links capturados: {len(links_paginas)}\n")


noticias = []

# cpaturar as noticias de cada página
for pagina in links_paginas:
    res = req.get(pagina)
    res.encoding = "utf-8"
    soup = bs(res.text,'html.parser')
    
    noticias_brutas = soup.find_all(class_="holder-noticia-unica")

    for noticia in noticias_brutas:
        n = {}

        title = noticia.find("h4").text
        n["title"]=title

        data_raw = noticia.find(class_="data").text
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        data = dt.strptime(data_raw,'%d, %B de %Y').strftime('%Y-%m-%d')
        n["date"]=data
        # extrai um datetime do texto na noticia e converte no formato apropriado

        link = noticia.a.get("href")
        n["link"]=link

        if n not in noticias:
            noticias.append(n)

    print(f"Noticias da página #{links_paginas.index(pagina)} adicionadas")        
        # na lista links_paginas são retornados dois valores que remetem a mesma página
        # assim essa checagem evita itens duplicados
        # https://www.uvv.br/noticias-e-eventos/?pagina=1  e https://www.uvv.br/noticias-e-eventos/# 



# salvando no arquivo json
with open('noticias.json','w',encoding='utf-8') as json_file:
    json.dump(noticias,json_file,indent=3, ensure_ascii=False)

