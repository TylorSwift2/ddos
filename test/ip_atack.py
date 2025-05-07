from colorama import Fore

from socket import inet_aton, error
class index:
    @staticmethod

    def ip_attack(validar_porta, validar_quantidade):
        """
        Function to extract and validate the target IP and port for an attack.

        Parameters:
            validar_porta (function): Function that validates the provided port number.
            validar_quantidade (function): Function that validates the number of requests.

        Returns:
            tuple: (ip, door, quantity) if valid; otherwise, (None, None, None).
        """
        try:
            ip = input("Enter the target IP address: ")
            if len(ip.split('.')) != 4:
                raise ValueError("Invalid IP format. Please enter a valid IPv4 address.")
            inet_aton(ip)  # Validate the IP format

            door = int(input("Which port do you want to attack? (usually 80 or 443): "))
            validar_porta(door)

            quantidade = int(input("How many times do you want to attack? (enter 0 for indefinite attack): "))
            validar_quantidade(quantidade)

            print(Fore.GREEN + f"Validated inputs: IP={ip}, Port={door}, Quantity={quantidade}")
            return ip, door, quantidade
        except error:
            print(Fore.RED + "Error: Invalid IP address.")
            return None, None, None
        except ValueError as e:
            print(Fore.RED + f"Input error: {e}")
            return None, None, None