# python-fdc: A python interface to FoodDataCentral
![Travis Build](https://travis-ci.com/Nelson-Gon/python-fdc.svg?branch=master)

**This is a work in progress. Things might break and change unannounced. It is still highly experimental.**

----

**Installation**

```
# clone the repo
git clone https://www.github.com/Nelson-Gon/python-fdc.git
cd python-fdc
python3 python-fdc/setup.py install

```
---

**Sample usage**

```
import python-fdc

```

**Query the database**

```
res = query_db(api_key= "my_api_key_here","search_query= "chicken")

```

**Extract specific Information**

To extract information about our search result, we can use `extract_food_info`:

```
extract_food_info(res, "fdcId")

[464651]
[504905]
[472365]
[490957]
[464664]


```

To get food descriptions:

```
extract_food_info(res, "description")

['CHICKEN']
['CHICKEN VIENNA SAUSAGE IN CHICKEN BROTH']
['CHICKEN STOCK']
['CHICKEN WINGS']
['CHICKEN ASADA']
['CHICKEN PICCATA']
['CHICKEN & RICE']

```

Given a Food DataCentral ID(`fdc_id`), one can get detailed information about a specific food as 
follows:

```
res = get_food_details(api_key="my_api_key_here", fdc_id=464651,
                       process_result=True, 
target_fields="description")

# 'CHICKEN'

```

