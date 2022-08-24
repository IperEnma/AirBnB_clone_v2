#!/usr/bin/python3
"""module that compress using fabric"""

from fabric.api import *
from datetime import datetime

def do_pack():
    try:
        date = datetime.utcnow().strftime('%Y%m%d%H%M%S')
        print("Packing web_static to versions/web_static_{}.tgz web_static".format(date))
        local("sudo mkdir -p versions")
        local("sudo tar -cvzf versions/web_static_{}.tgz web_static".format(date))
        return "versions/web_static_{}.tgz web_static".format(date)
    except Exception:
        return None
