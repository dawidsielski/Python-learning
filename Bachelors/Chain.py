from PIL import Image
import numpy as np
import os.path

class Chain:
    def __init__(self, tree):
        self.height = tree.size[1]
        self.width = tree.size[0]

        self.pixels = tree.load()

        self.begin = self.first_black_pixel()
        self.end = self.last_black_pixel()

        self.shape_height = self.roi_height()
        self.shape_width = self.roi_width()

        self.points = 0
        self.perimiter = 0

        self.visited = np.zeros([self.width, self.height])

        self.chain_code = []

    def first_black_pixel(self):
        for height in range(self.height):
            for width in range(self.width):
                if self.pixels[width, height] == 1:
                    return (width, height)

    def last_black_pixel(self):
        for height in reversed(range(self.height)):
            for width in reversed(range(self.width)):
                if self.pixels[width, height] == 1:
                    return (width, height)

    def roi_height(self):
        return self.end[1] - self.begin[1]

    def roi_width(self):
        # left most pixel
        left_most = 0
        for width in range(self.width):
            for height in range(self.height):
                # print(width, height, pixels[width, height])
                if self.pixels[width, height] == 1:
                    left_most = width
                    break
            if left_most != 0: # to leave second loop
                break
        # right most pixel
        right_most = 0
        for width in reversed(range(self.width)):
            for height in reversed(range(self.height)):
                if self.pixels[width, height] == 1:
                    right_most = width
                    break
            if right_most != 0: # to leave second loop
                break
        return right_most - left_most
    
    def border(self):
        for height in range(self.height):
            for width in range(self.width):
                if self.border_pixel(width, height):
                    self.points += 1


    def border_pixel(self, i, j):

        # only consider black pixels
        if(self.pixels[i, j] == 0): return False

        #check left
        if(j == 0): return True
        if(j < 0):
            if (self.pixels[i, j - 1] == 0): return True

        #check up
        if(i == 0): return True
        if(i < 0):
            if (self.pixels[i - 1, j] == 0): return True
        
        #check right
        if(i == self.width): return True
        if(i < self.width):
            if (self.pixels[i, j + 1] == 0): return True
        
        #check down
        if(i == self.height): return True
        if(i < self.height):
            if (self.pixels[i + 1, j] == 0): return True
        
        # no empty pixel around = not border pixel
        return False

    # def border_neighbors(i, j):
    #     index = (i, j)
    #     flat = False

    #     #check east
    #     if(border_pixel())













def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    tree = Image.open(os.path.join(script_dir, 'Acer campestre 1.png'))
    
    print(script_dir)

    c = Chain(tree)
    print("Size of image", tree.size)
    print("Position of first black pixel: ", c.begin)
    print("Position of last black pixel: ", c.end)

    print("Shape height: ", c.shape_height)
    print("Shape width: ", c.shape_width)

    # import time
    # start = time.time()
    # c.border(tree)
    # print("Points: ", c.points)
    # print("Time execution: ", (time.time() - start) * 1000)

    tree.close()

if __name__ == "__main__":
    main()