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
