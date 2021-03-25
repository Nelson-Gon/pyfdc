from pyfdc.pyfdc import FoodDataCentral
from pandas import DataFrame
import unittest
import os
from unittest.mock import patch
import requests

# Create a test object


my_search = FoodDataCentral(api_key="EMgmhkxg9Jfp2N8zw6gQ29u5Oek1sHvsWmkFJycE")
# Using one object will fail because the base_url will change.
my_details = FoodDataCentral(api_key="EMgmhkxg9Jfp2N8zw6gQ29u5Oek1sHvsWmkFJycE")


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
            my_details.get_food_details()
        self.assertEqual(str(err.exception), "fdc_id should not be None")

        with self.assertRaises(AssertionError) as err:
            my_details.get_food_details(fdc_id="string_id")
        self.assertEqual(str(err.exception), "fdc_id should be an int not str")

        with self.assertWarns(UserWarning) as uwarn2:
            my_details.get_food_details(fdc_id=496446)
        self.assertEqual(str(uwarn2.warning), "No target_field was provided, returning low level results.")

        # Check that we get the expected result

        food_details = my_details.get_food_details(fdc_id=496446, target_field="nutrients")

        self.assertIsInstance(food_details, DataFrame)


if __name__ == "__main__":
    unittest.main()
