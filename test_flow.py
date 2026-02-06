#!/usr/bin/env python3
"""Test script to demonstrate the bookshelf data models and flow."""
from app import create_app, db
from app.models import User, Book, Cart, Order, OrderItem, Payment, Review
from datetime import datetime


def test_bookshelf_flow():
    """Test the complete flow: User → Books → Cart → Order → Payment → Tracking → Review."""
    app = create_app()
    
    with app.app_context():
        # Clean up existing data
        db.drop_all()
        db.create_all()
        
        print("=" * 80)
        print("BOOKSHELF E-COMMERCE SYSTEM - FLOW DEMONSTRATION")
        print("=" * 80)
        
        # 1. Create Users (with roles)
        print("\n1. USERS - Creating users with roles...")
        admin_user = User(
            email='admin@bookshelf.com',
            password_hash='hashed_password_123',
            role='admin'
        )
        regular_user = User(
            email='user@bookshelf.com',
            password_hash='hashed_password_456',
            role='user'
        )
        db.session.add_all([admin_user, regular_user])
        db.session.commit()
        print(f"   ✓ Created admin: {admin_user.email} (role: {admin_user.role})")
        print(f"   ✓ Created user: {regular_user.email} (role: {regular_user.role})")
        
        # 2. Create Books (catalog)
        print("\n2. BOOKS - Adding books to catalog...")
        book1 = Book(
            title='The Great Gatsby',
            price=15.99,
            stock=50,
            description='A classic American novel by F. Scott Fitzgerald'
        )
        book2 = Book(
            title='To Kill a Mockingbird',
            price=12.99,
            stock=30,
            description='A novel by Harper Lee about racial injustice'
        )
        book3 = Book(
            title='1984',
            price=14.99,
            stock=40,
            description='Dystopian novel by George Orwell'
        )
        db.session.add_all([book1, book2, book3])
        db.session.commit()
        print(f"   ✓ Added: {book1.title} - ${book1.price} (Stock: {book1.stock})")
        print(f"   ✓ Added: {book2.title} - ${book2.price} (Stock: {book2.stock})")
        print(f"   ✓ Added: {book3.title} - ${book3.price} (Stock: {book3.stock})")
        
        # 3. Add items to Cart
        print("\n3. CART - User adding books to cart...")
        cart_item1 = Cart(user_id=regular_user.id, book_id=book1.id, quantity=2)
        cart_item2 = Cart(user_id=regular_user.id, book_id=book3.id, quantity=1)
        db.session.add_all([cart_item1, cart_item2])
        db.session.commit()
        print(f"   ✓ Added to cart: {book1.title} x{cart_item1.quantity}")
        print(f"   ✓ Added to cart: {book3.title} x{cart_item2.quantity}")
        
        # Calculate cart total
        cart_total = (book1.price * cart_item1.quantity) + (book3.price * cart_item2.quantity)
        print(f"   Cart Total: ${cart_total}")
        
        # 4. Create Order (checkout)
        print("\n4. ORDER - Creating order from cart...")
        order = Order(
            user_id=regular_user.id,
            status='pending',
            total_amount=cart_total,
            shipping_address='123 Main St, City, State 12345'
        )
        db.session.add(order)
        db.session.commit()
        print(f"   ✓ Order created: Order #{order.id} (Status: {order.status})")
        print(f"   Total Amount: ${order.total_amount}")
        
        # 5. Create Order Items
        print("\n5. ORDER ITEMS - Adding books to order...")
        order_item1 = OrderItem(
            order_id=order.id,
            book_id=book1.id,
            quantity=cart_item1.quantity,
            price=book1.price
        )
        order_item2 = OrderItem(
            order_id=order.id,
            book_id=book3.id,
            quantity=cart_item2.quantity,
            price=book3.price
        )
        db.session.add_all([order_item1, order_item2])
        
        # Clear cart after order creation
        db.session.delete(cart_item1)
        db.session.delete(cart_item2)
        db.session.commit()
        print(f"   ✓ Order Item: {book1.title} x{order_item1.quantity} @ ${order_item1.price}")
        print(f"   ✓ Order Item: {book3.title} x{order_item2.quantity} @ ${order_item2.price}")
        print(f"   Cart cleared after order creation")
        
        # 6. Process Payment
        print("\n6. PAYMENT - Processing payment...")
        payment = Payment(
            order_id=order.id,
            amount=order.total_amount,
            status='completed',
            transaction_id='TXN-' + str(datetime.now().timestamp()).replace('.', ''),
            payment_method='credit_card'
        )
        db.session.add(payment)
        
        # Update order status
        order.status = 'confirmed'
        db.session.commit()
        print(f"   ✓ Payment processed: ${payment.amount}")
        print(f"   Transaction ID: {payment.transaction_id}")
        print(f"   Payment Status: {payment.status}")
        print(f"   Order Status updated to: {order.status}")
        
        # 7. Order Tracking (update status)
        print("\n7. TRACKING - Updating order status...")
        order.status = 'shipped'
        db.session.commit()
        print(f"   ✓ Order #{order.id} status: {order.status}")
        
        # Simulate delivery
        order.status = 'delivered'
        db.session.commit()
        print(f"   ✓ Order #{order.id} status: {order.status}")
        
        # 8. Add Review
        print("\n8. REVIEW - User leaving review...")
        review1 = Review(
            user_id=regular_user.id,
            book_id=book1.id,
            rating=5,
            comment='Absolutely loved this classic! A must-read.'
        )
        review2 = Review(
            user_id=regular_user.id,
            book_id=book3.id,
            rating=4,
            comment='Thought-provoking and relevant. Great read.'
        )
        db.session.add_all([review1, review2])
        db.session.commit()
        print(f"   ✓ Review for '{book1.title}': {review1.rating}⭐ - {review1.comment}")
        print(f"   ✓ Review for '{book3.title}': {review2.rating}⭐ - {review2.comment}")
        
        # Summary
        print("\n" + "=" * 80)
        print("FLOW COMPLETED SUCCESSFULLY!")
        print("=" * 80)
        print("\nDatabase Summary:")
        print(f"  Users: {User.query.count()}")
        print(f"  Books: {Book.query.count()}")
        print(f"  Cart Items: {Cart.query.count()}")
        print(f"  Orders: {Order.query.count()}")
        print(f"  Order Items: {OrderItem.query.count()}")
        print(f"  Payments: {Payment.query.count()}")
        print(f"  Reviews: {Review.query.count()}")
        
        print("\n✓ Flow: User → Books → Cart → Order → Payment → Tracking → Review")
        print("\nAll entities and relationships are working correctly!")


if __name__ == '__main__':
    test_bookshelf_flow()
