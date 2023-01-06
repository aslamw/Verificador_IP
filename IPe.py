import re, json, webbrowser
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

resposta = urlopen(url)

dados = json.loads(resposta)

ip = dados['ip']
org = dados['org']
cid = dados['city']
pais = dados['country']
regiao = dados['regiao']

print(f'Detalhes do IP externo \n IP: {ip} Região: {regiao} Pais: {pais} Cidade: {cid} Org: {org}')