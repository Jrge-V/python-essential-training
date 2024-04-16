# Save dictionary function upon exiting program
def save_dict(my_dict, output_file):

    with open(output_file, 'w') as file:
        file.write('{')
        for key, value in my_dict.items():
            file.write(f'{key}: \'{value}\', ')
        file.write('}')


# Load dictionary function upon execution
def load_dict(input_file):
    with open(input_file, 'r') as file:
        return file.read()




# TEST CODE
save_dict({1: 'a', 2: 'b', 10: 'c'}, 'test.pickle')
print(load_dict('test.pickle'))  # {1: 'a', 2: 'b', 3: 'c'}
