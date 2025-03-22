import json

class BookCollection:
    """A class to manage a collection of books, allowing users to store and organize their library."""

import os

# File to store library data
LIBRARY_FILE = "library.txt"

# Function to load the library from a file
def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            library = eval(file.read())  # Safely evaluate the string as a Python list
        return library
    return []

# Function to save the library to a file
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        file.write(str(library))

# Function to display the menu
def display_menu():
    print("\nWelcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

# Function to add a book
def add_book(library):
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ").strip()
    read_status = input("Have you read this book? (yes/no): ").strip().lower()
    read_status = True if read_status == "yes" else False

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }
    library.append(book)
    print("Book added successfully!")

# Function to remove a book
def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip()
    found = False
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            found = True
            print("Book removed successfully!")
            break
    if not found:
        print("Book not found in the library.")

# Function to search for a book
def search_book(library):
    print("Search by:")
    print("1. Title")
    print("2. Author")
    choice = input("Enter your choice: ").strip()
    if choice == "1":
        title = input("Enter the title: ").strip()
        matching_books = [book for book in library if title.lower() in book["title"].lower()]
    elif choice == "2":
        author = input("Enter the author: ").strip()
        matching_books = [book for book in library if author.lower() in book["author"].lower()]
    else:
        print("Invalid choice.")
        return

    if matching_books:
        print("Matching Books:")
        for i, book in enumerate(matching_books, 1):
            status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("No matching books found.")

# Function to display all books
def display_all_books(library):
    if not library:
        print("Your library is empty.")
    else:
        print("Your Library:")
        for i, book in enumerate(library, 1):
            status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

# Function to display statistics
def display_statistics(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0

    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.1f}%")

# Main function
def main():
    library = load_library()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()