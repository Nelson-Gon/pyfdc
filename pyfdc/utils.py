# Utility functions to use with(in) pyfdc

import os
import webbrowser
import sys


# Set and get important environmental variables

def set_api_key(api_key=None):
    """
    :param api_key: Session api key as obtained from Food Data Central

    :return: Sets the Environmental variable "pyfdc_key"

    """
    if "pyfdc_key" not in os.environ.keys():
        os.environ["pyfdc_key"] = api_key
    else:
        print("pyfdc_key is already a valid key")
        pass


def key_signup():
    """

    :return: Opens a browser and takes a user to the api key sign up page.

    """
    valid_choices = {'yes': True, 'no': False, 'n': False, 'y': True, 'Y': True,
                     'No': False, 'N': False}
    answer = input('Please run set_api_key first. Otherwise,do you want to sign up for an api key?! Yes or No?')

    if valid_choices[answer]:
        sys.stdout.write("\033[0;31m")
        sys.stdout.write("Now taking you to the api key sign up page.")
        webbrowser.open("https://fdc.nal.usda.gov/api-key-signup.html", new=2)
    else:
        raise ValueError("You provided no api key. Please provide one and try again")
