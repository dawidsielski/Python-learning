import shelve
import os


script_dir = os.path.dirname(os.path.abspath(__file__))
trees_chain_code_abs_path = os.path.join(script_dir, "trees_database")

trees_chain_code = shelve.open(trees_chain_code_abs_path)

count_wrong = 0
for element in trees_chain_code:
    # print(element)
    if len(trees_chain_code[element]['Code']) < 2000:
        count_wrong += 1
    else:
        print(element)
        print(trees_chain_code[element]['Code'])

print(count_wrong)

# print(trees_chain_code['Robinia pseudacacia 1.png']['Code'])
# print(trees_chain_code['Vitis vinifera 2.png']['Code'])
trees_chain_code.close()