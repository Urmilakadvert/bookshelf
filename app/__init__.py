from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

# Initialize SQLAlchemy
db = SQLAlchemy()


def create_app(config_class=Config):
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    
    # Create database tables
    with app.app_context():
        # Import models to ensure they are registered with SQLAlchemy
        from app.models import user, book, cart, order, order_item, payment, review
        db.create_all()
    
    return app
