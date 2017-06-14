correct_numbers = [x for x in range(101) if x % 5 == 0 and x % 7 == 0]
print(",".join([str(x) for x in correct_numbers]))