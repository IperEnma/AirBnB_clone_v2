#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv

type_s = getenv('HBNB_TYPE_STORAGE')

if (type_s == 'db'):
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
