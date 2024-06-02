# importing libraries
import pandas as pd
import numpy as np
import requests
import json

def getting_food_recalls(number_of_reports, initial_date, final_date):
    # Replacing "-" to "" to be sure the dates can be passed into the api url
    initial_date = initial_date.replace("-", "")
    final_date = final_date.replace("-", "")

    # Defining url for the api
    fda_url_api = f"https://api.fda.gov/food/enforcement.json?search=report_date:[{initial_date}+TO+{final_date}]&limit={number_of_reports}"

    # Trying to call the api
    r = requests.get(fda_url_api)
    status_code = r.status_code

    if status_code == 200:
        try:
            print('API Called Successfully :)')

            # Getting the text
            raw_data = r.json()

            # Normalize the data using pandas
            normalized_data = pd.json_normalize(raw_data['results'])

            # Convert it into a pandas dataframe
            df = pd.DataFrame(normalized_data)

            return df
        except Exception as e:
            print(f'ERROR: {e}')
    else:
        print('Error while calling the API :(')
        
