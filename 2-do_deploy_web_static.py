#!/usr/bin/python3
"""module that compress using fabric"""

from fabric.api import *
import os


env.hosts = ["34.201.143.161", "35.175.196.152"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/school"


def do_deploy(archive_path):
    """function send file"""
    if archive_path is None:
        return False
    if not os.path.exists(archive_path):
        return False
    if os.path.isfile(archive_path) is False:
        return False
    upload = put(archive_path, "/tmp")
    if (upload.succeeded is not True):
        return False
    file = os.path.basename(archive_path)
    try:
        with cd("/tmp"):
            file = file.split(".")
            run("mkdir -p /data/web_static/releases/{}".format(file[0]))
            run("sudo tar -xzf {}.{} -C /data/web_static/releases/{}".format(
                file[0], file[1], file[0]))
            run("sudo rm -rf {}.{}".format(file[0], file[1]))
            run("sudo rm -rf /data/web_static/current")
            run("sudo cp -r /data/web_static/releases/{}/web_static/*\
                /data/web_static/releases/{}".format(file[0], file[0]))
            run("sudo rm -rf /data/web_static/releases/{}/web_static".format(
                    file[0]))
            run("sudo ln -s -f /data/web_static/releases/{}/\
                /data/web_static/current".format(file[0]))
    except Exception:
        return False
    print("New version deployed!")
    return True
