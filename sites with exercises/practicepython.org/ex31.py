import random
file_name = open("sowpods.txt", "r")
content = file_name.readlines()

random_word = content[random.randrange(len(content))]
print(random_word)

guessing_word = random_word
guessing_word_list = list(guessing_word)

table = []
for element in guessing_word_list:
    table.append([element, False])

guesses_available = 6
wrong_guesses = 0
correct_guesses = 0
user_guesses = []
while correct_guesses < len(guessing_word) and wrong_guesses < 6:
    user_guess = str(input("\nEnter user guess: ")).upper()
    while user_guess in user_guesses:
        user_guess = str(input("You have already tried entering \"" + user_guess.upper() + "\" letter. Try another one: ")).upper()
    user_guesses.append(user_guess)
    if user_guess[0] not in guessing_word_list:
        wrong_guesses += 1
        print("Wrong guess! Guesses left: {}".format(guesses_available - wrong_guesses))
    else:
        for element in table:
            if element[0] == user_guess[0] and element[1] == False:
                correct_guesses += 1
                element[1]= True

        for element in table:
            if element[1]:
                print(element[0], end = "")
            else:
                print("_", end = "")

if correct_guesses == len(guessing_word):
    print("\nYou win!")
else:
    print("\nYou lose!")