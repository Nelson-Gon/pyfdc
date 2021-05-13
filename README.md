# pyfdc: A python interface to FoodDataCentral
[![PyPI version fury.io](https://badge.fury.io/py/pyfdc.svg)](https://pypi.python.org/pypi/pyfdc/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3764453.svg)](https://doi.org/10.5281/zenodo.3764453)
[![Project Status](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active) 
[![Codecov](https://codecov.io/gh/Nelson-Gon/pyfdc/branch/master/graph/badge.svg)](https://codecov.io/gh/Nelson-Gon/pyfdc?branch=master)
![Test-Package](https://github.com/Nelson-Gon/pyfdc/workflows/Test-Package/badge.svg)
![Travis Build](https://travis-ci.com/Nelson-Gon/pyfdc.svg?branch=master)
[![PyPI license](https://img.shields.io/pypi/l/pyfdc.svg)](https://pypi.python.org/pypi/pyfdc/)
[![Documentation Status](https://readthedocs.org/projects/pyfdc/badge/?version=latest)](https://pyfdc.readthedocs.io/en/latest/?badge=latest)
[![Total Downloads](https://pepy.tech/badge/pyfdc)](https://pepy.tech/project/pyfdc)
[![Monthly Downloads](https://pepy.tech/badge/pyfdc/month)](https://pepy.tech/project/pyfdc)
[![Weekly Downloads](https://pepy.tech/badge/pyfdc/week)](https://pepy.tech/project/pyfdc)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Nelson-Gon/pyfdc/graphs/commit-activity)
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
git clone git@github.com:Nelson-Gon/pyfdc.git
cd pyfdc
python3 setup.py install

```



**Sample usage**


There are two ways to use `pydfc`. In script mode, one does the following:

```shell
python -m pyfdc --method "info" --phrase "cheese" | head
#/pyfdc/pyfdc/pyfdc.py:109: UserWarning: No target_fields were provided, returning fdc_id, ingredients, and description.
#  warn("No target_fields were provided, returning fdc_id, ingredients, and description.")
#     fdc_id  ...                                   description
#0    816524  ...                                        CHEESE
#1   1463368  ...                                        CHEESE
#2   1597534  ...                                        CHEESE
#3   1653804  ...                                        CHEESE
#4   1660793  ...                                        CHEESE
#5   1497465  ...                                        CHEESE
#6   1465399  ...                                        CHEESE
#7    515803  ...                                        CHEESE
#8    500370  ...                                        CHEESE
#



```

The above uses the `get_food_info` method. To use, the `get_food_details` method, one simply sets method to "details" 
and provides the target FoodDataCentral ID. 

```shell
 python -m pyfdc --method "details" --phrase 816524  --fields "nutrients"
 
#      id number                                      name   rank unitName
#0   1004    204                         Total lipid (fat)    800        g
#1   1257    605                  Fatty acids, total trans  15400        g
#2   1079    291                      Fiber, total dietary   1200        g
#3   1003    203                                   Protein    600        g
#4   1005    205               Carbohydrate, by difference   1110        g
#5   1110    324  Vitamin D (D2 + D3), International Units   8650       IU
#6   1008    208                                    Energy    300     kcal
#7   2000    269              Sugars, total including NLEA   1510        g
#8   1089    303                                  Iron, Fe   5400       mg
#9   1087    301                               Calcium, Ca   5300       mg
#10  1258    606              Fatty acids, total saturated   9700        g
#11  1093    307                                Sodium, Na   5800       mg
#12  1253    601                               Cholesterol  15700       mg

```


```python

from pyfdc.pyfdc import FoodDataCentral
from pyfdc.utils import set_api_key

```

**Set session api key**

To avoid providing an api key for each call, one can set a session api key as follows:

```python

set_api_key("my_api_key_here")


```


**Key Features**

There is one major class `FoodDataCentral`. 
See the [changelog](https://github.com/Nelson-Gon/pyfdc/blob/master/changelog.md) 
for more details.:

To instantiate an object:

```python
my_search = FoodDataCentral()
```

To get details about foods for a given search term, one can do the following:

```python

my_search.get_food_info(search_phrase="cheese").head(6)

```

The above will result in the following output:

```shell

#
#UserWarning: No target_fields were provided, returning fdc_id, ingredients, and description.
#    fdc_id                                        ingredients description
#0   816524  BELLAVITANO CHEESE (PASTEURIZED MILK, CHEESE C...      CHEESE
#1  1210322  BELLAVITANO CHEESE (PASTEURIZED MILK, CHEESE C...      CHEESE
#2  1291586  CHEDDAR CHEESE (PASTEURIZED MILK, CHEESE CULTU...      CHEESE
#3  1305389   PASTEURIZED COWS' MILK, SALT, CULTURES, ENZYMES.      CHEESE
#4  1361608  CULTURED PASTEURIZED MILK, SALT, NON-ANIMAL EN...      CHEESE
#5  1420013  FRESH PART-SKIM COW'S MILK, CHEESE CULTURE SAL...      CHEESE


```


In the above, we got a warning message because we used defaults out-of-the-box. To customize, we can set 
the `target_fields` we wish to have.

```python
mysearch.get_food_info(search_phrase="cheese", target_fields=["description"]).head(4)

# description
# 0      CHEESE
# 1      CHEESE
# 2      CHEESE
# 3      CHEESE
```





To get full details about a given `fdcId`, one can do the following:

```python

mysearch.get_food_details(168977)

```

This will give us the following output(truncated):

```shell
# UserWarning: No target_field was provided, returning low level results.
#           0                                                  1
#0                      fdcId                                             168977
#1                description  Agutuk, meat-caribou (Alaskan ice cream) (Alas...
#2            publicationDate                                           4/1/2019
#3              foodNutrients  [{'nutrient': {'id': 2045, 'number': '951', 'n...
#4                   dataType                                          SR Legacy

```

The above is a low-level result that may be useful for development purpises. 

To get nutrient details:

```shell

my_search.get_food_details(fdc_id= 496446,target_field="nutrients")

#   id number                                name   rank unitName
#0   2045    951                          Proximates     50        g
#1   1051    255                               Water    100        g
#2   1008    208                              Energy    300     kcal
#3   1062    268                              Energy    400       kJ
#4   1003    203                             Protein    600        g
#5   1004    204                   Total lipid (fat)    800        g


  

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
@misc{Gonzabato2021,
  author = {Gonzabato, N},
  title = {pyfdc: A python interface to FoodDataCentral},
  year = {2021},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/Nelson-Gon/pyfdc}},
  commit = {20923d9dbea9dcf1b5cba741625b01f6637a6d7b}
} 
```