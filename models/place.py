#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Float, String, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship
import models
from models.review import Review
from os import getenv



place_amenity = Table('place_amenity', Base.metadata,
            Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
            Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
            )

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
    amenity_ids = []

    if (getenv('HBNB_TYPE_STORAGE') == 'db'):
        reviews = relationship("Review", backref="place", cascade="all, delete")
        amenities = relationship("Amenity", secondary=place_amenity, viewonly=False, backref="places")

    if (getenv('HBNB_TYPE_STORAGE') != 'db'):
        @property
        def reviews(self):
            new_list = []
            instance_review = models.storage.all[Review]

            for key, value in instance_review:
                if self.id == value.place_id:
                    new_list.append(value)
            return new_list

    @property
    def amenities(self):
        from models import storage
        from models.amenity import Amenity
        new_list = []
        amenities = storage.all(Amenity)
        for amenity in amenities:
            if amenity.id in amenity_ids:
                new_list.append(amenity)
        return new_list

    @amenities.setter
    def amenities(self, obj=None):
        from models.amenity import Amenity
        if type(obj) is Amenity:
            self.amenity_ids.append(obj.id)
