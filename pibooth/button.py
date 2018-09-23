# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import time

from . import threaded


class Button(object):
    """This class represents the button"""

    def __init__(self, pin):
        """Button initialization

        :param pin: The GPIO pin number for this button
        :type pin: int
        """
        self.pin = int(pin)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def _get_state(self):
        return GPIO.input(self.pin)

    @threaded
    def on_press(self, function):
        """Execute function on button press

        :param function: The function to execute on button press
        :type function: function
        """
        while True:
            time.sleep(.050) # 50ms debounce time
            if self._get_state() == 0:
                function()


