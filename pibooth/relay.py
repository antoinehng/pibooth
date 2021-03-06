# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import time


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
        self._open()

    def _open(self):
        """Open the relay"""
        GPIO.output(self.pin, 1)

    def _close(self):
        """Close the relay"""
        GPIO.output(self.pin, 0)

    def on(self, timeout=None, release=None):
        """Turn On

        :param timeout: If defined, keep on for the timeout time and then turn off
        :type timeout: float
        :param release: If defined, keep off for release time before letting go the following actions
        :type timeout: float
        """
        self._close()
        if timeout:
            time.sleep(timeout)
            self._open()
        if release:
            time.sleep(release)

    def off(self):
        self._open()
