#dependencies
import requests
import numpy as np
import datetime as dt
import pandas as pd
import os


import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, render_template, redirect, url_for, request
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
#engine = create_engine("sqlite:///travel.sqlite")

# reflect an existing database into a new model
#Base = automap_base()
# reflect the tables
#Base.prepare(engine, reflect=True)

# Save reference to the table
#Passenger = Base.classes.passenger

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################



# WEB ROUTES
@app.route("/",methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        form = request.form
        print(form)
    print("Server accessed to the Home route")
    return render_template("index.html")

@app.route("/results",methods=['GET', 'POST'])
def searchresults():
    if request.method == 'POST':
        form = request.form
        return form
    else:
        return "something"


# accessing a different route
@app.route("/Hotels")
def popular():
    print("Server accessed to the Popular route")
    return("Popular Hotels")



@app.route("/Gyms")
def workout():
    print("Server accessed to the Popular route")
    return("Popular Hotels")


@app.route("/Entertainment")
def party():
    print("Server accessed to the Popular route")
    return("Popular Hotels")

#API ROUTES
#@app.route("api/<lan")
#def get_landmarks():
    #showme = col.find({"landmarks"})
    #showme = dict(showme)
    #return jsonify(showme)

# defining main function
if __name__ == "__main__":
    app.run(debug=True)
    
    
#make requests for updated location, remarks, etc. Create new script


# update database on api calls manually by going to browser
# or schedule to update daily
#@app.route("api/update_db")
#def update_database():
    
    # establish db connection



    # call api
    #url = "provide"
    ###if len(data) > db_entries:
    # add new to database if true
    