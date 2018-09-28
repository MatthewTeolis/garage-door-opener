import sys
import RPi.GPIO as GPIO
from config import Config
from garage_door_opener import GarageDoorOpener


door = sys.argv[1]
config = Config(Config.DEFAULT_CONFIG_FILE)
garage_door_opener = GarageDoorOpener(config, GPIO)
garage_door_opener.open_right_door()
