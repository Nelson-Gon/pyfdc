# pyfdc: A python interface to FoodDataCentral
![Travis Build](https://travis-ci.com/Nelson-Gon/pyfdc.svg?branch=master)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Nelson-Gon/pyfdc/graphs/commit-activity)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub issues](https://img.shields.io/github/issues/Nelson-Gon/pyfdc.svg)](https://GitHub.com/Nelson-Gon/pyfdc/issues/)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/Nelson-Gon/pyfdc.svg)](https://GitHub.com/Nelson-Gon/pyfdc/issues?q=is%3Aissue+is%3Aclosed)


**This is a work in progress. Things might break and change unannounced. It is still highly experimental.**

----

**Installation**

The simplest way to install is as follows:

Open the Terminal/CMD/Git bash/shell and enter

```
# You should use your default python interpreter
python3.7 -m pip install git+https://github.com/Nelson-Gon/pyfdc.git

```

Otherwise:

```
# clone the repo
git clone https://www.github.com/Nelson-Gon/pyfdc.git
cd pyfdc
python3 setup.py install

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
my_search = FoodSearch(api_key=api_key, search_phrase="nugget")
list(my_search.get_food_info(target="fdcId"))

```

The above will result in the following output(truncated):

```

[[337348], [337394], [170725], [340673], [337347], [173721], [173722], [337346].....]]


```
To get descriptions of the different results, one could do something like this(truncated again):

```
[['Chicken nuggets'], ['Turkey, nuggets'], ["WENDY'S, Chicken Nuggets"], ['Nutty Nuggets, Ralston Purina']]]

```
The simplest way to find out all available `targets` is to simply call:

```
list(my_search.get_food_info())

```
**This will of course throw an error showing what options are available.**:

```

target should be one of ['fdcId', 'description', 'scientificName', 'commonNames', 'additionalDescriptions', 'dataType', 'foodCode', 'gtinUpc', 'ndbNumber', 'publishedDate', 'brandOwner', 'ingredients', 'allHighlightFields', 'score']

```
For more details, please see the documentation of each of these classes and the
associated documents.


2. `FoodDetails`

The `FoodSearch` class has an important advantage: it can allow us to obtain
FoodDataCentral(fdcId) IDs using a simple search term. To get full details about a given 
fdcId, one can do the following:

```
my_details = FoodDetails(api_key=api_key, fdc_id=504905)
my_details.get_food_details("ingredients")

```
This will give us the following output:

```
 'CHICKEN VIENNA SAUSAGE IN CHICKEN BROTH'

```
To get nutrient details, we can use the following which returns a list of all 
nutrient details. For brevity, only part of the first list item is shown.

```

list(my_details.get_nutrients())

[      id number                  name  rank unitName
 0   1079    291  Fiber, total dietary  1200        g
 1   1079    291  Fiber, total dietary  1200        g
 2   1079    291  Fiber, total dietary  1200        g
 3   1079    291  Fiber, total dietary  1200        g
 4   1079    291  Fiber, total dietary  1200        g
 5   1079    291  Fiber, total dietary  1200        g
 6   1079    291  Fiber, total dietary  1200        g

```

To return a merge of the above results, we can use `merge_food_nutrients` as follows:

```
my_details.merge_nutrient_results()
     number                          name  rank unitName
id                                                      
1079    291          Fiber, total dietary  1200        g
1079    291          Fiber, total dietary  1200        g
1079    291          Fiber, total dietary  1200        g
1079    291          Fiber, total dietary  1200        g
1079    291          Fiber, total dietary  1200        g
     ...                           ...   ...      ...
1258    606  Fatty acids, total saturated  9700        g
1258    606  Fatty acids, total saturated  9700        g
1258    606  Fatty acids, total saturated  9700        g
1258    606  Fatty acids, total saturated  9700        g
1258    606  Fatty acids, total saturated  9700        g
[225 rows x 4 columns]

```
