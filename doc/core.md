# 🔍 Code Analysis  

## 📥 **Importing Modules**  
- **`socket`** → Used to send data packets over the network.  
- **`threading`** → Creates multiple threads to increase the intensity of the attack.  
- **`colorama`** → Colors messages on the terminal for better readability.  
- **`_urandom`** → Generates random data packets.  

## 🚀 **`DDoSAttack` Class**  

### 🔹 `perform_ip_attack(port, number_ips, number_packets)`  
- Generates **random IPs** and starts attacks against them.  
- Logs attacks in a **report file (`report.log`)**.  

### 🔹 `main_ddos(hostname, port, number)`  
- Resolves the **target's IP** and starts multiple threads to send packets.  
- Uses `_urandom(1490)` to generate **1490-byte packets** and send them to the target.  

### 🔹 `execute_attack(target, bytes, number)`  
- Sends **UDP packets** to the target **indefinitely** or until the specified number is reached.  
- Displays messages on the terminal **tracking the number of packets sent**.  
