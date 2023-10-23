import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
from flask_cors import CORS

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///clean.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table
clean = Base.classes.clean

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
# Configure CORS
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5000"}})

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/covid: <br/>"
        f"/api/v1.0/test"
    )





@app.route("/api/v1.0/covid")
def covid():
     #Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of passenger data including the name, age, and sex of each passenger"""
    #Query all passengers
    results = session.query(clean.Province_State, clean.Country_Region, clean.Lat, clean.Long, clean.Date, clean.Confirmed, clean.Deaths, clean.Recovered, clean.Active, clean.WHO_Region).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_COVID = []
    for Province_State, Country_Region,Lat, Long, Date, Confirmed, Deaths, Recovered, Active, WHO_Region in results:
        COVID_dict = {}
        COVID_dict["Province_State"] = Province_State
        COVID_dict["Country_Region"] = Country_Region
        COVID_dict["Lat"] = Lat
        COVID_dict["Long"] = Long
        COVID_dict["Date"] = Date
        COVID_dict["Confirmed"] = Confirmed
        COVID_dict["Deaths"] = Deaths
        COVID_dict["Recovered"] = Recovered
        COVID_dict['Active'] = Active
        COVID_dict["WHO_Region"] = WHO_Region
        all_COVID.append(COVID_dict)

    return jsonify(all_COVID)


if __name__ == '__main__':
    app.run(debug=True)
