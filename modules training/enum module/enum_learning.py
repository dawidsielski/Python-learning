import enum

class Color(enum.Enum):
    RED = 1
    GREEN = 2
    YELLOW = 3


print(Color.GREEN)
print(repr(Color.GREEN))
print(Color.GREEN.name)
print(Color.GREEN.value)


for color in Color:
    print(color)


print(Color(1))
print(Color['RED'])


try:
    @enum.unique
    class Number(enum.Enum):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 3
except ValueError as error:
    print(error)


print([member for name, member in Color.__members__.items()])