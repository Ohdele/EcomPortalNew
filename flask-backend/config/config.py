class Config:
    """
    Configuration class for Flask application.

    Attributes:
        SECRET_KEY (str): Secret key for session management and security.
        SQLALCHEMY_DATABASE_URI (str): URI for the database connection.
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): Disable modification tracking.
    """
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Change to your database URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
