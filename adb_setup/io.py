"""Modules for IO tasks."""

import requests
from pathlib import Path
from urlpath import URL

from adb_setup.config import CACHE_DIR


def download_apk(apk_url: URL) -> Path:
    """Download APK file to cache folder.

    Args:
        apk_url (URL): URL of APK to download.

    Returns:
        Path: Path to downloaded file.
    """
    print(f"Downloading {apk_url.name}...")
    file_content = requests.get(url=apk_url).content

    # download package
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    path_dest = CACHE_DIR / apk_url.name
    open(file=path_dest, mode="wb").write(file_content)

    return path_dest
