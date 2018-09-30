# -*- coding: utf8 -*-

from Queue import Queue
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
    def on_press(self, return_value_queue, function, *args, **kwargs):
        """Execute function with args and kwargs on button press

        :param function: The function to execute on button press
        :type function: function
        :param *args: args to be passed to function
        :param **kwargs: kwargs to be passed to function
        """
        while True:
            time.sleep(.050) # 50ms debounce time
            if self._get_state() == 0:
                return_value_queue.put(function(*args, **kwargs))


