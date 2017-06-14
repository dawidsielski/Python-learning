"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
Implement a function that determines whether a string that contains only letters is an isogram. 
Assume the empty string is an isogram. Ignore letter case.
"""

def is_isogram(letter_sequence):
    return sorted(list(set(letter_sequence.lower()))) == sorted(letter_sequence.lower())


print(is_isogram("adiw"))