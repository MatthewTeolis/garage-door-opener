from yaml import load


class Config:
    DEFAULT_CONFIG_FILE = ".config.yaml"

    def __init__(self, config_file_path=DEFAULT_CONFIG_FILE):
        config_contents = open(config_file_path, "r")
        self.config = load(config_contents.read())

    def auth_key(self):
        return self.config["authkey"]

    def port(self):
        return self.config["port"]
