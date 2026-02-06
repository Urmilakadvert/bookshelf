from datetime import datetime, timezone
from app import db


class Review(db.Model):
    """Review model for storing user ratings and comments."""
    __tablename__ = 'reviews'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False, index=True)
    rating = db.Column(db.Integer, nullable=False)  # 1-5 stars
    comment = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    # Constraint: rating must be between 1 and 5
    __table_args__ = (db.CheckConstraint('rating >= 1 AND rating <= 5', name='check_rating_range'),)
    
    def __repr__(self):
        return f'<Review user_id={self.user_id} book_id={self.book_id} rating={self.rating}>'
