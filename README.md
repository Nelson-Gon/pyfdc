# pyfdc: A python interface to FoodDataCentral
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3764453.svg)](https://doi.org/10.5281/zenodo.3764453)
![Travis Build](https://travis-ci.com/Nelson-Gon/pyfdc.svg?branch=master)
[![Documentation Status](https://readthedocs.org/projects/pyfdc/badge/?version=latest)](https://pyfdc.readthedocs.io/en/latest/?badge=latest)
![Test-Package](https://github.com/Nelson-Gon/pyfdc/workflows/Test-Package/badge.svg)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Nelson-Gon/pyfdc/graphs/commit-activity)
[![PyPI version fury.io](https://badge.fury.io/py/pyfdc.svg)](https://pypi.python.org/pypi/pyfdc/)
[![PyPI license](https://img.shields.io/pypi/l/pyfdc.svg)](https://pypi.python.org/pypi/pyfdc/)
[![PyPI Downloads Month](https://img.shields.io/pypi/dm/pyfdc.svg)](https://pypi.python.org/pypi/pyfdc/)
[![Project Status](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active) 
[![GitHub last commit](https://img.shields.io/github/last-commit/Nelson-Gon/pyfdc.svg)](https://github.com/Nelson-Gon/pyfdc/commits/master)
[![GitHub issues](https://img.shields.io/github/issues/Nelson-Gon/pyfdc.svg)](https://GitHub.com/Nelson-Gon/pyfdc/issues/)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/Nelson-Gon/pyfdc.svg)](https://GitHub.com/Nelson-Gon/pyfdc/issues?q=is%3Aissue+is%3Aclosed)



**Installation**

The simplest way to install the latest release is as follows:

```shell
pip install pyfdc

```

To install the development version:


Open the Terminal/CMD/Git bash/shell and enter

```shell

pip install git+https://github.com/Nelson-Gon/pyfdc.git

# or for the less stable dev version
pip install git+https://github.com/Nelson-Gon/pyfdc.git@develop

```

Otherwise:

```shell
# clone the repo
git clone https://www.github.com/Nelson-Gon/pyfdc.git
cd pyfdc
python3 setup.py install

```



**Sample usage**

```python
from pyfdc import *

```

**Set session api key**

To avoid providing an api key for each call, one can set a session api key as follows:

```python

utils.set_api_key("my_api_key_here")


```


**Key Features**

There is now one major class `FoodDataCentral`. 
See the [changelog](https://github.com/Nelson-Gon/pyfdc/blob/master/changelog.md) 
for more details.:

To instantiate an object:

```python
my_search = FoodDataCentral()
```

To get details about foods for a given search term, one can do the following:

```python

list(my_search.get_food_info(search_phrase="kung pao", target="fdc_id"))
```

The above will result in the following output(truncated):

```shell

[[783264],
 [783328],
 [783287],
 [783389],
 [167676],
 [668446],
 [897958],
 [736522],
 [927376],


```

To get descriptions of the different results:


```python

list(my_search.get_food_info(search_phrase="kung pao", target="description"))


```

This will result in the following result(truncated):

```shell

[['Kung Pao beef'],
 ['Kung pao chicken'],
 ['Kung Pao pork'],
 ['Kung Pao shrimp'],
 ['Restaurant, Chinese, kung pao chicken'],
 ['KUNG PAO SAUCE, KUNG PAO'],
 ['VEGAN KUNG PAO CHICKEN, KUNG PAO'],
 ['KUNG PAO STIR FRY SAUCE, KUNG PAO'],
 ['KUNG PAO STIR FRY SAUCE, KUNG PAO'],

```

The simplest way to find out all available `targets` is to simply call:

```python

list(my_search.get_food_info())


```

**This will throw an error showing what options are available.**:

> KeyError: "target should be one of dict_keys(['fdc_id', 'description', 'scientific_name', 'common_names', 'additional_descriptions', 'gtin_upc', 'ndb_number', 'published_date', 'brand_owner', 'ingredients', 'score'])"




For more details, please see the docs for each function or raise an issue.

To get a `DataFrame` from multiple target fields, we can use `get_multiple_details` as shown:

```shell

my_search.get_multiple_details(search_phrase="noodle",target_fields=["fdc_id","description", "ndb_number"])[:5]

    fdc_id          description ndb_number
0   508613               NOODLE      20134
1   546979               NOODLE      20133
2  1101523      Noodles, cooked      20113
3  1102193  Adobo, with noodles      20109
4  1102334       Noodle pudding      20409



```

To get full details about a given `fdcId`, one can do the following:

```python

my_search.get_food_details(fdc_id=504905, target_field="ingredients")

```

This will give us the following output(truncated):

```shell

'MECHANICALLY SEPARATED CHICKEN, CHICKEN BROTH, WATER, CONTAINS LESS THAN 2% OF: SALT, SUGAR, SPICES, SODIUM PHOSPHATE, SODIUM ASCORBATE, SODIUM NITRITE, 
NATURAL FLAVORS, EXTRACTIVES OF PAPRIKA.'

```

To get nutrient details, we can use the following which returns a list of all 
nutrient details. For brevity, only part of the first list item is shown.

```shell

my_search.get_nutrients(fdc_id=" 496446")
Out[131]: 
      id number                            name   rank unitName
0   1087    301                     Calcium, Ca   5300       mg
1   1089    303                        Iron, Fe   5400       mg
2   1104    318                   Vitamin A, IU   7500       IU
3   1162    401  Vitamin C, total ascorbic acid   6300       mg
4   1253    601                     Cholesterol  15700       mg
5   1258    606    Fatty acids, total saturated   9700        g
6   1003    203                         Protein    600        g
7   1004    204               Total lipid (fat)    800        g
8   1005    205     Carbohydrate, by difference   1110        g

  

```


**Credit**

1. **Original Food Data Central API**

The API interfaced is available [here](https://fdc.nal.usda.gov/api-guide.html)

**Thank you very much**. 

> To report any issues, suggestions or improvement, please do so 
at [issues](https://github.com/Nelson-Gon/pyfdc/issues). 

> “Before software can be reusable it first has to be usable.” – Ralph Johnson

---

If you would like to cite this work, please use:

Nelson Gonzabato(2020) pyfdc: A python interface to FoodDataCentral, https://github.com/Nelson-Gon/pyfdc

BibTex:

```shell
@misc{Gonzabato2020,
  author = {Gonzabato, N},
  title = {pyfdc: A python interface to FoodDataCentral},
  year = {2020},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/Nelson-Gon/pyfdc}},
  commit = {ead2bef877ef28ff75b949267f95cf1ceb09c5c4}
} 
```