
# 📚 Personal Library Manager

A command-line application to manage your book collection. Add, remove, search, and track your books with ease!

---

## Features
- **Add a Book**: Add a new book with details like title, author, publication year, genre, and read status.
- **Remove a Book**: Remove a book by its title.
- **Search for a Book**: Search for books by title or author.
- **Display All Books**: View all books in your library in a formatted list.
- **Display Statistics**: See the total number of books and the percentage of books you’ve read.
- **Save and Load Library**: Your library is saved to a file (`library.txt`) and loaded automatically when the program starts.


### Add a Book
```
Enter the book title: The Great Gatsby
Enter the author: F. Scott Fitzgerald
Enter the publication year: 1925
Enter the genre: Fiction
Have you read this book? (yes/no): yes
Book added successfully!
```

### Remove a Book
```
Enter the title of the book to remove: The Great Gatsby
Book removed successfully!
```

### Search for a Book
```
Search by:
1. Title
2. Author
Enter your choice: 1
Enter the title: The Great Gatsby
Matching Books:
1. The Great Gatsby by F. Scott Fitzgerald (1925) - Fiction - Read
```

### Display All Books
```
Your Library:
1. The Great Gatsby by F. Scott Fitzgerald (1925) - Fiction - Read
2. 1984 by George Orwell (1949) - Dystopian - Unread
```

### Display Statistics
```
Total books: 2
Percentage read: 50.0%
```

### Exit
```
Library saved to file. Goodbye!
```

---

## Code Structure

- **`library_manager.py`**: The main Python script.
  - Manages the library using a list of dictionaries.
  - Provides a menu-driven interface for user interaction.
  - Saves and loads the library to/from `library.txt`.

---
