# We shall use the requests module to interface with Food Data Central
# We need an API key parameter
# We need to test rate limits
# We need to process the JSON or XML into something more meaningful
import requests
import json

# Setup basics first
base_url = "https://api.nal.usda.gov/fdc/v1/"
# Setup headers for the url
# Might use this later
headers = {'content-Type': 'application/json'}


# Get Food Search End Points

# This is overly long
# api_key, search_query, ingredients, sort_by="PublishedDate",require_all=True, ascending=True, page_number=1

def get_food_search_endpoint(search_query=None, api_key=None):
    search_query = {'generalSearchInput': search_query}
    request_parameters = {'api_key': api_key}
    url_response = requests.post(r"https://api.nal.usda.gov/fdc/v1/search",
                                 json=search_query,
                                 params=request_parameters)
    if url_response.status_code == 200:
        return json.loads(url_response.content.decode('utf-8'))
    else:
        return None



