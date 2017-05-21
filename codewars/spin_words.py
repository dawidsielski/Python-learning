def spin_words(sentence):
    result = []
    for element in sentence.split():
        if len(element) >= 5:
            result.append(element[::-1])
            print(element)
        else:
            result.append(element)
    print(result)
    return " ".join(result)

print(spin_words("this is a testt"))