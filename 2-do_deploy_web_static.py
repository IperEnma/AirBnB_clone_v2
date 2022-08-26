#!/usr/bin/python3
"""module that compress using fabric"""

from fabric.api import *
from datetime import datetime
from sys import argv
import os

env.hosts = ["34.201.143.161", "35.175.196.152"]


def do_pack():
    """funtion compress file"""
    try:
        date = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        local("sudo mkdir -p versions")
        local("sudo tar -cvzf versions/web_static_{}.tgz web_static".format(
            date))
        return "versions/web_static_{}.tgz".format(date)
    except Exception:
        return None


def do_deploy(archive_path):
    """function send file"""
    if not os.path.exists(archive_path) or not os.path.isfile(archive_path):
        return False

    file = os.path.basename(archive_path)
    try:
        put(archive_path, "/tmp/")

        file = file.split(".")

        run("mkdir -p /data/web_static/releases/" + file[0])

        run("tar -xzf /tmp/" + file[0] + "." + file[1] +
            " -C " + "/data/web_static/releases/" + file[0])

        run("rm -rf /tmp/" + file[0] + "." + file[1])

        source = "/data/web_static/releases/" + file[0] + "/web_static/* "
        dest = "/data/web_static/releases/" + file[0]
        run("cp -R " + source + dest)

        run("rm -rf /data/web_static/releases/" + file[0] + "/web_static")

        run("rm -f /data/web_static/current")

        source = "/data/web_static/releases/" + file[0]
        dest = " /data/web_static/current"
        run("ln -s " + source + dest)

    except Exception:
        return False
    return True
