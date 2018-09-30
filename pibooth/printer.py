# -*- coding: utf8 -*-

from PIL import Image
from Adafruit_Thermal import *


class Printer(object):
    """This class represents the printer"""

    def __init__(self, device, baud_rate, timeout):
        """Printer initialization
        
        :param device: Device path
        :type device: str
        :param baud: Baud rate
        :type baud: int
        :param timeout: Timeout in seconds
        :type timeout: int
        """
        self.device = Adafruit_Thermal(device, baud_rate, timeout=timeout)

    def print_image(self, image_file_path):
        """Print Image

        :param image_file_path: Image file path
        :type image_file_path: str
        """
        self.device.printImage(Image.open(image_file_path), True)
