"""Tests on package metadata."""

from adb_setup import __version__


def test_version():
    """Test versoin of package."""
    assert __version__ == "0.1.0"
