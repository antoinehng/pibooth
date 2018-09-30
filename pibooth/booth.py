# -*- coding: utf8 -*-

from Queue import Queue

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

        self.image_path_queue=Queue(maxsize=1)

        self.camera = Camera()
        self.button = Button(18)
        self.printer = Printer("/dev/ttyUSB0", 9600, 5)

        self.event = {}
        self.event['title'] = "HALO MAUD + YOLANDE BASHING"
        self.event['place'] = "LA CAVE AUX POETES, ROUBAIX"

    def start(self):
        """Start booth"""
        self.button.on_press(self.image_path_queue, self.camera.take_picture_with_countdown)
        
        while True:
            if not self.image_path_queue.empty():
                image_path = self.image_path_queue.get()
                self.printer.print_image(image_path, event)
