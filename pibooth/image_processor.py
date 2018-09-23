# -*- coding: utf8 -*-

class ImageProcessor(object):
    """This class defines various image processing tasks"""

    __init__(self, image_source_path):
        """Image processor initialization

        :param image_source_path: The image source path
        :type image_source_path: str
        """
        if os.path.isfile(image_source_path) is True:
            self.image_source_path = image_source_path
        else:
            raise ValueError('Cannot access the image: {}'.format(image_source_path))
    