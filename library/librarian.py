import json
import os

def save_library(library, filename="library_data.json"):
    with open(filename, "w") as f:
        json.dump(library, f, indent=4)

def load_library(filename="library_data.json"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return {}

def add_book(library, title, author, isbn):
    if isbn in library:
        print("Book already exists!")
        return False
    library[isbn] = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "available": True
    }
    save_library(library)
    print(f"Book '{title}' added successfully!")
    return True

def remove_book(library, isbn):
    if isbn in library:
        del library[isbn]
        save_library(library)
        print(f"Book with ISBN {isbn} removed.")
        return True
    print("Book not found.")
    return False

def check_out_book(library, isbn):
    if isbn in library:
        if library[isbn]["available"]:
            library[isbn]["available"] = False
            save_library(library)
            print("Checked out successfully.")
        else:
            print("Book is already checked out.")
    else:
        print("Book not found.")

def return_book(library, isbn):
    if isbn in library:
        library[isbn]["available"] = True
        save_library(library)
        print("Returned successfully.")
    else:
        print("Book not found.")

def display_books(library):
    if not library:
        print("Library is empty.")
        return
    for book in library.values():
        status = "Available" if book["available"] else "Checked Out"
        print(f"{book['title']} by {book['author']} (ISBN: {book['isbn']}) - {status}")

def search_books(library, keyword):
    found = False
    for book in library.values():
        if keyword.lower() in book['title'].lower() or keyword.lower() in book['author'].lower():
            status = "Available" if book["available"] else "Checked Out"
            print(f"Found: {book['title']} by {book['author']} - {status}")
            found = True
    if not found:
        print("No matches found.")