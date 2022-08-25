#!/usr/bin/python3
"""module that compress using fabric"""

from fabric.api import *
from datetime import datetime
from sys import argv
import os


env.hosts = ["34.201.143.161", "35.175.196.152"]
env.user = argv[7]
env.key_filename = argv[5]


def do_pack():
    """function compress file"""
    try:
        date = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        print("Packing web_static to versions/web_static_{}.\
                tgz web_static".format(date))
        local("sudo mkdir -p versions")
        local("sudo tar -cvzf versions/web_static_{}.tgz web_static".format(
            date))
        return "versions/web_static_{}.tgz web_static".format(date)
    except Exception:
        return None


def do_deploy(archive_path):
    """function send file"""
    if archive_path is None:
        return False
    upload = put(archive_path, "/tmp")
    file = os.path.basename(archive_path)
    print(file)
    with cd("/tmp"):
        file = file.split(".")
        run("tar -xvf {}.{} -C /data/web_static/releases".format(
            file[0], file[1]))
        run("rm -f {}.{}".format(file[0], file[1]))
        run("rm -f /data/web_static/current")
        run("mv /data/web_static/releases/web_static\
                /data/web_static/releases/{}".format(file[0]))
        run("ln -s -f /data/web_static/releases/{}/\
                /data/web_static/current".format(file[0]))
    print(upload.succeeded)
