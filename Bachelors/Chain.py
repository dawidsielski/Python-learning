from PIL import Image, ImageMorph

tree = Image.open("Acer campestre 1.png")
# tree.show()

print(tree.size[0])
print(tree.size[1])


def first_black_pixel(tree):
    pixels = tree.load()
    for height in range(tree.size[1]):
        for width in range(tree.size[0]):
            if pixels[width, height] == 1:
                return (width, height)

def last_black_pixel(tree):
    pixels = tree.load()
    for height in reversed(range(tree.size[1])):
        for width in reversed(range(tree.size[0])):
            if pixels[width, height] == 1:
                return (width, height)

    

print(first_black_pixel(tree))
print(last_black_pixel(tree))
