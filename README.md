# pyfdc: A python interface to FoodDataCentral
![Travis Build](https://travis-ci.com/Nelson-Gon/python-fdc.svg?branch=master)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)


**This is a work in progress. Things might break and change unannounced. It is still highly experimental.**

----

**Installation**

```
# clone the repo
git clone https://www.github.com/Nelson-Gon/pyfdc.git
cd pyfdc
python3 pyfdc/setup.py install

```
---

**Sample usage**

```
import pyfdc

```

**Key Features**

There are two key classes defined in `pyfdc`: 
1. `FoodSearch` implements the class for objects aimed at querying the database with a search term.
To get details about foods for a given search term, one can do the following:
```
my_search = FoodSearch(api_key="my_api_key", search_phrase="chicken", brand_owner="usa")
my_search.get_food_info(target="description")

```

The above will result in the following output(truncated):

```
['CHICKEN']
['CHICKEN VIENNA SAUSAGE IN CHICKEN BROTH']
['CHICKEN STOCK']
['CHICKEN WINGS']
['CHICKEN ASADA']

```

For more details, please see the documentation of each of these classes and the
associated documents.


2. `FoodDetails`

The `FoodSearch` class has an important advantage: it can allow us to obtain
FoodDataCentral(fdcId) IDs using a simple search term. To get full details about a given 
fdcId, one can do the following:

```
my_details = FoodDetails(api_key="my_api_key", fdc_id=504905)
my_details.get_food_details("ingredients")

```
This will give us the following output:

```
 'CHICKEN VIENNA SAUSAGE IN CHICKEN BROTH'

```


