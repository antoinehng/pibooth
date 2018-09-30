# -*- coding: utf8 -*-

from __future__ import print_function
import os

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
        self.print_size = 384, 512 # max_width=384 

        self.device = Adafruit_Thermal(device, baud_rate, timeout=timeout)
    
    def _calibrate(self):
        for i in range(0,256,15):
	        self.device.begin(i)
	        self.device.println(i)                 # Print heat time
	        self.device.inverseOn()
	        self.device.print('{:^32}'.format('')) # Print 32 spaces (inverted)
	        self.device.inverseOff()

        self.device.begin() # Reset heat time to default
        self.device.feed(4)

    def print_image(self, image_file_path):
        """Print Image

        :param image_file_path: Image file path
        :type image_file_path: str
        """
        # print logo
        self.device.printImage(Image.open("/home/pi/pibooth/pibooth/config/logo.jpg"), True)

        self.device.justify('C')

        self.device.doubleHeightOn()
        self.device.println("HALO MAUD + YOLANDE BASHING")

        self.device.doubleHeightOff()
        self.device.println("2018-11-12 21:08:44") # time

        self.device.feed(1)

        # print picture
        image_for_print_path = image_file_path+".print"
        image_for_print = Image.open(image_file_path) # create proxy image for print
        image_for_print = image_for_print.transpose(Image.ROTATE_90) # rotate image
        image_for_print.thumbnail(self.print_size, Image.ANTIALIAS) # resize
        image_for_print.save(image_for_print_path, "JPEG") # save
        self.device.printImage(Image.open(image_for_print_path), True)
        self.device.feed(1)

        # print text
        self.device.println("LA CAVE AUX POETES, ROUBAIX")
        self.device.feed(1)

        # line
        self.device.println("------------------------------")

        self.device.feed(1)
        self.device.boldOn()
        self.device.println("partagez votre")
        self.device.println("photo avec le code")
        self.device.boldOff()
        self.device.doubleHeightOn()
        self.device.doubleWidthOn()
        self.device.println("C0D3")
        self.device.doubleWidthOff()
        self.device.doubleHeightOff()
        self.device.boldOn()
        self.device.println("sur")
        self.device.boldOff()
        self.device.println("shootomatic.net")
        self.device.feed(1)

        # line
        self.device.println("------------------------------")



        # space to detach 
        self.device.feed(3)

        # delete proxy image used for print
        os.remove(image_for_print_path)
