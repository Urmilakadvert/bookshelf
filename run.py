#!/usr/bin/env python3
"""Run script for the bookshelf application."""
from app import create_app

if __name__ == '__main__':
    app = create_app()
    print("Bookshelf application created successfully!")
    print(f"Database: {app.config['SQLALCHEMY_DATABASE_URI']}")
    print("\nAll models have been created:")
    print("  - User (login details and roles)")
    print("  - Book (catalog info: title, price, stock, description)")
    print("  - Cart (temporarily holds selected books per user)")
    print("  - Order (checkout details and order status)")
    print("  - OrderItem (multiple books per order)")
    print("  - Payment (transaction tracking and payment status)")
    print("  - Review (user ratings and comments)")
    print("\nFlow: User → Books → Cart → Order → Payment → Tracking → Review")
