import pandas as pd

tabelas = pd.read_html("https://www.cnnbrasil.com.br/esportes/futebol/tabela-do-brasileirao/")

tabela = tabelas[0]

tabela_filtrada = tabela[["Classificação"]]

# print(tabela)
print(tabela_filtrada)