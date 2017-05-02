from PIL import Image
import numpy as np
import os.path
import math

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
                # print(self.pixels[width, height])
                if self.pixels[width, height] == 0:
                    return [width, height]

    def last_black_pixel(self):
        for height in reversed(range(self.height)):
            for width in reversed(range(self.width)):
                # print(self.pixels[width, height])
                if self.pixels[width, height] == 0:
                    return [width, height]

    def roi_height(self):
        return self.end[1] - self.begin[1] + 1

    def roi_width(self):
        # left most pixel
        left_most = 0
        for width in range(self.width):
            for height in range(self.height):
                if self.pixels[width, height] == 0:
                    left_most = width
                    break
            if left_most != 0: # to leave second loop
                break
        # right most pixel
        right_most = 0
        for width in reversed(range(self.width)):
            for height in reversed(range(self.height)):
                if self.pixels[width, height] == 0:
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
        # print("Checking pixel: {} {}".format(i, j))
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
        index = [i, j]
        # print(index)
        flag = False

        # check east
        if(self.border_pixel(i, j + 1) and not flag and self.visited[i, j + 1] == 0):
            j += 1
            self.chain_code.append(0)
            self.perimiter += 1
            flag = True
            index.clear()
            index = [i, j]
            return index

        # check southeast
        if(self.border_pixel(i + 1, j + 1) and not flag and self.visited[i + 1, j + 1] == 0):
            i += 1
            j += 1
            self.chain_code.append(1)
            self.perimiter += math.sqrt(2)
            flag = True
            index.clear()
            index = [i, j]
            return index

        # check south
        if(self.border_pixel(i + 1, j) and not flag and self.visited[i + 1, j] == 0):
            i += 1
            self.chain_code.append(2)
            self.perimiter += 1
            flag = True
            index.clear()
            index = [i, j]
            return index

        # check southwest
        if(self.border_pixel(i + 1, j - 1) and not flag and self.visited[i + 1, j - 1] == 0):
            i += 1
            j -= 1
            self.chain_code.append(3)
            self.perimiter += math.sqrt(2)
            flag = True
            index.clear()
            index = [i, j]
            return index

        # check west
        if(self.border_pixel(i, j - 1) and not flag and self.visited[i, j - 1] == 0):
            j -= 1
            self.chain_code.append(4)
            self.perimiter += 1
            flag = True
            index.clear()
            index = [i, j]
            return index

        # check northwest
        if(self.border_pixel(i - 1, j - 1) and not flag and self.visited[i - 1, j - 1] == 0):
            i -= 1
            j -= 1
            self.chain_code.append(5)
            self.perimiter += math.sqrt(2)
            flag = True
            index.clear()
            index = [i, j]
            return index

        # check north
        if(self.border_pixel(i - 1, j) and not flag and self.visited[i - 1, j] == 0):
            i -= 1
            self.chain_code.append(6)
            self.perimiter += 1
            flag = True
            index.clear()
            index = [i, j]
            return index

        # check northeast
        if(self.border_pixel(i - 1, j + 1) and not flag and self.visited[i - 1, j + 1] == 0):
            i -= 1
            j += 1
            self.chain_code.append(7)
            self.perimiter += 1
            flag = True
            index.clear()
            index = [i, j]
            return index

        # no neighbor border pixels
        index.clear()
        index = [i, j]
        return index

    def chain_code_generator(self, i, j):
        index = self.border_neighbors(i, j)
        print(index)
        # print(index)
        self.visited[i, j] = 1

        if self.visited[index[0], index[1]] == 0:
            self.chain_code_generator(index[0], index[1])
        else:
            print()


def main():
    acer = 'Acer campestre 1.png'
    shape = 'shape1.png'
    paint = 'paint1.png'
    script_dir = os.path.dirname(os.path.abspath(__file__))
    tree = Image.open(os.path.join(script_dir, paint))
    imfile = tree.convert("1", dither = Image.NONE)
    # imfile = Image.fromarray(bw)
    imfile.save("result_bw.png")
    pix = imfile.load()
    
    for w in range(6):
        for h in range(6):
            print(pix[w,h] , end = "\t")
        print()

    c = Chain(imfile)
    print("Size of image", tree.size)
    print("Position of first black pixel: ", c.begin)
    print("Position of last black pixel: ", c.end)

    print("Shape height: ", c.shape_height)
    print("Shape width: ", c.shape_width)

    # print(c.border_pixel(5,5))

    for w in range(6):
        for h in range(6):
            print("{}".format(c.border_pixel(w,h)), end= "\t")
        print()

    print("Chain code:\n")
    index = c.border_neighbors(c.begin[0], c.begin[1])
    c.chain_code_generator(index[0], index[1])
    print(c.chain_code)
    # print(c.border)

    # import time
    # start = time.time()
    # c.border(tree)
    # print("Points: ", c.points)
    # print("Time execution: ", (time.time() - start) * 1000)

    # tree.close()

if __name__ == "__main__":
    main()