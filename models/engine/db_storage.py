#!/usr/bin/python3
"""New engine DBStorage"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import Base


class DBStorage:
    """Define class"""

    __engine = None
    __session = None

    def __init__(self):
        """initialize instance"""
        user = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        test = getenv('HBNB_ENV')

        self.__engine = create_engine(
                "mysql+mysqldb://{}:{}@{}/{}".format(
                    user,
                    passwd,
                    host,
                    db
                    ),
                pool_pre_ping=True
                )
        if (test == 'test'):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """all objecsts depending of the cls"""
        new_dict = {}
        if cls is not None:
            for obj in self.__session.query(cls):
                key = cls.__class.__.__name__ + obj.id
                new_dict[key] = obj
        else:
            for _cls in ['State', 'City']:
                objs = self.__session.query(eval(_cls)).all()
                for obj in objs:
                    key = _cls + "." + obj.id
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """add the object"""
        self.__session.add(obj)

    def save(self):
        """commit all changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from te current session"""
        if (obj is not None):
            self.__session.query(obj.__class__).filter(
                    obj.__class__.id == obj.id).delete(synchronize_session="fetch")

    def reload(self):
        """create all tables in db"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session_reg = scoped_session(session_factory)
        self.__session = session_reg()
