import shelve


trees_chain_code = shelve.open('trees_database')

count_wrong = 0
for element in trees_chain_code:
    # print(element)
    if len(trees_chain_code[element]['Code']) < 500:
        count_wrong += 1
        print(element)

print(count_wrong)

print(trees_chain_code['Robinia pseudacacia 1.png']['Code'])
trees_chain_code.close()
