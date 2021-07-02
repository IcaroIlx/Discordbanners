import requests
import sys
import os
  
try:
    token = sys.argv[1]
    base = sys.argv[2]
    dt = "Imagens/" + base

    cabecalho = {'Host': 'discord.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
                'Accept': '*/*',
                'Accept-Language': 'pt-BR',
                'Accept-Encoding': 'gzip, deflate, br',
                'Content-Type': 'application/json',
                'Authorization': token,
                'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJwdC1CUiIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2Ojg5LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvODkuMCIsImJyb3dzZXJfdmVyc2lvbiI6Ijg5LjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODg4NjMsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
                'Content-Length': '743295',
                'Origin': 'https://discord.com',
                'Connection': 'keep-alive',
                'Referer': 'https://discord.com/channels/@me',
                'Cookie': '__dcfduid=23ab57daeb9eb87c5dfa68a1c83cd9f7; OptanonConsent=isIABGlobal=false&datestamp=Mon+Jun+28+2021+09%3A42%3A43+GMT-0300+(Brasilia+Standard+Time)&version=6.17.0&hosts=&consentId=7a4ac5a6-1429-4fec-a79b-fe6d336cbf33&interactionCount=1&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0; locale=pt-BR',
                'TE': 'Trailers'}


    sla = open(dt, 'r')
    info = '{"banner":"data:image/gif;base64,' + sla.read() + '"}'
    #print(str(info))
    data = str(info)
    requisicao = requests.patch('https://discord.com/api/v9/users/@me', headers=cabecalho, data=data)
    print(requisicao.text)
# Apaga tudo !!
    os.remove('Imagens/' + sys.argv[1] + '.txt')
    os.remove('Imagens/' +  sys.argv[1] + '.gif') 
    print("%s Removido com sucesso")

except Exception as e:
    print(e)  