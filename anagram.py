from itertools import permutations


# check if the whole word appears in the dictionary (by default the entry of the permutation is represented as a tuple)
def word_check(word_to_check):
    if dictionary.__contains__(''.join(word_to_check)):
        return word_to_check


if __name__ == '__main__':
    dictionary = []
    # read each word, decode it and then append it to a list
    with open('dictionary.txt', 'r') as file:
        for line in file:
            for word in line.split():
                dictionary.append(word)

    word = input("Input a word to see if it's meaningful:")
    word_permutations = permutations(word)  # compute all the permutations of the word

    # filter the entry of each permutation based on the dictionary and collect the result into a set, to prevent duplicates
    result = set(filter(word_check, word_permutations))

    for meaningful_word in result:
        print(''.join(meaningful_word))
