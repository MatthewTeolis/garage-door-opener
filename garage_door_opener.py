import time


class GarageDoorOpener:

    def __init__(self, config, gpio):
        self.config = config
        self.gpio = gpio
        self.gpio.setmode(self.gpio.BCM)

    def open_left_door(self):
        pin = self.config.get_left_door_pin()
        self.__trigger_pin(pin)

    def open_right_door(self):
        pin = self.config.get_right_door_pin()
        self.__trigger_pin(pin)

    def open_other_door(self):
        pin = self.config.get_right_door_pin()
        self.__trigger_pin(pin)

    def __trigger_pin(self, pin_for_garage_door):
        gpio = self.gpio
        gpio.setup(pin_for_garage_door, gpio.OUT)
        gpio.output(pin_for_garage_door, True)
        time.sleep(0.3)
        gpio.output(pin_for_garage_door, False)
        gpio.cleanup()
