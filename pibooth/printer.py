# -*- coding: utf8 -*-

from __future__ import print_function

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
        self.print_size = 384, 288 # max_width=384

    def print_image(self, image_file_path):
        """Print Image

        :param image_file_path: Image file path
        :type image_file_path: str
        """

        image_for_print_path = image_file_path+".print"
        image_for_print = Image.open(image_file_path)
        image_for_print.thumbnail(self.print_size, Image.ANTIALIAS)
        image_for_print.save(image_for_print_path, "JPEG")

        self.device.printImage(Image.open(image_for_print_path), True)
