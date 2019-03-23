# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
from Queue import Queue
import os
import json

from .camera import Camera
from .button import Button
from .printer import Printer
from .relay import Relay
from .ftp import FtpClient


class Booth(object):
    """This class represents the booth"""

    def __init__(self, config_file_path):
        """Booth initialization"""
        self.image_path_queue = Queue(maxsize=1)
        self.config = self._get_config_from_file(config_file_path)
        self._init_devices()

    def _get_config_from_file(self, config_file_path):
        with open(config_file_path) as config_file:
            return json.load(config_file)
    
    def _init_devices(self):
        self.flash = Relay(self.config["gpio"]["flash"])
        self.camera = Camera(flash=self.flash)
        self.button = Button(self.config["gpio"]["button"])
        self.printer = Printer(
            self.config["printer"]["usb_device"],
            self.config["printer"]["baud_rate"],
            self.config["printer"]["timeout"],
        )

    def start(self):
        """Start booth daemon"""
        try:
            self.button.on_press(
                self.image_path_queue, self.camera.take_picture_with_countdown
            )

            while True:
                if not self.image_path_queue.empty():
                    image_path = self.image_path_queue.get()

                    self.printer.print_image(image_path, self.config["event"])

                    try:
                        ftp = FtpClient(self.config["ftp"])
                        ftp.upload(image_path)
                    except:
                        print(
                            "Something went wrong, but do not want to break the booth flow"
                        )

                    os.remove(image_path)

        except KeyboardInterrupt:
            GPIO.cleanup()
        GPIO.cleanup()
