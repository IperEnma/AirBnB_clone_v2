#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.city import City
import models
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """

    if (getenv('HBNB_TYPE_STORAGE') == 'db'):
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")

    if (getenv('HBNB_TYPE_STORAGE') == 'fs'):
        name = ''

        @property
        def cities(self):
            new_list = []
            instance_city = models.storage.all(City)

            for key, value in instance_city.items():
                if self.id == value.state_id:
                    new_list.append(value)
            return new_list
