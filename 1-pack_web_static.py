#!/usr/bin/python3
""" A Fabric script that generates a .tgz """

from datetime import datetime
from fabric.api import local
import os.path


def do_pack():
    """Archives the static files."""
    cur_time = datetime.now()
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        cur_time.year,
        cur_time.month,
        cur_time.day,
        cur_time.hour,
        cur_time.minute,
        cur_time.second
    )
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(output)).failed is True:
        return None
    return output
