import ssl
import urllib.request

context = ssl._create_unverified_context()

try:
    site = urllib.request.urlopen('https://www.pudim.com.br/', context=context)

except urllib.request.URLError as e:
    print(f'\033[1;31mO site não está acessível no momento. Erro: {e.reason}\033[m')
else:
    print('\033[1;32mConsegui abrir o site com sucesso!\033[m')
    #print(site.read()) forma para ler o html de um site
