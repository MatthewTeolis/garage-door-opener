import sys
import RPi.GPIO as GPIO
from garage_door_opener import GarageDoorOpener


def __main__(args):
    door = args[1]
    garage_door_opener = GarageDoorOpener(GPIO)

    if door == "left":
        garage_door_opener.open_left_door()
    elif door == "right":
        garage_door_opener.open_right_door()
    elif door == "other":
        garage_door_opener.open_other_door()


__main__(sys.argv)
