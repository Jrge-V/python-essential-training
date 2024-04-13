# TODO initialize is_palindrome method

def is_palindrome(my_string):
    # lowercase the string
    my_string = my_string.lower()

    # for loop that loops through every character of the string
    for char in my_string:
        # Check if the lowercase character falls under the ascii number value (a-z)
        # 'using ord()'. a-z falls under the values 97 - 122
        # remove any extra character or symbols that are not letters
        if ord(char) < 97 or ord(char) > 122:
            # If found replace the character with and empty character
            my_string = my_string.replace(char, '')

    # Check if the string is a palindrome
    # The string slicing '[::-1]' reverses my original string
    # If the original string = revere string, return True, else False
    if my_string == my_string[::-1]:
        return True
    return False


# TEST CODE
# Call the method is_palindrome
print(is_palindrome('hello world'))  # False
print(is_palindrome('Go hang a salami, I’m a lasagna hog.'))  # True
