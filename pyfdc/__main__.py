def main():
    from pyfdc.pyfdc import FoodDataCentral
    import argparse
    import os

    arg_parser = argparse.ArgumentParser()

    # First ensure that we have an api_key set
    class NoAPIKey(Exception):
        pass

    try:
        os.environ["pyfdc_key"]
    except KeyError as err:
        raise NoAPIKey("A valid FDC API Key is required. Please set one first, programmatically")
    else:
        # Create FoodDataCentral object
        fdc_object = FoodDataCentral()

        # Create an argument to choose the kind of method to use

        arg_parser.add_argument("-m", "--method", type=str, help="Method to use, one of info or details",
                                choices=["info", "details"], required=True)
        arg_parser.add_argument("-sp", "--phrase", type=str, required=True,
                                help="Search term if food info, otherwise fdc_id")
        # List of target fields
        # TODO: Figure out why this only returns a duplicated version of the first target field
        arg_parser.add_argument("-f", "--fields", type=str,nargs="*", help="Target fields to return")

        arg_parser.add_argument("-ps", "--page-size", type=int, help="Number of results to return",
                                default=50, required=False)
        arg_parser.add_argument("-sf", "--sort-field", type=str, help="Sort by?", default=None, required=False)
        arg_parser.add_argument("-sd", "--sort-direction", type=str, help="Sort in which direction?",
                                default="asc", choices=["asc", "desc"], required=False)
        arg_parser.add_argument("-p", "--page", type=int, help="Page number of results to return", required=False,
                                default=1)

        arguments = arg_parser.parse_args()

        if arguments.method == "info":
            print(fdc_object.get_food_info(search_phrase=arguments.phrase, target_fields=arguments.fields,
                                           sort_field=arguments.sort_field, sort_direction=arguments.sort_direction,
                                           page_size=arguments.page_size, page_number=arguments.page))
        else:
            print(fdc_object.get_food_details(fdc_id=int(arguments.phrase), target_field=arguments.fields[0]))


if __name__ == "__main__":
    main()
