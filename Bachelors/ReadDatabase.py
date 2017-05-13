import shelve
import os


script_dir = os.path.dirname(os.path.abspath(__file__))
trees_chain_code_abs_path = os.path.join(script_dir, "trees_database")

db_txt_file = open("database txt", "w")

trees_chain_code = shelve.open(trees_chain_code_abs_path)

count_wrong = 0
for element in trees_chain_code:
    # print(element)
    if len(trees_chain_code[element]['Code']) < 2000:
        count_wrong += 1
    else:
        print(element)
        print(trees_chain_code[element]['Code'])

    db_txt_file.writelines(element[:-4])
    db_txt_file.writelines("\n")
    db_txt_file.writelines(str(trees_chain_code[element]['Code']))
    db_txt_file.writelines("\n")
    db_txt_file.writelines(str(len(trees_chain_code[element]['Code'])))
    db_txt_file.writelines("\n")

print(count_wrong)

# print(trees_chain_code['Robinia pseudacacia 1.png']['Code'])
# print(trees_chain_code['Vitis vinifera 2.png']['Code'])
db_txt_file.close()
trees_chain_code.close()