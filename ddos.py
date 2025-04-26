
from colorama import Fore, init  # For terminal colors
from urllib.parse import urlparse  # To analyze URLs
# Local modules
from modules.https.https import  https  # For HTTPS attackss
from modules.ip_atack.ip_atack import index  # For IP-based attacks
from modules.validar.validar import validar  # To validate quantity of packages
from modules.ddos_core.ddos_core import DDoSAttack
from modules.config.config import ConfigLoader


class Menu:
    """
    Displays the main menu and handles user input.
    """

    @staticmethod
    def display():
        """
        Displays the menu and handles user input for different attack options.
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
                [3] to test DDoS
                [0] quit
                Option:"""))
               
                if option == 1:
                    hostname, porta, quantidade = https.http(validar.validar_porta, validar.validar_quantidade)
                    if hostname is not None and door is not None and quantidade is not None:
                        DDoSAttack.main_ddos(hostname, door, quantidade)
                    else:
                        print(Fore.RED + "Invalid input for HTTPS attack.")

                elif option == 2:
                    ip, porta, quantidade = index.ip_attack(validar.validar_porta, validar.validar_quantidade)
                    if ip is not None and door is not None and quantidade is not None:
                        DDoSAttack.main_ddos(ip, door, quantidade)
                    else:
                        print(Fore.RED + "Invalid input for IP attack.")

                elif option == 3:
                    print(Fore.CYAN + "Option 3 selected: Testing DDoS with random IPs...")
                    door, quantity_ips, quantity_packages = ConfigLoader.load_config()
                    DDoSAttack.perform_ip_attack(door, quantity_ips, quantity_packages)

                elif option == 0:
                    print(Fore.CYAN + "Exiting...")
                    break
                else:
                    print(Fore.RED + "Invalid option. Try again.")
            except ValueError:
                print(Fore.RED + "Error: Please enter a valid number.")
            except Exception as e:
                print(Fore.RED + f"An unexpected error occurred: {e}")


# Initialize colorama for terminal colors
init(autoreset=True)

# Start the program
Menu.display()