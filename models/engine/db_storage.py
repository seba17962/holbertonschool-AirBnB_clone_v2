#!/usr/bin/python3
""" Db storage for HBNB project """
from sqlalchemy import create_engine , MetaData
from os import getenv

class DBstorage():
    """class"""
    __engine = None
    __session = None

    def __init__(self):
        self.mysql_user = getenv("HBNB_MYSQL_USER")
        self.mysql_passwword = getenv("HBNB_MYSQL_PWD")
        self.mysql_host = getenv("HBNB_MYSQL_HOST")
        self.mysql_database = getenv("HBNB_MYSQL_DB")
        url_str = "mysql+mysqldb://{}:{}@{}/{}".format(
            self.mysql_user,
            self.mysql_passwword,
            self.mysql_host,
            self.mysql_database
        )
        self.__engine = create_engine(url_str, pool_pre_ping=True)

        if getenv("HBNB_ENV") == 'test':
            self.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns all instances of the given class"""
        new_dict = {}
        