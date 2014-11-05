__author__ = 'Charlie'

from flask import Flask, Response
from db_tools import std_connection
import json

from sql_statements import FULLY_QUALIFIED_PRICE_QUERY, ALL_PRICES_QUERY

# Register the Flask Container
app = Flask(__name__)



def parcel_json_response(payload):
    """returns a Response() object with payload, status 200, mimetype application/json"""
    return Response(response = payload, status = 200, mimetype = "application/json")



@app.route('/all_routes')
def all_routes():
    """returns all the routes we have!"""
    with std_connection() as conn:
        rows = conn.execute(ALL_PRICES_QUERY)
        res = json.dumps(rows.fetchall())
        return parcel_json_response(res)



@app.route("/api/<from_iata>/<to_iata>/<departure_date>/<return_date>")
def api(from_iata, to_iata, departure_date, return_date):
    """Takes the parameters and returns a price response from the cache"""
    with std_connection() as conn:

        SQL = FULLY_QUALIFIED_PRICE_QUERY

        filters = {
            "from_iata": from_iata,
            "to_iata": to_iata,
            "departure_date": departure_date,
            "return_date": return_date
            }

        rows = conn.execute(SQL, filters)
        res = json.dumps(rows.fetchall())

        return parcel_json_response(res)



def run_api():
    # Turn on application debugging
    app.debug = True
    # Disable access control (otherwise only this machine could see the api)
    app.host = '0.0.0.0'
    # enable multi-threaded (so we can server more than one request at once)
    app.threaded = True
    # Run the application
    app.run()



# Run the application
if __name__ == "__main__":
    run_api()