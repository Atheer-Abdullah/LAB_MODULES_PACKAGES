import dateOP

dateOP.date_time()

from library import librarian

my_library = librarian.load_library()

while True:
    print("\n1. Add Book\n2. Display Books\n3. Search\n4. Checkout\n5. Return\n6. Delete\n7. Exit")
    choice = input("Choice: ")

    if choice == '1':
        title = input("Title: ")
        author = input("Author: ")
        isbn = input("ISBN: ")
        librarian.add_book(my_library, title, author, isbn)
    elif choice == '2':
        librarian.display_books(my_library)
    elif choice == '3':
        keyword = input("Search for: ")
        librarian.search_books(my_library, keyword)
    elif choice == '4':
        isbn = input("ISBN to checkout: ")
        librarian.check_out_book(my_library, isbn)
    elif choice == '5':
        isbn = input("ISBN to return: ")
        librarian.return_book(my_library, isbn)
    elif choice == '6':
        isbn = input("ISBN to delete: ")
        librarian.remove_book(my_library, isbn)
    elif choice == '7':
        print("Goodbye!")
        break