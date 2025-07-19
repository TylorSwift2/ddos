from urllib.parse import urlparse
from colorama import Fore

class HTTPSStrategy:
    """
    Handles target extraction and validation for HTTPS-based attacks.
    """

    @staticmethod
    async def get_target(validate_port, validate_quantity):
        """
        Asynchronously retrieves and validates target parameters for an HTTPS attack.

        Args:
            validate_port (function): Function to validate the port number.
            validate_quantity (function): Function to validate the number of requests.

        Returns:
            tuple: (hostname, port, quantity), or (None, None, None) on error.
        """
        try:
            url = input("Enter the target URL (with http:// or https://): ")
            parsed_url = urlparse(url)

            if not parsed_url.scheme or not parsed_url.hostname:
                print(Fore.RED + "Error: Invalid URL. Please include http:// or https://.")
                return None, None, None

            hostname = parsed_url.hostname

            port = int(input("Which port do you want to attack? (usually 80 or 443): "))
            validate_port(port)

            quantity = int(input("How many times do you want to attack? (set 0 for indefinite attack): "))
            validate_quantity(quantity)

            return hostname, port, quantity
        except ValueError as e:
            print(Fore.RED + f"Input error: {e}")
            return None, None, None
        except Exception as e:
            print(Fore.RED + f"Unexpected error: {e}")
            return None, None, None
