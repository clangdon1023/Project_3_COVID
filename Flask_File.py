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

# Reflect an existing database into a new model
Base = automap_base()
# Reflect the tables
Base.prepare(engine, reflect=True)

# Save references to the tables
Clean = Base.classes.clean
USA = Base.classes.usacountry  # Renamed to "USA" for clarity

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
CORS(app)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available API routes."""
    return (
        "Available Routes:<br/>"
        "/api/v1.0/covid:<br/>"
        "/api/v1.0/USA:"
    )

@app.route("/api/v1.0/covid")
def covid():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all COVID data
    results = session.query(
        Clean.Province_State, Clean.Country_Region, Clean.Lat, Clean.Long,
        Clean.Date, Clean.Confirmed, Clean.Deaths, Clean.Recovered,
        Clean.Active, Clean.WHO_Region
    ).all()

    session.close()

    # Create a list of dictionaries to store the COVID data
    all_COVID = []
    for record in results:
        Province_State, Country_Region, Lat, Long, Date, Confirmed, Deaths, Recovered, Active, WHO_Region = record
        COVID_dict = {
            "Province_State": Province_State,
            "Country_Region": Country_Region,
            "Lat": Lat,
            "Long": Long,
            "Date": Date,
            "Confirmed": Confirmed,
            "Deaths": Deaths,
            "Recovered": Recovered,
            "Active": Active,
            "WHO_Region": WHO_Region
        }
        all_COVID.append(COVID_dict)

    return jsonify(all_COVID)

@app.route("/api/v1.0/USA")
def usa_data():  # Renamed function to avoid variable conflict
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all USA data
    results = session.query(
        USA.id, USA.UID, USA.iso2, USA.iso3, USA.code3, USA.FIPS,
        USA.Admin2, USA.Province_State, USA.Lat, USA.Long_, USA.Combined_Key,
        USA.Date, USA.Confirmed, USA.Deaths
    ).all()

    session.close()

    # Create a list of dictionaries to store the USA data
    usa_data = []
    for record in results:
        id, UID, iso2, iso3, code3, FIPS, Admin2, Province_State, Lat, Long_, Combined_Key, Date, Confirmed, Deaths = record
        usa_dict = {
            "id": id,
            "UID": UID,
            "iso2": iso2,
            "iso3": iso3,
            "code3": code3,
            "FIPS": FIPS,
            "Admin2": Admin2,
            "Province_State": Province_State,
            "Lat": Lat,
            "Long_": Long_,
            "Combined_Key": Combined_Key,
            "Date": Date,
            "Confirmed": Confirmed,
            "Deaths": Deaths
        }
        usa_data.append(usa_dict)

    return jsonify(usa_data)

if __name__ == '__main__':
    app.run(debug=True)
