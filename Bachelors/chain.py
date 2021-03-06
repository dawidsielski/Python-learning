from PIL import Image
import os.path
import numpy as np
import math
import sys

class Chain:
    def __init__(self, path):
        imfile = Image.open(path)
        tree = imfile.convert("1", dither=Image.NONE)

        self.width, self.height = tree.size

        self.pixels = tree.load()
        tree.close()
        # treshold
        for w in range(self.width):
            for h in range(self.height):
                if self.pixels[w, h] >= 128:
                    self.pixels[w, h] = 0
                else:
                    self.pixels[w, h] = 1

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

    def _roi_left(self):
        # left most pixel
        for width in range(self.width):
            for height in range(self.height):
                if self.pixels[width, height] == 1:
                    return width

    def _roi_right(self):
        # right most pixel
        for width in reversed(range(self.width)):
            for height in reversed(range(self.height)):
                if self.pixels[width, height] == 1:
                    return width

    def roi_width(self):
        return self._roi_right() - self._roi_left() + 1

    def border(self):
        for height in range(self.height):
            for width in range(self.width):
                if self.border_pixel(width, height):
                    self.points += 1


    def border_pixel(self, i, j):
        # only consider black pixels
        if(self.pixels[i, j] == 0): return False

        #check left
        if j == 0:
            return True
        if j > 0:
            if self.pixels[i, j - 1] == 0:
                return True

        #check up
        if i == 0:
            return True
        if i > 0:
            if self.pixels[i - 1, j] == 0:
                return True

        #check right
        if j == self.width - 1:
            return True
        if j < self.width - 1:
            if self.pixels[i, j + 1] == 0:
                return True

        #check down
        if i == self.height - 1:
            return True
        if i < self.height - 1:
            if self.pixels[i + 1, j] == 0:
                return True

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
            return [i, j - 1]

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
                print(self.pixels[w, h], end="")
            print()

    def print_border_pixels(self):
        for w in range(self.width):
            for h in range(self.height):
                print("{}".format(self.border_pixel(w, h)), end="\t")
            print()

    def print_information(self):
        print("Size of image: width({width}, heigth({height}))".format(width=self.width, height=self.height))
        print("Position of first black pixel: ", self.begin)
        print("Position of last black pixel: ", self.end)

        print("Shape height: ", self.shape_height)
        print("Shape width: ", self.shape_width)

        print("Border pixels: " + str(self.points))
        print("Perimeter: " + str(self.perimeter))
        print("Chain code (size: {}) :".format(len(self.chain_code)))
        print(self.chain_code)

    def prepare_photo(self):
        pass

def main():
    sys.setrecursionlimit(5000)
    PAINT = 'paint1.png'
    ACER = 'Acer campestre 1.png'
    IM = 'image001.png'
    S1 = 'shape1.png'
    S2 = 'shape2.png'
    S3 = 'shape3.png'
    MAGNOLIA = 'Magnolia soulangeana 7.png'


    script_dir = os.path.dirname(os.path.abspath(__file__))
    absolute_path_trees = os.path.join(script_dir, "trees")
    absolute_path_trees = os.path.join(script_dir, "test_images")
    trees_content = os.listdir(absolute_path_trees)
    print(trees_content)
    # imfile.save("result_bw.png")

    for filename in trees_content[4:5]:
        c = Chain(os.path.join(absolute_path_trees, filename))
        c.print_information()
        print(filename)


if __name__ == "__main__":
    main()
