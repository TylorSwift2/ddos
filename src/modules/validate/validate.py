class Validate:
    """
    Provides static validation methods for input parameters such as port number and quantity.
    """

    @staticmethod
    def validate_port(port):
        """
        Validates the given port number.

        Args:
            port (int): The port number to validate.

        Returns:
            int: The validated port number.

        Raises:
            ValueError: If the port number is outside the valid range (1-65535).
        """
        if port < 1 or port > 65535:
            raise ValueError("Invalid port. Enter a value between 1 and 65535.")
        return port

    @staticmethod
    def validate_quantity(quantity):
        """
        Validates the number of packets to send.

        Args:
            quantity (int): The number of packets to validate.

        Returns:
            int: The validated quantity.

        Raises:
            ValueError: If the quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        return quantity
