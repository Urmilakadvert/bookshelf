from app import db


class OrderItem(db.Model):
    """OrderItem model for storing multiple books per order."""
    __tablename__ = 'order_items'
    
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False, index=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False, index=True)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)  # Store price at time of purchase
    
    def __repr__(self):
        return f'<OrderItem order_id={self.order_id} book_id={self.book_id}>'
