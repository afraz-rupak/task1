# -*- coding: utf-8 -*-
"""Task3_Integration with Google API.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ELBdgSZqC7B6pFmpjdCZJkAfs5W7HzEE
"""

import requests

def get_location_info(api_key, address):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"

    # Set up parameters for the API request
    params = {
        'address': address,
        'key': api_key,
    }

    # Make the API request
    response = requests.get(base_url, params=params)
    data = response.json()

    # Check if the request was successful
    if response.status_code == 200 and data['status'] == 'OK':
        # Extract relevant information from the response
        results = data['results'][0]
        location = results['formatted_address']
        coordinates = results['geometry']['location']

        return location, coordinates
    else:
        print(f"Error: {data['status']}")
        return None

# i don't have any "google_api_key" that the reason i blank it.
google_api_key = 'google_api_key'
location_address = 'Any location we can enter'

result = get_location_info(google_api_key, location_address)

if result:
    location, coordinates = result
    print(f"Location: {location}")
    print(f"Coordinates: {coordinates}")