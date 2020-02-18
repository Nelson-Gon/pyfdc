"""
A python interface to the USDA's FoodDataCentral API

.. author: Nelson Gonzabato

"""

import requests
import json
import sys
import os
import pandas as pd
from itertools import chain
import os
__author__ = "Nelson Gonzabato"
__version__ = "0.1.0"
__all__ = ["pyfdc", "utils"]



