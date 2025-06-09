# 📌 Code Explanation  

## 🔹 **Imports Necessary Modules**  
- `json.load` → Used to read and parse JSON files.  
- `os` → Used to handle file paths dynamically.  

## 🏗️ **Class Definition: `ConfigLoader`**  
This class is designed to **read configuration settings** from a JSON file.  

## ⚙️ **Method: `load_config()`**  

### 📂 **Builds the file path**  
- Constructs the path to `config.json` by **navigating up two directories** from the current file location.  

### 📖 **Opens and reads the JSON file**  
- Loads the contents of `config.json` into a **Python dictionary** for easy access.  

### 🔍 **Extracts specific values**  
Retrieves three key configuration settings:  
- **`"door"`** → Likely represents a **port number** (integer).  
- **`"quantity_ips"`** → Could represent the **number of IPs** involved in an operation.  
- **`"quantity_packages"`** → Might indicate the **number of data packets** to be sent.  

## 🔄 **Returns a tuple**  
- The method returns these three values as a **tuple**:  
  ```python
  (door, quantity_ips, quantity_packages)
