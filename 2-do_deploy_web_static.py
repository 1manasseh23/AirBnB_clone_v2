#!/usr/bin/python3
"""
Write a Fabric script (based on the file 1-pack_web_static.py
that distributes an archive to your web servers, using the
function do_deploy
"""
from fabric.api import *
import os


env.user = 'ubuntu'
env.hosts = ['']
def do_deploy(archive_path):
    try:
        dist = local('python3 1-pack_web_static.py --fullname', capture=True).strip()
        filename = 
