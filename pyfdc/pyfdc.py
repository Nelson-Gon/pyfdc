# Accesses the food search endpoint
import requests
import json
import pandas as pd
from pandas.io.json import json_normalize
from itertools import chain
import os
from utils import key_signup


class FoodSearch(object):
    """

    This class provides access to and manipulation of the Food Data Central food search end point.

    For more details, please see: https://fdc.nal.usda.gov/api-guide.html

    """

    def __init__(self, search_phrase, brand_owner=None, ingredients=None):

        if "api_key" in os.environ:
            self.api_key = os.environ.get("api_key")
        else:
            key_signup()

        self.search_phrase = search_phrase
        self.brand_owner = brand_owner
        self.ingredients = ingredients

    def get_food_info(self, target=None, page_number=None, require_all=True, sort_field='publishedDate',
                      sort_direction='asc'):

        """

        :param target: A string specifying which of the available values should be returned. Can also
        be a list of strings.

        :param page_number: The page number of results to return. Defaults to 1.

        :param require_all: Boolean. If True, the results returned contain foods that contain all of the
        words in the search field. Defaults to True.
        :param sort_field: A string specifying which field to use to sort the returned results.
        :param sort_direction: One of `asc` or `desc` to indicate an ascending or descending sort respectively.
        :return: A generator object with the required results.

        """
        search_query = {'generalSearchInput': self.search_phrase,
                        'ingredients': self.ingredients,
                        'requireAllWords': require_all,
                        'pageNumber': page_number,
                        'sortField': sort_field,
                        'sortDirection': sort_direction,
                        'brandOwner': self.brand_owner}
        # Maybe this can be done with a decorator, I just don't know how(yet)
        available_targets = ["fdcId", "description", "scientificName", "commonNames",
                             "additionalDescriptions", "dataType", "foodCode",
                             "gtinUpc", "ndbNumber", "publishedDate", "brandOwner",
                             "ingredients", "allHighlightFields", "score"]

        request_parameters = {'api_key': self.api_key}
        url_response = requests.post(r"https://api.nal.usda.gov/fdc/v1/search",
                                     json=search_query, params=request_parameters)
        try:
            url_response.raise_for_status()
            unprocessed_result = json.loads(url_response.content)["foods"]
            if target is None or target not in available_targets:
                raise ValueError("target should be one of {}".format(available_targets))

            else:
                for x in unprocessed_result:
                    yield [value for key, value in x.items() if key == target]

        except requests.exceptions.HTTPError as error:
            print(error)
            sys.exit(1)

    def get_multiple_details(self, target_fields=None):
        result = []
        for target_key in target_fields:
            result.append(list(self.get_food_info(target_key)))

        return pd.DataFrame(list(map(lambda x: list(chain.from_iterable(x)), result)),
                            index=target_fields).transpose()


# Accesses the food details endpoint hence the name
class FoodDetails(object):
    """

     This class provides access to and manipulation of the Food Data Central food details end point.

     For more details, please see: https://fdc.nal.usda.gov/api-guide.html

     """

    def __init__(self, fdc_id):
        # There must be a way to avoid repeating this, I haven't learnt how yet

        if "api_key" in os.environ:
            self.api_key = os.environ.get("api_key")
        else:
            key_signup()

        self.fdc_id = fdc_id

    def get_food_details(self, target_field=None):
        """

        :param target_field: A string indicating which field to return

        :return: A JSON object with the desired results.

        """
        base_url = "https://api.nal.usda.gov/fdc/v1/{}?api_key={}".format(self.fdc_id, self.api_key)
        url_response = requests.get(base_url)
        try:
            url_response.raise_for_status()
            if target_field is None:
                return url_response.json()
            else:
                return url_response.json()[target_field]
        except requests.exceptions.HTTPError as error:
            print(error)
            sys.exit(1)

    def get_nutrients(self):
        """
        :return: A DataFrame showing nutrient details

        """
        use_object = self.get_food_details("foodNutrients")
        return json_normalize(pd.DataFrame(use_object)["nutrient"])





