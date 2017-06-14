s = input("Enter your message: ")

def len_last_word(s):
    s = s.split()
    return len(s[-1])

print(len_last_word(s))