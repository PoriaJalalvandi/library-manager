class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, title, author):
        book = {"title": title, "author": author}
        self.books.append(book)

    def remove_book(self, title): 
        self.books = [book for book in self.books if book["title"] != title]

    def search_book(self, title):
        for book in self.books:
            if book["title"] == title:
                return self.books.index(book)
        return None
    
    def show_books(self):
        for book in self.books:
            print(f"{book['title']} by {book['author']}")