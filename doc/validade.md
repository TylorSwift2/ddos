🔍 What does it do?

- **validate_port(port)**  
  Checks if the port number is within the valid range (1 to 65535).  
  If the value is outside this range, it raises a `ValueError`.

- **validate_quantity(quantity)**  
  Checks if the number of packets to be sent is not negative.  
  If the value is less than 0, it raises a `ValueError`.