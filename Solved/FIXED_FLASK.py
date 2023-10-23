import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
from flask_cors import CORS  # Import Flask-CORS

# Database Setup
engine = create_engine("sqlite:///clean.sqlite")
Base = automap_base()
Base.prepare(autoload_with=engine)
clean = Base.classes.clean

# Flask Setup
app = Flask(__name__)
# Enable CORS for your app
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Flask Routes

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
    session = Session(engine)
    results = session.query(clean.Province_State, clean.Country_Region, clean.Lat, clean.Long, clean.Date, clean.Confirmed, clean.Deaths, clean.Recovered, clean.Active, clean.WHO_Region).all()
    session.close()

    all_COVID = []
    for Province_State, Country_Region, Lat, Long, Date, Confirmed, Deaths, Recovered, Active, WHO_Region in results:
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

if __name__ == '__main__':
    app.run(debug=True)
