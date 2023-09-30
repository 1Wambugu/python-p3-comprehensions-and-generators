#!/usr/bin/env python3

# list_comprehension.py

def return_evens(num_list):
    """
    Returns a list of all even elements from the input list of numbers.
    """
    return [x for x in num_list if x % 2 == 0]

def make_exclamation(sentence_list):
    """
    Adds an exclamation mark at the end of each sentence in the input list of sentences.
    """
    return [sentence + '!' for sentence in sentence_list]
