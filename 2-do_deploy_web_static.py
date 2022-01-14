#!/usr/bin/python3
"""
Fabric script that distributes an archive to a pair of
web servers, using the function do_deploy.
"""
from fabric.api import run, put, env, local
import os
from datetime import datetime

env.hosts = ['ubuntu@34.139.188.96', 'ubuntu@54.209.148.200']


def do_pack():
    """
    Function to create a .tgz archive.
    """
    try:
        local("mkdir -p versions")
        d_t = datetime.now().strftime("%Y%m%d%H%M%S")
        compr_file = "versions/web_static_{}.tgz".format(d_t)
        local("tar -cvzf {} web_static".format(compr_file))
        return compr_file
    except:
        return None


def do_deploy(archive_path):
    """
    Function that distributes an archive.
    """
    name_dir = archive_path[9:-4]
    if os.path.exists(archive_path):
        put(archive_path, '/tmp/')
        run("mkdir -p /data/web_static/releases/{}/".format(name_dir))
        run("tar -xzf /tmp/web_static_{}.tgz -C \
        /data/web_static/releases/web_static_{}/".format(name_dir, name_dir))
        run("rm /tmp/{}.tgz".format(name_dir))
        run("mv /data/web_static/releases/web_static_{}/web_static/* \
            /data/web_static/releases/web_static_{}/".
            format(name_dir, name_dir))
        run("rm -rf /data/web_static/releases/web_static_{}/web_static"
            .format(name_dir))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/web_static_{}/ \
            /data/web_static/current".format(name_dir))
        print("New version deployed!")
        return True
    else:
        return False
