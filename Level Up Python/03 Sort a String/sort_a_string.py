
def sort_words(s1):
    # split the string into a list at every space using the .split operator
    s1 = s1.split(' ')
    # sort the list using the str.lower key to ignore cases sensitivity
    s1.sort(key=str.lower)
    # join the list back into a string with a blank space seperator using the .join operator
    s1 = ' '.join(s1)

    # return the sorted string
    # can also do "return ' '.join(sorted(s1.split(), key=str.lower))"
    return s1


# TEST CODE
print(sort_words('banana ORANGE apple'))  # 'apple banana ORANGE')
