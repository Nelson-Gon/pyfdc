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

    def get_food_info(self, target=None, page_number=None, require_all=True, sort_field='publishedDate',
                      sort_direction='asc'):
        search_query = {'generalSearchInput': self.search_phrase,
                        'ingredients': self.ingredients,
                        'requireAllWords': require_all,
                        'pageNumber': page_number,
                        'sortField': sort_field,
                        'sortDirection': sort_direction,
                        'brandOwner': self.brand_owner}
        request_parameters = {'api_key': self.api_key}
        url_response = requests.post(r"https://api.nal.usda.gov/fdc/v1/search",
                                     json=search_query,
                                     params=request_parameters)
        try:
            url_response.raise_for_status()
            unprocessed_result = json.loads(url_response.content)["foods"]
            for x in unprocessed_result:
                print([value for key, value in x.items() if key == target])

        except requests.exceptions.HTTPError as error:
            print(error)
            sys.exit(1)


class FoodDetails(object):
    def __init__(self, api_key, fdc_id):
        self.api_key = api_key
        self.fdc_id = fdc_id

    def get_food_details(self, target_field=None):
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






