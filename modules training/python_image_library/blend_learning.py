from PIL import Image

im = Image.open("lena.png")
im.show()
blended = Image.blend(im,im.rotate(90), 0.5)
# blended.show()

blended.save("blended.jpeg", "JPEG")