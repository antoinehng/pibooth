# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
from Queue import Queue
import json

from .camera import Camera
from .button import Button
from .printer import Printer
from .relay import Relay

CONFIG_FILE_PATH = "/home/pi/pibooth/pibooth/config/event.json"


class Booth(object):
    """This class represents the booth"""

    def __init__(self):
        """Booth initialization"""
        self.image_path_queue = Queue(maxsize=1)
        self._set_devices()
        self._set_event_info()

    def _set_devices(self):
        self.flash = Relay(23)
        self.camera = Camera(flash=self.flash)
        self.button = Button(18)
        self.printer = Printer("/dev/ttyUSB0", 9600, 5)

    def _set_event_info(self):
        with open(CONFIG_FILE_PATH) as config_file:  
            self.event = json.load(config_file)

    def start(self):
        """Start booth"""
        try:
            self.button.on_press(
                self.image_path_queue, self.camera.take_picture_with_countdown
            )

            while True:
                if not self.image_path_queue.empty():
                    image_path = self.image_path_queue.get()
                    self.printer.print_image(image_path, self.event)
                    # TODO: Here, upload image to FTP

        except KeyboardInterrupt:
            GPIO.cleanup()
        GPIO.cleanup()
