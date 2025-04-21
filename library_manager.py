import streamlit as st
import os
import json

# JSON file to store the library
LIBRARY_FILE = "library.json"

# ✅ Optional Books (3)
OPTIONAL_BOOKS = [
    {"title": "The Secret", "author": "Rhonda Byrne", "year": 2006, "genre": "Self-help", "read": False},
    {"title": "Zindagi Gulzar Hai", "author": "Umera Ahmed", "year": 2012, "genre": "Drama", "read": False},
    {"title": "The Key to Success", "author": "Jim Rohn", "year": 1986, "genre": "Motivational", "read": False}
]

# ✅ Motivational & Educational Books
MOTIVATIONAL_BOOKS = [
    {"title": "Think and Grow Rich", "author": "Napoleon Hill", "year": 1937, "genre": "Self-help", "read": False},
    {"title": "Rich Dad Poor Dad", "author": "Robert Kiyosaki", "year": 1997, "genre": "Financial Education", "read": False},
    {"title": "The 7 Habits of Highly Effective People", "author": "Stephen R. Covey", "year": 1989, "genre": "Personal Growth", "read": False},
    {"title": "The Power of Now", "author": "Eckhart Tolle", "year": 1997, "genre": "Mindfulness", "read": False},
    {"title": "Man's Search for Meaning", "author": "Viktor E. Frankl", "year": 1946, "genre": "Philosophy", "read": False}
]

# 🔄 Load library from JSON file
def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    return []

# 💾 Save library to file
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file)

# 📚 Load current library
library = load_library()

# 🌟 Streamlit UI
st.title("📚 Personal Library Manager")

# 🎛 Sidebar Menu
menu = [
    "Add a Book", 
    "Remove a Book", 
    "Search a Book", 
    "Show All Books", 
    "Library Stats", 
    "Add Predefined Books"
]
choice = st.sidebar.selectbox("Choose an Option", menu)

# ➕ Add a Book
if choice == "Add a Book":
    st.subheader("➕ Add a New Book")

    title = st.text_input("📖 Enter the book title")
    author = st.text_input("✍️ Enter the author")
    year = st.number_input("📅 Enter the publication year", min_value=0, step=1)
    genre = st.text_input("📚 Enter the genre")
    read_status = st.radio("✅ Have you read this book?", ["Yes", "No"])

    if st.button("Add Book"):
        book = {
            "title": title,
            "author": author,
            "year": int(year),
            "genre": genre,
            "read": True if read_status == "Yes" else False
        }
        library.append(book)
        save_library(library)
        st.success("✅ Book added successfully!")

# 🗑 Remove a Book
elif choice == "Remove a Book":
    st.subheader("🗑️ Remove a Book")
    if library:
        book_titles = [book["title"] for book in library]
        selected_title = st.selectbox("Select a book to remove", book_titles)
        if st.button("Remove Book"):
            library = [book for book in library if book["title"] != selected_title]
            save_library(library)
            st.success(f"'{selected_title}' removed successfully!")
    else:
        st.info("Your library is empty.")

# 🔍 Search a Book
elif choice == "Search a Book":
    st.subheader("🔍 Search for a Book")
    search_by = st.radio("Search by:", ["Title", "Author"])
    query = st.text_input("Enter your search keyword")

    if query:
        if search_by == "Title":
            results = [book for book in library if query.lower() in book["title"].lower()]
        else:
            results = [book for book in library if query.lower() in book["author"].lower()]

        if results:
            for book in results:
                st.markdown(f"**{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {'✅ Read' if book['read'] else '📖 Unread'}")
        else:
            st.warning("No matching books found.")

# 📖 Show All Books
elif choice == "Show All Books":
    st.subheader("📚 Your Library")
    if library:
        for i, book in enumerate(library, 1):
            status = "✅ Read" if book["read"] else "📖 Unread"
            st.write(f"{i}. **{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        st.info("Your library is empty.")

# 📊 Show Stats
elif choice == "Library Stats":
    st.subheader("📊 Library Statistics")
    total = len(library)
    read = sum(1 for book in library if book["read"])
    unread = total - read
    percentage = (read / total) * 100 if total > 0 else 0

    st.write(f"**Total Books:** {total}")
    st.write(f"**Books Read:** {read}")
    st.write(f"**Books Unread:** {unread}")
    st.progress(percentage / 100)

# 📘 Add Predefined Books
elif choice == "Add Predefined Books":
    st.subheader("📘 Add Predefined Books")
    category = st.radio("Choose category:", ["Optional Books", "Motivational Books"])

    if category == "Optional Books":
        if st.button("Add Optional Books"):
            library.extend(OPTIONAL_BOOKS)
            save_library(library)
            st.success("✅ Optional books added!")

    elif category == "Motivational Books":
        if st.button("Add Motivational Books"):
            library.extend(MOTIVATIONAL_BOOKS)
            save_library(library)
            st.success("✅ Motivational books added!")
