# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import time

from . import threaded


class Relay(object):
    """This class represents the relay"""

    def __init__(self, pin):
        """Relay initialization

        :param pin: The GPIO pin number for this button
        :type pin: int
        """
        self.pin = int(pin)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def open(self):
        """Open the relay"""
        GPIO.output(self.pin,1)

    def close(self):
        """Close the relay"""
        GPIO.output(self.pin,0)


