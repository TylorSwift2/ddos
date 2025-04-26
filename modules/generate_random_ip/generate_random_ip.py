from random import randint
class generate_ip:

    @staticmethod
    def generate_random_ip():
        """
    Generates a valid random IP address.
        """
        return f"{randint(1, 255)}.{randint(0, 255)}.{randint(0, 255)}.{randint(0, 255)}"
    # Definition of the test_ddos_with_ips function