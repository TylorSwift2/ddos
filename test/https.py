from urllib.parse import urlparse
from colorama import Fore
from io import StringIO
import unittest
import sys

class https:
    @staticmethod
    def http(validar_porta, validar_quantidade):
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


# Automated Tests
class TestHttps(unittest.TestCase):
    def test_http_valid_input(self):
        """
        Tests the http function with simulated valid inputs.
        """
        def mock_validar_porta(porta):
            if porta not in [80, 443]:
                raise ValueError("Invalid port")

        def mock_validar_quantidade(quantidade):
            if quantidade < 0:
                raise ValueError("Invalid quantity")

        simulated_input = "http://example.com\n80\n10\n"
        sys.stdin = StringIO(simulated_input)  # Simulates user inputs

        try:
            hostname, porta, quantidade = https.http(mock_validar_porta, mock_validar_quantidade)
            self.assertEqual(hostname, "example.com")
            self.assertEqual(porta, 80)
            self.assertEqual(quantidade, 10)
        finally:
            sys.stdin = sys.__stdin__  # Restore original stdin



    def test_http_invalid_url(self):
        """
        Tests the http function with an invalid URL.


        """
        simulated_input = "invalid-url\n"
        sys.stdin = StringIO(simulated_input)  # Simulates user inputs

        try:
            hostname, porta, quantidade = https.http(lambda x: x, lambda x: x)
            self.assertIsNone(hostname)
            self.assertIsNone(porta)
            self.assertIsNone(quantidade)
        finally:
            sys.stdin = sys.__stdin__  # Restore original stdin
    def test_http_invalid_port(self):
        """
        Tests the http function with an invalid port.
        """
        def mock_validar_porta(porta):
            if porta not in [80, 443]:
                raise ValueError("Invalid port")

        simulated_input = "http://example.com\n9999\n"
        sys.stdin = StringIO(simulated_input)  # Simulates user inputs



        try:
            hostname, porta, quantidade = https.http(mock_validar_porta, lambda x: x)
            self.assertIsNone(hostname)
            self.assertIsNone(porta)
            self.assertIsNone(quantidade)
        finally:
            sys.stdin = sys.__stdin__  # Restore original stdin




#Runs tests if file is executed directly
if __name__ == "__main__":
    unittest.main()