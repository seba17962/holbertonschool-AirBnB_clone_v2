#!/usr/bin/python3
""" Db storage for HBNB project """
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBStorage():
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
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Retun instances of a given class or all classes"""
        obj_dict = {}
        self.__session = sessionmaker(bind=self.__engine)()
        if cls is not None:
            sess_objs = self.__session.query(cls).all()
            for obj in sess_objs:
                obj_dict['{}.{}'.format(
                    obj.__class__.__name__,
                    obj.id
                )] = obj
            return obj_dict
        else:
            sess_objs = self.__session.query(cls).all()
            for obj in sess_objs:
                if obj.__class__.__name__ != 'BaseModel':
                    obj_dict['{}.{}'.format(
                        obj.__class__.__name__,
                        obj.id
                    )] = obj
            return obj_dict

    def new(self, obj):
        """Create new object."""
        if obj is not None:
            self.__session.add(obj)

    def save(self):
        """save"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete a given object."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Loads objects from db and create new session"""
        from models.user import User
        from models.city import City
        from models.place import Place
        from models.state import State
        from models.review import Review
        from models.amenity import Amenity
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False))
        self.__session = Session()

    def close(self):
        self.__session.close()
