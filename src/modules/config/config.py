import os
import json
import asyncio

class ConfigLoader:
    """
    Async loader for configuration from JSON files.
    Supports multiple config profiles (like 'test', 'prod', etc.).
    """

    @staticmethod
    async def load_config(profile="default"):
        """
        Asynchronously reads settings from config.json and returns values.
        
        Args:
            profile (str): Optional config profile.

        Returns:
            tuple: door (int), quantity_ips (int), quantity_packages (int)
        """
        config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'config.json')

        # Load file asynchronously
        loop = asyncio.get_event_loop()
        with open(config_path, 'r') as config_file:
            raw_data = await loop.run_in_executor(None, config_file.read)

        config = json.loads(raw_data)

        # Load profile or default values
        cfg = config.get(profile, config)
        return cfg["door"], cfg["quantity_ips"], cfg["quantity_packages"]
