"""
A python interface to the USDA's FoodDataCentral API

.. author: Nelson Gonzabato

"""

# Credit to https://stackoverflow.com/questions/16981921/relative-imports-in-python-3


import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from version import __version__
assert isinstance(__version__, str)


__author__ = "Nelson Gonzabato"
__all__ = ["pyfdc", "utils"]
__version__ = __version__