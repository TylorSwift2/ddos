from colorama import Fore, init

import socket


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
        ip = input("enter the target IP address: ")

        socket.inet_aton(ip)  

        door = int(input("which port do you want to attack? (usually 80 or 443): "))

        validar_porta(door)

        quantidade = int(input("quantas vezes voce quer atacar? (coloque 0 para ataque indefinido): "))
        validar_quantidade(quantidade)
    except socket.error:
        print(Fore.RED + "Error: Invalid IP.")

        return None, None, None
    except ValueError as e:
        print(Fore.RED + f"Input error: {e}")

        return None, None, None
    
    return ip, door, quantidade
