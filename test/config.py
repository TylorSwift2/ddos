from json import load  # To manipulate JSON files
import os  # To handle file paths

class ConfigLoader:
    """
    Handles loading configuration from the config.json file.
    """

    @staticmethod
    def load_config():
        """
        Reads settings from the config.json file and returns the required values.
        Returns:
            tuple: door (int), quantity_ips (int), quantity_packages (int)
        """
        # Build the path to the config.json file by going up two directories
        config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'config.json')

        # Open and load the JSON file
        with open(config_path, 'r') as config_file:
            config = load(config_file)

        # Return the required configuration values
        return config["door"], config["quantity_ips"], config["quantity_packages"]
# Runs tests if the file is executed directly
if __name__ == "__main__":
    import unittest
    unittest.main()