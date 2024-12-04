import sqlite3

def create_table():
    db = sqlite3.connect('ebookstore.db') # Connect to the SQLite database
    cursor = db.cursor()

    # Create a book database
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS book (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT, 
        qty INTEGER)
    ''')
    db.commit() # Save the database
    db.close() # Close connection to the databse


def populate_table():
    db = sqlite3.connect('ebookstore.db')
    cursor = db.cursor()

    # Create data to populate the book table
    books = [
        (3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
        (3002, "Harry Potter and the Philosopher's Stone", 'J.K Rowling', 40),
        (3003, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25),
        (3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37),
        (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)
    ]
    db.executemany('INSERT OR IGNORE INTO book (id, title, author, qty) VALUES (?, ?, ?, ?)', books)
    db.commit() # Save the database
    db.close() # Close connection to the databse


def add_book():
    db = sqlite3.connect('ebookstore.db')
    cursor = db.cursor()

    # prompt user to enter book details
    id = int(input("Enter book id: "))
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    qty = int(input("Enter quantity: "))

    cursor.execute('INSERT INTO book (id, title, author, qty) VALUES (?, ?, ?, ?)', (id, title, author, qty))
    db.commit() # Save the database
    db.close() # Close connection to the databse


def update_book():
    db = sqlite3.connect('ebookstore.db')
    cursor = db.cursor() 

    # Get book id and new details from the user
    id = int(input("Enter book id to update: "))
    title = input("Enter new book title: ")
    author = input("Enter new book author: ")
    qty = int(input("Enter new quantity: "))

    cursor.execute('UPDATE book SET title = ?, author = ?, qty = ? WHERE id = ?', (title, author, qty, id))
    db.commit() # Save the database
    db.close() # Close connection to the databse


def delete_book():
    db = sqlite3.connect('ebookstore.db')
    cursor = db.cursor()

    # Get book id to delete from the user
    id = int(input("Enter book id to delete: "))
    cursor.execute('DELETE FROM book WHERE id = ?', (id,))
    db.commit() # Save the database
    db.close() # Close connection to the databse


def search_books():
    db = sqlite3.connect('ebookstore.db')
    cursor = db.cursor()

    # Prompt user to search
    search = input("Enter book title to search: ")
    cursor.execute('SELECT * FROM book WHERE title LIKE ?', ('%' + search + '%',))
    results = cursor.fetchall()
    for row in results:
        print(row)
    db.close() # Close connection to the databse


def main():
    create_table()
    populate_table()
    while True:
        print('''
        1. Enter book
        2. Update book
        3. Delete book
        4. Search books
        0. Exit 
        ''')
        
        choice = input("Enter your choice: ") # Get user's choice
        if choice == '1':
            add_book()

        elif choice == '2':
            update_book()

        elif choice == '3':
            delete_book()

        elif choice == '4':
            search_books()

        elif choice == '0':
            break

        else:
            print("Invalid input, please enter a correct number.") # Correct Invalid input

if __name__ == "__main__":
    main()