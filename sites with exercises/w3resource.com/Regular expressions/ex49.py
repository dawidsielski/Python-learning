def remove_words(text, n):
    import re
    print(re.sub(r'\W*\b\w{1,7}\b', "", text))



remove_words("Dawid korkotrampki warzywniak eloszka", 6)
