# Python OOP, Basic class Definitions

# TODO: create a basic class
# You can also write a class as so: 'class Book():' <- if the class inherits from another class
class Book:
    def __init__(self, title):
        self.title = title


# TODO: create instances of a class
book1 = Book("Brave New World")
book2 = Book("War and Peace")

# TODO: print the class and property
print(book1)
print(book1.title)
