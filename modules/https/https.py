from urllib.parse import urlparse
from colorama import Fore

def https(validar_porta, validar_quantidade):
    """
    Function to extract and validate the target details from a user-provided URL.

    Parameters:
        validar_porta (function): Function to validate the port number.
        validar_quantidade (function): Function to validate the number of requests.

    Returns:
        tuple: (hostname, port, quantity) if valid; otherwise, (None, None, None).
    """
    try:
        url = input("Enter the target URL (with http:// or https://): ")
        parsed_url = urlparse(url)

        if not parsed_url.scheme or not parsed_url.hostname:
            print(Fore.RED + "Error: Invalid URL. Please include http:// or https://.")
            return None, None, None

        hostname = parsed_url.hostname
        

        porta = int(input("Which port do you want to attack? (usually 80 or 443): "))
        validar_porta(porta)
        

        quantidade = int(input("How many times do you want to attack? (set 0 for indefinite attack): "))
        validar_quantidade(quantidade)
       

        return hostname, porta, quantidade
    except ValueError as e:
        print(Fore.RED + f"Input error: {e}")
        return None, None, None