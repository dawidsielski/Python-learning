from PIL import Image, ImageMorph

tree = Image.open("Acer campestre 1.png")
# tree.show()

pixels = tree.load()
print(tree.size[0])
print(tree.size[1])

print(pixels[1000,1000])
# tree.show()

# print(dir(tree))