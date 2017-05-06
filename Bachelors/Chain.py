from PIL import Image
import os.path
import numpy as np
import math
import sys

class Chain:
    def __init__(self, tree):
        self.width, self.height = tree.size

        self.pixels = tree.load()

        # treshold
        for w in range(self.width):
            for h in range(self.height):
                if self.pixels[w,h] >= 128:
                    self.pixels[w,h] = 0
                else:
                    self.pixels[w,h] = 1

        self.begin = self.first_black_pixel()
        self.end = self.last_black_pixel()

        self.shape_height = self.roi_height()
        self.shape_width = self.roi_width()

        self.points = 0
        self.perimeter = 0

        self.visited = np.zeros([self.width, self.height])

        self.chain_code = []
        self.border()

        __index = self.border_neighbors(self.begin[0], self.begin[1])
        self.chain_code_generator(*__index)

    def first_black_pixel(self):
        for height in range(self.height):
            for width in range(self.width):
                if self.pixels[width, height] == 1:
                    return [width, height]

    def last_black_pixel(self):
        for height in reversed(range(self.height)):
            for width in reversed(range(self.width)):
                if self.pixels[width, height] == 1:
                    return [width, height]

    def roi_height(self):
        return self.end[1] - self.begin[1] + 1

    def roi_width(self):
        # left most pixel
        left_most = 0
        for width in range(self.width):
            for height in range(self.height):
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
        return right_most - left_most + 1

    def border(self):
        for height in range(self.height):
            for width in range(self.width):
                if self.border_pixel(width, height):
                    self.points += 1


    def border_pixel(self, i, j):
        # only consider black pixels
        if(self.pixels[i, j] == 0): return False

        #check left
        if(j ==0): return True
        if(j > 0):
            if (self.pixels[i, j - 1] == 0): return True

        #check up
        if(i == 0): return True
        if(i > 0):
            if (self.pixels[i - 1, j] == 0): return True

        #check right
        if(j == self.width - 1): return True
        if(j < self.width - 1):
            if (self.pixels[i, j + 1] == 0): return True

        #check down
        if(i == self.height - 1): return True
        if(i < self.height - 1):
            if (self.pixels[i + 1, j] == 0): return True

        # no empty pixel around = not border pixel
        return False

    def border_neighbors(self, i, j):
        flag = False

        # check east
        if (self.border_pixel(i, j + 1)) and (not flag) and (self.visited[i, j + 1] == 0):
            self.chain_code.append(0)
            self.perimeter += 1
            flag = True
            return [i, j + 1]

        # check southeast
        if (self.border_pixel(i + 1, j + 1)) and (not flag) and (self.visited[i + 1, j + 1] == 0):
            self.chain_code.append(1)
            self.perimeter += math.sqrt(2)
            flag = True
            return [i + 1, j + 1]

        # check south
        if (self.border_pixel(i + 1, j)) and (not flag) and (self.visited[i + 1, j] == 0):
            self.chain_code.append(2)
            self.perimeter += 1
            flag = True
            return [i + 1, j]

        # check southwest
        if (self.border_pixel(i + 1, j - 1)) and (not flag) and (self.visited[i + 1, j - 1] == 0):
            self.chain_code.append(3)
            self.perimeter += math.sqrt(2)
            flag = True
            return [i + 1, j - 1]

        # check west
        if (self.border_pixel(i, j - 1)) and (not flag) and (self.visited[i, j - 1] == 0):
            self.chain_code.append(4)
            self.perimeter += 1
            flag = True
            return [i , j - 1]

        # check northwest
        if (self.border_pixel(i - 1, j - 1)) and (not flag) and (self.visited[i - 1, j - 1] == 0):
            self.chain_code.append(5)
            self.perimeter += math.sqrt(2)
            flag = True
            return [i - 1, j - 1]

        # check north
        if (self.border_pixel(i - 1, j)) and (not flag) and (self.visited[i - 1, j] == 0):
            self.chain_code.append(6)
            self.perimeter += 1
            flag = True
            return [i - 1, j]

        # check northeast
        if (self.border_pixel(i - 1, j + 1)) and (not flag) and (self.visited[i - 1, j + 1] == 0):
            self.chain_code.append(7)
            self.perimeter += 1
            flag = True
            return [i - 1, j + 1]

        # no neighbor border pixels
        return [i, j]

    def chain_code_generator(self, i, j):
        index = self.border_neighbors(i, j)
        # print(index)
        self.visited[i, j] = 1

        if self.visited[index[0], index[1]] == 0:
            self.chain_code_generator(index[0], index[1])
        else:
            pass

    def print_pixels(self):
        for w in range(self.width):
            for h in range(self.height):
                print(self.pixels[w,h], end = "")
            print()

    def print_border_pixels(self):
        for w in range(self.width):
            for h in range(self.height):
                print("{}".format(self.border_pixel(w,h)), end= "\t")
            print()

    def print_information(self):
        print("Size of image: width({width}, heigth({height}))".format(width = self.width, height = self.height) )
        print("Position of first black pixel: ", self.begin)
        print("Position of last black pixel: ", self.end)

        print("Shape height: ", self.shape_height)
        print("Shape width: ", self.shape_width)

        print("Border pixels: " + str(self.points))
        print("Perimeter: " + str(self.perimeter))
        print("Chain code:")
        print(self.chain_code)
    
def main():
    paint = 'paint1.png'
    acer = 'Acer campestre 1.png'
    im = 'image001.png'
    s1 = 'shape1.png'
    s2 = 'shape2.png'
    s3 = 'shape3.png'


    arguments = sys.argv[1:]
    if arguments:
        filename = arguments[0]
        print(arguments)
    else:
        print("No arguments given.")
        filename = s1


    script_dir = os.path.dirname(os.path.abspath(__file__))
    tree = Image.open(os.path.join(script_dir, filename))
    imfile = tree.convert("1", dither = Image.NONE)
    # imfile.save("result_bw.png")

    c = Chain(imfile)
    c.print_information()
    tree.close()

    # import time
    # start = time.time()
    # c.border(tree)
    # print("Points: ", c.points)
    # print("Time execution: ", (time.time() - start) * 1000)


if __name__ == "__main__":
    main()