"""
Your grandfather criticises your overuse of the word 'like', claiming that it makes up more than 5% of the total words you speak.

You argue that it is much lower than this and so to settle the debate, you have been fitted with a recorder that stores every word you say as a string in an array.

Your task is to make an algorithm that returns true if 'like' accounts for more than 5% of words in the array, otherwise false (if no words are spoken, return false also).
"""


def eval_likes(words):
    # insert your code here
    pass



# test code
print(eval_likes(['I','am','sooo','like','tired']) == True)
print(eval_likes(['likely','story']) == False)
print(eval_likes(['today','was','so','like','awesome']) == True)
print(eval_likes(['yesterday','was','even','ummm','better']) == False)