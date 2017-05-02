import os
import time

print("Current working directory ",os.getcwd())

print(os.listdir())

os.mkdir("test")
time.sleep(1)
os.rmdir("test")

os.system("dir") # invoke command line commands
