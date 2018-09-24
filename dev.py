# -*- coding: utf8 -*-

from pibooth.camera import Camera
from pibooth.button import Button
#from pibooth.booth import Booth


c = Camera()
b = Button(18)

for image_path in b.on_press(c.take_picture_with_countdown):
    print(image_path)
    
#booth = Booth()
#booth.start()

