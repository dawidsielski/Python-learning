number = 2**1000000

filename = open("result.txt", "w")
filename.write(str(number))
filename.close()

print(len(str(number)))
