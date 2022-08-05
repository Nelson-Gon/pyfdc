from pyfdc.pyfdc import FoodDataCentral
from pandas import DataFrame
import os
from unittest.mock import patch
import requests
from unittest import mock
from pyfdc.utils import set_api_key
import pytest

# set API key from a users OS environ
# Only on Github actions
# TODO: Check that this only runs on GH Actions 
set_api_key("EMgmhkxg9Jfp2N8zw6gQ29u5Oek1sHvsWmkFJycE")

@pytest.fixture 
def my_search():
    def _search(**kwargs):
        return FoodDataCentral(**kwargs)
    return _search    


def test_instance(my_search):
    assert isinstance(my_search(), FoodDataCentral)
    assert isinstance(my_search().available_targets, dict)
    with pytest.warns(Warning, match = "Providing an api_key is discouraged, please consider using set_api_key.") as wrng:
        my_search(api_key = "fakekey")



# This mocks what set_api_key does.
# TODO: use an actual mock, this looks like a poor mxn's mock?
def test_api_key_mocks():
    with patch.dict('os.environ', {"pyfdc_key": "EMgmhkxg9Jfp2N8zw6gQ29u5Oek1sHvsWmkFJycE"}):
        assert os.environ["pyfdc_key"] == "EMgmhkxg9Jfp2N8zw6gQ29u5Oek1sHvsWmkFJycE"
        assert "pyfdc_key" in os.environ
    pass

def test_get_food_info(my_search):
    with pytest.warns(UserWarning, match = "No target_fields were provided, returning fdc_id, ingredients, and description.") as uwarn:
        my_search().get_food_info(search_phrase="cheese")
                        
    with pytest.raises(TypeError, match ="target should be a list or tuple not int") as err:
        my_search().get_food_info(search_phrase="cheese", target_fields=1234)

    # Check that we indeed get cheese
    res = my_search().get_food_info(search_phrase="cheese", target_fields=["description"])
    say_cheese = res["description"].iloc[0]
    assert say_cheese == "CHEESE"

    # Check that we raise a KeyError
    with pytest.raises(KeyError):
        # Need to figure out how to test the actual error
        my_search().get_food_info(search_phrase="cheese", target_fields=["not_in"])

    # Check that we get an HTTPError if we have the wrong api_key
    with pytest.raises(requests.exceptions.HTTPError):
        FoodDataCentral(api_key="fakekey").get_food_info(search_phrase="cheese")

def test_get_food_details(my_search):
    with pytest.raises(AssertionError, match ="fdc_id should not be None") as err:
        my_search().get_food_details()

    with pytest.raises(AssertionError, match = "fdc_id should be an int not str") as err:
        my_search().get_food_details(fdc_id="string_id")

    with pytest.warns(UserWarning, match = "No target_field was provided, returning low level results.") as uwarn2:
        my_search().get_food_details(fdc_id=496446)
       

    # Check that we get the expected result

    food_details = my_search().get_food_details(fdc_id=496446, target_field="nutrients")

    assert isinstance(food_details, DataFrame)

    # Expect HTTP Errors if we have fake api keys for instance
    # https://docs.pytest.org/en/6.2.x/reference.html#pytest._code.ExceptionInfo
    with pytest.raises(requests.HTTPError) as exc_info:
        FoodDataCentral(api_key="fake").get_food_details(fdc_id=496446,
                                                             target_field="description")

        # Fake API Key --> I will not let you in :)
    assert exc_info.value.response.status_code == 403

    with pytest.raises(KeyError):
        my_search().get_food_details(fdc_id=496446, target_field="some_fake_key")

        # Check that we get the same fdc_id as we sent

    assert my_search().get_food_details(fdc_id=496446, target_field="fdcId") == 496446

    assert isinstance(my_search().get_food_details(fdc_id=496446, target_field="label_nutrients"),
                             DataFrame)
    # Check that we can raise a KeyError if no label nutrients are present 
    # print(my_search.get_food_details(fdc_id=168977, target_field="label_nutrients"))
    with pytest.raises(KeyError, match="FDC ID 168977 has no label nutrients."):
            my_search().get_food_details(fdc_id=168977, target_field="label_nutrients")
    # @mock.patch("pyfdc.utils.input")
    # def test_utils(self, mock_input):
    #     mock_input.side_effect = "False"
    #     with self.assertRaises(ValueError):
    #         set_api_key()




