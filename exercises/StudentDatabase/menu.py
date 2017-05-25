def print_menu():
    print("Simple menu")
    print("1. Option")
    print("2. Option")
    print("3. Option")
    print("4. Option")



def option_one():
    print("Do option one")

def option_two():
    print("Do option two")

def option_three():
    print("Do option three")

def option_four():
    print("Do option four")


def main():
    user_choice = 0
    while user_choice > -1:
        user_choice = int(input("Enter yout choice: "))

        if user_choice == 1:
            option_one()
        elif user_choice == 2:
            option_two()
        elif user_choice == 3:
            option_three()
        elif user_choice == 4:
            option_four()
        else:
            print("Invalid option. Try once again.")


if __name__ == "__main__":
    main()