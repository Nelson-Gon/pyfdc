
pyfdc 0.1.3
===========

**Major Changes**


* 
  Classes FoodSearch and FoodDetails have been dropped. Use ``FoodDataCentral`` instead.

* 
  ``api_key`` was renamed to ``pyfdc_api_key``

* 
  ``target_field`` in ``get_food_info`` now uses snake_case instead of CamelCase. 

**Major additions**


* Added an option to signup for an api key

**Major deletions**


* merge_nutrient_results was removed. Use ``get_nutrients``
  instead. 

pyfdc 0.1.2
===========

Initial stable release on PyPI.

**Available features**


* FoodSearch class that allows access to the food search end point
* FoodDetails class that allows access to the food details end point
* Fixed issues with PyPI installs
