# initiate function taking in the multidimensional list and item to look for
def index_all(my_list, item):
    # initiate an empty list where we will be appending the indices of found items
    indices = []

    # for loop that takes the range of the length of my_list
    for i in range(len(my_list)):
        # if the item at indices i equals the item we are looking for:
        if my_list[i] == item:
            # append that indices (NOT THE ITEM ITSELF) to the indices list
            indices.append([i])
        # otherwise check if the indices is a list object
        elif isinstance(my_list[i], list):
            # if it is then loop through the index and recursively call the function
            # but with the new inner lists and item we are looking for
            for index in index_all(my_list[i], item):
                # append the indices and index
                indices.append([i] + index)

    return indices


# TEST CODE
example_list = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]

# example = [[1, 2, [2]]]  # [[0, 1], [1, 0]]
print(index_all(example_list, 2))  # [[0, 0, 1], [0, 1], [1, 1]]
