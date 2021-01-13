from pyfdc.pyfdc import *
from pyfdc.utils import *
# Set session api key
set_api_key()
# Instance init
my_search = FoodDataCentral()
# get food details

print(my_search.get_food_info(search_phrase="cake",target_fields=["fdc_id","description","brand_owner"]).head())

print(my_search.get_food_details(fdc_id="496446", target_field="nutrients"))        
