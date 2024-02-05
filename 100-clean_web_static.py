#!/usr/bin/python3
"""
Deletes out-of-date archives, using the function do_clean
"""

import os
from fabric.api import *


env.hosts = ["54.237.218.228", "34.203.75.52"]


def do_clean(number=0):
    """Delete out-of-date archives """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
