import requests
import json
import sys
import pandas as pd


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
        # Maybe this can be done with a decorator, I just don't know how(yet)
        available_targets = ["fdcId", "description", "scientificName", "commonNames",
                             "additionalDescriptions", "dataType", "foodCode",
                             "gtinUpc", "ndbNumber", "publishedDate", "brandOwner",
                             "ingredients", "allHighlightFields", "score"]
        request_parameters = {'api_key': self.api_key}
        url_response = requests.post(r"https://api.nal.usda.gov/fdc/v1/search",
                                     json=search_query,
                                     params=request_parameters)
        try:
            url_response.raise_for_status()
            unprocessed_result = json.loads(url_response.content)["foods"]
            if target is None or target not in available_targets:
                raise ValueError("target should be one of {}".format(available_targets))
            else:
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


    def get_nutrients(self):
        """
        :return: A DataFrame showing nutrient details

        """
        # This is expensive currently and there might be a better way but it works
        result_as_df = pd.DataFrame.from_dict(json.loads(json.dumps(self.get_food_details()["foodNutrients"])))
        #nutrient_results = list()
        for row in range(result_as_df.shape[0]):
           yield pd.DataFrame(result_as_df.get("nutrient")[row],
                                                 index=result_as_df.get("nutrient").keys())







