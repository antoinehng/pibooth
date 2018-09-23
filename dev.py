# -*- coding: utf8 -*-

from pibooth.camera import Camera
from pibooth.button import Button

c = Camera()
c.take_photo()

b = Button(18)
print("wait for button press")
b.on_press(c.take_photo)
