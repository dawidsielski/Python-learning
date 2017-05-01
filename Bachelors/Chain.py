from PIL import Image
import numpy as np
import os.path

class Chain:
    def __init__(self, tree):
        self.height = tree.size[1]
        self.width = tree.size[0]

        self.begin = self.first_black_pixel(tree)
        self.end = self.last_black_pixel(tree)

        self.shape_height = self.roi_height()
        self.shape_width = self.roi_width(tree)

        self.points = 0
        self.perimiter = 0

        self.visited = np.zeros([self.width, self.height])

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
    
    def border(self, tree):
        pixels = tree.load()
        for height in range(tree.size[1]):
            for width in range(tree.size[0]):
                if self.border_pixel(tree, width, height):
                    self.points += 1


    def border_pixel(self, tree, i, j):
        pixels = tree.load()

        # only consider black pixels
        if(pixels[i, j] == 0): return False

        #check left
        if(j == 0): return True
        if(j < 0):
            if (pixels[i, j - 1] == 0): return True

        #check up
        if(i == 0): return True
        if(i < 0):
            if (pixels[i - 1, j] == 0): return True
        
        #check right
        if(i == self.width): return True
        if(i < self.width):
            if (pixels[i, j + 1] == 0): return True
        
        #check down
        if(i == self.height): return True
        if(i < self.height):
            if (pixels[i + 1, j] == 0): return True
        
        # no empty pixel around = not border pixel
        return False


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    tree = Image.open(os.path.join(script_dir, 'Acer campestre 1.png'))
    
    print(script_dir)

    print("Size of image", tree.size)
    print("Position of first black pixel: ", Chain.first_black_pixel(tree))
    print("Position of last black pixel: ", Chain.last_black_pixel(tree))

    c = Chain(tree)
    print("Shape height: ", c.shape_height)
    print("Shape width: ", c.shape_width)

    import time
    start = time.time()
    c.border(tree)
    print("Points: ", c.points)
    print("Time execution: ", (time.time() - start) * 1000)

    tree.close()

if __name__ == "__main__":
    main()