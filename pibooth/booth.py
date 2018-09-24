# -*- coding: utf8 -*-

from .camera import Camera
from .button import Button
from .printer import Printer


class Booth(object):
    """This class represents the booth"""

    def __init__(self, config_file_path=None):
        """Booth initialization
        
        :param config_file_path: Config json file path
        :type config_file_path: str
        """
        self.config_file_path = config_file_path

        self.camera = Camera()
        self.button = Button(18)
        self.printer = Printer("/dev/serial0", 19200, 5")

    def start(self):
        """Start booth"""
        for image_path in self.button.on_press(self.camera.take_picture_with_countdown(3)):
            self.printer.print_image(image_path)
