import os
import json
from os.path import join
from pathlib import Path


class SettingsHelper:
    def __init__(self):
        self.meltano_model_path = join(os.getcwd(), "model")

        self.settings_file_path = Path(self.meltano_model_path).joinpath(
            "database.settings.ma"
        )
        if not self.settings_file_path.is_file():
            with open(self.settings_file_path, "w") as f:
                settings = {"settings": {"connections": []}}
                json.dump(settings, f)

    def get_connections(self):
        with open(self.settings_file_path, "r") as f:
            settings = json.load(f)
        return settings

    def save_connection(self, connection):
        with open(self.settings_file_path, "r") as f:
            settings = json.load(f)
        settings["settings"]["connections"].append(connection)
        with open(self.settings_file_path, "w") as f:
            json.dump(settings, f)
        return settings

    def delete_connection(self, connection):
        with open(self.settings_file_path, "r") as f:
            settings = json.load(f)
        connections = settings["settings"]["connections"]
        updated_connections = [
            conn for conn in connections if conn["name"] != connection["name"]
        ]
        settings["settings"]["connections"] = updated_connections
        with open(self.settings_file_path, "w") as f:
            json.dump(settings, f)
        return settings