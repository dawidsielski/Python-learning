text = "google.com"

letter_frequency = {}
for character in text:
    if character not in letter_frequency.keys():
        letter_frequency[character] = 1
    else:
        letter_frequency[character] += 1


print(letter_frequency)