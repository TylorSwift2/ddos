from urllib.parse import urlparse
from colorama import Fore, init
def https(validar_porta,validar_quantidade ):
    """
    Function to extract and validate the target details from a user-provided URL.

    Parameters:
        validar_porta (function): Function to validate the port number.
        validar_quantidade (function): Function to validate the number of requests.

    Returns:
        tuple: (hostname, port, quantity) if valid; otherwise, (None, None, None).
    """
    url = input("enter the target URL (with http:// or https://): ")
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname
    
    try:
        porta = int(input("which port do you want to attack? (usually 80 or 443):"))
        validar_porta(porta)
        quantidade = int(input("How many times do you want to attack? (set 0 for indefinite attack):"))
        validar_quantidade(quantidade)
    except ValueError as e:
        print(Fore.RED + f"Input error: {e}")
        return None, None, None
    
    return hostname, porta, quantidade
