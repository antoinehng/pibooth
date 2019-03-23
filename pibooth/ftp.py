# -*- coding: utf8 -*-

import ftplib


class FTPClient(object):
    """This class is the FTP Client"""

    def __init__(self, ftp_config):
        """FTP Client initialization

        :param host: FTP Host address
        :type host: str
        :param username: Account username
        :type username: str
        :param password: Account password
        :type password: str
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
        self.session = ftplib.FTP(ftp_config.get("host"), ftp_config.get("username"), ftp_config.get("password"))

        if destination_dir:
            self.session.cwd(destination_dir)
        else:
            self.session.cwd(self.dir)
        
        file = open(source_file_path,'rb')
        self.session.storbinary('STOR TEST.jpg', file)
        file.close()
        self.session.quit()
