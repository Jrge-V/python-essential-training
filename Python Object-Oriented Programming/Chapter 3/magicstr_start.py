# Using the __str__ and __repr__ magic methods


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # TODO: use the __str__ method to return a string
    # __str__ is used to provide a user friendly string description of the object
    # and it is usually intended to be displayed to the user
    def __str__(self):
        return f'{self.title} by {self.author}, costs {self.price}'

    # TODO: use the __repr__ method to return an obj representation
    # __repr__ is used to generate a more developer facing string
    # ideally used to recreate the object in its current state
    # also used LOADS for DEBUGGING purposes so its used to display loads of information
    def __repr__(self):
        return f'title={self.title},author={self.author},price={self.price}'


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

print(b1)
print(b2)

print(str(b1))
print(repr(b2))