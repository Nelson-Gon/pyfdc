# Accesses the food search endpoint
import collections
from typing import Sequence
import requests
import json
from pandas import DataFrame, json_normalize
from itertools import chain
from utils import key_signup
import os
from warnings import warn
import re 


class FoodDataCentral(object):
    """

    This class provides access to and manipulation of the Food Data Central food search and details end points.

    For more details, please see: https://fdc.nal.usda.gov/api-guide.html

    This uses version one of the API access point.

    """

    def __init__(self, api_key=None):

        if api_key is None:
            self.api_key = os.environ.get("pyfdc_key") if "pyfdc_key" in os.environ else key_signup()
        else:
            warn("Providing an api_key is discouraged, please consider using set_api_key.")
            self.api_key = api_key
        self.base_url = f"https://api.nal.usda.gov/fdc/v1/foods/search?api_key={self.api_key}"
        # alias camel with snake case
        # Allow for users to see what keys we have.
        self.available_targets = {"fdc_id": 'fdcId',
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

    def get_food_info_internal(self, search_phrase=None,
                               ingredients=None,
                               brand_owner=None,
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

        assert page_number is not None and isinstance(page_number, int), \
            f"page_number should be an int not {type(page_number).__name__} "

        search_query = {'query': search_phrase,
                        'ingredients': ingredients,
                        'pageSize': page_size,
                        'pageNumber': page_number,
                        'sortBy': sort_field,
                        'sortOrder': sort_direction,
                        'brandOwner': brand_owner}

        # docs
        # https://fdc.nal.usda.gov/api-spec/fdc_api.html#/FDC/postFoodsSearch

        try:
            url_response = requests.get(self.base_url, params=search_query, headers={"User-Agent": "Mozilla-5.0"})
            url_response.raise_for_status()
            unprocessed_result = json.loads(url_response.content)["foods"]

        except requests.exceptions.HTTPError:
            raise

        else:
            for x in unprocessed_result:
                yield [val for key_id, val in x.items() if key_id == self.available_targets[target]]

    def get_food_info(self, search_phrase=None, target_fields=None,
                      ingredients=None, brand_owner=None, page_number=1,
                      page_size=50,
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
        # Check that page number is not none and is an int (for now)

        if target_fields is None:
            warn("No target_fields were provided, returning fdc_id, ingredients, and description.")
            target_fields = ["fdc_id", "ingredients", "description"]

        if not isinstance(target_fields, (list, tuple)):
            raise TypeError(f"target should be a list or tuple not {type(target_fields).__name__}")

        for target_key in target_fields:
            if target_key not in self.available_targets.keys():
                raise KeyError(f"target_key should be one of {self.available_targets.keys()} not {target_key}")
            result.append(list(self.get_food_info_internal(search_phrase=search_phrase, target=target_key,
                                                           ingredients=ingredients,
                                                           brand_owner=brand_owner,
                                                           page_number=page_number,
                                                           page_size=page_size,
                                                           sort_field=sort_field,
                                                           sort_direction=sort_direction)))

        return DataFrame(list(map(lambda x: list(chain.from_iterable(x)), result)), index=target_fields).transpose()

    def get_food_details(self, fdc_id=None, target_field=None, result_format="full",nutrients=None):
        """
        Accesses the FoodDetails EndPoint
        :param fdc_id: A FoodDataCentral Food ID
        :param target_field: A string indicating which field to return e.g nutrients If none is provided,
        a low level result will be returned
        :return: A DataFrame object with the desired results.
        """
 
        try:
            # base_url = f"https://api.nal.usda.gov/fdc/v1/{fdc_id}?api_key={self.api_key}"
            # Replace in base url so we have only for a specific FDC ID.
            assert fdc_id is not None, "fdc_id should not be None"
            assert isinstance(fdc_id, int), f"fdc_id should be an int not {type(fdc_id).__name__}"
            base_url = self.base_url.replace("foods/search", f"food/{fdc_id}")
            base_url = base_url + "&format=" + result_format 
            # print(base_url)
            if nutrients:
                base_url = base_url + "&nutrients=" + ",".join(nutrients)
            url_response = requests.get(base_url, headers={"User-Agent": "Mozilla-5.0"})
            url_response.raise_for_status()
            result = url_response.json()

        except requests.exceptions.HTTPError:
            raise

        except AssertionError:
            raise

        else:
            if target_field is None:
                warn("No target_field was provided, returning low level results.")
                # Return a low level result that contains everything if it is not empty
                return DataFrame([(key, value) for key, value in result.items() if value])

            else:
                # if len(target_field) > 1:
                    # warn("More than one target field was requested, returning only the first")
                 
                if target_field == "nutrients":
                    result = result["foodNutrients"]
                    return json_normalize(result)[{'id', 'amount', 'nutrient.id', 'nutrient.number',
                                                   'nutrient.name', 'nutrient.rank', 'nutrient.unitName',
                                                   'foodNutrientDerivation.description'}]
                if target_field == "label_nutrients":
                    if not "labelNutrients" in result.keys():
                        raise KeyError(f"FDC ID: {fdc_id} has no label nutrients.")
                    label_nutrients_df = json_normalize(result["labelNutrients"])  
                    label_nutrients_df.columns = [re.sub(".value", "", x) for x in label_nutrients_df] 
                    return label_nutrients_df                    

                else:
                    return result[target_field]


