import os
import urllib.request

# PREWORK
TMP = os.getenv("TMP", "/tmp")
S3 = 'https://bites-data.s3.us-east-2.amazonaws.com/'
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(f'{S3}{DICT}', DICTIONARY)

scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}

# start coding

def load_words():
    """Load the words dictionary (DICTIONARY constant) into a list and return it"""
    with open(urllib.request.urlretrieve(f'{S3}{DICT}', DICTIONARY)[0], 'r') as word_dict:
        word_list = [word for word in word_dict.read().split('\n') if len(word) > 0]
    return word_list

def calc_word_value(word):
    """Given a word calculate its value using the LETTER_SCORES dict"""
    tot_value = sum([LETTER_SCORES.get(letter.upper(), 0) for letter in word])
    return tot_value

def max_word_value(words):
    """Given a list of words calculate the word with the maximum value and return it"""
    # best, best_word = 0, None
    # for word in words:
    #     value = calc_word_value(word)
    #     if value > best:
    #         best = value
    #         best_word = word
    word_scores = {calc_word_value(word): word for word in words}
    return word_scores[max(word_scores.keys())]
    # return best_word