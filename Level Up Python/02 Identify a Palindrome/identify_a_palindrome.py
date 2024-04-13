# TODO initialize is_palindrome method

def is_palindrome(my_string):
    my_string = my_string.lower()
    # my_string = [char for char in my_string]
    # my_string = my_string.replace(' ', '').replace(',', '').replace('’', '')
    print(my_string[::-1])
    return my_string




# TEST CODE
print(is_palindrome('hello world'))  # False
print(is_palindrome('Go hang a salami, I’m a lasagna hog.'))  # True

