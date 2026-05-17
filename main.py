from my_library import library

def show_menu():
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Show all books")
    print("0. Exit")
    
def main():
    my_library = library.Library("My Library")

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            my_library.add_book(title, author)
            print(f"Book '{title}' by {author} added to the library.")
        elif choice == "2":
            title = input("Enter book title to remove: ")
            before_count = len(my_library.books)
            my_library.remove_book(title)
            after_count = len(my_library.books)
            if before_count == after_count:
                print(f"Book '{title}' not found in the library.")
            else:
                print(f"Book '{title}' removed from the library.")
        elif choice == "3":
            title = input("Enter book title to search: ")
            index = my_library.search_book(title)
            if index is not None:
                print(f"Book found at index {index}")
            else:
                print("Book not found.")
        elif choice == "4":
            my_library.show_books()
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()