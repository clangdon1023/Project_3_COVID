from flask import Flask, render_template, jsonify
from flask_cors import CORS
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

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

@app.route("/")
def index():
    return render_template("Index3_Map and side summary by country.html")

@app.route("/api/v1.0/covid")
def covid():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all data
    results = session.query(clean.Province_State, clean.Country_Region, clean.Lat, clean.Long, clean.Date, clean.Confirmed, clean.Deaths, clean.Recovered, clean.Active, clean.WHO_Region).all()

    session.close()

    # Create a dictionary from the row data
    all_COVID = []
    for (Province_State, Country_Region, Lat, Long, Date, Confirmed, Deaths, Recovered, Active, WHO_Region) in results:
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
            "WHO_Region": WHO_Region,
        }
        all_COVID.append(COVID_dict)

    return jsonify(all_COVID)

if __name__ == '__main__':
    app.run(debug=True)




