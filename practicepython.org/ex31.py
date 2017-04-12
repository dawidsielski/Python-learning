guessing_word = "EVAPORATE"
guessing_word_list = list(guessing_word)

table = []
for element in guessing_word_list:
    table.append([element, False])

wrong_guesses = 6
correct_guesses = 0
while correct_guesses < len(guessing_word):
    user_guess = str(input("\nEnter user guess: ")).upper()
    for element in table:
        if element[0] == user_guess[0] and  element[1] == False:
            correct_guesses += 1
            element[1]= True

    for element in table:
        if element[1]:
            print(element[0], end = "")
        else:
            print("_", end = "")

if correct_guesses == len(guessing_word):
    print("\nEnd game!")
else:
    print("\nYou lose!")