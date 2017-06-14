def recall_password(cipher_grille, ciphered_password):
    password = ""
    for x in cipher_grille:
        for element in x:
            print(element)
            if element == "X":
                # print(element)
    print(password)
    return password


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print( recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example' )

    print( recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example' )
