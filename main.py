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
            "Book Title": input("Enter the book title: ").capitalize(),
            "Author": input("Enter the author's name: ").capitalize(),
            "Genre": input("Enter the book genre: ").capitalize(),
            "Publication Year": input("Enter the publication year: "),
            "Status": "Available" 
    }
        Book.data.append(book_info)

        print(f'\n✅ "{book_info["Book Title"]}" has been added successfully!')
        print(f'📖 Book ID: {book_info["Book ID"]}')
        print(f'📚 Status: {book_info["Status"]}')

        Book.__update()


    def borrow_book(self):
        author_name = input("Enter the author's name: ").capitalize()
        book_id = int(input("Enter the book ID: "))

        book_data  = [x for x in Book.data if x["Author"] == author_name and x["Book ID"] == book_id]

        if not book_data:
            print("No matching book was found.")
            return

        if book_data[0]["Status"] == "Unavailable":
            print("Sorry, this book is currently unavailable.")
            return
        
        borrow_days = int(input("Enter the number of days you want to borrow the book: "))

        book_data[0]["Status"] = "Unavailable"
        book_data[0]["Borrow Days"] = borrow_days

        print(f'✅ You have successfully borrowed "{book_data[0]["Book Title"]}".')
        print(f'📅 Borrowing Period: {borrow_days} days')

        Book.__update()


    def return_book(self):
        author_name = input("Enter the author's name: ").capitalize()
        book_id = int(input("Enter the book ID: "))

        book_data  = [x for x in Book.data if x["Author"] == author_name and x["Book ID"] == book_id]

        if not book_data:
            print("❌ No matching book was found.")
            return

        book_data[0]["Status"] = "Available"
        book_data[0].pop("Borrow Days")

        print(f'✅ "{book_data[0]["Book Title"]}" has been returned successfully.')
        print("📚 Status: Available")

        Book.__update()


    def view_books(self):
        count = 1

        print("\n📚 AVAILABLE BOOKS")
        print("-" * 40)

        for book in self.data:
            if book["Status"] == "Available":
                print(
                    f"{count}.\n"
                    f"   📖 Title : {book['Book Title']}\n"
                    f"   ✍️  Author: {book['Author']}\n"
                    )
                count += 1

            if count == 1:
                print("No books are currently available.")


library = Book()


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
    library.add_book()

elif choice == 2:
    library.borrow_book()

elif choice == 3:
    library.return_book()

elif choice == 4:
    library.view_books()

elif choice == 5:
    print("👋 Thank you for using the Library Management System!")

else:
    print("❌ Invalid choice. Please enter a number between 1 and 5.")