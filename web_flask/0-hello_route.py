#!/usr/bin/python3
"""
Fabric script that distributes an archive to a pair of
web servers, using the function do_deploy.
"""
from fabric.api import run, put, env, local
import os
from datetime import datetime
