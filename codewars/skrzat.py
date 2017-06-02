"""
Geek Challenge [SKRZAT] is an old, old game from Poland that uses a game console with two buttons plus a joy stick. As is true to its name, the game communicates in binary, so that one button represents a zero and the other a one. Even more true to its name, the game chooses to communicate so that the base of the number system is minus two, not plus two, so we'll call this representation "Weird Binary". Thus the bit positions label the powers of minus two, as seen in the following five-bit tables:

Numbers are presented on the screen in Weird Binary, and then numbers are accepted in response from the console as a stream of zeroes and ones, terminated by a five-second pause. You are writing a computer program to support the novice geek in playing the game by translating numbers between decimal and Weird Binary.

#Input

The skrzat function will either convert into Weird Binary or out of Weird Binary: The first parameter will be either the letter "b", which indicates that the second parameter is written in Weird Binary and needs to be converted to decimal; the letter "d" indicates that the second parameter is a decimal and needs to be converted to Weird Binary. The second parameter will be in the range to fit within a 15-bit Weird Binary number, which represents the decimal number range -10922 to 21845, inclusive.

#Output

For each conversion problem, return the type of problem, its input string, and the converted result in the format shown below, replicating even the spacing exactly as shown. Leading zeroes are not allowed.

return format: 'From {binary || decimal}: {non-converted value} is {converted value}'

#Sample Input

skrzat('b', '1001101')
skrzat('b', '0111111')
skrzat('b', '101001000100001')
skrzat('b', '010010001000010')
skrzat('b', '100110100110100')
skrzat('d', -137)
skrzat('d', 137)
skrzat('d', 8191)
skrzat('d', -10000)
skrzat('d', 21000)
#Sample Output

'From binary: 1001101 is 61'
'From binary: 0111111 is -21'
'From binary: 101001000100001 is 19937'
'From binary: 010010001000010 is -7106'
'From binary: 100110100110100 is 15604'
'From decimal: -137 is 10001011'
'From decimal: 137 is 110011001'
'From decimal: 8191 is 110000000000011'
'From decimal: -10000 is 10100100110000'
'From decimal: 21000 is 101011000011000'
"""

def skrzat(base, number):
    # start coding!
    pass

print(skrzat('b', '1001101') == 'From binary: 1001101 is 61')
print(skrzat('b', '0111111') == 'From binary: 0111111 is -21')
print(skrzat('d', -137) == 'From decimal: -137 is 10001011')
print(skrzat('d', 137) == 'From decimal: 137 is 110011001')