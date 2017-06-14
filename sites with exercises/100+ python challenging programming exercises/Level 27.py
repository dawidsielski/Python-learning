def createDictionary():
    """line 901"""
    sqrt_dictionary = {}

    for i in range(1,21):
        sqrt_dictionary[i] = i**2

    for i in sqrt_dictionary.items():
        print(i)

createDictionary()