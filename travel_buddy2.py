# pip install sqlalchemy-utils

def getCoordinates(target):
# This function uses Google Geocode to convert the user's search into latitude / longitude coordinates.

    #Imports
    import requests
    import json

    # Get Google developer API key from file: api_keys.py
    from api_keys import google_key

    # Test Target (this will be passed in from calling routine)
    target = "30303"

    # Build the endpoint URL
    target_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={target}&key={google_key}"

    try:
        # Run a request to the endpoint and convert result to a json
        response = requests.get(target_url)
        geo_data = response.json()

        # Extract latitude and longitude
        lat = geo_data["results"][0]["geometry"]["location"]["lat"]
        lng = geo_data["results"][0]["geometry"]["location"]["lng"]

        # Output the coordinates
        print(f"Latitude: {lat}")
        print(f"Longitude: {lng}")
        return ([lat, lng])

    except:
        # Returnb an error message if API request failed
        print(f"An error has occured: {response.status_code} {response.reason}")
        return ("N/A")

##############################################################################################################################

def getYelpPlaces(input_lat, input_lon, category):
# This function collects the data from Yelp API and returns it as a dataframe.

    #Imports
    import requests
    import json
    import pandas as pd

    # Get Yelp API key from file: api_keys.py
    from api_keys import yelp_key

    # Test parameters (these will be passed in from calling routine)
    input_lat = lat
    input_lon = lng
    category = 'restaurants'

    # Construct the search parameters
    headers = {'Authorization': 'Bearer {}'.format(yelp_key)}
    url = 'https://api.yelp.com/v3/businesses/search'
    params = {
        'categories': category, 
        'latitude': input_lat,
        'longitude': input_lon,
        'limit': 50
    }

    # Run a request to the endpoint and convert to a json
    try:
        response = requests.get(url, headers=headers, params=params, timeout=5)
        yelp_data = response.json()
    except:
        print(f"An error has occured: {response.status_code} {response.reason}")    
        return ("N/A")

    num_places = len(yelp_data["businesses"])

    # Define empty lists to place data into
    search_zip = []
    name = []
    price = []
    rating = []
    address = []
    city = []
    zip_code = []
    phone = []
    img = []
    latitude = []
    longitude = []

    # Populate the lists
    for place in yelp_data["businesses"]:
        price_available =  "price" in place
        search_zip.append(f'{input_lat},{input_lon}')
        name.append(place['name'])
        if price_available:
            price.append(place['price'])
        else:
            price.append('N/A')  # in case the price rating is missing
        rating.append(place['rating'])
        address.append(place['location']['address1'])
        city.append(place['location']['city'])
        zip_code.append(place['location']['zip_code'])
        latitude.append(place['coordinates']['latitude'])
        longitude.append(place['coordinates']['longitude'])
        phone.append(place['phone'])
        img.append(place['image_url'])

    # Put lists into dictionary
    yelp_dict = {
        'Search Area': search_zip,
        'Name':name,
        'Price':price,
        'Rating':rating,
        'Address':address,
        'City':city,
        'Zip Code':zip_code,
        'Phone':phone,
        'Image':img,
        'Latitude':latitude,
        'Longitude':longitude 
    }

    # Convert distionary to dataframe
    yelp_DF = pd.DataFrame(yelp_dict)

    # Return the dataframe
    return (yelp_DF.head())

##############################################################################################################################

def appendTable(DF, table_name):
# This function inserts a table into the PostgreSQL database.

    # Imports
    import pandas as pd
    import sqlalchemy as sql
    from sqlalchemy_utils import database_exists, create_database

    # Get PostgreSQL password from file: api_keys.py
    from api_keys import postgresql_pwd

    # Test parameters (these will be passed in from the calling routine)
    DF = yelp_DF
    table_name = "Restaurants"

    # Put dataframes into PostgreSQL database
    # Make sure your password has been retrieved above and make sure that PostgreSQL is running!!!
    try:
        engine = sql.create_engine(f"postgresql://postgres:{postgresql_pwd}@localhost/TravelBuddyDB")
        print("Connection to PostgreSQL successful.")
        if not database_exists(engine.url):
            create_database(engine.url)
            print("New database created: TravelBuddyDB")
        else:
            print("Connection to database TravelBuddyDB successful.")
        try:
            with engine.connect() as cnxn:  # the connection will automatically close after executing the with block
                DF.to_sql(table_name, cnxn, if_exists="append")
                print(f"{table_name} successfully inserted.")            
        except:
            print("Failed to create table.")
    except:
        print("Failed to connect.")

##############################################################################################################################

