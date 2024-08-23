"""
This module creates a simple Flask application.

It defines a single route that returns a 'Hello, Flask!' message when accessed.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    """
    Handle requests to the root URL.

    Returns:
        str: A message indicating that Flask is running.
    """
    return 'Hello, Flask!'

if __name__ == '__main__':
    """
    Run the Flask application in debug mode if this module is executed directly.
    """
    app.run(debug=True)
