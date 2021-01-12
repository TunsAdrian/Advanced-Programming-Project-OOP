from functools import reduce

# iterable to be used in reduce function
decoding_table = (('!', 's'), ('@', 'h'), ('#', 'e'), ('$', 'r'), ('%', 'l'), ('^', 'o'), ('&', 'c'), ('*', 'k'))


# use reduce function with 3 parameters version; start from current word and for each entry of the table make the proper replacement
def decoder(current_word):
    return reduce(lambda string, table_entry: string.replace(table_entry[0], table_entry[1]), decoding_table,
                  current_word)


if __name__ == '__main__':
    decoded_text = []
    # read each word, decode it and then append it to a list
    with open('sherlock.txt', 'r') as file:
        for line in file:
            for word in line.split():
                decoded_text.append(decoder(word))

    # collect the words starting with letter 'a' to another list
    desired_result = list(filter(lambda first_char: first_char[0].lower() == 'a', decoded_text))
    print(desired_result)
