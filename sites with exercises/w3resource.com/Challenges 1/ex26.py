def if_anagram(a,b):
    return sorted(a) == sorted(b)


print(if_anagram("abcde", "abdce"))
print(if_anagram("abcde", "abdcr"))