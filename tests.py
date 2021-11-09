from pyfdc.pyfdc import FoodDataCentral
from pandas import DataFrame
import unittest
import os
from unittest.mock import patch
import requests
from unittest import mock
from pyfdc.utils import set_api_key
# Create a test object

# set API key from a users OS environ
# Only on Github actions
# TODO: Check that this only runs on GH Actions 
set_api_key(os.environ["PYFDC_KEY"])

my_search = FoodDataCentral()


class Testpyfdc(unittest.TestCase):

    def test_instance(self):
        self.assertIsInstance(my_search, FoodDataCentral)
        # Check that available targets exists
        self.assertIsInstance(my_search.available_targets, dict)
        with self.assertWarns(Warning) as wrnng:
            FoodDataCentral(api_key="fakekey")
        self.assertEqual(str(wrnng.warning), "Providing an api_key is discouraged, please consider using set_api_key.")

    # Check api_key equality
    # This mocks what set_api_key does.

    def test_api_key_mocks(self):
        with patch.dict('os.environ', {"pyfdc_key": "EMgmhkxg9Jfp2N8zw6gQ29u5Oek1sHvsWmkFJycE"}):
            assert os.environ["pyfdc_key"] == "EMgmhkxg9Jfp2N8zw6gQ29u5Oek1sHvsWmkFJycE"
            assert "pyfdc_key" in os.environ
        pass

    def test_get_food_info(self):
        with self.assertWarns(UserWarning) as uwarn:
            my_search.get_food_info(search_phrase="cheese")
        self.assertEqual(str(uwarn.warning),
                         "No target_fields were provided, returning fdc_id, ingredients, and description.")
        with self.assertRaises(TypeError) as err:
            my_search.get_food_info(search_phrase="cheese", target_fields=1234)

        self.assertEqual(str(err.exception), "target should be a list or tuple not int")

        # Check that we indeed get cheese
        res = my_search.get_food_info(search_phrase="cheese", target_fields=["description"])
        say_cheese = res["description"].iloc[0]
        self.assertEqual(say_cheese, "CHEESE")

        # Check that we raise a KeyError
        with self.assertRaises(KeyError):
            # Need to figure out how to test the actual error
            my_search.get_food_info(search_phrase="cheese", target_fields=["not_in"])

        # Check that we get an HTTPError if we have the wrong api_key
        with self.assertRaises(requests.exceptions.HTTPError):
            FoodDataCentral(api_key="fakekey").get_food_info(search_phrase="cheese")

    def test_get_food_details(self):
        with self.assertRaises(AssertionError) as err:
            my_search.get_food_details()
        self.assertEqual(str(err.exception), "fdc_id should not be None")

        with self.assertRaises(AssertionError) as err:
            my_search.get_food_details(fdc_id="string_id")
        self.assertEqual(str(err.exception), "fdc_id should be an int not str")

        with self.assertWarns(UserWarning) as uwarn2:
            my_search.get_food_details(fdc_id=496446)
        self.assertEqual(str(uwarn2.warning), "No target_field was provided, returning low level results.")

        # Check that we get the expected result

        food_details = my_search.get_food_details(fdc_id=496446, target_field="nutrients")

        self.assertIsInstance(food_details, DataFrame)

        # Expect HTTP Errors if we have fake api keys for instance

        with self.assertRaises(requests.HTTPError) as err:
            FoodDataCentral(api_key="fake").get_food_details(fdc_id=496446,
                                                             target_field="description")

        # Fake API Key --> I will not let you in :)
        self.assertEqual(err.exception.response.status_code, 403)

        with self.assertRaises(KeyError):
            my_search.get_food_details(fdc_id=496446, target_field="some_fake_key")

        # Check that we get the same fdc_id as we sent

        self.assertEqual(my_search.get_food_details(fdc_id=496446, target_field="fdcId"), 496446)

        self.assertIsInstance(my_search.get_food_details(fdc_id=496446, target_field="label_nutrients"),
                             DataFrame)
        # Check that we can raise a KeyError if no label nutrients are present 
        # print(my_search.get_food_details(fdc_id=168977, target_field="label_nutrients"))
        with self.assertRaises(KeyError, msg="FDC ID 168977 has no label nutrients."):
            my_search.get_food_details(fdc_id=168977, target_field="label_nutrients")
        pass
    # @mock.patch("pyfdc.utils.input")
    # def test_utils(self, mock_input):
    #     mock_input.side_effect = "False"
    #     with self.assertRaises(ValueError):
    #         set_api_key()



if __name__ == "__main__":
    unittest.main()
