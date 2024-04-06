# Using instance methods and attributes

class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized

    def __init__(self, title, author, pages, price):
        self.title = title
        # TODO: add properties
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = 'This is a secret attribute'

    # TODO: create instance methods
    def get_price(self):
        # 'hasattr' is built into python to check if an attribute exists
        if hasattr(self, '_discount'):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def set_discount(self, amount):
        # The underscore is a way to tell other developers who
        # might look at the code that this is internal to the class
        # and not in a global scope
        self._discount = amount


# TODO: create some book instances
b1 = Book('War and Peace', 'Leo Tolstoy', 1225, 39.95)
b2 = Book('The Catcher in the Rye', 'JD Salinger', 234, 29.95)

# TODO: Print the price of book1
print(b1.get_price())

# TODO: try setting the discount
print(b2.get_price())
b2.set_discount(0.25)
print(b2.get_price())


# TODO: properties with double underscore are hidden by the interpreter
# If other classes try to access a double underscore they will get an error
print(b2._Book__secret)









