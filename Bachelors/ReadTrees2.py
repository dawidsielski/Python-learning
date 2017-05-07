import os


# print(os.path.dirname())

script_path = os.path.dirname(os.path.realpath(__file__))
trees2_absolute_path = os.path.join(script_path, 'trees2')

for root, dirname, filenames in os.walk(trees2_absolute_path):
    print(root)
    print("Dirname: ", dirname)
    for name in filenames:
        print(name)