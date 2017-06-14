"""
Move the first letter of each word to the end of it, then add 'ay' to the end of the word.

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
"""

def pig_it(text):
    return " ".join([element[1:] + element[0] + "ay" if element.isalpha() else element for element in text.split()])


print(pig_it('Pig latin is cool ?'))