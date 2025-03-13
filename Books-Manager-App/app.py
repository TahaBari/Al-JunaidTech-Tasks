import os
import logging
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import json

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create the Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "fallback-secret-key-for-development")

# Book inventory dictionary
# Structure: ISBN -> (Title, Author, Price, {Genres})
book_inventory = {}

# Function to save inventory to a python dictionary in memory
def save_inventory():
    """Save the inventory to memory"""
    # In a real application, this would save to a database
    pass

# Function to load inventory
def load_inventory():
    """Load inventory from memory"""
    # In a real application, this would load from a database
    pass

# Search by author function
def search_by_author(author):
    """
    Search for books by author
    Returns a list of tuples (ISBN, title) of matching books
    """
    results = []
    for isbn, book_details in book_inventory.items():
        if author.lower() in book_details[1].lower():
            results.append((isbn, book_details[0]))
    return results

# Update price function
def update_price(isbn, new_price):
    """
    Update the price of a book
    Returns True if successful, False if book not found
    """
    if isbn in book_inventory:
        book_details = book_inventory[isbn]
        # Create new tuple with updated price
        updated_details = (
            book_details[0],  # Title
            book_details[1],  # Author
            new_price,       # Updated price
            book_details[3]   # Genres
        )
        book_inventory[isbn] = updated_details
        return True
    return False

# Standardize genres function
def standardize_genres():
    """
    Standardize all genres by converting to lowercase and trimming spaces
    """
    for isbn, book_details in book_inventory.items():
        # Get genres set
        genres = book_details[3]
        # Create new standardized genres set
        standardized_genres = {genre.lower().strip() for genre in genres}
        # Create new tuple with standardized genres
        updated_details = (
            book_details[0],  # Title
            book_details[1],  # Author
            book_details[2],  # Price
            standardized_genres  # Standardized genres
        )
        book_inventory[isbn] = updated_details

# Display inventory function
def display_inventory():
    """
    Display all books in the inventory
    Returns a list of dictionaries with book details
    """
    result = []
    for isbn, book_details in book_inventory.items():
        book_info = {
            'isbn': isbn,
            'title': book_details[0],
            'author': book_details[1],
            'price': book_details[2],
            'genres': list(book_details[3])
        }
        result.append(book_info)
    return result

# List all books function
def list_all_books():
    """
    List all book titles sorted alphabetically
    Returns a sorted list of book titles
    """
    titles = [book_details[0] for book_details in book_inventory.values()]
    return sorted(titles)

# Routes
@app.route('/')
def index():
    """Display the home page with book inventory"""
    books = display_inventory()
    return render_template('index.html', books=books)

@app.route('/search', methods=['POST'])
def search():
    """Search for books by author"""
    author = request.form.get('author', '')
    results = search_by_author(author)
    books = []
    for isbn, title in results:
        book_details = book_inventory[isbn]
        books.append({
            'isbn': isbn,
            'title': title,
            'author': book_details[1],
            'price': book_details[2],
            'genres': list(book_details[3])
        })
    return render_template('index.html', books=books, search_term=author)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    """Add a new book to the inventory"""
    if request.method == 'POST':
        isbn = request.form.get('isbn')
        title = request.form.get('title')
        author = request.form.get('author')
        price = float(request.form.get('price', 0))
        genres = set(request.form.get('genres', '').split(','))
        
        # Clean up genres
        genres = {genre.strip().lower() for genre in genres if genre.strip()}
        
        # Add book to inventory
        book_inventory[isbn] = (title, author, price, genres)
        flash('Book added successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('add_book.html')

@app.route('/edit/<isbn>', methods=['GET', 'POST'])
def edit_book(isbn):
    """Edit an existing book"""
    if isbn not in book_inventory:
        flash('Book not found!', 'danger')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        price = float(request.form.get('price', 0))
        genres = set(request.form.get('genres', '').split(','))
        
        # Clean up genres
        genres = {genre.strip().lower() for genre in genres if genre.strip()}
        
        # Update book in inventory
        book_inventory[isbn] = (title, author, price, genres)
        flash('Book updated successfully!', 'success')
        return redirect(url_for('index'))
    
    book = book_inventory[isbn]
    book_data = {
        'isbn': isbn,
        'title': book[0],
        'author': book[1],
        'price': book[2],
        'genres': ','.join(book[3])
    }
    
    return render_template('edit_book.html', book=book_data)

@app.route('/delete/<isbn>', methods=['POST'])
def delete_book(isbn):
    """Delete a book from the inventory"""
    if isbn in book_inventory:
        del book_inventory[isbn]
        flash('Book deleted successfully!', 'success')
    else:
        flash('Book not found!', 'danger')
    return redirect(url_for('index'))

@app.route('/api/update_price', methods=['POST'])
def api_update_price():
    """API endpoint to update book price"""
    data = request.get_json()
    isbn = data.get('isbn')
    new_price = float(data.get('price', 0))
    
    success = update_price(isbn, new_price)
    if success:
        return jsonify({'success': True, 'message': 'Price updated successfully'})
    else:
        return jsonify({'success': False, 'message': 'Book not found'}), 404

@app.route('/api/standardize_genres', methods=['POST'])
def api_standardize_genres():
    """API endpoint to standardize all genres"""
    standardize_genres()
    return jsonify({'success': True, 'message': 'Genres standardized successfully'})

# Initialize with some sample books if empty
if not book_inventory:
    book_inventory = {
        '9780553213119': ('Pride and Prejudice', 'Jane Austen', 8.99, {'romance', 'classic'}),
        '9780743273565': ('The Great Gatsby', 'F. Scott Fitzgerald', 12.50, {'fiction', 'classic'}),
        '9780060935467': ('To Kill a Mockingbird', 'Harper Lee', 14.99, {'fiction', 'classic'}),
        '9780451524935': ('1984', 'George Orwell', 11.99, {'dystopian', 'science fiction'})
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
