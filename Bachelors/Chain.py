from PIL import Image

class Chain:
    def __init__(self, tree):
        self.height = tree.size[1]
        self.width = tree.size[0]

        self.begin = self.first_black_pixel(tree)
        self.end = self.last_black_pixel(tree)

        self.shape_height = self.roi_height()
        self.shape_width = self.roi_width(tree)

    @staticmethod
    def first_black_pixel(tree):
        pixels = tree.load()
        for height in range(tree.size[1]):
            for width in range(tree.size[0]):
                if pixels[width, height] == 1:
                    return (width, height)

    @staticmethod
    def last_black_pixel(tree):
        pixels = tree.load()
        for height in reversed(range(tree.size[1])):
            for width in reversed(range(tree.size[0])):
                if pixels[width, height] == 1:
                    return (width, height)
    
    
    def roi_height(self):
        return self.end[1] - self.begin[1]

    @staticmethod
    def roi_width(tree):
        pixels = tree.load()
        # left most pixel
        left_most = 0
        for width in range(tree.size[0]):
            for height in range(tree.size[1]):
                # print(width, height, pixels[width, height])
                if pixels[width, height] == 1:
                    left_most = width
                    break
            if left_most != 0: # to leave second loop
                break
        # right most pixel
        right_most = 0
        for width in reversed(range(tree.size[0])):
            for height in reversed(range(tree.size[1])):
                if pixels[width, height] == 1:
                    right_most = width
                    break
            if right_most != 0: # to leave second loop
                break
        return right_most - left_most
    

def main():
    tree = Image.open("Acer campestre 1.png")
    print("Size of image", tree.size)
    print("Position of first black pixel: ", Chain.first_black_pixel(tree))
    print("Position of last black pixel: ", Chain.last_black_pixel(tree))

    c = Chain(tree)
    print("Shape height: ", c.shape_height)
    print("Shape width: ", c.shape_width)

if __name__ == "__main__":
    main()