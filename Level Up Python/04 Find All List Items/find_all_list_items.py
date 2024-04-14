
def index_all(my_lst, item):
    indices = []

    for i in range(len(my_lst)):
        if my_lst[i] == item:
            indices.append([i])
        elif isinstance(my_lst[i], list):
            for index in index_all(my_lst[i], item):
                indices.append([i] + index)

    return indices


# TEST CODE
example_list = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]

# example = [[1, 2, [2]]]  # [[0, 1], [1, 0]]
print(index_all(example_list, 2))  # [[0, 0, 1], [0, 1], [1, 1]]
