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
