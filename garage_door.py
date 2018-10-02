import time


class GarageDoor:
    LEFT_DOOR_PIN = 22
    RIGHT_DOOR_PIN = 27
    OTHER_DOOR_PIN = 17

    def __init__(self, gpio):
        self.gpio = gpio

    def toggle_left_door(self):
        self.__trigger_pin(self.LEFT_DOOR_PIN)

    def toggle_right_door(self):
        self.__trigger_pin(self.RIGHT_DOOR_PIN)

    def toggle_other_door(self):
        self.__trigger_pin(self.OTHER_DOOR_PIN)

    def __trigger_pin(self, pin_for_garage_door):
        gpio = self.gpio
        gpio.setmode(self.gpio.BCM)
        gpio.setup(pin_for_garage_door, gpio.OUT)
        gpio.output(pin_for_garage_door, True)
        time.sleep(0.3)
        gpio.output(pin_for_garage_door, False)
        gpio.cleanup()
