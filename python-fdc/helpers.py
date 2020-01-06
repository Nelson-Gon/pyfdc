# We shall use the requests module to interface with Food Data Central
# We need an API key parameter
# We need to test rate limits
# We need to process the JSON or XML into something more meaningful


# Setup basics first
base_url = "https://api.nal.usda.gov/fdc/v1/"
# Setup headers for the url
# Might use this later
headers = {'content-Type': 'application/json'}

import requests
import json


# Get Food Search End Points

# define error messages with a very rudimentary switch case
# Possible to define a custom error handler instead
# This uses only common(very common) status codes

def error_messages(error_status_code):
    """
    :param error_status_code: An HTTP error status code as returned by get_food_search_endpoint
    :return: An informative message based on the provided error_status_code

    """
    error_status = {
        400: "Bad request",
        401: "Unauthorized access. Do you have the correct API key?!",
        403: "No access. Please provide a correct API key",
        404: "The requested resource could not be found",
        503: "Site is temporarily unavailable, please try again later."
    }

    return error_status.get(error_status_code, "Unknown status code")


# This is overly long
# api_key, search_query, ingredients, sort_by="PublishedDate",require_all=True, ascending=True, page_number=1
# This is too rudimentary but until I think of a better way, I'll use this
# Maybe use **?
def get_food_search_endpoint(search_query=None, api_key=None, ingredients=None, require_all=False,
                             ascending=True, page_number=None,
                             sort_by="publishedDate",
                             brand_owner="usa"):
    """
    :param search_query: A string containing the search term
    :param api_key: A valid API key obtained from FoodDataCentral
    :param ingredients: List of ingredients as they appear on the label
    :param require_all: boolean If true, the search strictly returns only items that contain all words in search_query
    :param ascending: If True, the results are sorted in ascending order
    :param page_number: Page Number to show(maximum varies with search_query)
    :param sort_by: What field should be used to sort the results?
    :param brand_owner: Who owns the brand?
    :return: An unprocessed JSON object matching the chosen foods.

    """
    search_query = {'generalSearchInput': search_query,
                    'ingredients': ingredients,
                    'requireAllWords': require_all,
                    'pageNumber': page_number,
                    'sortField': sort_by,
                    'sortDirection': 'asc',
                    'brandOwner': brand_owner}
    # Currently not supporting data types
    # Will add it later
    # This was a bug for some reason
    # Should figure out sometime later
    #search_query = {key: "desc" for key, value in search_query.items() if key == "sortDirection" and not ascending}
    #print(search_query)

    request_parameters = {'api_key': api_key}
    url_response = requests.post(r"https://api.nal.usda.gov/fdc/v1/search",
                                 json=search_query,
                                 params=request_parameters)
    if url_response.status_code == 200:
        # return json.loads(url_response.content.decode('utf-8'))
        unprocessed_json = json.loads(url_response.content)
        return unprocessed_json
    else:
        raise ValueError(error_messages(url_response.status_code))


def extract_food_info(unprocessed_result, target="fdcId"):
    # Deal with only foods
    """

    :param unprocessed_result: A JSON object from get_food_search_endpoint
    :param target: What kind of information do you want to extract?
    Supports values in ["fdcId","description","scientificName","commonNames",
    "additionalDescriptions","dataType","foodCode","gtinUpc","ndbNumber","publishedDate",
    "brandOwner","ingredients","allHighlightFields","score"]
    Further details about these values are available here: https://fdc.nal.usda.gov/api-guide.html
    :return: Lists with the required target information.

    """
    foods_res = unprocessed_result["foods"]
    for x in foods_res:
        print([value for key, value in x.items() if key == target])





