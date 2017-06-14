import datetime

def if_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def main():
    user_year = int(input("Enter year: "))
    if if_leap_year(user_year):
        print("Your year is a leap one.")
    else:
        print("Your year is not a leap year.")


if __name__ == "__main__":
    main()