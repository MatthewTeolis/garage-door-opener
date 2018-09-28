from yaml import load


class Config:

    DEFAULT_CONFIG_FILE = ".config.yaml"

    def __init__(self, config_file_path):
        config_contents = open(config_file_path, "r")
        self.config = load(config_contents.read())

    def get_left_door_pin(self):
        return self.__get_door_pin("left")

    def get_right_door_pin(self):
        return self.__get_door_pin("right")

    def get_other_door_pin(self):
        return self.__get_door_pin("other")

    def __get_doors_data(self):
        return self.config["doors"]

    def __get_door_pin(self, door):
        return self.__get_doors_data()[door]
