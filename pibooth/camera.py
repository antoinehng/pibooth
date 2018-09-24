# -*- coding: utf8 -*-

import os, subprocess, time
from datetime import datetime


class Camera(object):
    """This class represents the pi camera"""

    def __init__(self, output_directory_path=os.getcwd()):
        """Camera initialization

        :param output_directory_path: The output directory path
        :type output_directory_path: str
        """
        if os.path.isdir(output_directory_path) is True:
            self.output_directory_path = output_directory_path
        else:
            raise ValueError('Cannot access the output_directory_path: {}'.format(output_directory_path))

        self.subprocess_pid = None
        self.subprocess_out = None
        self.subprocess_err = None
    
    def take_picture_with_countdown(self, countdown=3):
        """Take a single still photo after countdown

        :param countdown: Number of seconds to count down from
        :type countdown: int
        """
        for count in reversed(range(int(countdown))):
            print(count+1)
            time.sleep(1)
        self.take_picture()

    def take_picture(self):
        """Take a single still photo"""
        output_image_path = os.path.join(self.output_directory_path, "img_"+str(datetime.now()).replace(" ", "_")+".jpg")
        command = ['raspistill',
                '-n', # no preview
                '-t', '200', # 200 ms before shutdown camera
                '-ex', 'auto', # auto exposure
                '-e', 'jpg', # encoding jpg
                '-q', '100', # jpg quality = 100
                '-o', output_image_path]

        proc = subprocess.Popen(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        self.subprocess_pid = proc.pid

        try:
            self.subprocess_out, self.subprocess_err = proc.communicate()
        except:
            print(self.subprocess_err)
        
        return output_image_path