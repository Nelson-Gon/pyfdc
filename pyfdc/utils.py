# Utility functions to use with pyfdc

import os

# Set and get important environmental variables

def set_api_key(api_key):
    """
    :param api_key: Session api key as obtained from Food Data Central

    :return: Sets the Environmental variable "api_key"

    """
    os.environ["api_key"] = api_key




