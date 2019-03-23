# -*- coding: utf8 -*-

import os
import ftplib


class FtpClient(object):
    """This class is the FTP Client"""

    def __init__(self, ftp_config):
        """FTP Client initialization

        :param ftp_config: FTP config containning host, username, password and dir
        :type ftp_config: dict
        """
        self.host = ftp_config.get("host")
        self.username = ftp_config.get("username")
        self.password = ftp_config.get("password")
        self.dir = ftp_config.get("dir")

    def upload(self, source_file_path, destination_dir=None):
        """Upload a file to the FTP server

        :param source_file_path: Locale source file path
        :type source_file_path: str
        :param destination_dir: Distant destination dir
        :type destination_dir: str
        """
        self.session = ftplib.FTP(self.host, self.username, self.password)

        if destination_dir:
            self.session.cwd(destination_dir)
        else:
            self.session.cwd(self.dir)

        filename = os.path.basename(source_file_path)
        file = open(source_file_path, "rb")
        self.session.storbinary("STOR {}".format(filename), file)
        file.close()
        self.session.quit()
