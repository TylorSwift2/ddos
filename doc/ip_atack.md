# IP Attack: Function Overview

---

**🔍 What does it do?**

- **Prompts** the user for a destination IP address and checks that it is in the correct IPv4 format.
- **Validates** the IP using `inet_aton()`, ensuring it is a valid address.
- **Requests** a port number (typically 80 for HTTP or 443 for HTTPS).
- **Asks** for the number of attacks (entering 0 allows for indefinite attacks).
- **Returns** the IP, port, and number values, which can be used to launch an attack.

---