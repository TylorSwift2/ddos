import asyncio
from colorama import init, Fore

from src.modules.https.https import HTTPSStrategy
from src.modules.ip_atack.ip_atack import IPAttackStrategy
from src.modules.validate.validate import Validate
from src.modules.ddos_core.ddos_core import DDoSAttack
from src.modules.config.config import ConfigLoader

class MainMenu:
    @staticmethod
    async def display():
        while True:
            try:
                option = int(input(Fore.CYAN + """
                 ██████╗ ██████╗  ██████╗ ███████╗
                ██╔══██╗██╔══██╗██╔═══██╗██╔════╝
                ██║  ██║██║  ██║██║   ██║███████╗
                ██║  ██║██║  ██║██║   ██║╚════██║
                ██████╔╝██████╔╝╚██████╔╝███████║
                ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
                [1] HTTPS Attack
                [2] IP Attack
                [3] Random IP DDoS Test
                [0] Quit
                Option: """))

                if option == 1:
                    hostname, port, quantity = await HTTPSStrategy.get_target(
                        Validate.validate_port,
                        Validate.validate_quantity
                    )
                    if hostname is not None and port is not None and quantity is not None:
                        await DDoSAttack.launch_async_ddos(hostname, port, quantity)
                    else:
                        print(Fore.RED + "Invalid input for HTTPS attack.")

                elif option == 2:
                    ip, port, quantity = await IPAttackStrategy.get_target(
                        Validate.validate_port,
                        Validate.validate_quantity
                    )
                    if ip is not None and port is not None and quantity is not None:
                        await DDoSAttack.launch_async_ddos(ip, port, quantity)
                    else:
                        print(Fore.RED + "Invalid input for IP attack.")

                elif option == 3:
                    try:
                        port, quantity_ips, quantity_packages = await ConfigLoader.load_config()
                        await DDoSAttack.perform_ip_attack_async(port, quantity_ips, quantity_packages)
                    except Exception as e:
                        print(Fore.RED + f"Failed to load config: {e}")

                elif option == 0:
                    print(Fore.CYAN + "Exiting...")
                    break
                else:
                    print(Fore.RED + "Invalid option.")
            except ValueError:
                print(Fore.RED + "Please enter a valid number.")
            except Exception as e:
                print(Fore.RED + f"Unexpected error: {e}")

# Start menu
if __name__ == "__main__":
    init(autoreset=True)
    asyncio.run(MainMenu.display())
