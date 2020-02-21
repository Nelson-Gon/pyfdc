"""
A python interface to the USDA's FoodDataCentral API

.. author: Nelson Gonzabato

"""

# Credit to https://stackoverflow.com/questions/16981921/relative-imports-in-python-3

import os
import sys
os.chdir(os.path.dirname(os.path.realpath(__file__)) + "/pyfdc")
sys.path.append(os.path.dirname(os.path.realpath(__file__)))


__author__ = "Nelson Gonzabato"
__version__ = '0.1.3'
__all__ = ["pyfdc", "utils"]



