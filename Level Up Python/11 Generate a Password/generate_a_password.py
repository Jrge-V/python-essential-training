import random


def generate_passphrase(user_int):
    # open file for reading
    with open('random_words.txt', 'r') as file:
        lines = file.readlines()

    # initiate dictionary and pass keys: values from text file
    my_dict = {}
    for line in lines:
        key, value = line.strip().split(': ')
        my_dict[key] = value

    # initiate a list of number strings that appends the amount of times the user wanted to generate a word
    my_string_list = []
    for i in range(user_int):
        ran_num = str(random.randint(111, 333))
        # print(ran_num)
        my_string_list.append(ran_num)

    # initiate a password list that gets the specific key based on the randomint generated
    password = []
    for n in range(len(my_string_list)):
        password.append(my_dict.get(my_string_list[n]))

    # join and return the strings to make a password
    return print(f'{"".join(password)}')


user_int = int(input(f'Number of generated words: '))

generate_passphrase(user_int)
