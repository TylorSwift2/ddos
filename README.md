# DDoS (Distributed Denial of Service)

## 📖 Description
A Distributed Denial of Service (DDoS) is a type of cyber attack that aims to overload a system, server, or network with excessive traffic, rendering it unavailable to legitimate users. This project is a Python-based tool designed for educational and testing purposes.

## 🚀 Features
- 🌐 **High Request Rate**: Sends up to 1000 requests per second.
- 🔌 **Port Flexibility**: Supports all ports (1-65535).
- 🖥️ **Cross-Platform**: Compatible with any operating system that supports Python 3.
- 🛠️ **Customizable**: Easily configurable via a JSON file (`config.json`) for IPs, ports, and packet quantities.

## ⚙️ Installation
Follow these steps to set up and run the project:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/TylorSwift2/ddos.git
   cd ddos
   ```

2. **Install Dependencies**:
   Make sure you have Python 3 installed, then run:
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Configure the test Attack**:
   Edit the `config.json` file to set the number of IPs, port, and packet quantity:
   ```json
   {
    "quantity_ips": 10,
    "door": 80,
    "quantity_packages": 100
   }
   ```

4. **Run the Script**:
   Execute the script with:
   ```bash
   python3 ddos.py
   ```

## 📝 Usage
- **Option 1**: Perform an HTTPS attack.
- **Option 2**: Perform an IP-based attack.
- **Option 3**: Test DDoS functionality with random IPs.
- **Option 0**: Quit the program.

## ⚠️ Important Notes
- This tool is intended **only for educational purposes** and testing in environments where you have explicit permission.
- **The developers are not responsible for any misuse of this project.**
- Always obtain permission from the target system's owner before performing any tests.

## 📂 Project Structure
```
ddos/
├── ddos.py               # Main script
├── config.json           # Configuration file for attack test parameters
├── modules/              # Contains helper modules
│   ├── https/            # HTTPS attack logic
│   ├── ddos_core/        # ddos core
│   ├── config/           # config json
│   ├── ip_atack/         # IP attack logic
│   ├── generate_random_ip/ # Random IP generator
│   ├── validar_porta/    # Port validation
│   ├── validar_quantidade/ # Quantity validation
├── report/               # Logs and reports
└── README.md             # Project documentation
```

## 🛡️ Disclaimer
This project is for **educational purposes only**. Unauthorized use of this tool to attack systems without permission is illegal and unethical. Use responsibly.
