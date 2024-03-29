
Welcome to pyfdc's changelog
============================

**Version 0.2.3**


* 
  Tests are now written with the ``pytest`` framework which means that this is now a dependency. We also now use ``pytest_cov`` for coverage reports. This also 
  introduces yet another dependency. 

* 
  Fixed an issue in ``get_food_details`` due to a change in column naming in the API interface. This is now automated backend. 

**Version 0.2.2**


* 
  Tests rewritten to make tests easier to debug. 

* 
  Users can now supply ``label_nutrients`` to ``target_field`` to get label nutrient information. 

* 
  Added nutrition information after https://github.com/Nelson-Gon/rfdc/issues/2

* 
  Fixed a bug that caused wrong output in ``get_food_info``.  

* 
  Now supporting a script mode. 

* 
  Added coverage reports and auto download links. 

* 
  Initial tests. 

* 
  Support for manual api key entry. This is useful for tests only. 

* 
  Users can now view available targets by calling ``FoodDataCentral.available_targets``

* 
  ``get_food_details`` now returns a low level result if no ``fdc_id`` is provided.

* 
  Code was refactored to allow assertion statements and provide user warnings. 

**Release 0.2.1**
**Major Changes**


* 
  ``get_nutrients`` was dropped. Use ``get_food_info`` with ``target_field`` "nutrients."

* 
  ``get_multiple_details`` was dropped. Use ``get_food_info`` instead.

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
