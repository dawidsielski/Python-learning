def checkio(data):
    """Works up to 3999."""
    ones = ["", "I" , "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens = ["", "X", "XX" , "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hundreds = ["", "C", "CC" , "CCC", "CD", "D", "DC", "DCC", "DCCC", "MC"]
    thousands = [ "", "M", "MM", "MMM"]
    number = str(data)
    roman_number = ""
    if (len(number) == 4):
        roman_number = thousands[int(number[-4])] + hundreds[int(number[-3])] + tens[int(number[-2])] + ones[int(number[-1])]
    elif (len(number) == 3):
        roman_number = hundreds[int(number[-3])] + tens[int(number[-2])] + ones[int(number[-1])]
    elif (len(number) == 2):
        roman_number = tens[int(number[-2])] + ones[int(number[-1])]
    else:
        roman_number = ones[int(number[-1])]
    return roman_number



print(checkio(6) == 'VI', '6')
print(checkio(76) == 'LXXVI', '76')
print(checkio(499) == 'CDXCIX', '499')
print(checkio(3888) == 'MMMDCCCLXXXVIII', '3888')
