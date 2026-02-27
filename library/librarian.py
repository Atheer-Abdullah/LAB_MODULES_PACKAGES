def add_book(library: dict, title: str, author: str, isbn: str):
    """إضافة كتاب جديد إلى المكتبة"""
    if isbn in library:
        print(f"Book with ISBN {isbn} already exists!")
        return False
    library[isbn] = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "available": True
    }
    return True


def remove_book(library: dict, isbn: str):
    """حذف كتاب من المكتبة"""
    if isbn in library:
        del library[isbn]
        print(f"Book with ISBN {isbn} removed successfully!")
        return True
    else:
        print(f"Book with ISBN {isbn} not found.")
        return False


def check_out_book(library: dict, isbn: str):
    """استعارة كتاب (تغيير الحالة إلى غير متاح)"""
    if isbn in library:
        if library[isbn]["available"]:
            library[isbn]["available"] = False
            print(f"Book '{library[isbn]['title']}' checked out successfully!")
        else:
            print(f"Book '{library[isbn]['title']}' is already checked out.")
    else:
        print(f"Book with ISBN {isbn} not found.")


def return_book(library: dict, isbn: str):
    """إرجاع كتاب (تغيير الحالة إلى متاح)"""
    if isbn in library:
        library[isbn]["available"] = True
        print(f"Book '{library[isbn]['title']}' returned successfully!")
    else:
        print(f"Book with ISBN {isbn} not found.")


def display_books(library: dict):
    """عرض كل الكتب الموجودة في المكتبة"""
    if not library:
        print("No books in the library.")
        return

    for book in library.values():
        status = "Available" if book["available"] else "Checked Out"
        print(f"{book['title']} by {book['author']} (ISBN: {book['isbn']}) - {status}")