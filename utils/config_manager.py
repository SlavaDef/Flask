from pathlib import Path
import configparser


class ConfigManager:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config_path = Path(__file__).parent.parent / 'config' / 'config.ini'

        if not self.config.read(self.config_path):
            raise FileNotFoundError(f"Конфігураційний файл не знайдено: {self.config_path}")

    @property
    def api_url(self):
        return (
            f"{self.config['API']['base_url']}"
            f"?access_key={self.config['API']['api_key']}"
            f"&currencies={self.config['API']['currencies']}"
            f"&format=1"
        )


# Створюємо singleton
config = ConfigManager()