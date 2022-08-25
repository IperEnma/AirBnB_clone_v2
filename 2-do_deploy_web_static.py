#!/usr/bin/python3
"""module that compress using fabric"""

from fabric.api import *
import os


env.hosts = ["34.201.143.161", "35.175.196.152"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/school"


def do_pack():
    """function compress file"""
    try:
        date = datetime.utcnow().strftime('%Y%m%d%H%M%S')
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

    if os.path.exists(archive_path) is False:
        return False

    if os.path.isfile(archive_path) is False:
        return False

    if put(archive_path, "/tmp").succeeded is False:
        return False

    file = os.path.basename(archive_path)
    file = file.split(".")

    if run("mkdir -p /data/web_static/releases/{}".format(file[0])).succeeded is False:
        return False

    if run("sudo tar -xzf /tmp/{}.{} -C /data/web_static/releases/{}".format(
        file[0], file[1], file[0])).succeeded is False:
        return False

    if run("sudo rm -rf /tmp/{}.{}".format(file[0], file[1])).succeeded is False:
        return False

    if run("sudo mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}".format(file[0], file[0])).succeeded is False:
        return False

    if run("sudo rm -rf /data/web_static/current").succeeded is False:
        return False

    if run("sudo rm -rf /data/web_static/releases/{}/web_static".format(
        file[0])).succeeded is False:
        return False

    if run("sudo ln -s /data/web_static/releases/{}/\
            /data/web_static/current".format(file[0])).succeeded is False:
        return False
    return True
