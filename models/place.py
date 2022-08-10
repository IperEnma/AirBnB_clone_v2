#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Float, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
import models
from models.review import Review


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    """amenity_ids = []"""

    if (getenv('HBNB_TYPE_STORAGE') == 'db'):
        reviews = relationship("Review", backred="place", cascade="all, delete")
    else:
        @property
        def reviews(self):
            new_list = []
            instance_review = models.storage.all[Review]

            for key, value in instance_review:
                if self.id == value.place_id:
                    new_list.append(value)}
            return new_list
