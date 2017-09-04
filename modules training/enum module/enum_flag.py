from enum import Flag
from enum import auto


class Color(Flag):
    RED = auto()
    BLACK = auto()
    YELLOW = auto()
    WHITE = RED | BLACK | YELLOW

# print(Color.WHITE.value)

for color in Color:
    print(color.value)