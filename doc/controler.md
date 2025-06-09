# Controller Overview

## Attack Types

### HTTPS Attack
**Function:** `https.http(validate.validate_port, validate.validate_quantity)`  
Sends a large number of HTTPS requests to a target server, attempting to overload it.

---

### IP Attack
**Function:** `index.ip_attack(validate.validate_port, validate.validate_quantity)`  
Sends packets directly to a specific IP address, attempting to bring down the service.

---

### DDoS Test
**Function:** `DDoSAttack.perform_ip_attack(port, quantity_ips, quantity_packages)`  
Simulates a DDoS attack using multiple random IPs.

---

## Configuration and Validation

- Uses the `validate` module to check the number of packets and ports used.
- `ConfigLoader.load_config()` loads configurations for automated attacks.