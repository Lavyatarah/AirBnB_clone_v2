#!/usr/bin/python3
"""starts flask web application
"""
from flask import Flask

app = Flask(__name__)

#Define the route for the route URL '/'
@app.route('/airbnb-onepage/' strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!"""
    return "Hello HBNB"


if__name__ == "__main__":
    #start the Flask development server
    #listen on all available interfaces (0.0.0.0) and port 5000
    app.run(host='0.0.0.0',port=5000
