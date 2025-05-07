class validate:
    @staticmethod
    def validate_port(porta):
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

    @staticmethod
    def validate_quantity(quantidade):
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


# Automated Tests
import unittest

class TestValidate(unittest.TestCase):
    def test_validate_port_valid(self):
        """
        Tests validate_port with valid port numbers.
        """
        self.assertEqual(validate.validate_port(80), 80)
        self.assertEqual(validate.validate_port(443), 443)
        self.assertEqual(validate.validate_port(65535), 65535)

    def test_validate_port_invalid(self):
        """
        Tests validate_port with invalid port numbers.
        """
        with self.assertRaises(ValueError):
            validate.validate_port(0)  # Below valid range
        with self.assertRaises(ValueError):
            validate.validate_port(65536)  # Above valid range

    def test_validate_quantity_valid(self):
        """
        Tests validate_quantity with valid quantities.
        """
        self.assertEqual(validate.validate_quantity(0), 0)
        self.assertEqual(validate.validate_quantity(10), 10)

    def test_validate_quantity_invalid(self):
        """
        Tests validate_quantity with invalid quantities.
        """
        with self.assertRaises(ValueError):
            validate.validate_quantity(-1)  # Negative quantity


# Runs tests if the file is executed directly
if __name__ == "__main__":
    unittest.main()