#!/usr/bin/python3
"""module that compress using fabric"""

from fabric.api import *
from datetime import datetime
from sys import argv
import os


env.hosts = ["34.201.143.161", "35.175.196.152"]
env.user = argv[7]
env.key_filename = argv[5]


def do_deploy(archive_path):
    """function send file"""
    if archive_path is None:
        return False
    upload = put(archive_path, "/tmp")
    file = os.path.basename(archive_path)
    print(file)

