import json
import random
import string
from pathlib import Path 

class Book:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No data file was found.")
    except Exception as err:
        print(f"{err}")

    @classmethod
    def __update(cls):
         with open(cls.database, 'w') as fs:
            fs.write(json.dumps(Book.data))

    @classmethod
    def generate_unique_id(cls):
        return random.randint(100000, 999999)

    def add_book(self):
        book_info = {
            "Book ID": Book.generate_unique_id(),
            "Book Title": input("Enter the book title: "),
            "Author": input("Enter the author's name: "),
            "Genre": input("Enter the book genre: "),
            "Publication Year": input("Enter the publication year: "),
    }
        Book.data.append(book_info)

        print(f'\n✅ "{book_info["Book Title"]}" has been added successfully!')
        print(f'📖 Book ID: {book_info["Book ID"]}')

        Book.__update()

User = Book()

print("\n📚 LIBRARY MANAGEMENT SYSTEM 📚")
print("--------------------------------")
print("1. ➕ Add a Book")
print("2. 📖 Borrow a Book")
print("3. 🔄 Return a Book")
print("4. 📚 View Available Books")
print("5. ❌ Exit")
print("--------------------------------")

choice = int(input("Enter your choice (1-5): "))

if choice == 1:
    User.add_book()