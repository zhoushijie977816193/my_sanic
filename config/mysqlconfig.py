# !/usr/bin/env python
# !-*- conding: utf-8 -*-


SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_POOL_SIZE = 50
SQLALCHEMY_MAX_OVERFLOW = 10


class MySqlConfig(object):

    def __init__(self):
        self.server = 1

    def mysql_local_url_info(self):
        DIALECT = 'mysql'
        DRIVER = 'pymysql'
        USERNAME = 'root'
        PASSWORD = '123456'
        HOST = '127.0.0.1'
        PORT = '3306'
        DATABASE = 'reading'
        SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4'.format(DIALECT, DRIVER, USERNAME, PASSWORD,
                                                                                  HOST, PORT, DATABASE)
        return SQLALCHEMY_DATABASE_URI

    def mysql_local_url_info_1(self):
        DIALECT = 'mysql'
        DRIVER = 'pymysql'
        USERNAME = 'root'
        PASSWORD = '123456'
        HOST = '127.0.0.1'
        PORT = '3306'
        DATABASE = 'reading1'
        SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4'.format(DIALECT, DRIVER, USERNAME, PASSWORD,
                                                                                  HOST, PORT, DATABASE)
        return SQLALCHEMY_DATABASE_URI

    def mysql_read_write_db(self):
        read_db = self.mysql_local_url_info_1()
        write_db = self.mysql_local_url_info()
        return {"read_db": read_db, "write_db": write_db}
