from PIL import Image
im = Image.open("lena.png")
im.rotate(45).show()


import glob, os

size = 128, 128


print(glob.glob("*.*"))
for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size)
    im.save(file + ".thumbnail", "JPEG")