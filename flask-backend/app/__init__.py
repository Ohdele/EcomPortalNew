"""
This module initializes the Flask application and its configurations.
"""

from flask import Flask
from config.config import Config
from app.extensions import db  # Import db from app.extensions
from app.auth import auth_bp  # Import auth_bp from app.auth

def create_app():
    """
    Create and configure the Flask application instance.

    Returns:
        Flask app: The configured Flask application instance.
    """
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    @app.route('/')
    def home():
        """
        Define the home route for the application.

        Returns:
            str: A simple message indicating the home route is working.
        """
        return 'Hello, Flask!'

    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
