color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

for item in color_list_1:
    if item not in color_list_2:
        print(item)


#alternative

print(color_list_1.difference(color_list_2))
