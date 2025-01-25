"""A Python package for analyzing skeletons."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("skeleplex-v2")
except PackageNotFoundError:
    __version__ = "uninstalled"
__author__ = "Kevin Yamauchi"
__email__ = "kevin.yamauchi@gmail.com"
