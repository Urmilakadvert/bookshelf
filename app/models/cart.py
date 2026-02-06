from datetime import datetime
from app import db


class Cart(db.Model):
    """Cart model for temporarily holding selected books per user."""
    __tablename__ = 'carts'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False, index=True)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    # Unique constraint: one cart entry per user-book combination
    __table_args__ = (db.UniqueConstraint('user_id', 'book_id', name='_user_book_uc'),)
    
    def __repr__(self):
        return f'<Cart user_id={self.user_id} book_id={self.book_id}>'
