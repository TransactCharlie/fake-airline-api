__author__ = 'Charlie'

from flask import Flask
from db_tools import std_connection
import json

from sql_queries import FULLY_QUALIFIED_PRICE_QUERY, ALL_PRICES_QUERY

# Register the Flask Container
app = Flask(__name__)



@app.route('/all_routes')
def raw_db():
    """returns all the routes we have!"""
    with std_connection() as conn:
        rows = conn.execute(ALL_PRICES_QUERY)
        return json.dumps(rows.fetchall(), indent = 4)



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

        return json.dumps(rows.fetchall(), indent=4)



# Run the application
if __name__ == "__main__":
    # Turn on application debugging
    app.debug = True
    # Disable access control (otherwise only this machine could see the api)
    app.host = '0.0.0.0'
    # enable multi-threaded (so we can server more than one request at once)
    app.threaded = True
    # Run the application
    app.run()