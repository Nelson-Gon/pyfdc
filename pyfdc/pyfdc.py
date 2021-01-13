# Accesses the food search endpoint
import requests
import json
from pandas import DataFrame, json_normalize
from itertools import chain
from utils import key_signup
import os


class FoodDataCentral(object):
    """

    This class provides access to and manipulation of the Food Data Central food search and details end points.

    For more details, please see: https://fdc.nal.usda.gov/api-guide.html

    This uses version one of the API access point.

    """

    def __init__(self):
        if "pyfdc_key" in os.environ:
            self.api_key = os.environ.get("pyfdc_key")
        else:
            key_signup()

    def get_food_info_internal(self, search_phrase=None, ingredients=None, brand_owner=None,
                               target=None, page_number=None, page_size=50,
                               sort_field=None, sort_direction='asc'):

        """
        :param brand_owner: str Defaults to None
        :param ingredients: str to limit the search to certain ingredients
        :param search_phrase: str A search phrase eg "chicken"
        :param target: A string or list specifying which of the available values should be returned.
        :param page_number: Page number. Defaults to 1.
        :param page_size: Number of results returned
        :param sort_field: A string specifying which field to use to sort the returned results.
        :param sort_direction: One of "asc" or "desc" to indicate an ascending or descending sort respectively.
        :return: A generator object with the required results.
        """

        search_query = {'query': search_phrase,
                        'ingredients': ingredients,
                        'pageSize': page_size,
                        'pageNumber': page_number,
                        'sortBy': sort_field,
                        'sortOrder': sort_direction,
                        'brandOwner': brand_owner}
        # alias camel with snake case
        available_targets = {"fdc_id": 'fdcId',
                             "description": 'description',
                             "scientific_name": 'scientificName',
                             "common_names": 'commonNames',
                             "additional_descriptions": 'additionalDescriptions',
                             "gtin_upc": 'gtinUpc',
                             "ndb_number": 'ndbNumber',
                             "published_date": 'publicationDate',
                             "brand_owner": 'brandOwner',
                             "ingredients": 'ingredients',
                             "score": 'score'}

        # docs
        # https://fdc.nal.usda.gov/api-spec/fdc_api.html#/FDC/postFoodsSearch
        url_response = requests.get(f"https://api.nal.usda.gov/fdc/v1/foods/search?api_key={self.api_key}",
                                    params=search_query)
        try:
            url_response.raise_for_status()
            unprocessed_result = json.loads(url_response.content)["foods"]
            if target is None or target not in available_targets.keys():
                raise KeyError("target should be one of {}".format(available_targets.keys()))

            for x in unprocessed_result:
                yield [value for key, value in x.items() if key == available_targets[target]]

        except requests.exceptions.HTTPError as error:
            print(error)

    def get_food_info(self, search_phrase=None, target_fields=None,
                      ingredients=None, brand_owner=None, page_number=None, page_size=50,
                      sort_field=None, sort_direction='asc'):
        """
        :param search_phrase: A character string to search for.
        :param target_fields: A list of targets eg ['fdc_id','description']
        :param brand_owner: str Defaults to None
        :param ingredients: str to limit the search to certain ingredients
        :param search_phrase: str A search phrase eg "chicken"
        :param page_number: Page number. Defaults to 1.
        :param page_size: Number of results returned
        :param sort_field: A string specifying which field to use to sort the returned results.
        :param sort_direction: One of "asc" or "desc" to indicate an ascending or descending sort respectively.
        :return: A pandas DataFrame
        """
        # TODO: Avoid two functions when one will do aka drop get_food_info_internal
        result = []
        for target_key in target_fields:
            result.append(list(self.get_food_info_internal(search_phrase=search_phrase, target=target_key,
                                                           ingredients=ingredients,
                                                           brand_owner=brand_owner,
                                                           page_number=page_number, page_size=page_size,
                                                           sort_field=sort_field, sort_direction=sort_direction)))

        return DataFrame(list(map(lambda x: list(chain.from_iterable(x)), result)),
                         index=target_fields).transpose()

    def get_food_details(self, fdc_id=None, target_field=None):
        """

        Accesses the FoodDetails EndPoint

        :param fdc_id: A FoodDataCentral Food ID
        :param target_field: A string indicating which field to return e.g nutrients

        :return: A JSON object with the desired results.

        """

        base_url = f"https://api.nal.usda.gov/fdc/v1/{fdc_id}?api_key={self.api_key}"
        url_response = requests.get(base_url)
        try:
            url_response.raise_for_status()
            result = url_response.json()

            if target_field == "nutrients":
                result_custom = url_response.json()["foodNutrients"]
                result = json_normalize(DataFrame(result_custom)["nutrient"])
            else:
                result = result[target_field]


            return result

        except requests.exceptions.HTTPError as error:
            print(error)


