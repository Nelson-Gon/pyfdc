# Load all
import os
# This is just for local tests, not needed
os.chdir("pyautocv")
from pyfdc import *
# set session api key
set_api_key("7zDO40pS8yjKkdwbauZXrr8GBFvWJ3UAgVVZjQQh")
os.environ.get("pyfdc_key")
my_search = FoodDataCentral()
# Food search endpoint
list(my_search.get_food_info(search_phrase="+nugget", target="fdc_id"))
list(my_search.get_food_info(search_phrase="chicken", target="description"))
# Multiple food details
my_search.get_multiple_details(search_phrase="chicken", target_fields=["fdc_id","description"]).head(10)
# Food Details end point
my_search.get_food_details(fdc_id="630340",target_field="ingredients")
my_search.get_food_details(fdc_id="504905",target_field="ingredients")
my_search.get_nutrients(fdc_id="504905")