def disemvowel(string):
    vovels = "aeiouyAEIOUY"
    result = [x for x in string if x not in vovels]
    return "".join(result)



print(disemvowel("This website is for losers LOL!"))