# Bookshelf E-commerce System

A complete e-commerce system for managing a bookshelf with user authentication, cart management, order processing, payments, and reviews.

## System Overview

This application implements a full e-commerce flow for book sales:

**Flow**: User → Books → Cart → Order → Payment → Tracking → Review

## Entities

### 1. **Users**
- Stores login details and user roles (user/admin)
- Fields: id, email, password_hash, role, created_at
- Relationships: carts, orders, reviews

### 2. **Books**
- Stores catalog information
- Fields: id, title, price, stock, description, created_at
- Relationships: cart_items, order_items, reviews

### 3. **Cart**
- Temporarily holds selected books per user
- Fields: id, user_id, book_id, quantity, created_at
- Unique constraint: one cart entry per user-book combination

### 4. **Orders**
- Saves checkout details and order status
- Fields: id, user_id, status, total_amount, shipping_address, created_at, updated_at
- Status values: pending, confirmed, shipped, delivered, cancelled
- Relationships: order_items, payment

### 5. **OrderItems**
- Stores multiple books per order
- Fields: id, order_id, book_id, quantity, price
- Price is stored at time of purchase for historical accuracy

### 6. **Payments**
- Tracks transactions and payment status
- Fields: id, order_id, amount, status, transaction_id, payment_method, created_at, updated_at
- Status values: pending, completed, failed, refunded

### 7. **Reviews**
- Stores user ratings and comments
- Fields: id, user_id, book_id, rating, comment, created_at, updated_at
- Rating constraint: 1-5 stars

## Database Schema

```
users (1) ----< carts >---- (N) books
  |                           |
  |                           |
  +----< orders              |
          |                   |
          +----< order_items >+
          |                   |
          +---- payment       |
                              |
users (1) ----< reviews >---- (N) books
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd bookshelf
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create environment file:
```bash
cp .env.example .env
```

4. Run the application:
```bash
python run.py
```

## Testing

Run the flow demonstration to see all entities in action:

```bash
python test_flow.py
```

This will:
1. Create users with different roles (admin/user)
2. Add books to the catalog
3. Add books to a user's cart
4. Create an order from the cart
5. Process payment for the order
6. Track order status (pending → confirmed → shipped → delivered)
7. Add reviews for purchased books

## Project Structure

```
bookshelf/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── config.py            # Configuration
│   └── models/              # Database models
│       ├── __init__.py
│       ├── user.py          # User model
│       ├── book.py          # Book model
│       ├── cart.py          # Cart model
│       ├── order.py         # Order model
│       ├── order_item.py    # OrderItem model
│       ├── payment.py       # Payment model
│       └── review.py        # Review model
├── run.py                   # Application entry point
├── test_flow.py             # Flow demonstration
├── requirements.txt         # Python dependencies
├── .env.example            # Environment template
├── .gitignore              # Git ignore file
└── README.md               # This file
```

## Technology Stack

- **Framework**: Flask 3.0.0
- **ORM**: SQLAlchemy 2.0.23 with Flask-SQLAlchemy 3.1.1
- **Database**: SQLite (development)
- **Configuration**: python-dotenv for environment management

## Key Features

- ✅ User authentication with role-based access (user/admin)
- ✅ Book catalog management with stock tracking
- ✅ Shopping cart functionality per user
- ✅ Order processing and checkout
- ✅ Multiple items per order support
- ✅ Payment tracking with transaction IDs
- ✅ Order status tracking (lifecycle management)
- ✅ Product review and rating system
- ✅ Proper database relationships and constraints
- ✅ Cascading deletes for data integrity

## License

MIT License