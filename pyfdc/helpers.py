import requests
import json
import sys


# Experimenting with classes
class FoodSearch(object):
    def __init__(self, api_key, search_phrase, brand_owner=None, ingredients=None):

        self.api_key = api_key
        self.search_phrase = search_phrase
        self.brand_owner = brand_owner
        self.ingredients = ingredients

    def get_food_info(self, target=None, page_number=None, require_all=True, sort_field='PublishedDate',
                      sort_direction='asc'):
        search_query = {'generalSearchInput': self.search_phrase,
                        'ingredients': self.ingredients,
                        'requireAllWords': require_all,
                        'pageNumber': page_number,
                        'sortField': sort_field,
                        'sortDirection': sort_direction,
                        'brandOwner': self.brand_owner}
        request_parameters = {'api_key': self.api_key}
        try:
            url_response = requests.post(r"https://api.nal.usda.gov/fdc/v1/search",
                                         json=search_query,
                                         params=request_parameters)
            return url_response.raise_for_status()
        except requests.exceptions.HTTPError as error:
            print(error)
            sys.exit(1)








