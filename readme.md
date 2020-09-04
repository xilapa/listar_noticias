### Listar notícias

Projeto de web scrapping feito com auxílio do desafio prático "Extraindo dados da web com Python" ministrada por André Soares da **Digital Innovation One**

#### Objetivo

O objetivo deste pequeno projeto foi salvar as notícias do site da Universidade Vila Velha em um arquivo JSON formatado como no exemplo a seguir.

```json
   {
      "title": "Datas do Vest UVV 2021/1",
      "date": "2020-09-03",
      "link": "https://www.uvv.br/2020/09/03/datas-do-vest-uvv-2021-1/"
   }
```

#### Melhorias 

Como melhorias ao código apresentado na aula foi feito:
- Captura das notícias de **todas** as páginas de notícias do site
- Conversão da data capturada para um formato adequado ao armazenamento em banco de dados