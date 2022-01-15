# Travel Buddy: Know Your Options, Wherever You Go. 

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
* Date Check
 * We would eventually like for data to be cached temporarily, with data over a week old being flushed, and replaced via a new API call. 
* Schema for DB
 * Adding Primary and Foreign keys to allow for CASCADING deletes of data to support the Date Check. 
* Leaflet vs Google Maps
 * The Google Maps widget appears to cause issues to work around due to its pre-integrated tools. We would like to explore if it is the best map tool to produce our vision. 
* Visual Star Respresentation
 * Currently Stars are being displayed as numbers, but we would like to replace these numbers with a visual represention. (i.e. Yelp, Amazon)
* Online database hosting. 
 * Eventually we would like the database to be housed online, so allow for better security / maintenance, as well as to share data added from across our user base. 

## 

### Structure:

* The folder Project 3 DV contains all files to produce the front end product. 
* The folder "Resources" contains all of the backend files required to build and update the database.
  * "SQL" contains the SQL data files.
  * "Python" contains python scripts used for pulling API data and submitting to database. 
  * "Archive" contains all files that are no longer being used. 
