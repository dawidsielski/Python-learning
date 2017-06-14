"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized.

Examples:

# returns "theStealthWarrior"
to_camel_case("the-stealth-warrior") 

# returns "TheStealthWarrior"
to_camel_case("The_Stealth_Warrior")

"""

def to_camel_case(text):
    import re
    words = []
    text_list = re.split("_|-", text)
    for x in text_list[1:]:
        words.append( x[0].upper() + x[1:])
    return text_list[0] + "".join(words)



print(to_camel_case('') == '')
print(to_camel_case("the_stealth_warrior") == "theStealthWarrior")
print(to_camel_case("The-Stealth-Warrior") == "TheStealthWarrior")
print(to_camel_case("A-B-C") == "ABC")