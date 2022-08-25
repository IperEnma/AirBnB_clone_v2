#!/usr/bin/python3
"""module that compress using fabric"""

from fabric.api import run, put, env
import os


env.hosts = ["34.201.143.161", "35.175.196.152"]


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

    r = True
    if archive_path is None:
        return False

    if os.path.exists(archive_path) is False:
        return False

    if os.path.isfile(archive_path) is False:
        return False

    if put(archive_path, "/tmp").succeeded is False:
        r = False

    file = os.path.basename(archive_path)
    file = file.split(".")

    mkdir = "mkdir -p /data/web_static/releases/{}".format(file[0])
    if run(mkdir).succeeded is False:
        r = False

    if run("tar -xzf /tmp/{}.{} -C /data/web_static/releases/{}".format(
                file[0], file[1], file[0])).succeeded is False:
        r = False

    if run("rm -rf /tmp/{}.{}".format(file[0], file[1])).succeeded is False:
        r = False

    source = "/data/web_static/releases/{}/web_static/*".format(file[0])
    dest = "/data/web_static/releases/{}".format(file[0])
    if run("cp -R " + source + " " + dest).succeeded is False:
        r = False

    if run("rm -rf /data/web_static/current").succeeded is False:
        r = False

    rm = "rm -rf /data/web_static/releases/{}/web_static".format(file[0])
    if run(rm).succeeded is False:
        r = False

    web = "/data/web_static/releases/{} ".format(file[0])
    symbolic = "/data/web_static/current".format(file[0])
    if run("ln -s " + web + symbolic).succeeded is False:
        r = False
    return r
