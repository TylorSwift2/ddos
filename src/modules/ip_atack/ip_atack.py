from colorama import Fore
from socket import inet_aton, error as socket_error

class IPAttackStrategy:
    """
    Handles target input and validation for IP-based attack strategies.
    """

    @staticmethod
    async def get_target(validate_port, validate_quantity):
        """
        Asynchronously retrieves and validates IP attack parameters from user input.

        Args:
            validate_port (function): Function to validate port number.
            validate_quantity (function): Function to validate request quantity.

        Returns:
            tuple: (ip, port, quantity) if valid; otherwise, (None, None, None).
        """
        try:
            ip = input("Enter the target IP address: ")
            if len(ip.split('.')) != 4:
                raise ValueError("Invalid IP format. Please enter a valid IPv4 address.")

            # Validate IP format (throws socket.error if invalid)
            inet_aton(ip)

            port = int(input("Which port do you want to attack? (usually 80 or 443): "))
            validate_port(port)

            quantity = int(input("How many times do you want to attack? (enter 0 for indefinite attack): "))
            validate_quantity(quantity)

            print(Fore.GREEN + f"Validated inputs: IP={ip}, Port={port}, Quantity={quantity}")
            return ip, port, quantity

        except socket_error:
            print(Fore.RED + "Error: Invalid IP address.")
            return None, None, None
        except ValueError as e:
            print(Fore.RED + f"Input error: {e}")
            return None, None, None
        except Exception as e:
            print(Fore.RED + f"Unexpected error: {e}")
            return None, None, None
