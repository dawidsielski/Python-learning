fibbonacci = [1,1]
len_fibbonacci = len(fibbonacci)

def calculate_fibbonacci(number_of_elements):
    while len(fibbonacci) < number_of_elements:
        fibbonacci.append(fibbonacci[len(fibbonacci)-1] + fibbonacci[len(fibbonacci)-2])


calculate_fibbonacci(100)
print(fibbonacci)
