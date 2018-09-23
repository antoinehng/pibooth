# -*- coding: utf8 -*-

from pibooth.camera import Camera
from pibooth.button import Button

c = Camera()
b = Button(18)
b.on_press(c.take_photo)
