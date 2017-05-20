def print_alphabet(s = 1):
    import string
    for element in string.ascii_letters[::s]:
        print(element, end = "")


def is_palindrome(s):
    return s == ''.join(reversed(s))
        

def filter_elements(s):
    import string
    for element in s:
        if element not in string.ascii_letters:
            print(element, end=", ")

def filter_words(seq, n):
    s = seq.split()
    return(list(filter(lambda x: len(x) > n, s)))

def main():
    print_alphabet()
    print()
    print_alphabet(2)
    print()
    print(is_palindrome("oko"))
    print()
    filter_elements("dawid *&^")
    print()
    print(filter_words("dawid alskdj aak adf qwsec", 3))


if __name__ == "__main__":
    main()