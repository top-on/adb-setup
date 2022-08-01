#!/usr/bin/env python
"""Install packages and run configuration with ADB."""

import os

from urlpath import URL
from yaml import Loader, load

from adb_setup.adb import install_apk
from adb_setup.config import CACHE_DIR
from adb_setup.io import download_apk


# PARSE CONFIG
config = load(
    open("config/config_example.yaml", "r").read(),
    Loader=Loader,
)


# INSTALL PACKAGES
apk_urls = config.get("urls")

for url in apk_urls:
    url_typed = URL(url)

    path_dest = download_apk(apk_url=url_typed)

    install_apk(path_dest)


# RUN CONFIGURATION
commands = config.get("commands")

for command in commands:
    os.popen(command)
