import sys

argument_list = sys.argv
del argument_list[0]
print(argument_list)
print(tuple(argument_list))