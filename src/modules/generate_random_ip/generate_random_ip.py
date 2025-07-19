import asyncio
import random

class IPGeneratorStrategy:
    """
    Abstract base class for IP address generation strategies.
    """
    async def generate(self):
        """
        Asynchronously generates an IP address.
        Must be implemented by subclasses.
        """
        raise NotImplementedError


class RandomIPv4Generator(IPGeneratorStrategy):
    """
    Strategy for generating a random IPv4 address.
    """
    async def generate(self):
        """
        Asynchronously generates a random IPv4 address.
        
        Returns:
            str: A randomly generated IPv4 address.
        """
        return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"


class StaticListGenerator(IPGeneratorStrategy):
    """
    Strategy for selecting an IP address from a static list.
    
    Args:
        ip_list (list): List of predefined IP addresses.
    """
    def __init__(self, ip_list):
        self.ip_list = ip_list

    async def generate(self):
        """
        Asynchronously selects and returns a random IP from the static list.
        
        Returns:
            str: A randomly selected IP address from the provided list.
        """
        return random.choice(self.ip_list)


class IPGeneratorFactory:
    """
    Factory class to provide an appropriate IP generation strategy.
    """
    @staticmethod
    def get_strategy(mode="random", ip_list=None) -> IPGeneratorStrategy:
        """
        Returns the appropriate IP generation strategy based on mode.
        
        Args:
            mode (str): Strategy type. Options are 'random' or 'static'.
            ip_list (list, optional): List of IPs required for 'static' mode.
        
        Returns:
            IPGeneratorStrategy: An instance of the selected strategy class.
        """
        if mode == "static" and ip_list:
            return StaticListGenerator(ip_list)
        return RandomIPv4Generator()
