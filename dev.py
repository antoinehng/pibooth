# -*- coding: utf8 -*-

import RPi.GPIO as GPIO  

from pibooth.camera import Camera
from pibooth.button import Button
  
try:  
    c = Camera()
    b = Button(18)
    b.on_press(c.take_photo)

finally:  
    GPIO.cleanup() # this ensures a clean exit  