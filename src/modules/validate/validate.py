class Validate:
    @staticmethod
    def validate_port(porta):
        """
        Function to validate the target port.

        Parameter:
            porta (int): Port number.

        Returns:
            porta (int): Validated port.

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
            quantidade (int): Number of packets to be sent.

        Returns:
            quantidade (int): Validated quantity.

        Exceptions:
            Raises an error if the quantity is negative.
        """
        if quantidade < 0:
            raise ValueError("Quantity cannot be negative.")
        return quantidade
