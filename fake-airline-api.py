__author__ = 'Charlie'

from flask import Flask
import json

# Register the Flask Container
app = Flask(__name__)



@app.route("/about")
def about():
    return "A Fake API representing an Airline API"



@app.route("/api/<from_iata>/<to_iata>/<departure_date>/<return_date>/")
def api(from_iata, to_iata, departure_date, return_date):
    return json.dumps({
        'from_iata': from_iata,
        'to_iata': to_iata,
        'departure_date': departure_date,
        'return_date': return_date
    }, indent = 4)



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