
import streamlit as st
import os

LIBRARY_FILE = "library.txt"

# Load and save functions
def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            return eval(file.read())
    return []

def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        file.write(str(library))

# Optional books (3)
OPTIONAL_BOOKS = [
    {"title": "The Secret", "author": "Rhonda Byrne", "year": 2006, "genre": "Self-help", "read": False},
    {"title": "Zindagi Gulzar Hai", "author": "Umera Ahmed", "year": 2012, "genre": "Drama", "read": False},
    {"title": "The Key to Success", "author": "Jim Rohn", "year": 1986, "genre": "Motivational", "read": False}
]

# Motivational & Educational Books
MOTIVATIONAL_BOOKS = [
    {"title": "Think and Grow Rich", "author": "Napoleon Hill", "year": 1937, "genre": "Self-help", "read": False},
    {"title": "Rich Dad Poor Dad", "author": "Robert Kiyosaki", "year": 1997, "genre": "Financial Education", "read": False},
    {"title": "The 7 Habits of Highly Effective People", "author": "Stephen R. Covey", "year": 1989, "genre": "Personal Growth", "read": False},
    {"title": "The Power of Now", "author": "Eckhart Tolle", "year": 1997, "genre": "Mindfulness", "read": False},
    {"title": "Man's Search for Meaning", "author": "Viktor E. Frankl", "year": 1946, "genre": "Philosophy", "read": False}
]

# App layout
st.title("📚 Personal Library Manager")

library = load_library()

menu = ["Add Book", "Remove Book", "Search Book", "Display All", "Statistics", "Mark as Read", "Exit"]
choice = st.sidebar.selectbox("Select an option", menu)

if choice == "Add Book":
    st.subheader("➕ Add a New Book")
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    year = st.number_input("Publication Year", min_value=0, max_value=2050, step=1)
    genre = st.text_input("Genre")
    read = st.checkbox("Have you read this book?")
    if st.button("Add Book"):
        library.append({
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read": read
        })
        save_library(library)
        st.success("Book added successfully!")

elif choice == "Remove Book":
    st.subheader("🗑️ Remove a Book")
    titles = [book["title"] for book in library]
    if titles:
        selected = st.selectbox("Select a book to remove", titles)
        if st.button("Remove"):
            library = [book for book in library if book["title"] != selected]
            save_library(library)
            st.success("Book removed!")
    else:
        st.info("No books to remove.")

elif choice == "Search Book":
    st.subheader("🔍 Search for a Book")
    search_by = st.radio("Search by", ["Title", "Author"])
    keyword = st.text_input("Enter keyword to search")
    if st.button("Search"):
        results = []
        if search_by == "Title":
            results = [b for b in library if keyword.lower() in b["title"].lower()]
        else:
            results = [b for b in library if keyword.lower() in b["author"].lower()]
        if results:
            for book in results:
                st.markdown(f"- **{book['title']}** by *{book['author']}* ({book['year']}) - {book['genre']} - {'✅ Read' if book['read'] else '❌ Unread'}")
        else:
            st.warning("No matching books found.")

elif choice == "Display All":
    st.subheader("📖 All Books in Your Library")
    if library:
        for i, book in enumerate(library, 1):
            st.write(f"{i}. **{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {'✅ Read' if book['read'] else '❌ Unread'}")
    else:
        st.info("Your library is empty.")

elif choice == "Statistics":
    st.subheader("📊 Library Statistics")
    total = len(library)
    read_count = sum(1 for b in library if b["read"])
    unread_count = total - read_count
    percent = (read_count / total * 100) if total > 0 else 0
    st.write(f"📚 Total Books: **{total}**")
    st.write(f"✅ Books Read: **{read_count}**")
    st.write(f"❌ Books Unread: **{unread_count}**")
    st.write(f"📈 Reading Progress: **{percent:.2f}%**")

elif choice == "Mark as Read":
    st.subheader("📌 Mark a Book as Read")
    unread_books = [book for book in library if not book["read"]]
    if unread_books:
        book_titles = [book["title"] for book in unread_books]
        selected = st.selectbox("Select a book to mark as read", book_titles)
        if st.button("Mark as Read"):
            for book in library:
                if book["title"] == selected:
                    book["read"] = True
                    break
            save_library(library)
            st.success(f"Marked '{selected}' as Read ✅")
    else:
        st.info("All books are already marked as read!")

elif choice == "Exit":
    st.info("Goodbye! 👋")

# 📘 Optional Book Section
with st.expander("📘 Optional Books to Add"):
    st.write("Select any book to add to your library:")
    for i, book in enumerate(OPTIONAL_BOOKS):
        if st.checkbox(f"{book['title']} by {book['author']} ({book['year']})", key=f"opt_{i}"):
            if book not in library:
                library.append(book)
    save_library(library)

# 🌟 Motivational & Educational Book Section
with st.expander("🌟 Motivational & Educational Books"):
    st.write("These books are great for mindset, money and life wisdom:")
    for i, book in enumerate(MOTIVATIONAL_BOOKS):
        if st.checkbox(f"{book['title']} by {book['author']} ({book['year']})", key=f"mot_{i}"):
            if book not in library:
                library.append(book)
    save_library(library)
