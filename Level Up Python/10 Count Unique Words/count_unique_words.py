from collections import Counter


def count_words(input_file):
    # open the file using with to automatically close
    with open(input_file, 'r', encoding='utf-8') as file:
        # save the file in a text variable
        text = file.read()
    # make every word uppercase to match and split it to make it a list
    text = text.upper().split()
    # get the length of the list which gives us the total number of words
    # ignoring and special characters
    print(f'Total Words: {len(text)}')

    # create a counter object from the list, this assigns a number to it,
    # essentially making it a dict with the word as the key and time it occurs as the value
    word_count = Counter(text)

    # create a variable that only stores the top 20 words in the dict using the most_common method
    top_words = word_count.most_common(20)

    print('Top 20 Words')
    # print out the word and the number of times it occurs
    for word, count in top_words:
        print(f'{word}\t{count}')


# pass in the text file into my method
count_words('story.txt')
