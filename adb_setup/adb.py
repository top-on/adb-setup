"""Wrapper functions for Android Debug Bridge cli."""

import os
from pathlib import Path


def install_apk(apk_path: Path):
    """Install APK via Android Debug Bridge cli and verify success.

    Args:
        apk_path (Path): Path to APK to be installed.
    """
    print(f"Installing {apk_path.name}...")
    output = os.popen(f"adb install -d {apk_path}")

    line = output.readline()
    assert "Success" in line, f"Installation not successful, with error '{line}'!"

    print(f"Successfully installed {apk_path.name}.\n")
