# -*- coding: utf8 -*-

import os
import subprocess
import time
import uuid


class Camera(object):
    """This class represents the pi camera"""

    def __init__(self, output_directory_path=os.getcwd(), flash=None):
        """Camera initialization

        :param output_directory_path: The output directory path
        :type output_directory_path: str
        :param flash: The relay object managing the flash
        :type flash: Relay
        """
        if os.path.isdir(output_directory_path) is True:
            self.output_directory_path = output_directory_path
        else:
            raise ValueError(
                "Cannot access the output_directory_path: {}".format(
                    output_directory_path
                )
            )

        self.subprocess_pid = None
        self.subprocess_out = None
        self.subprocess_err = None

        self.flash = flash

    def take_picture_with_countdown(self, countdown=3):
        """Take a single still photo after countdown

        :param countdown: Number of seconds to count down from
        :type countdown: int
        """
        if not self.flash:
            time.sleep(1)
            return self.take_picture()

        for count in reversed(range(int(countdown))):
            print(count + 1)
            if count > 0:
                # all countdown numbers
                self.flash.on(timeout=0.5, release=0.5)
            else:
                # Last countdown
                self.flash.on(timeout=0.125, release=0.25)
                self.flash.on(timeout=0.125, release=0.25)
                self.flash.on(timeout=0.125, release=0.125)

        self.flash.on()
        output_image_path = self.take_picture()
        self.flash.off()

        return output_image_path

    def take_picture(self):
        """Take a single still photo"""
        output_image_path = os.path.join(
            self.output_directory_path, "{}.jpg".format(str(uuid.uuid4()).upper()[:4])
        )
        command = [
            "raspistill",
            "-n",  # no preview
            "-t",
            "200",  # 200 ms before shutdown camera
            "-ex",
            "auto",  # auto exposure
            "-e",
            "jpg",  # encoding jpg
            "-q",
            "100",  # jpg quality = 100
            "-o",
            output_image_path,
        ]

        proc = subprocess.Popen(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        self.subprocess_pid = proc.pid

        try:
            self.subprocess_out, self.subprocess_err = proc.communicate()
        except:
            print(self.subprocess_err)

        return output_image_path
