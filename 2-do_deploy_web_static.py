#!/usr/bin/python3
"""Fabric script  that distributes an
archive to your web servers, using the function do_deploy:
"""
from fabric.api import *
from os import path

env.hosts = ['35.175.196.152', '34.201.143.161']


def do_deploy(archive_path):
    """Deploys archives to servers
    """
    if not path.exists(archive_path) or not path.isfile(archive_path):
        return False
    ret_value = True
    # Set the folder
    d_folder = put(archive_path, '/tmp/')
    if d_folder.failed:
        ret_value = False
    # Prepare the file name and the destination folder
    archive_file = archive_path.replace(".tgz", "").replace("versions/", "")
    d_dest = run('mkdir -p /data/web_static/releases/' + archive_file + '/')
    if d_dest.failed:
        ret_value = False
    # Upload the archive to the /tmp/ directory of the web server
    # Uncompress the archive to the folder
    # /data/web_static/releases/<archive filename without extension>
    # on the web server
    d_unpack = run('tar -xzf /tmp/' + archive_file + '.tgz' +
                   ' -C /data/web_static/releases/' + archive_file + '/')
    if d_unpack.failed:
        ret_value = False
    # Delete the archive from the web server
    d_cleanfile = run('rm /tmp/' + archive_file + '.tgz')
    if d_cleanfile.failed:
        ret_value = False
    # The files are created under a web_static folder move it.
    d_move = run('cp -R /data/web_static/releases/' + archive_file +
                 '/web_static/* /data/web_static/releases/' + archive_file +
                 '/')
    d_del = run('rm -rf /data/web_static/releases/' + archive_file +
                '/web_static')
    if d_move.failed or d_del.failed:
        ret_value = False
    # Remove the now empty folder
    d_cleanfolder = run('rm -rf /data/web_static/releases/' + archive_file +
                        '/web_static')
    if d_cleanfolder.failed:
        ret_value = False
    # Delete the symbolic link /data/web_static/current from the web server
    d_removeold = run('rm -rf /data/web_static/current')
    if d_removeold.failed:
        ret_value = False
    # Create a new the symbolic link /data/web_static/current on the
    # web server, linked to the new version of your code
    # (/data/web_static/releases/<archive filename without extension>)
    d_createnew = run('ln -sf /data/web_static/releases/' + archive_file +
                      '/' + ' /data/web_static/current')
    if d_createnew.failed:
        ret_value = False
    # All set
    # if ret_value:
    #     print("All tasks succeeded!")
    return ret_value
