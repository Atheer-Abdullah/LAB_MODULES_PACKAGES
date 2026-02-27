from library import librarian

my_library = {}

librarian.add_book(my_library, "Tafsir Al-Jalalayn", "Jalalayn Scholars", "9780000000001")
librarian.add_book(my_library, "Riyadh As-Salihin", "Imam Nawawi", "9780000000002")
librarian.add_book(my_library, "Fortress of the Muslim", "Sa'id bin Ali bin Wahf Al-Qahtani", "9780000000003")

print("\nAll books in library:")
librarian.display_books(my_library)

print("\nChecking out a book:")
librarian.check_out_book(my_library, "9780000000001")

print("\nLibrary after checkout:")
librarian.display_books(my_library)

print("\nReturning the book:")
librarian.return_book(my_library, "9780000000001")

print("\nLibrary after return:")
librarian.display_books(my_library)

print("\nRemoving a book:")
librarian.remove_book(my_library, "9780000000003")

print("\nLibrary after removal:")
librarian.display_books(my_library)