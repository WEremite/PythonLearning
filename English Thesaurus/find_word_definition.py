'''
    The program should take a word and show its definition.
'''

import json
from difflib import get_close_matches

dictionary = json.load(open("data.json"))


def find_word_definition(word):
    lower_word = word.lower()
    close_matches = get_close_matches(word, dictionary.keys())
    if lower_word in dictionary:
        word_definition = dictionary[lower_word]
        if len(word_definition) == 1:
            print('Word definition is:')
        else:
            print('Word definitions are:')

        count = 1
        for sentence in word_definition:
            print('%s) %s' % (count, sentence))
            count += 1

    elif len(close_matches) > 0:
        print('Did you mean "%s" instead? [Y]/[n]' % close_matches[0])
        user_choice = input('')
        if user_choice.lower() == 'y':
            find_word_definition(close_matches[0])
        else:
            print(
                f'There is no definition for word "{word}". Please double check it.')
    else:
        print(
            f'There is no definition for word "{word}". Please double check it.')


word = input("Write a word and press enter: ")
find_word_definition(word)
