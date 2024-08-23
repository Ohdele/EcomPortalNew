"""
This module defines the data models for the application.
"""

from datetime import datetime
from app.extensions import db  # Import db from app.extensions

class User(db.Model):
    """Represents a user in the database."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f'<User {self.username}>'

    def get_user_info(self):
        """Return user information."""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'date_created': self.date_created
        }
