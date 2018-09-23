# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import threading

# to put in app init class later
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)


def threaded(fn):
    def wrapper(*args, **kwargs):
        threading.Thread(target=fn, args=args, kwargs=kwargs).start()
    return wrapper