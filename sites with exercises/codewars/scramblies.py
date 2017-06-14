"""
Write function scramble(str1,str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

For example:
str1 is 'rkqodlw' and str2 is 'world' the output should return true.
str1 is 'cedewaraaossoqqyt' and str2 is 'codewars' should return true.
str1 is 'katas' and str2 is 'steak' should return false.

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered
"""

def scramble(s1,s2):
    for element in s2:
        if element in s1:
            continue
        else:
            return False
    return True


print(scramble('rkqodlw', 'world') == True)
print(scramble('cedewaraaossoqqyt', 'codewars') == True)
print(scramble('katas', 'steak') == False)
print(scramble('scriptingjava','javascript') == True)
print(scramble('scriptjava','javascript') == True)