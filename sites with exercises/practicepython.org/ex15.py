my_string = "pies ma ale a ala ma kota"

split_string = my_string.split()
split_reverse_string = split_string[::-1]

result = " ".join(split_reverse_string)

print(my_string)
print(result)
