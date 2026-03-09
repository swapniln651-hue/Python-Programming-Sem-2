# A library dictionary stores book name and price. Update book price.
"""
Created on Mon Mar  9 15:12:59 2026

@author: swapnil
"""

# Initial dictionary
library = {
    "The Great Gatsby": 15.99,
    "1984": 12.50,
    "The Hobbit": 20.00
}

# Updating the price of "1984"
library["1984"] = 10.99

book_to_update = "The Hobbit"
new_price = 20.50

if book_to_update in library:
    library[book_to_update] = new_price
    print(f"Updated {book_to_update} price to ${new_price}")
else:
    print("Book not found in the library.")
