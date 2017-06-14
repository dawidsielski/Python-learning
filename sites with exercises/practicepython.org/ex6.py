input_word = input("Enter ypur word: ")

input_word_reversed = input_word[::-1]

print(input_word)
print(input_word_reversed)

if input_word == input_word_reversed:
    print("Your input is a palindrome.")
else:
    print("Your word is not a palindrome.")
