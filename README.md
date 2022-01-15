# Travel Buddy: Know Your Options Wherever You Go. 

## Travel Buddy is an interactive dashboard which allows you to submit a location of your choice in order to return nearby points of interest including hotels, restaurants, gyms, landmarks and entertainment.

### How It Works (User):

1. Input location into search bar (Cities, Zip Codes, and Landmarks accepted). The more specific your search, the better your results. 
2. The map will immediately show your searched location. 
3. Click on a category button to produce a list of the top 10 listings (by rating) in your chosen category. 

##

### How It Works (BTS):
1. HTML file loads with the google map - search bar, enter, 
2. App.py loads with HTML/CSS, which includes the integrated Google Map. 
3. Once an entry is received via the search bar, it is saved via JS, and passing it to the flask app. 
4. Clicking on one of the 5 location type buttons will call an app.py route, which will initiate a database check. 
5. If the data exists within the database, data will be returned and appear for the user. 
6. If the data does not exist within the database, a Yelp API call will be triggered, the data populated into the database, then returned for the user. 

##

### Future Considerations: 
1. Date Check
2. Schema for DB
3. Leaflet vs Google maps
4. Visual Star Respresentation

## 

### Structure:

* The folder Project 3 DV contains all files to produce the front end product. 
* The folder "Resources" contains all of the backend files required to build and update the database.
  * "SQL" contains the SQL data files.
  * "Python" contains python scripts used for pulling API data and submitting to database. 
  * "Archive" contains all files that are no longer being used. 
