try:
    a = 1 / 0
except Exception:
    print("Some error.")

print()

try:
    a = 1 / 0
except Exception as err:
    print("Value of error.")
    print(err)

print()

try:
    a = 1 / 0
except ZeroDivisionError:
    print("Divided by zero error.")

print("Else not executed")

try:
    a = 1 / 0
except ZeroDivisionError:
    print("Divided by zero error.")
else:
    print("Executed if no exception raised.")

print("Else executed")

try:
    a = 1 / 1
except ZeroDivisionError:
    print("Divided by zero error.")
else:
    print("Else executed if no exception raised.")




print("Finally block will be executed always.")
try:
    a = 1 / 1
except ZeroDivisionError:
    print("Divided by zero error.")
else:
    print("Else executed if no exception raised.")