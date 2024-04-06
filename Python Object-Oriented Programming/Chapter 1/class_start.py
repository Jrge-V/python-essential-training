# Using class-level and static methods

class Book:

    # TODO: Properties defined at the class level are shared by all instances
    # Can make class instances all caps to differentiate
    BOOK_TYPES = ('HARDCOVER', 'PAPERBACK', 'EBOOK')

    # TODO: double-underscore properties are hidden from other classes
    # this is basically like a private method in java
    __booklist = None

    # TODO: create a class method
    # To create a class method we need a class decorator '@classmethod'
    # this take a cls parameter rather than a self
    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES


    # TODO: create a static method
    @staticmethod
    def getbooklist():
        if Book.__booklist is None:
            Book.__booklist = []
        return Book.__booklist

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self, newtitle):
        self.newtitle = newtitle

    def __init__(self, title, booktype):
        self.title = title

        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f'{booktype} is not a valid type')
        else:
            self.booktype = booktype


# TODO: access the class attributes
print('Book Types: ', Book.get_book_types())

# TODO: Create some book instances
b1 = Book('Title1', 'HARDCOVER')
# b2 will cause an error because 'COMIC' is NOT a booktype I defined, change it to paperback
b2 = Book('Title1', 'PAPERBACK')

# TODO: Use the static method to access a singleton object
thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)
