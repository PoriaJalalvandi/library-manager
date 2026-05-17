# Library Manager

A simple book management system built with Python, designed as a modular and locally installable package via pip.

---

## 📁 Project Structure

```
library-manager/
├── my_library/
│   ├── __init__.py
│   └── library.py
├── main.py
├── setup.py
└── README.md
```

---

## ⚙️ Installation

Make sure you are in the project root directory, then run:

```bash
pip install .
```

---

## 🚀 Usage

Run the program directly:

```bash
python main.py
```

You will see an interactive menu:

```
1. Add a book
2. Remove a book
3. Search for a book
4. Show all books
0. Exit
```

---

## 📦 Importing the Package

After installation, you can import and use the package anywhere:

```python
from my_library.library import Library

lib = Library("My Library")
lib.add_book("Clean Code", "Robert C. Martin")
lib.show_books()
```

---

## 🛠️ Features

- Add a book with title and author
- Remove a book by title
- Search for a book by title
- Display all books in the library
- Modular structure with installable package support

---

## 📄 Library Class — Methods

| Method | Description |
|--------|-------------|
| `add_book(title, author)` | Adds a new book to the library |
| `remove_book(title)` | Removes a book by its title |
| `search_book(title)` | Searches and returns the book index |
| `show_books()` | Prints all books in the library |

---

## 🖥️ Environment

- **OS:** Ubuntu (WSL)
- **Language:** Python 3
- **Package Manager:** pip

---

## 👤 Author

- **Name:** Ali Jalalvandi
- **Email:** pouriyajalalvandi@gmail.com

---

## 📃 License

This project is for educational purposes only.
