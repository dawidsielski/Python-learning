from PIL import Image
im = Image.open("lena.png")
im.rotate(45).show()