import requests
from config import api_key


def pyvelp():
    # Define the Yelp API endpoint for business search
    url = 'https://api.yelp.com/v3/businesses/search'

    # Set up the headers with the API key for authentication
    headers = {
        "Authorization": "Bearer " + api_key
    }

    # Define the search parameters: looking for 'barber' in 'NYC'
    params = {
        "term": "barber",      # Search term
        "location": "NYC"      # Search location
    }

    # Send an HTTP GET request to the Yelp API with the headers and search parameters
    response = requests.get(url, headers=headers, params=params)

    # Parse the JSON response to get the list of businesses
    businesses = response.json()["businesses"]

    # Loop through the businesses and print their names
    for business in businesses:
        print(business['name'])

    # Create a list of business names with a rating higher than 4.5
    name = [business['name']
            for business in businesses if business['rating'] > 4.5]

    # Print the filtered list of names with high ratings
    print(name)
