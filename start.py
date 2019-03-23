# -*- coding: utf8 -*-

from pibooth.booth import Booth

CONFIG_FILE_PATH = "/home/pi/pibooth/config/config.json"


booth = Booth(CONFIG_FILE_PATH)
booth.start()
